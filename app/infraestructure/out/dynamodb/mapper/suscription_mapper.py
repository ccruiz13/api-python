from app.domain.model.suscription import Suscription
from  app.infraestructure.out.dynamodb.entities.subscription_entity import  SuscriptionEntity

class SubscriptionMapper:

    @staticmethod
    def to_entity(suscription: Suscription) -> SuscriptionEntity:
        return SuscriptionEntity(
            subscription_id=suscription.subscription_id,
            customer_id=suscription.customer_id,
            fund_id=suscription.fund_id,
            amount=suscription.amount,
            timestamp=suscription.timestamp.isoformat()
        )

    @staticmethod
    def to_domain(entity: SuscriptionEntity) -> Suscription:
        return Suscription(
            subscription_id=entity.subscription_id,
            customer_id=entity.customer_id,
            fund_id=entity.fund_id,
            amount=entity.amount,
            timestamp=entity.timestamp
        )
