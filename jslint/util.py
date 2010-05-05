import os


def resource_filename(package_name, resource_path):
	"""
	simple replacement for resource_filename when pkg_resources is not available
	assumes package is available in the current working directory

	This is required primarily on Google App Engine.

	resource_path is a Unix-style relative file path (using forward slashes)

	copied from tiddlywebplugins.utils
	"""
	return os.path.join(package_name, *resource_path.split("/"))
