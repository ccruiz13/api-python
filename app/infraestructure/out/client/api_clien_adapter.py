import os
from app.domain.model.request.Notification import Notification
from app.domain.ports.output.api_client_output import ApiClient

class NotificationAdapter(ApiClient):

    def __init__(self):
        url = os.getenv("BASE_URL")
        node_port = os.getenv("NODE_RUTE")
        java_port = os.getenv("JAVA_RUTE")

    def sendNotification(self, notification: Notification) -> None: