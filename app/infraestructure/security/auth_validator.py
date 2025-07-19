import httpx
from fastapi import Request, Response
from fastapi.responses import JSONResponse

from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.input.response.generic_response import ErrorResponse


class AuthValidator:
    """
    Middleware personalizado para validar JWT usando el servicio Java.
    """

    def __init__(self):
        url = os.getenv("BASE_URL")
        node_port = os.getenv("NODE_RUTE")
        self.decode_url = decode_url

    async def __call__(self, request: Request, call_next) -> Response:
        # Permitir rutas públicas (ej. documentación)
        if request.url.path.startswith(MessaginRouting.DOCS_URL) or request.url.path.startswith(MessaginRouting.OPENAPI_URL):
            return await call_next(request)

        #Token
        auth_header = request.headers.get(MessaginRouting.AUTHORIZATION_HEADER)
        if not auth_header or not auth_header.startswith(MessaginRouting.BEARER_PREFIX):
            return JSONResponse(status_code=401, content=ErrorResponse(message=MessaginRouting.INVALID_TOKEN_ERROR, error='').dict())

        token = auth_header.replace(MessaginRouting.BEARER_PREFIX, '')

        try:
            response = httpx.get(
                self.decode_url,
                headers={"Authorization": f"Bearer {token}"},
                timeout=5.0
            )
            response.raise_for_status()
            user_info = response.json().get('data')

            # Guardar usuario en el request (opcional)
            request.state.user = user_info

        except httpx.HTTPStatusError as e:
            return JSONResponse(status_code=401,
                                content=ErrorResponse(message=MessaginRouting.INVALID_TOKEN_ERROR, error=str(e)).dict())
        except httpx.RequestError as e:
            return JSONResponse(status_code=500,
                                content=ErrorResponse(
                                    message=MessaginRouting.INTERNAL_SERVER_ERROR_MESSAGE,
                                    error=str(e)
                                ).dict())

        return await call_next(request)