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



