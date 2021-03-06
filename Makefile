install:
	pip install -r requirements.txt

test:
	nosetests --with-coverage --cover-html --cover-html-dir=htmlcov --cover-inclusive

lint:
	pep8 --ignore=E501 .

.PHONY: install lint test
