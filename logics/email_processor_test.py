import datetime
import unittest
from unittest.mock import Mock

import email_processor


class MyTestCase(unittest.TestCase):
	def test_EmailProcessor_ProcessEmailTemplate_HappyCase(self):
		test_cases = [
			{
				"name": "customer without email",
				"template": {},
				"customers": [{}],
				"expected_output": [],
				"expected_error_customers": [{}]
			},
			{
				"name": "will auto fill title, first_name, last_name",
				"template": {
					"from": "from",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}}"
				},
				"customers": [{
					"TITLE": "Mr",
					"FIRST_NAME": "Quan",
					"LAST_NAME": "Vo",
					"EMAIL": "quan@gmail.com"
				}],
				"expected_output": [{
					"from": "from",
					"to": "quan@gmail.com",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am Mr Quan Vo"
				}],
				"expected_error_customers": []
			},
			{
				"name": "will also auto fill today",
				"template": {
					"from": "from",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}} and today is {{TODAY}}"
				},
				"customers": [{
					"TITLE": "Mr",
					"FIRST_NAME": "Quan",
					"LAST_NAME": "Vo",
					"EMAIL": "quan@gmail.com"
				}],
				"expected_output": [{
					"from": "from",
					"to": "quan@gmail.com",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am Mr Quan Vo and today is 01 Jan 2021"
				}],
				"expected_error_customers": []
			},
			{
				"name": "return empty string for missing fields in template",
				"template": {},
				"customers": [{
					"TITLE": "Mr",
					"FIRST_NAME": "Quan",
					"LAST_NAME": "Vo",
					"EMAIL": "quan@gmail.com"
				}],
				"expected_output": [{
					"from": "",
					"to": "quan@gmail.com",
					"subject": "",
					"mimeType": "",
					"body": ""
				}],
				"expected_error_customers": []
			}
		]

		for test in test_cases:
			get_date = Mock(return_value=datetime.date(2021, 1, 1))
			test_email_processor = email_processor.EmailProcessor(get_date)

			output, error_customers = test_email_processor.process_email_template(test["customers"], test["template"])

			self.assertEqual(error_customers, test["expected_error_customers"])
			self.assertEqual(output, test["expected_output"])

	def test_EmailProcessor_ProcessEmailTemplate_DirtyCase(self):
		test_cases = [
			{
				"name": "will also auto fill today",
				"template": {
					"from": "from",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}} and today is {{TODAY}}"
				},
				"customers": [{
					"FIRST_NAME": "Quan",
					"LAST_NAME": "Vo",
					"EMAIL": "quan@gmail.com"
				}],
				"expect_error": "TITLE is missing in customer"
			},
			{
				"name": "will also auto fill today",
				"template": {
					"from": "from",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}} and today is {{TODAY}}"
				},
				"customers": [{
					"TITLE": "Mr",
					"LAST_NAME": "Vo",
					"EMAIL": "quan@gmail.com"
				}],
				"expect_error": "FIRST_NAME is missing in customer"
			},
			{
				"name": "will also auto fill today",
				"template": {
					"from": "from",
					"subject": "subject",
					"mimeType": "mimetypes",
					"body": "I am {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}} and today is {{TODAY}}"
				},
				"customers": [{
					"TITLE": "Mr",
					"FIRST_NAME": "Quan",
					"EMAIL": "quan@gmail.com"
				}],
				"expect_error": "LAST_NAME is missing in customer"
			},
		]
		for test in test_cases:
			get_date = Mock(return_value=datetime.date(2021, 1, 1))
			test_email_processor = email_processor.EmailProcessor(get_date)

			try:
				test_email_processor.process_email_template(test["customers"], test["template"])
				self.assertEqual(1, 2, "this test suppose to throw error")
			except ValueError as err:
				self.assertEqual(str(err), test["expect_error"])


if __name__ == '__main__':
	unittest.main()
