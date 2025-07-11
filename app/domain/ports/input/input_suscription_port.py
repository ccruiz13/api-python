from abc import ABC, abstractmethod
from app.domain.model.suscription import Suscription


class SubscriptionInputPort(ABC):

    @abstractmethod
    def create_subscription(self, subscription: Suscription) -> Suscription:
        pass

