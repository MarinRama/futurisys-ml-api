from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    feature_1: float = Field(..., json_schema_extra={"example": 1.2})
    feature_2: float = Field(..., json_schema_extra={"example": 3.4})
    feature_3: float = Field(..., json_schema_extra={"example": 5.6})
    feature_4: float = Field(..., json_schema_extra={"example": 7.8})


class PredictionResponse(BaseModel):
    prediction: float