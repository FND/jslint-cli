.PHONY: jslib test dist release pypi clean purge

jslib:
	curl -o jslint/fulljslint.js http://www.jslint.com/fulljslint.js
	curl http://json.org/json2.js | sed -e "/^alert(.*);$$/d" > jslint/json2.js

test: jslib
	py.test -x test

dist: test
	python setup.py sdist

release: clean pypi

pypi: test
	python setup.py sdist upload

clean:
	find . -name "*.pyc" | xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *.egg-info || true

purge: clean
	cat .gitignore | while read -r entry; do rm -r $$entry; done || true
