from pydantic import BaseModel
from typing import Optional, Any

class SuccessResponse(BaseModel):
    message: str
    data: Optional[Any] = None

class ErrorResponse(BaseModel):
    message: str
    error: Optional[str] = None