test:
	nosetests --with-coverage --cover-html --cover-html-dir=htmlcov --cover-inclusive

lint:
	pep8 .

.PHONY: lint test
