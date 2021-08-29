import csv


class CustomersGetter:
	def get_customers(self):
		pass


class LocalFileCustomersGetter(CustomersGetter):
	def __init__(self, path: str, file_opener, csv_dict_reader):
		self.__path = path
		self.__file_opener = file_opener
		self.__csv_dict_reader = csv_dict_reader

	def get_customers(self):
		customers = []

		f = self.__file_opener(self.__path)
		data = self.__csv_dict_reader(f)
		for row in data:
			customers.append(row)

		return customers


def new_local_file_customers_getter(path: str):
	return LocalFileCustomersGetter(path, open, csv.DictReader)
