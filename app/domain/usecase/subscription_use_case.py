from app.domain.model.suscription import Suscription
from  app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.domain.ports.output.output_suscription_port import OutputSuscriptionPort
from datetime import datetime
import uuid

class SubscriptionUseCase(SubscriptionInputPort):
    def __init__(self, output_port: OutputSuscriptionPort):
        self.output_port = output_port


    def create_subscription(self, subscription: Suscription) -> Suscription:
        """
        Save a subscription to the output port.

        :param subscription: The subscription object to be saved.
        :return: The saved subscription object.
        """
        subscription.subscription_id = str(uuid.uuid4())
        subscription.timestamp = datetime.now()
        self.output_port.save(subscription)
        return subscription