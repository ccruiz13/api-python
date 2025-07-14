from  dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from app.domain.constants.subscription_status import SubscriptionStatus


@dataclass
class Suscription:
    subscription_id: str
    customer_id: str
    fund_id: str
    amount: Decimal
    timestamp: datetime
    status: SubscriptionStatus