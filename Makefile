install:
	poetry install

build:
	rm -rf dist
	poetry build

publish:
	poetry publish -r test