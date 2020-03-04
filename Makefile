install:
	poetry install

build:
	rm -rf dist
	poetry build

publish:
	poetry publish -r test

lint:
	poetry run flake8 brain_games