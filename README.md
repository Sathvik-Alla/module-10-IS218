# Module 10 — Secure User Model, Pydantic Validation, and CI/CD

FastAPI app with a SQLAlchemy `User` model (hashed passwords, unique
username/email), Pydantic validation, and a GitHub Actions pipeline
that tests against real Postgres and pushes the Docker image to Docker Hub.

## Running locally

1. Copy `.env.example` to `.env` and adjust if needed.
2. Start Postgres and the app: