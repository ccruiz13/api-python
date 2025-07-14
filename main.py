from fastapi import FastAPI
from dotenv import load_dotenv

from app.infraestructure.input.rest.subscription_router import SubscriptionRouter
from app.infraestructure.commons.route_constants import MessaginRouting
from app.infraestructure.config.exception_configurator import ExceptionConfigurator

load_dotenv()

app = FastAPI(
    title=MessaginRouting.TITLE,
    version=MessaginRouting.VERSION,
    description=MessaginRouting.DESCRIPTION
)

# Rutas
subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)

# Excepciones
ExceptionConfigurator.register(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
