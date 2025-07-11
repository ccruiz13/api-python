from app.application.dto.request.subscription_request import SubscriptionRequest
from app.domain.model.suscription import Suscription
from app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.application.mapper.subscription_mapper import SubscriptionMapper


class SubscriptionHandler:

    def __init__(self, user_case: SubscriptionInputPort):
        self.user_case = user_case

    def create_subscription(self, request: SubscriptionRequest) -> Suscription:
        subscription = SubscriptionMapper.to_domain(request)

        create_subscription = self.user_case.create_subscription(subscription)
        return create_subscription