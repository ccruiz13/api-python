import os
import httpx
from app.domain.model.request.Notification import Notification
from app.domain.ports.output.api_client_output import ApiClient
from app.infraestructure.exception.missing_configuration_exception import MissingConfigurationException


class NotificationAdapter(ApiClient):

    def __init__(self):
        url = os.getenv("BASE_URL")
        node_port = os.getenv("NODE_RUTE")

        self.notifacion_url =  f"{url}:{node_port}/notifications"

    def sendNotification(self, notification: Notification) -> None:
        print('URL de notificaciones ' , self.notifacion_url)
        payload = {
            "email": notification.email,
            "phone": notification.phone,
            "message": notification.message
        }
        try:
            response = httpx.post(self.notifacion_url, json=payload)
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise MissingConfigurationException(f"Error al enviar notificación: {e}")

