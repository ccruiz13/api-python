from fastapi import FastAPI
from mangum import Mangum
from dotenv import load_dotenv
import os

from app.infraestructure.input.rest.subscription_router import SubscriptionRouter
from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.config.exception_configurator import ExceptionConfigurator
from app.infraestructure.security.auth_validator import AuthValidator

# Si bien dotenv no es obligatorio en Lambda, lo dejamos por compatibilidad local
load_dotenv()

# Inicializa la app FastAPI
app = FastAPI(
    title=MessaginRouting.TITLE,
    version=MessaginRouting.VERSION,
    description=MessaginRouting.DESCRIPTION
)

# Rutas protegidas por token
subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)

# Configurar manejo de excepciones
ExceptionConfigurator.register(app)

# Middleware para validar token llamando al decode en Java
app.middleware("http")(AuthValidator())

# Handler para AWS Lambda con Mangum
handler = Mangum(app)

# Para desarrollo local (opcional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PYTHON_RUTE", 8000)), reload=True)
