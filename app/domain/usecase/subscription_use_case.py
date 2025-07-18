from app.domain.constants.domain_constans import DomainConstans
from app.domain.constants.subscription_status import SubscriptionStatus
from app.domain.model.request.Notification import Notification
from app.domain.model.suscription import Suscription
from  app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.domain.ports.output.api_client_output import ApiClient
from app.domain.ports.output.output_suscription_port import OutputSuscriptionPort
from datetime import datetime
from app.domain.exception.domain_exception import DomainConfigurationException
import uuid

class SubscriptionUseCase(SubscriptionInputPort):


    def __init__(self, output_port: OutputSuscriptionPort, notification_client: ApiClient):
        self.output_port = output_port
        self.notification_client = notification_client


    def create_subscription(self, subscription: Suscription) -> Suscription:
        """
        Save a subscription to the output port.

        :param subscription: The subscription object to be saved.
        :return: The saved subscription object.
        """
        subscription.subscription_id = str(uuid.uuid4())
        subscription.timestamp = datetime.now()
        subscription.status = SubscriptionStatus.ACTIVE
        self.output_port.save(subscription)
        notification = Notification(email=DomainConstans.DEFAULT_EMAIL,
                                    phone=DomainConstans.DEFAULT_PHONE,
                                    message=DomainConstans.DEFAULT_SUBJECT)
        self.notification_client.sendNotification(notification)
        return subscription

    def get_by_customer_id(self, customer_id: str) -> Suscription | None:
        """
        Retrieve a subscription from the output port by its ID.

        :param customer_id: The unique identifier of the subscription to be retrieved.
        :return: The subscription object if found, otherwise None.
        """
        subscription = self.output_port.get_by_customer_id(customer_id)
        if not subscription:
            raise DomainConfigurationException(customer_id)
        return subscription

    def cancel_subscription(self, customer_id: str) -> Suscription:
        """
            Cancela una suscripción actualizando su estado a CANCELLED en DynamoDB.

            :param customer_id: El identificador único de la suscripción a cancelar.
            :return: el modelo Suscription actualizada si existe, de lo contrario None.
            """
        subscription = self.output_port.cancel_subscription(customer_id)
        if not subscription:
            raise DomainConfigurationException(customer_id)
        return subscription



