import boto3
import os
from dotenv import load_dotenv
from app.infraestructure.config.dynamo_tables import DynamoTableConfig
from app.infraestructure.out.dynamodb.entities.subscription_entity import SuscriptionEntity

load_dotenv()

class SubscriptionDynamoClient:
    def __init__(self):
        aws_region = os.getenv("AWS_REGION")
        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        if not aws_region or not aws_access_key or not aws_secret_key:
            raise RuntimeError("Missing one or more AWS environment variables.")

        # Inicializa el cliente DynamoDB con las credenciales del .env
        dynamodb = boto3.resource(
            "dynamodb",
            region_name=aws_region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        table_name = DynamoTableConfig.get_subscription_table_name()
        self.table = dynamodb.Table(table_name)


    def save(self, entity: SuscriptionEntity) -> None:
        """Guarda una suscripción en DynamoDB."""
        self.table.put_item(Item=entity.to_item())

    def get_by_id(self, subscription_id: str) -> dict | None:
        """Consulta una suscripción por su ID."""
        response = self.table.get_item(Key={"subscription_id": subscription_id})
        return response.get("Item")
