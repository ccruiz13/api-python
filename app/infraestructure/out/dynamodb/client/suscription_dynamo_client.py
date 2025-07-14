import boto3
import os

from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv

from app.domain.constants.subscription_status import SubscriptionStatus
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

    def get_by_customer_id(self, customer_id: str) -> SuscriptionEntity | None:
        response = self.table.query(
            IndexName="customer_id-index",
            KeyConditionExpression=Key("customer_id").eq(customer_id)
        )
        items = response.get("Items", [])
        if not items:
            return None
        return SuscriptionEntity(**items[0])

    def cancel_subscription(self, subscription_id: str) -> SuscriptionEntity | None:

        original = self.table.get_item(Key={"subscription_id": subscription_id})
        item = original.get("Item")

        if not item:
            return None  # No existe

        item["status"] = SubscriptionStatus.CANCELLED.value

        self.table.put_item(Item=item)

        return SuscriptionEntity(**item)



