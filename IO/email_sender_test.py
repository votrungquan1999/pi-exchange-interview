import unittest
import email_sender
from unittest.mock import Mock


class MyTestCase(unittest.TestCase):
	def test_LocalEmailSender_SendEmail(self):
		file_opener = Mock(return_value='this is a file')

		mock_json_writer = Mock()
		mock_csv_writer = Mock()
		mock_csv_writer.writerows = Mock()
		mock_csv_writer.writeheader = Mock()
		csv_writer = Mock(return_value=mock_csv_writer)

		test_email_sender = email_sender.LocalEmailSender(
			"./output/",
			"./errors/customers.csv",
			file_opener,
			csv_writer,
			mock_json_writer
		)

		test_email_sender.send_email([{"abc": "def"}], [{"email": "quan.test@gmail.com"}])

		file_opener.assert_any_call('./output/0.json', 'w')
		file_opener.assert_any_call('./errors/customers.csv', 'w')

		csv_writer.assert_called_with('this is a file', ["TITLE", "FIRST_NAME", "LAST_NAME", "EMAIL"])
		mock_csv_writer.writeheader.assert_called_once()
		mock_csv_writer.writerows.asser_called_with([{"email": "quan.test@gmail.com"}])
		mock_json_writer.assert_called_with({"abc": "def"}, 'this is a file')


if __name__ == '__main__':
	unittest.main()
