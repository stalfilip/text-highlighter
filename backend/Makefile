test:
	poetry run pytest tests/ --cov=api --cov-report=term-missing

lint:
	poetry run ruff .

lint-fix:
	poetry run ruff . --fix

format:
	poetry run ruff format .

typecheck:
	poetry run pyright
