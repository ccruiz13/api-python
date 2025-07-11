from fastapi import FastAPI
from app.infraestructure.input.rest.subscription_router import SubscriptionRouter
from app.infraestructure.commons.route_constants import SubscriptionRoute

app = FastAPI(
    title=SubscriptionRoute.TITLE,
    version=SubscriptionRoute.VERSION,
    description=SubscriptionRoute.DESCRIPTION
)

subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)

subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)