import pytest
from pydantic import ValidationError
from app.api.schemas import PredictionRequest


def valid_payload():
    return {
        "age": 26,
        "genre": "M",
        "revenu_mensuel": 2000,
        "statut_marital": "Célibataire",
        "departement": "Consulting",
        "poste": "Consultant",
        "nombre_experiences_precedentes": 2,
        "nombre_heures_travailless": 80,
        "annee_experience_totale": 2,
        "annees_dans_l_entreprise": 1,
        "annees_dans_le_poste_actuel": 1,
        "satisfaction_employee_environnement": 4,
        "note_evaluation_precedente": 4,
        "satisfaction_employee_nature_travail": 3,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": "Oui",
        "augementation_salaire_precedente": "11%",
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 3,
        "nombre_employee_sous_responsabilite": 0,
        "distance_domicile_travail": 12,
        "niveau_education": 3,
        "domaine_etude": "Informatique",
        "ayant_enfants": "Oui",
        "frequence_deplacement": "Rarement",
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 2,
    }


def test_prediction_request_valid_payload():
    data = PredictionRequest(**valid_payload())
    assert data.age == 26
    assert data.genre == "M"


def test_prediction_request_missing_required_field():
    payload = valid_payload()
    del payload["age"]

    with pytest.raises(ValidationError):
        PredictionRequest(**payload)


def test_prediction_request_invalid_numeric_type():
    payload = valid_payload()
    payload["age"] = "not_a_number"

    with pytest.raises(ValidationError):
        PredictionRequest(**payload)