import unittest
from datetime import datetime
from unittest.mock import Mock

from app.domain.constants.domain_constans import DomainConstans
from app.domain.constants.subscription_status import SubscriptionStatus
from app.domain.exception.domain_exception import DomainConfigurationException
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

    def test_should_return_subscription_when_customer_exists(self):
        customer_id = 'cust-001'
        expected_subscription = Suscription(
            subscription_id='abc-123',
            customer_id=customer_id,
            fund_id='fund-001',
            amount=1000,
            timestamp=None,
            status='ACTIVE'
        )
        self.mock_output_port.get_by_customer_id.return_value = expected_subscription

        result = self.use_case.get_by_customer_id(customer_id)

        self.assertEqual(result, expected_subscription)

    def test_should_raise_exception_when_customer_not_found(self):
        customer_id = 'not-found'
        self.mock_output_port.get_by_customer_id.return_value = None

        with self.assertRaises(DomainConfigurationException) as context:
            self.use_case.get_by_customer_id(customer_id)
        self.assertEqual(str(context.exception), f"Missing configuration for: {customer_id}")


def test_should_cancel_subscription_successfully(self):

    customer_id = 'cust-001'
    cancelled_subscription = Suscription(
        subscription_id='abc-123',
        customer_id=customer_id,
        fund_id='fund-001',
        amount=1000,
        timestamp=None,
        status='CANCELLED'
    )
    self.mock_output_port.cancel_subscription.return_value = cancelled_subscription

    result = self.use_case.cancel_subscription(customer_id)

    self.assertEqual(result, cancelled_subscription)


def test_should_raise_exception_when_cancelling_nonexistent_subscription(self):

    customer_id = 'not-found'
    self.mock_output_port.cancel_subscription.return_value = None
    
    with self.assertRaises(DomainConfigurationException) as context:
        self.use_case.cancel_subscription(customer_id)

    self.assertEqual(str(context.exception), f"Missing configuration for: {customer_id}")


if __name__ == '__main__':
    unittest.main()
