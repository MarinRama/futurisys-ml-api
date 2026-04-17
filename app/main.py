from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Futurisys ML API",
    description="API de prédiction pour exposer un modèle de machine learning",
    version="1.0.0",
)

app.include_router(router)