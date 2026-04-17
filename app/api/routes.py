from fastapi import APIRouter, HTTPException
from app.api.schemas import PredictionRequest, PredictionResponse
from app.ml.predict import make_prediction

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Futurisys ML API is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    try:
        result = make_prediction(data.model_dump())
        return PredictionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))