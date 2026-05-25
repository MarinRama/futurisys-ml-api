# Futurisys ML API

API FastAPI permettant d’exposer un modèle de Machine Learning de prédiction d’attrition employé via des endpoints REST.

Le projet applique des bonnes pratiques de Machine Learning Engineering :

- API REST avec FastAPI
- Documentation automatique Swagger/OpenAPI
- Validation robuste des données avec Pydantic
- Base PostgreSQL pour la traçabilité des échanges
- Tests unitaires et fonctionnels avec Pytest
- Rapport de couverture avec pytest-cov
- Intégration continue (CI/CD) avec GitHub Actions
- Déploiement automatisé sur Hugging Face Spaces

---

# Sommaire

- [Présentation du projet](#présentation-du-projet)
- [Architecture du projet](#architecture-du-projet)
- [Stack technique](#stack-technique)
- [Choix techniques](#choix-techniques)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Configuration](#configuration)
- [Configuration PostgreSQL](#configuration-postgresql)
- [Lancer l’API](#lancer-lapi)
- [Documentation API](#documentation-api)
- [Tests](#tests)
- [CI/CD](#cicd)
- [Environnements](#environnements)
- [Documentation complémentaire](#documentation-complémentaire)
- [Maintenance du modèle](#maintenance-du-modèle)
- [Améliorations futures](#améliorations-futures)

---

# Présentation du projet

L’objectif du projet est de prédire le risque de départ d’un employé (**employee attrition**) à partir de données RH.

L’API permet :

- d’exposer un modèle de Machine Learning via une API REST
- de valider les données entrantes avant prédiction
- de stocker les interactions avec le modèle dans PostgreSQL
- d’automatiser les tests et le déploiement

Le modèle actuellement utilisé est une **Régression Logistique (Logistic Regression)** entraînée sur un dataset RH.

---

# Architecture du projet

Le flux global de l’application est le suivant :

```text
Client
   ↓
FastAPI API
   ↓
Validation Pydantic
   ↓
Enregistrement PostgreSQL
   ↓
Modèle ML (attrition_model.joblib)
   ↓
Réponse de prédiction
```

### Fonctionnement

1. Le client envoie une requête à l’API.
2. FastAPI reçoit les données.
3. Pydantic valide les entrées.
4. Les données sont enregistrées dans PostgreSQL.
5. Le modèle Machine Learning effectue la prédiction.
6. La réponse est renvoyée au client.

---

# Stack technique

Le projet repose sur les technologies suivantes :

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **Scikit-learn**
- **Joblib**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **Pytest**
- **pytest-cov**
- **GitHub Actions**
- **Hugging Face Spaces**

---

# Choix techniques

## FastAPI

FastAPI a été choisi pour :

- sa rapidité d’exécution
- sa simplicité de développement
- sa documentation Swagger/OpenAPI intégrée
- sa validation automatique des données

## Pydantic

Pydantic est utilisé pour :

- valider les données entrantes
- garantir leur conformité
- réduire les erreurs avant la prédiction

## PostgreSQL

PostgreSQL permet :

- d’assurer la traçabilité des échanges
- d’enregistrer les inputs envoyés au modèle
- d’enregistrer les outputs générés

## SQLAlchemy

SQLAlchemy est utilisé comme ORM afin de :

- simplifier les interactions avec la base
- rendre le code plus maintenable
- séparer logique métier et persistance

## Pytest + pytest-cov

Utilisés afin de :

- garantir la robustesse du projet
- tester les cas critiques
- mesurer la couverture du code

## GitHub Actions

GitHub Actions permet :

- l’exécution automatique des tests
- la validation continue du code
- l’automatisation du déploiement

## Hugging Face Spaces

Hugging Face Spaces est utilisé comme plateforme de déploiement de l’API.

---

# Structure du projet

```text
futurisys-ml-api/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── ml/
│   ├── services/
│   └── main.py
│
├── models/
│   └── attrition_model.joblib
│
├── tests/
│   ├── test_api.py
│   ├── test_model.py
│   ├── test_validation.py
│   └── test_smoke.py
│
├── scripts/
│   ├── create_db.py
│   ├── load_dataset.py
│   └── test_db_connection.py
│
├── docs/
│   ├── STANDARDS.md
│   └── MODEL_DOCUMENTATION.md
│
├── .github/workflows/
├── requirements.txt
├── README.md
└── .env.example
```

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/<username>/futurisys-ml-api.git
cd futurisys-ml-api
```

## 2. Créer un environnement virtuel

Mac/Linux :

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows :

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Configuration

Créer un fichier `.env` à la racine :

```env
APP_ENV=dev
MODEL_PATH=models/attrition_model.joblib
API_HOST=0.0.0.0
API_PORT=8000
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/futurisys
```

---

# Configuration PostgreSQL

## Créer la base de données

```bash
createdb futurisys
```

## Créer les tables

```bash
python -m scripts.create_db
```

## Charger le dataset

```bash
python -m scripts.load_dataset
```

## Tester la connexion

```bash
python -m scripts.test_db_connection
```

---

# Lancer l’API

Démarrer le serveur :

```bash
uvicorn app.main:app --reload
```

API disponible ici :

```text
http://127.0.0.1:8000
```

---

# Documentation API

FastAPI génère automatiquement une documentation interactive Swagger/OpenAPI.

Documentation Swagger :

```text
http://127.0.0.1:8000/docs
```

Documentation ReDoc :

```text
http://127.0.0.1:8000/redoc
```

## Endpoints disponibles

### GET /

Retourne un message indiquant que l’API fonctionne.

### GET /health

Retourne l’état de santé de l’API.

Exemple :

```json
{
  "status": "ok"
}
```

### POST /predict

Retourne une prédiction d’attrition employé.

Exemple de payload :

```json
{
  "age": 26,
  "genre": "M",
  "revenu_mensuel": 2000,
  "statut_marital": "Célibataire",
  "departement": "Consulting",
  "poste": "Consultant",
  "nombre_experiences_precedentes": 2,
  "annee_experience_totale": 4,
  "annees_dans_l_entreprise": 1,
  "annees_dans_le_poste_actuel": 2,
  "satisfaction_employee_environnement": 3,
  "note_evaluation_precedente": 4,
  "satisfaction_employee_nature_travail": 3,
  "satisfaction_employee_equipe": 4,
  "satisfaction_employee_equilibre_pro_perso": 3,
  "note_evaluation_actuelle": 4,
  "heure_supplementaires": "Oui",
  "augementation_salaire_precedente": "11 %",
  "nombre_participation_pee": 1,
  "nb_formations_suivies": 3,
  "distance_domicile_travail": 12,
  "niveau_education": 3,
  "domaine_etude": "Infra & Cloud",
  "frequence_deplacement": "Occasionnel",
  "annees_depuis_la_derniere_promotion": 1,
  "annes_sous_responsable_actuel": 2
}
```

Exemple de réponse :

```json
{
  "prediction": 0,
  "probability": 0.12,
  "interpretation": "Faible risque d’attrition"
}
```

---

# Tests

## Exécuter tous les tests

```bash
pytest
```

## Générer un rapport de couverture

```bash
pytest --cov=app --cov-report=term-missing --cov-report=html
```

## Résultats actuels

- **13 tests passés**
- **97 % de couverture**

Les tests couvrent :

- les endpoints FastAPI
- la logique de prédiction
- la validation Pydantic
- les erreurs HTTP
- les payloads invalides
- les temps de réponse

---

# CI/CD

## Intégration Continue (CI)

GitHub Actions exécute automatiquement :

- installation des dépendances
- exécution des tests
- validation avant merge

Chaque Pull Request vers `main` doit passer les checks CI.

## Déploiement Continu (CD)

Le déploiement est effectué automatiquement sur **Hugging Face Spaces** à partir de la branche `main`.

---

# Environnements

## Développement (`dev`)

Environnement local utilisé pendant le développement.

## Test (`test`)

Environnement automatisé exécuté dans GitHub Actions.

## Production (`prod`)

Environnement déployé sur Hugging Face Spaces.

---

# Documentation complémentaire

Documentation des standards :

```text
docs/STANDARDS.md
```

Documentation technique du modèle :

```text
docs/MODEL_DOCUMENTATION.md
```

---

# Maintenance du modèle

Processus recommandé de mise à jour :

1. Réentraîner le modèle
2. Remplacer `models/attrition_model.joblib`
3. Vérifier les performances
4. Lancer les tests

```bash
pytest
```

5. Vérifier la couverture

```bash
pytest --cov=app
```

6. Push des modifications
7. Vérifier la CI/CD

---

# Améliorations futures

- conteneurisation Docker
- monitoring du modèle
- versioning avancé des modèles
- authentification API
- monitoring des performances