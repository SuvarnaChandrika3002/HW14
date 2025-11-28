from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Calculation
from ..schemas import CalcCreate, CalcUpdate, CalcRead
from ..auth import SECRET, ALGO

router = APIRouter(prefix="/calculations")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_id(token: str):
    try:
        payload = jwt.decode(token, SECRET, ALGO)
        return payload["id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


# --------------------
# BROWSE
# --------------------
@router.get("/", response_model=list[CalcRead])
def browse(token: str, db: Session = Depends(get_db)):
    uid = get_user_id(token)
    records = db.query(Calculation).filter(Calculation.owner_id == uid).all()
    return records


# --------------------
# ADD
# --------------------
@router.post("/", response_model=CalcRead)
def add(calc: CalcCreate, token: str, db: Session = Depends(get_db)):
    uid = get_user_id(token)

    
    try:
        allowed_ops = {"+": calc.operand1 + calc.operand2,
                       "-": calc.operand1 - calc.operand2,
                       "*": calc.operand1 * calc.operand2,
                       "/": calc.operand1 / calc.operand2}
        result = allowed_ops[calc.operation]
    except Exception:
        raise HTTPException(400, "Invalid operation")

    new = Calculation(
        operation=calc.operation,
        operand1=calc.operand1,
        operand2=calc.operand2,
        result=result,
        owner_id=uid
    )
    db.add(new)
    db.commit()
    db.refresh(new)   
    return new


# --------------------
# READ
# --------------------
@router.get("/{id}", response_model=CalcRead)
def read(id: int, token: str, db: Session = Depends(get_db)):
    uid = get_user_id(token)
    c = db.query(Calculation).filter(Calculation.id == id,
                                     Calculation.owner_id == uid).first()
    if not c:
        raise HTTPException(404, "Not found")
    return c


# --------------------
# EDIT
# --------------------
@router.put("/{id}", response_model=CalcRead)
def edit(id: int, data: CalcUpdate, token: str, db: Session = Depends(get_db)):
    uid = get_user_id(token)
    c = db.query(Calculation).filter(Calculation.id == id,
                                     Calculation.owner_id == uid).first()
    if not c:
        raise HTTPException(404, "Not found")

    if data.operation is not None:
        c.operation = data.operation
    if data.operand1 is not None:
        c.operand1 = data.operand1
    if data.operand2 is not None:
        c.operand2 = data.operand2

    
    try:
        allowed_ops = {"+": c.operand1 + c.operand2,
                       "-": c.operand1 - c.operand2,
                       "*": c.operand1 * c.operand2,
                       "/": c.operand1 / c.operand2}
        c.result = allowed_ops[c.operation]
    except Exception:
        raise HTTPException(400, "Invalid operation")

    db.commit()
    db.refresh(c)
    return c


# --------------------
# DELETE
# --------------------
@router.delete("/{id}")
def delete(id: int, token: str, db: Session = Depends(get_db)):
    uid = get_user_id(token)
    c = db.query(Calculation).filter(Calculation.id == id,
                                     Calculation.owner_id == uid).first()
    if not c:
        raise HTTPException(404, "Not found")

    db.delete(c)
    db.commit()
    return {"message": "Deleted"}
