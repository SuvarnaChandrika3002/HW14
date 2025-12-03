from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str

class CalculationBase(BaseModel):
    operation: str
    operand1: float
    operand2: float

class CalculationCreate(CalculationBase):
    pass

class CalculationUpdate(BaseModel):
    operation: Optional[str] = None
    operand1: Optional[float] = None
    operand2: Optional[float] = None

class CalculationOut(CalculationBase):
    id: int
    result: float
    class Config:
        orm_mode = True
