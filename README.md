# Module 10 — Secure User Model, Pydantic Validation, and CI/CD

FastAPI app with a SQLAlchemy `User` model (hashed passwords, unique
username/email), Pydantic validation, and a GitHub Actions pipeline
that tests against real Postgres and pushes the Docker image to Docker Hub.

## Running locally

1. Copy `.env.example` to `.env` and adjust if needed.
2. Start Postgres and the app:

## Docker Hub

Docker image:

https://hub.docker.com/r/sathvikalla/module10-secure-user

## Running Tests Locally

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
docker compose up -d db
$env:DATABASE_URL="postgresql://postgres:postgres@localhost:5433/module10_db"
$env:TEST_DATABASE_URL="postgresql://postgres:postgres@localhost:5433/module10_test_db"
pytest --cov=app --cov-report=term-missing


## 3. Create the reflection document

Write approximately 200–250 words covering:

- Creating the SQLAlchemy `User` model
- Using Pydantic validation
- Hashing and salting passwords
- Testing uniqueness constraints with PostgreSQL
- Problems you encountered with ports `5432` and `8000`
- Docker build problems caused by `__pycache__`
- GitHub Actions and Docker Hub authentication
- What you learned about CI/CD and application security

## 4. Collect the required screenshots

Take clear screenshots of:

1. GitHub Actions showing both jobs successful
2. Docker Hub repository showing the `latest` image tag
3. Swagger showing `POST /users` returning `201`
4. PostgreSQL showing the bcrypt password hash
5. Terminal showing all tests passing

The assignment explicitly requires the first two. The others strengthen your submission and reflection.

## 5. Commit the final documentation

After updating the README and adding the reflection document:

```powershell
git status
git add README.md
git add .
git commit -m "Complete Module 10 documentation and reflection"
git push