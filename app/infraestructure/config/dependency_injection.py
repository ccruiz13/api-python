from app.application.handler.subscription_handler import SubscriptionHandler
from app.domain.ports.input.input_suscription_port import SubscriptionInputPort
from app.domain.ports.output.output_suscription_port import OutputSuscriptionPort
from app.domain.usecase.subscription_use_case import SubscriptionUseCase
from app.infraestructure.out.dynamodb.adapter.subscription_adapter import SubscriptionAdapter

class DependencyContainer:
    """Contenedor de dependencias para instanciar servicios."""

    @classmethod
    def subscription_handler(cls) -> SubscriptionHandler:
        repository: OutputSuscriptionPort = SubscriptionAdapter()
        use_case: SubscriptionInputPort = SubscriptionUseCase(repository)
        return SubscriptionHandler(use_case)