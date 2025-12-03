from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Calculation
from app.schemas import CalculationCreate, CalculationUpdate, CalculationOut
from app.auth import get_current_user

router = APIRouter(prefix="/calculations", tags=["Calculations"])

@router.get("/", response_model=list[CalculationOut])
def browse(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Calculation).filter(Calculation.user_id == user.id).all()

@router.get("/{id}", response_model=CalculationOut)
def read(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = db.query(Calculation).filter(Calculation.id == id, Calculation.user_id == user.id).first()
    if not c:
        raise HTTPException(404)
    return c

@router.post("/", response_model=CalculationOut)
def create(data: CalculationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if data.operation not in ["add", "subtract", "multiply", "divide"]:
        raise HTTPException(400)
    if data.operation == "divide" and data.operand2 == 0:
        raise HTTPException(400)
    if data.operation == "add":
        r = data.operand1 + data.operand2
    elif data.operation == "subtract":
        r = data.operand1 - data.operand2
    elif data.operation == "multiply":
        r = data.operand1 * data.operand2
    else:
        r = data.operand1 / data.operand2
    c = Calculation(user_id=user.id, operation=data.operation, operand1=data.operand1, operand2=data.operand2, result=r)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@router.put("/{id}", response_model=CalculationOut)
def update(id: int, data: CalculationUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = db.query(Calculation).filter(Calculation.id == id, Calculation.user_id == user.id).first()
    if not c:
        raise HTTPException(404)
    if data.operation:
        if data.operation not in ["add", "subtract", "multiply", "divide"]:
            raise HTTPException(400)
        c.operation = data.operation
    if data.operand1 is not None:
        c.operand1 = data.operand1
    if data.operand2 is not None:
        if c.operation == "divide" and data.operand2 == 0:
            raise HTTPException(400)
        c.operand2 = data.operand2
    if c.operation == "add":
        c.result = c.operand1 + c.operand2
    elif c.operation == "subtract":
        c.result = c.operand1 - c.operand2
    elif c.operation == "multiply":
        c.result = c.operand1 * c.operand2
    else:
        c.result = c.operand1 / c.operand2
    db.commit()
    db.refresh(c)
    return c

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = db.query(Calculation).filter(Calculation.id == id, Calculation.user_id == user.id).first()
    if not c:
        raise HTTPException(404)
    db.delete(c)
    db.commit()
    return {"message": "deleted"}
