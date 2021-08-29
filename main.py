from logics import email_processor, full_flow
import sys

if __name__ == '__main__':
	arguments = sys.argv

	template_path = arguments[1]
	customers_path = arguments[2]
	output_path = arguments[3]
	error_path = arguments[4]

	fullFlow = full_flow.get_full_flow(template_path, customers_path, output_path, error_path)
	fullFlow.execute_flow()
