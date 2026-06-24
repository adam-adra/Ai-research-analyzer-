install:
	uv sync

run:
	uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

test:
	uv run pytest

lint:
	uv run flake8 app/
	uv run mypy app/