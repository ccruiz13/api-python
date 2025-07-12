from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from app.application.dto.request.subscription_request import SubscriptionRequest
from app.application.handler.subscription_handler import SubscriptionHandler
from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.config.dependency_injection import DependencyContainer
from app.infraestructure.input.response.generic_response import SuccessResponse, ErrorResponse
from app.infraestructure.exception.MissingConfigurationException import MissingConfigurationException


class SubscriptionRouter:

    def __init__(self):
        self.router = APIRouter(prefix="/subscription", tags=["subscription"])
        self._configure_routes()

    def _configure_routes(self):
        handler = DependencyContainer.subscription_handler()

        @self.router.post(
            path=MessaginRouting.CREATE_SUBSCRIPTION,
            status_code=status.HTTP_201_CREATED,
            response_model=SuccessResponse,
            responses={
                201: {"description": MessaginRouting.SUBSCRIPTION_SUCCESS, "model": SuccessResponse},
                400: {"description": MessaginRouting.INVALID_REQUEST_MESSAGE, "model": ErrorResponse},
                401: {"description": MessaginRouting.UNAUTHORIZED_MESSAGE, "model": ErrorResponse},
                404: {"description": MessaginRouting.RESOURCE_NOT_FOUND_MESSAGE, "model": ErrorResponse},
                500: {"description": MessaginRouting.INTERNAL_SERVER_ERROR_MESSAGE, "model": ErrorResponse},
            }
        )
        def create_subscription(request: SubscriptionRequest):
            try:
                handler.create_subscription(request)
                return SuccessResponse(message=MessaginRouting.SUBSCRIPTION_SUCCESS)
            except MissingConfigurationException as e:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content=ErrorResponse(
                        message=MessaginRouting.SUBSCRIPTION_CREATION_ERROR_MESSAGE,
                        error=str(e)
                    ).dict())
            except Exception as e:
                return JSONResponse(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content=ErrorResponse(
                        message=MessaginRouting.UNEXPECTED_SUBSCRIPTION_CREATION_ERROR_MESSAGE,
                        error = str(e)
                ).dict())

        def get_router(self):
            return self.router
