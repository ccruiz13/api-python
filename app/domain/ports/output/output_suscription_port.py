from abc import ABC, abstractmethod
from app.domain.model.suscription import Suscription

class OutputSuscriptionPort(ABC):

    @abstractmethod
    def save(self, suscription: Suscription) -> None:
        pass

    @abstractmethod
    def find_by_id(self, subscription_id: str) -> Suscription | None:
        pass
