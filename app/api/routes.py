from fastapi import APIRouter, HTTPException
from app.api.schemas import PredictionRequest, PredictionResponse
from app.ml.predict import make_prediction
from app.db.session import SessionLocal
from app.db.models import PredictionRequestDB, PredictionResultDB

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Futurisys ML API is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    db = SessionLocal()

    try:
        payload = data.model_dump()

        request_row = PredictionRequestDB(**payload)
        db.add(request_row)
        db.commit()
        db.refresh(request_row)

        result = make_prediction(payload)

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
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        db.close()