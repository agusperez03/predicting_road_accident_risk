"""
Model Utilities
===============
Handles model loading and predictions.
"""

import joblib
import pandas as pd
import os
from typing import Dict, Tuple


class RiskPredictor:
    """Handles model loading and predictions."""
    
    def __init__(self, models_dir: str = "models"):
        """
        Initialize the predictor.
        
        Args:
            models_dir: Directory containing model files
        """
        self.models_dir = models_dir
        self.model = None
        self.label_encoders = None
        self.feature_names = None
        self.load_model()
    
    def load_model(self):
        """Load the trained model and encoders."""
        try:
            model_path = os.path.join(self.models_dir, "accident_risk_model.joblib")
            encoders_path = os.path.join(self.models_dir, "label_encoders.joblib")
            features_path = os.path.join(self.models_dir, "feature_names.joblib")
            
            self.model = joblib.load(model_path)
            self.label_encoders = joblib.load(encoders_path)
            self.feature_names = joblib.load(features_path)
            
            print("✓ Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def preprocess_scenario(self, scenario: Dict) -> pd.DataFrame:
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
            df[col] = self.label_encoders[col].transform(df[col])
        
        # Create engineered features
        df['speed_curvature'] = df['speed_limit'] * df['curvature']
        df['lanes_accidents'] = df['num_lanes'] * df['num_reported_accidents']
        df['high_speed'] = (df['speed_limit'] >= 60).astype(int)
        df['sharp_curve'] = (df['curvature'] >= 0.7).astype(int)
        
        return df
    
    def predict(self, scenario: Dict) -> float:
        """
        Predict accident risk for a road scenario.
        
        Args:
            scenario: Dictionary with road characteristics
        
        Returns:
            Predicted accident risk (0-1)
        """
        processed_data = self.preprocess_scenario(scenario)
        prediction = self.model.predict(processed_data)[0]
        return float(prediction)
    
    def compare_scenarios(self, scenario1: Dict, scenario2: Dict) -> Tuple[float, float, int]:
        """
        Compare two scenarios and return which has higher risk.
        
        Args:
            scenario1: First road scenario
            scenario2: Second road scenario
        
        Returns:
            Tuple of (risk1, risk2, higher_risk_index)
            higher_risk_index is 0 for scenario1, 1 for scenario2
        """
        risk1 = self.predict(scenario1)
        risk2 = self.predict(scenario2)
        
        higher_risk_index = 0 if risk1 > risk2 else 1
        
        return risk1, risk2, higher_risk_index
