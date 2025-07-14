from fastapi import APIRouter, status
from app.application.dto.request.subscription_request import SubscriptionRequest
from app.application.handler.subscription_handler import SubscriptionHandler
from app.infraestructure.input.response.generic_response import SuccessResponse, ErrorResponse
from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.config.dependency_injection import DependencyContainer

class SubscriptionRouter:

    def __init__(self):
        self.router = APIRouter(prefix="/subscription", tags=["subscription"])
        self._configure_routes()

    def _configure_routes(self):
        handler: SubscriptionHandler = DependencyContainer.subscription_handler()

        @self.router.post(
            path=MessaginRouting.CREATE_SUBSCRIPTION,
            status_code=status.HTTP_201_CREATED,
            response_model=SuccessResponse,
            responses={
                201: {"description": MessaginRouting.SUBSCRIPTION_SUCCESS, "model": SuccessResponse},
                400: {"description": MessaginRouting.INVALID_REQUEST_MESSAGE, "model": ErrorResponse},
                401: {"description": MessaginRouting.UNAUTHORIZED_MESSAGE, "model": ErrorResponse},
                404: {"description": MessaginRouting.RESOURCE_NOT_FOUND_MESSAGE, "model": ErrorResponse},
                422: {
                    "description": MessaginRouting.INVALID_REQUEST_MESSAGE,
                    "content": {
                        "application/json": {
                            "example": {
                                "message": MessaginRouting.INVALID_REQUEST_MESSAGE,
                                "error": "field -> name: field required"
                            }
                        }
                    }
                },
                500: {"description": MessaginRouting.INTERNAL_SERVER_ERROR_MESSAGE, "model": ErrorResponse},
            }
        )
        def create_subscription(request: SubscriptionRequest):
            handler.create_subscription(request)
            return SuccessResponse(message=MessaginRouting.SUBSCRIPTION_SUCCESS)

        @self.router.get(
            path=MessaginRouting.GET_SUBSCRIPTION_BY_ID,
            status_code=status.HTTP_200_OK,
            response_model=SuccessResponse,
            responses={
                200: {"description": MessaginRouting.SUBSCRIPTION_FOUND_MESSAGE, "model": SuccessResponse},
                400: {"description": MessaginRouting.INVALID_REQUEST_MESSAGE, "model": ErrorResponse},
                404: {"description": MessaginRouting.RESOURCE_NOT_FOUND_MESSAGE, "model": ErrorResponse},
                422: {
                    "description": MessaginRouting.INVALID_REQUEST_MESSAGE,
                    "content": {
                        "application/json": {
                            "example": {
                                "message": MessaginRouting.INVALID_REQUEST_MESSAGE,
                                "error": "field -> name: field required"
                            }
                        }
                    }
                },
                500: {"description": MessaginRouting.INTERNAL_SERVER_ERROR_MESSAGE, "model": ErrorResponse},
            }
        )
        def get_subscription(subscription_id: str):
            response_dto = handler.get_subscription_by_id(subscription_id)
            return SuccessResponse(
                message=MessaginRouting.SUBSCRIPTION_FOUND_MESSAGE,
                data=response_dto
            )

    def get_router(self):
        return self.router
