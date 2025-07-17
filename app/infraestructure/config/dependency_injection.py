from app.application.handler.subscription_handler import SubscriptionHandler
from app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.domain.ports.output.api_client_output import ApiClient
from app.domain.ports.output.output_suscription_port import OutputSuscriptionPort
from app.domain.usecase.subscription_use_case import SubscriptionUseCase
from app.infraestructure.out.client.api_clien_adapter import NotificationAdapter
from app.infraestructure.out.dynamodb.adapter.subscription_adapter import SubscriptionAdapter

class DependencyContainer:
    """Contenedor de dependencias para instanciar servicios."""

    @classmethod
    def subscription_handler(cls) -> SubscriptionHandler:
        repository: OutputSuscriptionPort = SubscriptionAdapter()
        notification_client = ApiClient = NotificationAdapter()
        use_case: SubscriptionInputPort = SubscriptionUseCase(repository, notification_client   )
        return SubscriptionHandler(use_case)