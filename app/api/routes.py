from fastapi import APIRouter, HTTPException
from app.api.schemas import PredictionRequest, PredictionResponse
from app.ml.predict import make_prediction
from app.db.session import SessionLocal
from app.db.models import PredictionRequestDB, PredictionResultDB

router = APIRouter()


@router.get(
    "/",
    summary="Point d’entrée de l’API",
    description=(
        "Retourne un message indiquant que l’API Futurisys ML "
        "est disponible et fonctionne correctement."
    ),
)
def root():
    return {"message": "Futurisys ML API is running"}


@router.get(
    "/health",
    summary="Vérification de l’état de l’API",
    description=(
        "Permet de vérifier que l’API est accessible "
        "et opérationnelle."
    ),
)
def health():
    return {"status": "ok"}


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Prédire le risque d’attrition d’un employé",
    description=(
        "Prédit si un employé est susceptible de quitter l’entreprise "
        "à partir de caractéristiques RH (âge, salaire, département, "
        "niveau de satisfaction, mobilité, etc.).\n\n"
        "Le fonctionnement de cet endpoint suit les étapes suivantes :\n"
        "1. Validation des données d’entrée via Pydantic.\n"
        "2. Enregistrement des données d’entrée dans PostgreSQL.\n"
        "3. Exécution du modèle de Machine Learning.\n"
        "4. Enregistrement du résultat de prédiction en base de données.\n"
        "5. Retour d’une réponse contenant :\n"
        "- la prédiction,\n"
        "- la probabilité associée,\n"
        "- une interprétation métier."
    ),
)
def predict(data: PredictionRequest):
    db = SessionLocal()

    try:
        payload = data.model_dump()

        # Sauvegarde des données d'entrée
        request_row = PredictionRequestDB(**payload)
        db.add(request_row)
        db.commit()
        db.refresh(request_row)

        # Prédiction ML
        result = make_prediction(payload)

        # Sauvegarde du résultat
        result_row = PredictionResultDB(
            request_id=request_row.id,
            prediction=result["prediction"],
            probability=result["probability"],
            interpretation=result["interpretation"],
        )

        db.add(result_row)
        db.commit()

        return PredictionResponse(**result)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Erreur interne lors de la prédiction : {str(e)}"
        )

    finally:
        db.close()