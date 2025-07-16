from abc import ABC, abstractmethod

from app.domain.model.request.Notification import Notification


class ApiClient(ABC):
    @abstractmethod
    def sendNotification(self, notification: Notification) -> None:
        pass
