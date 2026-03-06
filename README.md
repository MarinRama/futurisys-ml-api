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