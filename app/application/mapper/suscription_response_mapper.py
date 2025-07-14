from app.application.dto.response.subscription_response import SubscriptionResponse
from app.domain.model.suscription import Suscription

class SuscriptionResponseMapper:

    @staticmethod
    def to_response(response: Suscription) -> SubscriptionResponse:
        return SubscriptionResponse(
            subscription_id=response.subscription_id,
            customer_id=response.customer_id,
            fund_id=response.fund_id,
            amount=response.amount,
            timestamp=response.timestamp
        )