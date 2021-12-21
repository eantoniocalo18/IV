FROM python:3.9-slim-bullseye

LABEL version "1.0" mantainer="e.antoniocalo18@go.ugr.es"

WORKDIR /app/

COPY pyproject.toml poetry.lock tasks.py ./

RUN useradd --create-home testuser && chown testuser:testuser /app


RUN  pip install poetry && poetry config virtualenvs.create false && poetry install 

WORKDIR /app/test


USER testuser

ENV PATH="$PATH:/home/testuser/.local/bin"



ENTRYPOINT ["invoke", "test"]
