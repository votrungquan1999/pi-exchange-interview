import json


class TemplateGetter:
	def get_template(self):
		pass


class LocalFileTemplateGetter(TemplateGetter):
	def __init__(self, path: str, json_loader, file_opener):
		self.__path = path
		self.__jsonLoader = json_loader
		self.__fileOpener = file_opener

	def get_template(self):
		f = self.__fileOpener(self.__path)
		data = self.__jsonLoader(f)

		return data


def new_local_file_template_getter(path: str):
	return LocalFileTemplateGetter(path, json.load, open)
