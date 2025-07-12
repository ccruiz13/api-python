import os
from app.infraestructure.exception.MissingConfigurationException import MissingConfigurationException

import os

import os

class DynamoTableConfig:
    @staticmethod
    def get_subscription_table_name() -> str:
        table_name = os.getenv("SUBSCRIPTION_TABLE_NAME")
        if not table_name:
            raise RuntimeError("Missing environment variable: SUBSCRIPTION_TABLE_NAME")
        return table_name

