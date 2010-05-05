#!/usr/bin/env python

"""
wrapper for JSLint
requires Spidermonkey

Usage:
  $ wrapper_spidermonkey.py <filepath>

TODO:
* support for JSLint options
"""

import sys
import os

from subprocess import Popen, PIPE
from simplejson import loads as json


resources_path = os.getcwd() # TODO: use pkg_resources.resource_filename
DEPENDENCIES = [os.path.join(resources_path, filename) for filename in
	["fulljslint.js", "json2.js", "stdin.js", "lintwrapper.js"]]
# XXX: JSON support built in from Spidermonkey 1.8


def main(args=None):
	filepath = args[1]
	errors = lint(filepath)
	print format(errors, filepath)
	return len(errors) == 0


def lint(filepath):
	"""
	check given file using JSLint (via Spidermonkey)
	"""
	options = {} # TODO: read from argument

	command = ["js"]
	for filename in DEPENDENCIES:
		command.extend(["-f", filename])
	source = open(filepath)
	errors = Popen(command, stdin=source, stdout=PIPE).communicate()[0]
	# XXX: errors incomplete (e.g. not reporting missing var)!?
	source.close()

	return json(errors)


def format(errors, filepath):
	"""
	convert JSLint errors object into report using standard error format

	<filepath>:<line>:<column>:<message>
	"""
	lines = (":".join([
		filepath,
		str(error["line"] + 1),
		str(error["character"] + 1),
		error["reason"]
		]) for error in errors if error)
	# XXX: ignoring members id, evidence, raw, a, b, c, d
	return "\n".join(lines)


if __name__ == "__main__":
	status = not main(sys.argv)
	sys.exit(status)
