import os

from setuptools import setup, find_packages

from jslint import __version__ as VERSION


AUTHOR = "FND"
AUTHOR_EMAIL = "FNDo@gmx.net"
NAME = "jslint"
DESCRIPTION = "command-line wrapper for JSLint"


setup(
	name = NAME,
	version = VERSION,
	description = DESCRIPTION,
	long_description = open(os.path.join(os.path.dirname(__file__), "README")).read(),
	author = AUTHOR,
	author_email = AUTHOR_EMAIL,
	license = "BSD",
	url = "http://pypi.python.org/pypi/%s" % NAME,
	platforms = "Posix; MacOS X; Windows",
	scripts = ["jslint-cli"],
	packages = find_packages(exclude=["test"]),
    include_package_data = True,
	zip_safe = False
)
