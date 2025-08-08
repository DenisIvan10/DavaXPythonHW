from pydantic import BaseModel, Field
from datetime import datetime

class OperationRequest(BaseModel):
    operation: str = Field(..., description="Numele operației: pow, fib, fact")
    input: str = Field(..., description="Datele de intrare ca text")
    result: str = Field(..., description="Rezultatul operației ca text")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
