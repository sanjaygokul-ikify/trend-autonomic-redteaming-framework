setup:
	poetry install

build:
	poetry build

deploy:
	docker-compose up -d

clean:
	rm -rf __pycache__/ .pytest_cache/

lint:
	python -m mypy . || true
	poetry run black . --check

test:
	poetry run pytest tests/

run:
	poetry run uvicorn main:app --reload

install-dev:
	pip install -e .
	pip install -r dev-requirements.txt