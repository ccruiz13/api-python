import unittest
from unittest.mock import Mock

from app.domain.usecase.subscription_use_case import SubscriptionUseCase


class TestSubscriptionUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_output_port = Mock()
        self.mock.notification_client = Mock()
        self.use_case = SubscriptionUseCase(output_port= self.mock_output_port,
                                            notification_client = self.mock_output_port)
        self.token = 'bearer'



if __name__ == '__main__':
    unittest.main()
