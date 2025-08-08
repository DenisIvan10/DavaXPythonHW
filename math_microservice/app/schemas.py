from pydantic import BaseModel, Field, validator
from typing import Optional

class PowRequest(BaseModel):
    base: int
    exp: int

class FactorialRequest(BaseModel):
    n: int

class FibonacciRequest(BaseModel):
    n: int

class MathResponse(BaseModel):
    result: int
    operation: str
    user: str

class MathRequestLog(BaseModel):
    id: int
    operation: str
    input_data: str
    result: str
    user: str
    timestamp: str
