from abc import ABC, abstractmethod
from app.domain.model.suscription import Suscription


class SubscriptionInputPort(ABC):

    @abstractmethod
    def create_subscription(self, subscription: Suscription, token:str) -> Suscription:
        pass

    @abstractmethod
    def get_by_customer_id(self, customer_id: str) -> Suscription:
        pass

    @abstractmethod
    def cancel_subscription(self, customer_id: str) -> Suscription:
        pass

