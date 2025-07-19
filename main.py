from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from fastapi.security import HTTPBearer
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from app.infraestructure.input.rest.subscription_router import SubscriptionRouter
from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.config.exception_configurator import ExceptionConfigurator
from app.infraestructure.security.auth_validator import AuthValidator

load_dotenv()

security_scheme = HTTPBearer()

app = FastAPI(
    title=MessaginRouting.TITLE,
    version=MessaginRouting.VERSION,
    description=MessaginRouting.DESCRIPTION,
    swagger_ui_oauth2_redirect_url=None,  # evita errores de oauth2 redirect
    openapi_tags=[],
    dependencies=[Depends(security_scheme)]
)

# Rutas
subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)

# Excepciones
ExceptionConfigurator.register(app)
app.middleware("http")(AuthValidator())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
