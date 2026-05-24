import time
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


VALID_PAYLOAD = {
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
    "annes_sous_responsable_actuel": 2,
}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Futurisys ML API is running"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    response = client.post("/predict", json=VALID_PAYLOAD)

    assert response.status_code == 200
    body = response.json()
    assert "prediction" in body
    assert "probability" in body
    assert "interpretation" in body
    assert body["prediction"] in [0, 1]
    assert 0 <= body["probability"] <= 1
    assert isinstance(body["interpretation"], str)


def test_predict_validation_error():
    payload = {
        "age": 35,
        "genre": "Homme",
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_predict_empty_payload():
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_predict_wrong_http_method():
    response = client.get("/predict")
    assert response.status_code == 405


def test_unknown_endpoint():
    response = client.get("/unknown")
    assert response.status_code == 404


def test_predict_response_time():
    start = time.time()
    response = client.post("/predict", json=VALID_PAYLOAD)
    duration = time.time() - start

    assert response.status_code == 200
    assert duration < 2