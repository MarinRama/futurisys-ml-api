from app.ml.loader import load_model

model = load_model()


def make_prediction(features: list[float]) -> float:
    prediction = model.predict([features])[0]
    return float(prediction)