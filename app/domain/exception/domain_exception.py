class DomainConfigurationException(Exception):
    """
    Exception raised when a required configuration is missing.
    """
    def __init__(self, variable_name: str):
        """
        Initialize the exception with the name of the missing configuration variable.

        :param variable_name: The name of the missing configuration variable.
        """
        super().__init__(f"Missing configuration for: {variable_name}")

