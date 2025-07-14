from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError

from app.domain.exception.domain_exception import DomainConfigurationException
from app.infraestructure.exception.missing_configuration_exception import MissingConfigurationException
from app.infraestructure.commons.error_handler import ErrorHandler
from app.infraestructure.commons.route_constants import MessaginRouting


class ExceptionConfigurator:
    @classmethod
    def register(cls, app: FastAPI):
        app.add_exception_handler(
            RequestValidationError,
            ErrorHandler.validation_exception_handler
        )
        app.add_exception_handler(
            DomainConfigurationException,
            ErrorHandler.async_handler_with_message(
                MessaginRouting.RESOURCE_NOT_FOUND_MESSAGE,
                status.HTTP_404_NOT_FOUND
            )
        )
        app.add_exception_handler(
            MissingConfigurationException,
            ErrorHandler.async_handler_with_message(
                MessaginRouting.SUBSCRIPTION_CREATION_ERROR_MESSAGE,
                status.HTTP_400_BAD_REQUEST
            )
        )
        app.add_exception_handler(
            Exception,
            ErrorHandler.async_handler_with_message(
                MessaginRouting.UNEXPECTED_SUBSCRIPTION_CREATION_ERROR_MESSAGE,
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        )
