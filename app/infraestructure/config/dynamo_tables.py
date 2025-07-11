import os
from app.infraestructure.exception.MissingConfigurationException import MissingConfigurationException

class DynamoTableConfig:
    @staticmethod
    def get_subscription_table_name() -> str:
        name = os.getenv("SUBSCRIPTION_TABLE_NAME", "customer_fund_subscription")
        if not name:
            raise MissingConfigurationException("SUBSCRIPTION_TABLE_NAME")
        return name
