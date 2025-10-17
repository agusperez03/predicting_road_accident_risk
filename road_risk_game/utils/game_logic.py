"""
Game Logic Utilities
=====================
Handles scenario generation, scoring, and game mechanics.
"""

import random
import numpy as np
from typing import Dict, List, Tuple
import pandas as pd


class ScenarioGenerator:
    """Generates random road scenarios for the game."""
    
    # Possible values for each feature
    ROAD_TYPES = ['highway', 'rural', 'urban']
    LIGHTING_CONDITIONS = ['daylight', 'dim', 'night']
    WEATHER_CONDITIONS = ['clear', 'foggy', 'rainy']
    TIME_OF_DAY = ['morning', 'afternoon', 'evening']
    
    # Difficulty levels affect how different the scenarios are
    DIFFICULTY_SETTINGS = {
        'easy': {'min_difference': 0.15, 'max_difference': 1.0},      # Very different scenarios
        'medium': {'min_difference': 0.10, 'max_difference': 0.20},   # Moderate difference
        'hard': {'min_difference': 0.05, 'max_difference': 0.15}      # Very similar scenarios
    }
    
    @staticmethod
    def generate_scenario() -> Dict:
        """
        Generate a random road scenario.
        
        Returns:
            Dictionary with road characteristics
        """
        return {
            'road_type': random.choice(ScenarioGenerator.ROAD_TYPES),
            'num_lanes': random.randint(1, 4),
            'curvature': round(random.uniform(0.0, 1.0), 2),
            'speed_limit': random.choice([25, 35, 45, 60, 70]),
            'lighting': random.choice(ScenarioGenerator.LIGHTING_CONDITIONS),
            'weather': random.choice(ScenarioGenerator.WEATHER_CONDITIONS),
            'road_signs_present': random.choice([True, False]),
            'public_road': random.choice([True, False]),
            'time_of_day': random.choice(ScenarioGenerator.TIME_OF_DAY),
            'holiday': random.choice([True, False]),
            'school_season': random.choice([True, False]),
            'num_reported_accidents': random.randint(0, 3)
        }
    
    @staticmethod
    def generate_contrasting_scenarios(difficulty: str = 'medium') -> Tuple[Dict, Dict]:
        """
        Generate two scenarios with controlled risk difference.
        
        Args:
            difficulty: Game difficulty level (easy, medium, hard)
        
        Returns:
            Tuple of (scenario1, scenario2)
        """
        # Generate base scenarios
        scenario1 = ScenarioGenerator.generate_scenario()
        
        # For contrasting scenarios, modify specific high-impact features
        scenario2 = scenario1.copy()
        
        if difficulty == 'easy':
            # Make very different scenarios
            scenario2['lighting'] = 'night' if scenario1['lighting'] == 'daylight' else 'daylight'
            scenario2['weather'] = 'foggy' if scenario1['weather'] == 'clear' else 'clear'
            scenario2['curvature'] = 0.9 if scenario1['curvature'] < 0.3 else 0.1
            scenario2['speed_limit'] = 70 if scenario1['speed_limit'] <= 45 else 25
        
        elif difficulty == 'medium':
            # Moderate differences
            if random.random() > 0.5:
                scenario2['lighting'] = random.choice([l for l in ScenarioGenerator.LIGHTING_CONDITIONS if l != scenario1['lighting']])
            scenario2['curvature'] = round(1.0 - scenario1['curvature'], 2)
            scenario2['speed_limit'] = random.choice([s for s in [25, 35, 45, 60, 70] if abs(s - scenario1['speed_limit']) >= 20])
        
        else:  # hard
            # Subtle differences
            scenario2['num_lanes'] = scenario1['num_lanes'] + random.choice([-1, 1]) if 1 < scenario1['num_lanes'] < 4 else scenario1['num_lanes']
            scenario2['curvature'] = round(scenario1['curvature'] + random.uniform(-0.2, 0.2), 2)
            scenario2['curvature'] = max(0.0, min(1.0, scenario2['curvature']))
            scenario2['road_signs_present'] = not scenario1['road_signs_present']
        
        return scenario1, scenario2


class GameScoring:
    """Manages game scoring and streak tracking."""
    
    @staticmethod
    def calculate_points(streak: int, is_correct: bool) -> int:
        """
        Calculate points earned for a round.
        
        Args:
            streak: Current streak count
            is_correct: Whether the answer was correct
        
        Returns:
            Points earned
        """
        if not is_correct:
            return 0
        
        # Base points + streak multiplier
        base_points = 10
        streak_multiplier = min(streak, 10)  # Cap at 10x
        return base_points * (1 + streak_multiplier)
    
    @staticmethod
    def get_streak_message(streak: int) -> str:
        """
        Get a motivational message based on streak.
        
        Args:
            streak: Current streak count
        
        Returns:
            Motivational message
        """
        if streak == 0:
            return "¡Comienza tu racha!"
        elif streak < 3:
            return f"¡Racha de {streak}! 🔥"
        elif streak < 5:
            return f"¡Excelente! ¡{streak} seguidas! 🔥🔥"
        elif streak < 10:
            return f"¡Increíble! ¡{streak} aciertos! 🔥🔥🔥"
        else:
            return f"¡LEYENDA! ¡{streak} ACIERTOS! 🏆🔥🔥🔥"
    
    @staticmethod
    def get_difficulty_recommendation(accuracy: float, total_games: int) -> str:
        """
        Recommend difficulty based on performance.
        
        Args:
            accuracy: Win rate (0-1)
            total_games: Number of games played
        
        Returns:
            Recommended difficulty
        """
        if total_games < 5:
            return "easy"
        
        if accuracy > 0.80:
            return "hard"
        elif accuracy > 0.60:
            return "medium"
        else:
            return "easy"


class RoadVisualizer:
    """Generates text descriptions and emojis for scenarios."""
    
    ROAD_EMOJIS = {
        'highway': '🛣️',
        'rural': '🌾',
        'urban': '🏙️'
    }
    
    WEATHER_EMOJIS = {
        'clear': '☀️',
        'foggy': '🌫️',
        'rainy': '🌧️'
    }
    
    LIGHTING_EMOJIS = {
        'daylight': '☀️',
        'dim': '🌤️',
        'night': '🌙'
    }
    
    TIME_EMOJIS = {
        'morning': '🌅',
        'afternoon': '☀️',
        'evening': '🌆'
    }
    
    @staticmethod
    def get_scenario_description(scenario: Dict) -> str:
        """
        Generate a human-readable description of a scenario.
        
        Args:
            scenario: Road scenario dictionary
        
        Returns:
            Formatted description string
        """
        road_emoji = RoadVisualizer.ROAD_EMOJIS.get(scenario['road_type'], '🛣️')
        weather_emoji = RoadVisualizer.WEATHER_EMOJIS.get(scenario['weather'], '')
        lighting_emoji = RoadVisualizer.LIGHTING_EMOJIS.get(scenario['lighting'], '')
        time_emoji = RoadVisualizer.TIME_EMOJIS.get(scenario['time_of_day'], '')
        
        curvature_desc = "recta" if scenario['curvature'] < 0.3 else "curva moderada" if scenario['curvature'] < 0.7 else "curva cerrada"
        signs = "con señales" if scenario['road_signs_present'] else "sin señales"
        
        description = f"""
{road_emoji} **{scenario['road_type'].capitalize()}** con {scenario['num_lanes']} carril(es)
🌀 {curvature_desc.capitalize()} (curv: {scenario['curvature']:.2f})
⚡ Límite: {scenario['speed_limit']} mph
{weather_emoji} Clima: {scenario['weather']}
{lighting_emoji} Iluminación: {scenario['lighting']}
{time_emoji} Momento: {scenario['time_of_day']}
🚸 {signs.capitalize()}
📊 Accidentes previos: {scenario['num_reported_accidents']}
        """
        return description.strip()
    
    @staticmethod
    def get_risk_color(risk_score: float) -> str:
        """
        Get color for risk score visualization.
        
        Args:
            risk_score: Risk score (0-1)
        
        Returns:
            Color name or hex code
        """
        if risk_score < 0.2:
            return "#28a745"  # Green
        elif risk_score < 0.4:
            return "#90EE90"  # Light green
        elif risk_score < 0.6:
            return "#ffc107"  # Yellow
        elif risk_score < 0.8:
            return "#fd7e14"  # Orange
        else:
            return "#dc3545"  # Red
    
    @staticmethod
    def get_risk_emoji(risk_score: float) -> str:
        """
        Get emoji representation of risk level.
        
        Args:
            risk_score: Risk score (0-1)
        
        Returns:
            Risk emoji
        """
        if risk_score < 0.2:
            return "✅"
        elif risk_score < 0.4:
            return "🟢"
        elif risk_score < 0.6:
            return "🟡"
        elif risk_score < 0.8:
            return "🟠"
        else:
            return "🔴"
