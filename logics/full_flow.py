from IO import template_getter, customers_getter, email_sender
from logics import email_processor


def get_full_flow(path_to_template: str, path_to_customers: str, path_to_output: str, path_to_error: str):
	template_gettable = template_getter.new_local_file_template_getter(path_to_template)
	customers_gettable = customers_getter.new_local_file_customers_getter(path_to_customers)
	email_processable = email_processor.get_email_processor()
	email_sendable = email_sender.new_local_email_sender(path_to_output, path_to_error)

	return FullFlow(template_gettable, customers_gettable, email_processable, email_sendable)


class FullFlow:
	def __init__(self, template_gettable: template_getter.TemplateGetter,
				 customer_gettable: customers_getter.CustomersGetter,
				 email_processable: email_processor.EmailProcessable,
				 email_sendable: email_sender.EmailSender):
		self.__template_getter = template_gettable
		self.__customer_getter = customer_gettable
		self.__email_processor = email_processable
		self.__email_sender = email_sendable

	def execute_flow(self):
		template = self.__template_getter.get_template()
		customers = self.__customer_getter.get_customers()
		output_emails, error_customers = self.__email_processor.process_email_template(customers, template)
		self.__email_sender.send_email(output_emails, error_customers)
