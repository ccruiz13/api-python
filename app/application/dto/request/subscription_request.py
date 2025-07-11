from pydantic import BaseModel, Field
from  app.application.util.swagger_constants import SwaggerConstants
from decimal import Decimal

class SubscriptionRequest(BaseModel):
    customer_id: str = Field(
        ...,
        description=SwaggerConstants.CUSTOMER_ID_DESCRIPTION,
        example=SwaggerConstants.CUSTOMER_ID_EXAMPLE
    )
    fund_id: str = Field(
        ...,
        description=SwaggerConstants.FUND_ID_DESCRIPTION,
        example=SwaggerConstants.FUND_ID_EXAMPLE
    )
    amount: Decimal = Field(
        ...,
        description=SwaggerConstants.AMOUNT_DESCRIPTION,
        example=SwaggerConstants.AMOUNT_EXAMPLE
    )
