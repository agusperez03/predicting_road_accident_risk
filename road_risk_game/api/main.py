"""
FastAPI Backend for Road Risk Game
===================================
Provides API endpoints for the ML model predictions.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from typing import Dict, Any
import os

app = FastAPI(title="Road Risk Prediction API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and encoders on startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "accident_risk_model.joblib")
ENCODERS_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "label_encoders.joblib")
FEATURES_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "feature_names.joblib")

model = None
label_encoders = None
feature_names = None

@app.on_event("startup")
async def load_model():
    """Load the ML model and encoders when the API starts."""
    global model, label_encoders, feature_names
    try:
        model = joblib.load(MODEL_PATH)
        label_encoders = joblib.load(ENCODERS_PATH)
        feature_names = joblib.load(FEATURES_PATH)
        print("✓ Model and encoders loaded successfully")
    except Exception as e:
        print(f"Error loading model: {e}")
        raise


class RoadScenario(BaseModel):
    """Schema for road scenario input."""
    road_type: str
    num_lanes: int
    curvature: float
    speed_limit: int
    lighting: str
    weather: str
    road_signs_present: bool
    public_road: bool
    time_of_day: str
    holiday: bool
    school_season: bool
    num_reported_accidents: int


class PredictionResponse(BaseModel):
    """Schema for prediction response."""
    accident_risk: float
    risk_level: str
    risk_percentage: str


def preprocess_scenario(scenario: Dict[str, Any]) -> pd.DataFrame:
    """
    Preprocess a road scenario for prediction.
    
    Args:
        scenario: Dictionary with road characteristics
    
    Returns:
        Preprocessed DataFrame ready for prediction
    """
    df = pd.DataFrame([scenario])
    
    # Encode categorical variables
    categorical_features = ['road_type', 'lighting', 'weather', 'road_signs_present',
                          'public_road', 'time_of_day', 'holiday', 'school_season']
    
    for col in categorical_features:
        df[col] = label_encoders[col].transform(df[col])
    
    # Create engineered features
    df['speed_curvature'] = df['speed_limit'] * df['curvature']
    df['lanes_accidents'] = df['num_lanes'] * df['num_reported_accidents']
    df['high_speed'] = (df['speed_limit'] >= 60).astype(int)
    df['sharp_curve'] = (df['curvature'] >= 0.7).astype(int)
    
    return df


def get_risk_level(risk_score: float) -> str:
    """
    Convert risk score to human-readable level.
    
    Args:
        risk_score: Accident risk score (0-1)
    
    Returns:
        Risk level string
    """
    if risk_score < 0.2:
        return "Muy Bajo"
    elif risk_score < 0.4:
        return "Bajo"
    elif risk_score < 0.6:
        return "Moderado"
    elif risk_score < 0.8:
        return "Alto"
    else:
        return "Muy Alto"


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "message": "Road Risk Prediction API",
        "status": "active",
        "model_loaded": model is not None
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict_risk(scenario: RoadScenario):
    """
    Predict accident risk for a road scenario.
    
    Args:
        scenario: Road characteristics
    
    Returns:
        Prediction with risk score and level
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert to dict and preprocess
        scenario_dict = scenario.dict()
        processed_data = preprocess_scenario(scenario_dict)
        
        # Make prediction
        risk_score = float(model.predict(processed_data)[0])
        
        # Prepare response
        return PredictionResponse(
            accident_risk=risk_score,
            risk_level=get_risk_level(risk_score),
            risk_percentage=f"{risk_score * 100:.1f}%"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.get("/health")
async def health_check():
    """Detailed health check."""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "encoders_loaded": label_encoders is not None,
        "features_count": len(feature_names) if feature_names else 0
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
