#!/usr/bin/env python

"""
wrapper for JSLint using Spidermonkey engine

TODO:
* support for JSLint options
"""

import os

from subprocess import Popen, PIPE

try:
	from json import loads as json
except ImportError:
	from simplejson import loads as json

try:
	from pkg_resources import resource_filename
except ImportError:
	from jslint.util import resource_filename


DEPENDENCIES = [resource_filename("jslint", filename) for filename in
	["fulljslint.js", "json2.js", "lintwrapper.js"]]
# XXX: JSON support built in from Spidermonkey 1.8


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
