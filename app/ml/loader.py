from pathlib import Path
import joblib

MODEL_PATH = Path("models/attrition_model.joblib")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)