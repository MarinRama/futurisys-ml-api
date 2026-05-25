from app.db.session import SessionLocal
from app.db.models import PredictionLog


def test_insert_prediction():
    db = SessionLocal()

    prediction = PredictionLog(
        prediction=1,
        probability=0.8,
        interpretation="Risque élevé"
    )

    db.add(prediction)
    db.commit()

    saved = db.query(PredictionLog).first()

    assert saved is not None

    db.close()
