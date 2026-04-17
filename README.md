# Futurisys - ML Model Deployment API (POC)

API FastAPI exposant un modèle de Machine Learning via des endpoints REST, avec bonnes pratiques
d’ingénierie logicielle : tests Pytest, base PostgreSQL, CI/CD et gestion de versions Git.


## Stack
- Python 3.11+
- FastAPI + Uvicorn
- Scikit-learn (ou autre) + Joblib
- PostgreSQL
- Pytest + pytest-cov
- GitHub Actions


## Installation (local)
```bash
git clone <repo>
cd futurisys-ml-api
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```


## Project Structure

app/ → API & business logic
tests/ → Unit tests
models/ → Trained model
scripts/ → DB scripts
.github/workflows/ → CI/CD


futurisys-ml-api/
├─ app/
│  ├─ __init__.py
│  ├─ main.py                # FastAPI entrypoint (plus tard)
│  ├─ api/
│  │  ├─ __init__.py
│  │  ├─ routes.py           # endpoints (plus tard)
│  │  └─ schemas.py          # Pydantic models (plus tard)
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ config.py           # settings (env vars) (plus tard)
│  │  └─ logging.py          # logging (optionnel)
│  ├─ ml/
│  │  ├─ __init__.py
│  │  ├─ loader.py           # chargement modèle (joblib/pickle)
│  │  └─ predict.py          # logique de prédiction
│  ├─ db/
│  │  ├─ __init__.py
│  │  ├─ session.py          # connexion DB (plus tard)
│  │  └─ models.py           # ORM / tables (plus tard)
│  └─ services/
│     ├─ __init__.py
│     └─ inference.py        # service qui orchestre predict + DB (plus tard)
│
├─ tests/
│  ├─ __init__.py
│  ├─ test_smoke.py          # tests init (plus tard)
│  └─ test_predict.py        # tests predict (plus tard)
│
├─ models/
│  └─ model.joblib           # artefact (si tu le versionnes)
│
├─ scripts/
│  ├─ create_db.py           # création DB (plus tard)
│  └─ seed_db.py             # exemples data (plus tard)
│
├─ sql/
│  └─ schema.sql             # DDL (plus tard)
│
├─ .github/
│  └─ workflows/
│     └─ ci.yml              # pipeline (plus tard)
│
├─ .env.example              # variables d'env exemple
├─ .gitignore
├─ requirements.txt
├─ README.md
└─ pyproject.toml            # optionnel (si tu préfères à requirements)



## Versioning

- main → stable
- feature/* → new features
- Tags → semantic versioning (v0.1.0, v1.0.0)



## Objectifs
- Exposer le modèle ML via une API FastAPI (Swagger/OpenAPI intégré)
- Garantir la fiabilité via des tests unitaires et fonctionnels (Pytest + coverage)
- Tracer les requêtes/réponses dans PostgreSQL
- Automatiser tests et déploiement via CI/CD (GitHub Actions)
- Gérer les secrets via variables d’environnement (12-factor)



## Environments

The project uses three environments:

### Development (dev)
Local development environment used by developers.

- Runs on the developer machine
- Uses `.env` configuration
- Used to develop and debug the API

### Test (test)
Automated testing environment.

- Executed by GitHub Actions
- Runs unit tests with Pytest
- Validates the code before merging to `main`

### Production (prod)
Production deployment environment.

- Hosted on Hugging Face Spaces
- Automatically deployed from the `main` branch
- Uses secrets and environment variables for configuration

Sensitive variables are stored securely:
- GitHub Secrets (for CI/CD)
- Hugging Face Space Secrets (for production)