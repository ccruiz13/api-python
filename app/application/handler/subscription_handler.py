from app.application.dto.request.subscription_request import SubscriptionRequest
from app.application.dto.response.subscription_response import SubscriptionResponse
from app.domain.model.suscription import Suscription
from app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.application.mapper.subscription_request_mapper import SubscriptionRequestMapper
from app.application.mapper.suscription_response_mapper import SuscriptionResponseMapper



class SubscriptionHandler:

    def __init__(self, user_case: SubscriptionInputPort):
        self.user_case = user_case

    def create_subscription(self, request: SubscriptionRequest, token:str) -> Suscription:
        subscription = SubscriptionRequestMapper.to_domain(request)

        create_subscription = self.user_case.create_subscription(subscription, token)
        return create_subscription

    def get_by_customer_id(self, customer_id: str) -> SubscriptionResponse:
        subscription = self.user_case.get_by_customer_id(customer_id)
        response_dto = SuscriptionResponseMapper.to_response(subscription)
        return response_dto

    def cancel_subscription(self, subscription_id: str) -> Suscription:
        subscription = self.user_case.cancel_subscription(subscription_id)
        return subscription