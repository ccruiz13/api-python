from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.exceptions import RequestValidationError

from app.infraestructure.commons.error_handler import ErrorHandler
from app.infraestructure.input.rest.subscription_router import SubscriptionRouter
from app.infraestructure.commons.route_constants import MessaginRouting

load_dotenv()

app = FastAPI(
    title=MessaginRouting.TITLE,
    version=MessaginRouting.VERSION,
    description=MessaginRouting.DESCRIPTION
)
app.add_exception_handler(RequestValidationError, ErrorHandler.validation_exception_handler)
subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)