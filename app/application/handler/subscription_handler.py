from app.application.dto.request.subscription_request import SubscriptionRequest
from app.application.dto.response.subscription_response import SubscriptionResponse
from app.domain.model.suscription import Suscription
from app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.application.mapper.subscription_request_mapper import SubscriptionRequestMapper
from app.infraestructure.out.dynamodb.mapper.suscription_mapper import SubscriptionMapper


class SubscriptionHandler:

    def __init__(self, user_case: SubscriptionInputPort):
        self.user_case = user_case

    def create_subscription(self, request: SubscriptionRequest) -> Suscription:
        subscription = SubscriptionRequestMapper.to_domain(request)

        create_subscription = self.user_case.create_subscription(subscription)
        return create_subscription

    def get_subscription_by_id(self, subscription_id: str) -> SubscriptionResponse:
        subscription = self.user_case.find_by_id(subscription_id)
        response_dto = SubscriptionMapper.to_response(subscription)
        return response_dto