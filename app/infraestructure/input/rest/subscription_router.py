from fastapi import APIRouter, status
from app.application.dto.request.subscription_request import SubscriptionRequest
from app.application.handler.subscription_handler import SubscriptionHandler
from app.infraestructure.commons.route_constants import SubscriptionRoute
from app.infraestructure.config.dependency_injection import DependencyContainer

class SubscriptionRouter:

    def __init__(self):
        self.router = APIRouter(prefix="/subscription", tags=["subscription"])
        self._configure_routes()

    def _configure_routes(self):
        handler = DependencyContainer.subscription_handler()

        @self.router.post(
            path=SubscriptionRoute.CREATE_SUBSCRIPTION,
            status_code=status.HTTP_201_CREATED,
            response_model=SubscriptionRequest
        )
        def create_subscription(request: SubscriptionRequest):
            return handler.create_subscription(request)

    def get_router(self):
        return self.router
