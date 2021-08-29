import unittest
from unittest.mock import Mock

import customers_getter


class MyTestCase(unittest.TestCase):
	def test_LocalFileCustomersGetter_GetCustomers(self):
		file_opener = Mock(return_value="some csv value")
		csv_reader = Mock(return_value=[{"key1": "value1"}, {"key2": "value2"}])

		mock_customer_getter = customers_getter.LocalFileCustomersGetter("./abc.csv", file_opener, csv_reader)
		result = mock_customer_getter.get_customers()

		file_opener.assert_called_with("./abc.csv")
		csv_reader.assert_called_with("some csv value")

		self.assertEqual(result, [{"key1": "value1"}, {"key2": "value2"}])


if __name__ == '__main__':
	unittest.main()
