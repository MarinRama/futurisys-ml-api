# ML Model Deployment API

Production-ready deployment of a Machine Learning model using:

- FastAPI
- PostgreSQL
- Pytest
- GitHub Actions (CI/CD)

## Installation

```bash``
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Project Structure

app/ → API & business logic
tests/ → Unit tests
models/ → Trained model
scripts/ → DB scripts
.github/workflows/ → CI/CD

## Versioning

- main → stable
- feature/* → new features
- Tags → semantic versioning (v0.1.0, v1.0.0)


