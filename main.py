from fastapi import FastAPI
from dotenv import load_dotenv
from app.infraestructure.input.rest.subscription_router import SubscriptionRouter
from app.infraestructure.commons.route_constants import SubscriptionRoute

load_dotenv()

app = FastAPI(
    title=SubscriptionRoute.TITLE,
    version=SubscriptionRoute.VERSION,
    description=SubscriptionRoute.DESCRIPTION
)

subscription_router = SubscriptionRouter().get_router()
app.include_router(subscription_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)