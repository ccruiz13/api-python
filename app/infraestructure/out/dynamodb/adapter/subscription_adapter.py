from app.domain.model.suscription import Suscription
from app.domain.ports.output.output_suscription_port import OutputSuscriptionPort
from app.infraestructure.out.dynamodb.client.suscription_dynamo_client import SubscriptionDynamoClient
from app.infraestructure.out.dynamodb.mapper.suscription_mapper import SubscriptionMapper


class SubscriptionAdapter(OutputSuscriptionPort):

    def __init__(self):
        self.client = SubscriptionDynamoClient()

    def save(self, suscription: Suscription) -> None:
        entity = SubscriptionMapper.to_entity(suscription)
        self.client.save(entity)

    def get_by_customer_id(self, customer_id: str) -> Suscription | None:
        item = self.client.get_by_customer_id(customer_id)
        if item:
            return SubscriptionMapper.to_domain(item)
        return None

    def cancel_subscription(self, customer_id: str) -> Suscription | None:
        item = self.client.cancel_subscription(customer_id)
        if item:
            return SubscriptionMapper.to_domain(item)
        return None
