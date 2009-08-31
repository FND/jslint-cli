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

import spidermonkey

from simplejson import loads as json


cwd = sys.path[0]
lint_path = os.path.join(cwd, "fulljslint.js")
json_path = os.path.join(cwd, "json2.js") # XXX: built in from Spidermonkey 1.8


def main(args=None):
	filepath = args[1]
	status, errors = lint(filepath)
	print format(errors, filepath)
	return status


def lint(filepath):
	rt = spidermonkey.Runtime()
	cx = rt.new_context()

	options = {} # TODO: read from argument
	cx.add_global("options", options)
	cx.add_global("getFileContents", get_file_contents)

	# load JavaScript code
	for path in (lint_path, json_path):
		cx.execute('eval(getFileContents("%s"));' % path)
	cx.execute('var code = getFileContents("%s");' % filepath)

	# lint code
	status = cx.execute("JSLINT(code, options);") # True if clean, False otherwise
	errors = cx.execute("JSON.stringify(JSLINT.errors);");
	# XXX: errors incomplete (e.g. not reporting missing var)!?

	return status, errors


def format(errors, file):
	"""
	convert JSLint errors object into report using standard error format

	<filepath>:<line>:<column>:<message>
	"""
	lines = [":".join([
		file,
		str(error["line"] + 1),
		str(error["character"] + 1),
		error["reason"]
		]) for error in json(errors)] # XXX: don't use generator expression!?
	# XXX: ignoring members id, evidence, raw, a, b, c, d
	return "\n".join(lines)


def get_file_contents(filepath):
	return open(filepath).read()


if __name__ == "__main__":
	status = not main(sys.argv)
	sys.exit(status)
