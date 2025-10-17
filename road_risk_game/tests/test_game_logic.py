"""
Tests for game logic
"""
import pytest
from utils.game_logic import ScenarioGenerator, GameScoring, RoadVisualizer


class TestScenarioGenerator:
    """Test scenario generation"""
    
    def test_generate_scenario(self):
        """Test that scenario generation works"""
        scenario = ScenarioGenerator.generate_scenario()
        
        assert isinstance(scenario, dict)
        assert 'road_type' in scenario
        assert 'num_lanes' in scenario
        assert 'speed_limit' in scenario
        assert scenario['num_lanes'] in [1, 2, 3, 4]
        assert scenario['speed_limit'] in [25, 35, 45, 60, 70]
    
    def test_generate_contrasting_scenarios_easy(self):
        """Test easy difficulty generates contrasting scenarios"""
        scenario1, scenario2 = ScenarioGenerator.generate_contrasting_scenarios('easy')
        
        assert isinstance(scenario1, dict)
        assert isinstance(scenario2, dict)
        assert scenario1 != scenario2
    
    def test_generate_contrasting_scenarios_medium(self):
        """Test medium difficulty generates contrasting scenarios"""
        scenario1, scenario2 = ScenarioGenerator.generate_contrasting_scenarios('medium')
        
        assert isinstance(scenario1, dict)
        assert isinstance(scenario2, dict)
    
    def test_generate_contrasting_scenarios_hard(self):
        """Test hard difficulty generates contrasting scenarios"""
        scenario1, scenario2 = ScenarioGenerator.generate_contrasting_scenarios('hard')
        
        assert isinstance(scenario1, dict)
        assert isinstance(scenario2, dict)
    
    def test_scenario_has_all_features(self):
        """Test that generated scenario has all required features"""
        scenario = ScenarioGenerator.generate_scenario()
        
        required_features = [
            'road_type', 'num_lanes', 'curvature', 'speed_limit',
            'lighting', 'weather', 'road_signs_present', 'public_road',
            'time_of_day', 'holiday', 'school_season', 'num_reported_accidents'
        ]
        
        for feature in required_features:
            assert feature in scenario, f"Missing feature: {feature}"


class TestGameScoring:
    """Test game scoring logic"""
    
    def test_calculate_points_first_correct(self):
        """Test points calculation for first correct answer"""
        points = GameScoring.calculate_points(1, True)
        assert points == 20  # 10 * (1 + 1)
    
    def test_calculate_points_streak(self):
        """Test points calculation with streak"""
        points = GameScoring.calculate_points(3, True)
        assert points == 40  # 10 * (1 + 3)
    
    def test_calculate_points_incorrect(self):
        """Test points calculation for incorrect answer"""
        points = GameScoring.calculate_points(5, False)
        assert points == 0
    
    def test_calculate_points_max_streak(self):
        """Test points calculation with max streak (10x)"""
        points = GameScoring.calculate_points(10, True)
        assert points == 110  # 10 * (1 + 10)
        
        # Above 10 should still be 10x
        points = GameScoring.calculate_points(15, True)
        assert points == 110  # 10 * (1 + 10) - capped at 10
    
    def test_get_streak_message(self):
        """Test streak messages"""
        msg1 = GameScoring.get_streak_message(0)
        assert isinstance(msg1, str)
        
        msg2 = GameScoring.get_streak_message(5)
        assert isinstance(msg2, str)
        
        msg3 = GameScoring.get_streak_message(15)
        assert isinstance(msg3, str)


class TestRoadVisualizer:
    """Test visualization helpers"""
    
    def test_get_risk_color(self):
        """Test risk color assignment"""
        color_low = RoadVisualizer.get_risk_color(0.2)
        color_high = RoadVisualizer.get_risk_color(0.8)
        
        assert isinstance(color_low, str)
        assert isinstance(color_high, str)
        assert color_low != color_high
    
    def test_get_risk_color_boundaries(self):
        """Test risk color at boundaries"""
        color_zero = RoadVisualizer.get_risk_color(0.0)
        color_one = RoadVisualizer.get_risk_color(1.0)
        
        assert isinstance(color_zero, str)
        assert isinstance(color_one, str)
    
    def test_get_risk_emoji(self):
        """Test risk emoji assignment"""
        emoji_low = RoadVisualizer.get_risk_emoji(0.2)
        emoji_high = RoadVisualizer.get_risk_emoji(0.8)
        
        assert isinstance(emoji_low, str)
        assert isinstance(emoji_high, str)
        assert len(emoji_low) > 0
        assert len(emoji_high) > 0
    
    def test_get_scenario_description(self):
        """Test scenario description generation"""
        scenario = ScenarioGenerator.generate_scenario()
        description = RoadVisualizer.get_scenario_description(scenario)
        
        assert isinstance(description, str)
        assert len(description) > 0
        
        # Check that description contains some scenario details
        assert str(scenario['num_lanes']) in description or 'lane' in description.lower()
