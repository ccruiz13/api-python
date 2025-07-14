from  dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class SubscriptionResponse:
    subscription_id: str
    customer_id: str
    fund_id: str
    amount: Decimal
    timestamp: datetime