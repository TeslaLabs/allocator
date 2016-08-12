test:
	nosetests --with-coverage --cover-html --cover-html-dir=htmlcov --cover-inclusive

lint:
	pep8 --ignore=E501 .

.PHONY: lint test
