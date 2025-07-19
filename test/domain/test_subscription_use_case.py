import unittest
from datetime import datetime
from unittest.mock import Mock

from app.domain.constants.domain_constans import DomainConstans
from app.domain.constants.subscription_status import SubscriptionStatus
from app.domain.model.suscription import Suscription
from app.domain.usecase.subscription_use_case import SubscriptionUseCase


class TestSubscriptionUseCase(unittest.TestCase):

    def setUp(self):
        self.mock_output_port = Mock()
        self.mock_notification_client = Mock()
        self.use_case = SubscriptionUseCase(
            output_port=self.mock_output_port,
            notification_client=self.mock_notification_client
        )
        self.token = 'bearer'

    def test_should_generate_subscription_id(self):
        subscription = Suscription(None, 'cust-001', 'fund-001', 1000, None, None)
        result = self.use_case.create_subscription(subscription, self.token)
        self.assertIsNotNone(result.subscription_id)

    def test_should_set_timestamp(self):
        subscription = Suscription(None, 'cust-001', 'fund-001', 1000, None, None)
        result = self.use_case.create_subscription(subscription, self.token)
        self.assertIsInstance(result.timestamp, datetime)

    def test_should_save_subscription(self):
        subscription = Suscription(None, 'cust-001', 'fund-001', 1000, None, None)
        result = self.use_case.create_subscription(subscription, self.token)
        self.mock_output_port.save.assert_called_once_with(result)

    def test_should_send_notification(self):
        subscription = Suscription(None, 'cust-001', 'fund-001', 1000, None, None)
        self.use_case.create_subscription(subscription, self.token)

        self.mock_notification_client.sendNotification.assert_called_once()
        args, _ = self.mock_notification_client.sendNotification.call_args
        actual_notification, actual_token = args
        self.assertEqual(actual_token, self.token)
        self.assertEqual(actual_notification.email, DomainConstans.DEFAULT_EMAIL)
        self.assertEqual(actual_notification.phone, DomainConstans.DEFAULT_PHONE)
        self.assertEqual(actual_notification.message, DomainConstans.DEFAULT_SUBJECT)






if __name__ == '__main__':
    unittest.main()
