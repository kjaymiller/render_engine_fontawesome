_default:
  just --list

test:
  uv run pytest -v

lint:
  uv run ruff check .

typecheck:
  uv run ruff check .

check:
  just lint
  just test
