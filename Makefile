format:
	black .
	isort .

test:
	pytest

build: format test

update:
	poetry update

dependencies: update
	poetry export --with=dev > requirements.txt
