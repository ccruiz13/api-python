import boto3
from app.infraestructure.config.dynamo_tables import DynamoTableConfig
from app.infraestructure.out.dynamodb.entities.subscription_entity import SuscriptionEntity

class SubscriptionDynamoClient:

    def __init__(self):
        dynamodb = boto3.resource("dynamodb")
        table_name = DynamoTableConfig.get_subscription_table_name()
        self.table = dynamodb.Table(table_name)

    def save(self, entity: SuscriptionEntity) -> None:
        """Guarda una suscripción en DynamoDB."""
        self.table.put_item(Item=entity.model_dump())


    def get_by_id(self, subscription_id: str) -> dict | None:
        """Consulta una suscripción por su ID."""
        response = self.table.get_item(Key={"subscription_id": subscription_id})
        return response.get("Item")



