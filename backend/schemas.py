from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True


class CalcBase(BaseModel):
    operation: str
    operand1: float
    operand2: float

class CalcCreate(CalcBase):
    pass

class CalcUpdate(BaseModel):
    operation: str | None = None
    operand1: float | None = None
    operand2: float | None = None

class CalcRead(CalcBase):
    id: int
    result: float
    class Config:
        orm_mode = True
