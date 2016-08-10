test:
	nosetests --with-coverage

lint:
	pep8 .

.PHONY: lint test
