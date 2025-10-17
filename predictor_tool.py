"""
Car Accident Risk Prediction - Analysis & Prediction Script
============================================================
Run this script to analyze your own data or make predictions.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

class AccidentRiskPredictor:
    """
    A simple predictor class for accident risk assessment.
    """
    
    def __init__(self):
        self.model = None
        self.label_encoders = {}
        self.categorical_features = ['road_type', 'lighting', 'weather', 
                                     'road_signs_present', 'public_road', 
                                     'time_of_day', 'holiday', 'school_season']
    
    def preprocess_input(self, data):
        """
        Preprocess input data for prediction.
        
        Args:
            data: DataFrame with road characteristics
        
        Returns:
            Processed DataFrame ready for prediction
        """
        df = data.copy()
        
        # Encode categorical variables
        for col in self.categorical_features:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                df[col] = self.label_encoders[col].fit_transform(df[col])
            else:
                df[col] = self.label_encoders[col].transform(df[col])
        
        # Create engineered features
        df['speed_curvature'] = df['speed_limit'] * df['curvature']
        df['lanes_accidents'] = df['num_lanes'] * df['num_reported_accidents']
        df['high_speed'] = (df['speed_limit'] >= 60).astype(int)
        df['sharp_curve'] = (df['curvature'] >= 0.7).astype(int)
        
        return df
    
    def predict_risk(self, road_data):
        """
        Predict accident risk for given road conditions.
        
        Args:
            road_data: Dictionary or DataFrame with road characteristics
        
        Returns:
            Predicted accident risk (0-1 scale)
        """
        if isinstance(road_data, dict):
            df = pd.DataFrame([road_data])
        else:
            df = road_data.copy()
        
        # Preprocess
        processed = self.preprocess_input(df)
        
        # Predict
        if self.model is None:
            raise ValueError("Model not loaded. Please train or load a model first.")
        
        prediction = self.model.predict(processed)
        return prediction[0] if len(prediction) == 1 else prediction
    
    def interpret_risk(self, risk_score):
        """
        Interpret the risk score in human-readable format.
        
        Args:
            risk_score: Accident risk score (0-1)
        
        Returns:
            Risk interpretation string
        """
        if risk_score < 0.2:
            return f"LOW RISK ({risk_score:.2%}): Safe conditions"
        elif risk_score < 0.4:
            return f"MODERATE RISK ({risk_score:.2%}): Exercise normal caution"
        elif risk_score < 0.6:
            return f"ELEVATED RISK ({risk_score:.2%}): Exercise increased caution"
        elif risk_score < 0.8:
            return f"HIGH RISK ({risk_score:.2%}): Dangerous conditions - reduce speed"
        else:
            return f"VERY HIGH RISK ({risk_score:.2%}): EXTREME DANGER - avoid if possible"


# Example Usage
if __name__ == "__main__":
    print("="*60)
    print("ACCIDENT RISK PREDICTION EXAMPLES")
    print("="*60)
    
    # Example 1: Safe conditions
    safe_road = {
        'road_type': 'urban',
        'num_lanes': 4,
        'curvature': 0.1,
        'speed_limit': 35,
        'lighting': 'daylight',
        'weather': 'clear',
        'road_signs_present': True,
        'public_road': True,
        'time_of_day': 'afternoon',
        'holiday': False,
        'school_season': True,
        'num_reported_accidents': 0
    }
    
    # Example 2: Dangerous conditions
    dangerous_road = {
        'road_type': 'highway',
        'num_lanes': 2,
        'curvature': 0.95,
        'speed_limit': 70,
        'lighting': 'night',
        'weather': 'foggy',
        'road_signs_present': False,
        'public_road': True,
        'time_of_day': 'evening',
        'holiday': True,
        'school_season': False,
        'num_reported_accidents': 3
    }
    
    # Example 3: Moderate conditions
    moderate_road = {
        'road_type': 'rural',
        'num_lanes': 2,
        'curvature': 0.5,
        'speed_limit': 45,
        'lighting': 'dim',
        'weather': 'clear',
        'road_signs_present': True,
        'public_road': True,
        'time_of_day': 'morning',
        'holiday': False,
        'school_season': True,
        'num_reported_accidents': 1
    }
    
    print("\n📊 To use this predictor with the trained model:")
    print("\n1. Load the trained model:")
    print("   predictor = AccidentRiskPredictor()")
    print("   # predictor.model = your_trained_model")
    print("\n2. Make predictions:")
    print("   risk = predictor.predict_risk(road_data)")
    print("   print(predictor.interpret_risk(risk))")
    print("\n3. Example road scenarios are defined above")
    print("\n" + "="*60)
    
    print("\n✨ Key Factors for Low Accident Risk:")
    print("  • Good lighting (daylight)")
    print("  • Clear weather")
    print("  • Low curvature (straight roads)")
    print("  • Moderate speed limits")
    print("  • Presence of road signs")
    print("  • Multiple lanes")
    
    print("\n⚠️  Key Factors for High Accident Risk:")
    print("  • Poor lighting (night/dim)")
    print("  • Bad weather (fog/rain)")
    print("  • High curvature + high speed")
    print("  • History of accidents")
    print("  • Rural roads without signs")
    
    print("\n" + "="*60)
    print("For complete analysis, run: python accident_prediction_simple.py")
    print("="*60)
