install:
	pip install -r requirements.txt

test:
	DB_NAME='Amity-test.db' pytest --cov-report html --cov-report term --cov=.

lint:
	pep8 --ignore=E501 .

.PHONY: lint test install
