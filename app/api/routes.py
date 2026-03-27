from fastapi import APIRouter
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
    features = [
        data.feature_1,
        data.feature_2,
        data.feature_3,
        data.feature_4,
    ]
    prediction = make_prediction(features)
    return PredictionResponse(prediction=prediction)