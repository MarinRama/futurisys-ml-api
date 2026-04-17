import pandas as pd
from app.ml.loader import load_model

model = load_model()

def make_prediction(data: dict) -> dict:
    df = pd.DataFrame([data])

    proba = model.predict_proba(df)[0][1]
    prediction = int(proba >= 0.5)

    if hasattr(proba, "item"):
        proba = proba.item()

    interpretation = (
        "High risk of leaving" if proba > 0.7 else
        "Moderate risk" if proba > 0.4 else
        "Low risk"
    )

    return {
        "prediction": prediction,
        "probability": float(proba),
        "interpretation": interpretation
    }