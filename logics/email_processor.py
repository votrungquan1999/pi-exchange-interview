from datetime import date


class EmailProcessable:
	def process_email_template(self, customers: [], template: dict):
		pass


def get_email_processor():
	return EmailProcessor(date.today)


class EmailProcessor(EmailProcessable):
	def __init__(self, get_today):
		self.__get_today = get_today

	def process_email_template(self, customers: [], template: dict):
		output = []
		error_customers = []
		for customer in customers:
			if not (self.__field_exists_in_customer(customer, "EMAIL")):
				error_customers.append(customer)
				continue

			body = self.__process_body(customer, template)

			formatted_output = {
				"body": body,
				"from": self.__field_value_in_template("from", template),
				"subject": self.__field_value_in_template("subject", template),
				"mimeType": self.__field_value_in_template("mimeType", template),
				"to": customer["EMAIL"]
			}
			output.append(formatted_output)

		return output, error_customers

	def __process_body(self, customer, template):
		body = self.__field_value_in_template("body", template)
		body = self.__fill_customer_info(body, customer)
		body = self.__fill_date(body)

		return body

	def __fill_customer_info(self, body: str, customer: {}):
		customer_fields_to_be_filled = ["TITLE", "FIRST_NAME", "LAST_NAME"]

		for field in customer_fields_to_be_filled:
			if not (self.__field_exists_in_customer(customer, field)):
				raise ValueError("{0} is missing in customer".format(field))

			body = body.replace('{{' + field + '}}', customer[field])

		return body

	def __fill_date(self, body: str):
		# print(body)
		return body.replace("{{TODAY}}", self.__get_today().strftime("%d %b %Y"))

	@staticmethod
	def __field_exists_in_customer(customer: {}, key: str):
		return (key in customer) and customer[key] is not None and customer[key] != ""

	@staticmethod
	def __field_value_in_template(key: str, template: {}):
		if not (key in template):
			return ""

		return template[key]
