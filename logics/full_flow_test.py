import unittest
from unittest.mock import Mock

from logics import full_flow


class MyTestCase(unittest.TestCase):
	def test_FullFlow_ExecuteFlow(self):
		template_getter = Mock()
		template_getter.get_template = Mock(return_value="template")
		customers_getter = Mock()
		customers_getter.get_customers = Mock(return_value="customers")
		email_processor = Mock()
		email_processor.process_email_template = Mock(return_value=("output", "error"))
		email_sender = Mock()
		email_sender.send_email = Mock()

		mock_full_flow = full_flow.FullFlow(template_getter, customers_getter, email_processor, email_sender)
		mock_full_flow.execute_flow()

		template_getter.get_template.assert_called_once()
		customers_getter.get_customers.assert_called_once()
		email_processor.process_email_template.assert_called_with("customers", "template")
		email_sender.send_email.assert_called_with("output", "error")


if __name__ == '__main__':
	unittest.main()
