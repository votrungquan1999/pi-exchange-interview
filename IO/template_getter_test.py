import unittest
from unittest.mock import Mock
import template_getter


class MyTestCase(unittest.TestCase):
	def test_LocalFileTemplateGetter_GetTemplate(self):
		json_loader = Mock(return_value={"data": "data"})
		file_opener = Mock(return_value='{"data": "data"}')

		getter = template_getter.LocalFileTemplateGetter("./abc.json", json_loader, file_opener)
		result = getter.get_template()

		json_loader.assert_called_with("./abc.json")
		file_opener.assert_called_with('{"data": "data"}')

		self.assertEqual(result, {"data": "data"})


if __name__ == '__main__':
	unittest.main()
