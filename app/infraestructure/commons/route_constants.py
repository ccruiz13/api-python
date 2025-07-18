class MessaginRouting:
    PREFIX = "/subscriptions"
    TAG = "Subscriptions"
    CREATE_SUBSCRIPTION = "/create_subscription"
    GET_CUSTOMER_BY_ID = "/{customer_id}"
    CANCEL_SUBSCRIPTION = "/canceled_subscription/{customer_id}"
    CREATE_SUBSCRIPTION_NAME = "create-subscription"
    TITLE = "API de Gestión de Fondos de Inversión"
    VERSION = "1.0.0"
    DESCRIPTION = "API para la gestión de suscripciones a fondos de inversión, incluyendo la creación de suscripciones y la validación de datos."

    #-- Mensajes de respuestas --
    SUBSCRIPTION_SUCCESS="Se ha creado suscripción exitosamente"
    INVALID_REQUEST_MESSAGE= "Solicitud inválida"
    SUBSCRIPTION_CREATION_ERROR_MESSAGE="Error al crear la suscripción"
    UNEXPECTED_SUBSCRIPTION_CREATION_ERROR_MESSAGE="Error inesperado al crear la suscripción"
    UNAUTHORIZED_MESSAGE="No autorizado"
    RESOURCE_NOT_FOUND_MESSAGE="Recurso no encontrado"
    INTERNAL_SERVER_ERROR_MESSAGE="Error interno del servidor"
    SUBSCRIPTION_FOUND_MESSAGE = "Suscripción encontrada exitosamente",
    SUBSCRIPTION_CANCELLED_MESSAGE="Suscripcion cancelada exitosamente"

    #constantes twilio
    # app/infraestructure/out/constants/notification_constants.py

    DEFAULT_EMAIL = "cliente@btg.com"
    DEFAULT_PHONE = "+573001234567"
    DEFAULT_SUBJECT = "Notificación de Suscripción BTG Funds"








