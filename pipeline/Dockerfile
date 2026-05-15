FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY ingest_data.py .

ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]