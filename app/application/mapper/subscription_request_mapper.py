from app.application.dto.request.subscription_request import SubscriptionRequest
from app.domain.model.suscription import Suscription

class SubscriptionRequestMapper:
    @staticmethod
    def to_domain(request: SubscriptionRequest) -> Suscription:
        return Suscription(
            subscription_id=None,
            customer_id=request.customer_id,
            fund_id=request.fund_id,
            amount=request.amount,
            timestamp=None,
            status=None
        )