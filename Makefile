install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r test

lint:
	poetry run flake8 brain_games