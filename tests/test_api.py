from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Futurisys ML API is running"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    payload = {
        "feature_1": 1.0,
        "feature_2": 2.0,
        "feature_3": 3.0,
        "feature_4": 4.0,
    }
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json() == {"prediction": 10.0}


def test_predict_validation_error():
    payload = {
        "feature_1": 1.0,
        "feature_2": 2.0,
    }
    response = client.post("/predict", json=payload)

    assert response.status_code == 422