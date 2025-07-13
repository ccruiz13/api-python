from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.input.response.generic_response import ErrorResponse

class ErrorHandler:
    ERROR_NAME = "Error de validación"

    @staticmethod
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        error_details = exc.errors()
        error_messages = []

        for err in error_details:
            loc = " -> ".join(str(loc) for loc in err.get("loc", []))
            msg = err.get("msg", ErrorHandler.ERROR_NAME)
            error_messages.append(f"{loc}: {msg}")

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ErrorResponse(
                message=MessaginRouting.INVALID_REQUEST_MESSAGE,
                error="; ".join(error_messages)
            ).dict()
        )