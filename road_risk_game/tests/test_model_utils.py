"""
Tests for model utilities
"""
import pytest
import numpy as np
from utils.model_utils import RiskPredictor


class TestRiskPredictor:
    """Test ML model predictions"""
    
    @pytest.fixture
    def predictor(self):
        """Create predictor instance"""
        return RiskPredictor(models_dir="models")
    
    def test_predictor_initialization(self, predictor):
        """Test that predictor initializes correctly"""
        assert predictor.model is not None
        assert predictor.label_encoders is not None
        assert predictor.feature_names is not None
    
    def test_model_attributes(self, predictor):
        """Test model has required attributes"""
        # Check that model can make predictions
        assert hasattr(predictor.model, 'predict')
        
        # Check that feature names is a list
        assert isinstance(predictor.feature_names, list)
        assert len(predictor.feature_names) > 0
        
        # Check that label encoders is a dict
        assert isinstance(predictor.label_encoders, dict)
    
    def test_predict_risk(self, predictor):
        """Test risk prediction"""
        scenario = {
            'road_type': 'highway',
            'num_lanes': 2,
            'curvature': 0.5,
            'speed_limit': 55,
            'lighting': 'daylight',
            'weather': 'clear',
            'road_signs_present': True,
            'public_road': True,
            'time_of_day': 'afternoon',
            'holiday': False,
            'school_season': True,
            'num_reported_accidents': 2
        }
        
        risk = predictor.predict(scenario)  # Changed from predict_risk to predict
        
        assert isinstance(risk, (float, np.floating))
        assert 0 <= risk <= 1, f"Risk {risk} is out of bounds [0, 1]"
    
    def test_predict_risk_different_scenarios(self, predictor):
        """Test predictions on different scenarios"""
        # Low risk scenario
        safe_scenario = {
            'road_type': 'highway',
            'num_lanes': 4,
            'curvature': 0.1,
            'speed_limit': 70,
            'lighting': 'daylight',
            'weather': 'clear',
            'road_signs_present': True,
            'public_road': True,
            'time_of_day': 'afternoon',
            'holiday': False,
            'school_season': False,
            'num_reported_accidents': 0
        }
        
        # High risk scenario
        risky_scenario = {
            'road_type': 'rural',
            'num_lanes': 1,
            'curvature': 0.9,
            'speed_limit': 25,
            'lighting': 'night',
            'weather': 'rainy',
            'road_signs_present': False,
            'public_road': False,
            'time_of_day': 'evening',
            'holiday': True,
            'school_season': True,
            'num_reported_accidents': 5
        }
        
        safe_risk = predictor.predict(safe_scenario)  # Changed from predict_risk to predict
        risky_risk = predictor.predict(risky_scenario)  # Changed from predict_risk to predict
        
        assert isinstance(safe_risk, (float, np.floating))
        assert isinstance(risky_risk, (float, np.floating))
        assert 0 <= safe_risk <= 1
        assert 0 <= risky_risk <= 1
    
    def test_compare_scenarios(self, predictor):
        """Test scenario comparison"""
        scenario1 = {
            'road_type': 'highway',
            'num_lanes': 4,
            'curvature': 0.1,
            'speed_limit': 70,
            'lighting': 'daylight',
            'weather': 'clear',
            'road_signs_present': True,
            'public_road': True,
            'time_of_day': 'afternoon',
            'holiday': False,
            'school_season': False,
            'num_reported_accidents': 0
        }
        
        scenario2 = {
            'road_type': 'rural',
            'num_lanes': 1,
            'curvature': 0.9,
            'speed_limit': 25,
            'lighting': 'night',
            'weather': 'rainy',
            'road_signs_present': False,
            'public_road': False,
            'time_of_day': 'evening',
            'holiday': True,
            'school_season': True,
            'num_reported_accidents': 5
        }
        
        risk1, risk2, higher_risk = predictor.compare_scenarios(scenario1, scenario2)
        
        assert isinstance(risk1, (float, np.floating))
        assert isinstance(risk2, (float, np.floating))
        assert higher_risk in [0, 1]
        assert 0 <= risk1 <= 1
        assert 0 <= risk2 <= 1
    
    def test_preprocess_scenario(self, predictor):
        """Test scenario preprocessing"""
        scenario = {
            'road_type': 'highway',
            'num_lanes': 2,
            'curvature': 0.5,
            'speed_limit': 55,
            'lighting': 'daylight',
            'weather': 'clear',
            'road_signs_present': True,
            'public_road': True,
            'time_of_day': 'afternoon',
            'holiday': False,
            'school_season': True,
            'num_reported_accidents': 2
        }
        
        processed = predictor.preprocess_scenario(scenario)
        
        # Should return a DataFrame
        import pandas as pd
        assert isinstance(processed, pd.DataFrame)
        
        # Should have one row
        assert len(processed) == 1
        
        # Should have all feature columns
        assert len(processed.columns) == len(predictor.feature_names)
