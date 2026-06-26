# base image
FROM python:3.13-slim

## the setup

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv pip install --system -r pyproject.toml

COPY app/ ./app/

RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
