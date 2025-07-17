from decimal import Decimal

from pydantic import  BaseModel
from datetime import datetime

class SuscriptionEntity(BaseModel):
    subscription_id: str
    customer_id: str
    fund_id: str
    amount: Decimal
    timestamp: str

    def to_item(self) -> dict:
        return self.model_dump()
