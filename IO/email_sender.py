import csv
import json


def new_local_email_sender(path_to_output: str, path_to_error_user: str):
	return LocalEmailSender(path_to_output, path_to_error_user, open, csv.DictWriter, json.dump)


class EmailSender:
	def send_email(self, formatted_payload: [], error_customers: []):
		pass


class LocalEmailSender(EmailSender):
	def __init__(self, path_to_output: str, path_to_error_user: str, file_opener, csv_writer, json_writer):
		self.__path_to_output = path_to_output
		self.__path_to_error_customers = path_to_error_user
		self.__file_opener = file_opener
		self.__csv_writer = csv_writer
		self.__json_writer = json_writer

	def send_email(self, formatted_payload: [], error_customers: []):
		self.__write_error_customers(error_customers)
		self.__write_output(formatted_payload)

	def __write_error_customers(self, error_customers: []):
		field_names = ["TITLE", "FIRST_NAME", "LAST_NAME", "EMAIL"]

		f = self.__file_opener(self.__path_to_error_customers, 'w')

		writer = self.__csv_writer(f, field_names)
		writer.writeheader()
		writer.writerows(error_customers)

	def __write_output(self, formatted_payload: []):
		for index in range(len(formatted_payload)):
			file_content = formatted_payload[index]

			path = self.__path_to_output + str(index) + ".json"
			# print(path)
			f = self.__file_opener(path, 'w')

			self.__json_writer(file_content, f)
# f = open()
# with self.__file_opener(self.__path_to_error_customers) as f:
# 	print(formatted_payload)
# 	# Do something here
# pass
