from abc import ABC, abstractmethod
from app.domain.model.suscription import Suscription

class OutputSuscriptionPort(ABC):

    @abstractmethod
    def save(self, suscription: Suscription) -> None:
        pass

    @abstractmethod
    def get_by_customer_id(self, customer_id: str) -> Suscription | None:
        pass
