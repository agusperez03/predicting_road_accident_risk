"""
Road Risk Game - Streamlit App
================================
Interactive game to predict which road scenario has higher accident risk.
"""

import streamlit as st
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.game_logic import ScenarioGenerator, GameScoring, RoadVisualizer
from utils.model_utils import RiskPredictor

# Page configuration
st.set_page_config(
    page_title="Road Risk Game 🛣️",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .scenario-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px solid #ddd;
        transition: all 0.3s;
    }
    .scenario-card:hover {
        border-color: #FF4B4B;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .score-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .streak-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .result-correct {
        background-color: #d4edda;
        border: 2px solid #28a745;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .result-incorrect {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .risk-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.games_played = 0
    st.session_state.games_won = 0
    st.session_state.difficulty = 'medium'
    st.session_state.current_scenarios = None
    st.session_state.show_result = False
    st.session_state.predictor = RiskPredictor(models_dir="models")
    st.session_state.last_result = None

# Initialize predictor
predictor = st.session_state.predictor

# Title
st.markdown('<h1 class="main-title">🚗 Road Risk Game 🛣️</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">¿Cuál camino tiene mayor riesgo de accidente?</p>', unsafe_allow_html=True)

# Sidebar with game stats and controls
with st.sidebar:
    st.header("📊 Estadísticas")
    
    # Score display
    st.markdown(f"""
    <div class="score-box">
        <h2>{st.session_state.score}</h2>
        <p>Puntos</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Streak display
    streak_message = GameScoring.get_streak_message(st.session_state.streak)
    st.markdown(f"""
    <div class="streak-box">
        <h2>{st.session_state.streak}</h2>
        <p>{streak_message}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Game statistics
    if st.session_state.games_played > 0:
        accuracy = (st.session_state.games_won / st.session_state.games_played) * 100
        st.metric("Partidas Jugadas", st.session_state.games_played)
        st.metric("Tasa de Acierto", f"{accuracy:.1f}%")
    else:
        st.info("¡Juega tu primera partida!")
    
    st.divider()
    
    # Difficulty selector
    st.subheader("⚙️ Configuración")
    difficulty = st.selectbox(
        "Dificultad",
        options=['easy', 'medium', 'hard'],
        index=1,
        format_func=lambda x: {'easy': '😊 Fácil', 'medium': '😐 Medio', 'hard': '😈 Difícil'}[x]
    )
    st.session_state.difficulty = difficulty
    
    st.divider()
    
    # Reset button
    if st.button("🔄 Reiniciar Juego", use_container_width=True):
        st.session_state.score = 0
        st.session_state.streak = 0
        st.session_state.games_played = 0
        st.session_state.games_won = 0
        st.session_state.current_scenarios = None
        st.session_state.show_result = False
        st.session_state.last_result = None
        st.rerun()
    
    st.divider()
    
    # Instructions
    with st.expander("📖 Cómo Jugar"):
        st.write("""
        1. **Observa** los dos escenarios de carreteras
        2. **Analiza** las condiciones de cada camino
        3. **Selecciona** el camino con MAYOR riesgo
        4. **Gana puntos** por cada acierto
        5. **Mantén la racha** para multiplicar puntos
        
        ⚠️ ¡Una respuesta incorrecta reinicia tu racha!
        """)

# Main game area
if st.session_state.show_result and st.session_state.last_result:
    # Show result
    result = st.session_state.last_result
    
    if result['correct']:
        st.markdown(f"""
        <div class="result-correct">
            <h2>✅ ¡CORRECTO!</h2>
            <p>Has ganado {result['points_earned']} puntos</p>
            <p>{result['message']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown(f"""
        <div class="result-incorrect">
            <h2>❌ INCORRECTO</h2>
            <p>{result['message']}</p>
            <p>Tu racha se ha reiniciado. ¡Sigue intentando!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Show the risks
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Camino A")
        risk1 = result['risk1']
        color1 = RoadVisualizer.get_risk_color(risk1)
        emoji1 = RoadVisualizer.get_risk_emoji(risk1)
        st.markdown(f"### {emoji1} Riesgo: {risk1:.1%}")
        st.progress(risk1)
    
    with col2:
        st.subheader("Camino B")
        risk2 = result['risk2']
        color2 = RoadVisualizer.get_risk_color(risk2)
        emoji2 = RoadVisualizer.get_risk_emoji(risk2)
        st.markdown(f"### {emoji2} Riesgo: {risk2:.1%}")
        st.progress(risk2)
    
    st.divider()
    
    if st.button("➡️ Siguiente Ronda", type="primary", use_container_width=True):
        st.session_state.show_result = False
        st.session_state.current_scenarios = None
        st.session_state.last_result = None
        st.rerun()

else:
    # Generate new scenarios if needed
    if st.session_state.current_scenarios is None:
        scenario1, scenario2 = ScenarioGenerator.generate_contrasting_scenarios(st.session_state.difficulty)
        st.session_state.current_scenarios = (scenario1, scenario2)
    
    scenario1, scenario2 = st.session_state.current_scenarios
    
    st.subheader("🎯 Elige el camino con MAYOR riesgo de accidente")
    
    # Display scenarios side by side
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🅰️ Camino A")
        st.markdown('<div class="scenario-card">', unsafe_allow_html=True)
        st.markdown(RoadVisualizer.get_scenario_description(scenario1))
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🎯 Seleccionar Camino A", key="btn_a", type="primary", use_container_width=True):
            # Make prediction
            risk1, risk2, higher_risk = predictor.compare_scenarios(scenario1, scenario2)
            user_choice = 0  # User chose scenario A
            correct = (user_choice == higher_risk)
            
            # Update game state
            st.session_state.games_played += 1
            
            if correct:
                st.session_state.games_won += 1
                st.session_state.streak += 1
                points_earned = GameScoring.calculate_points(st.session_state.streak, True)
                st.session_state.score += points_earned
                message = GameScoring.get_streak_message(st.session_state.streak)
            else:
                st.session_state.streak = 0
                points_earned = 0
                message = f"El Camino {'A' if higher_risk == 0 else 'B'} tenía mayor riesgo."
            
            # Store result
            st.session_state.last_result = {
                'correct': correct,
                'points_earned': points_earned,
                'message': message,
                'risk1': risk1,
                'risk2': risk2,
                'higher_risk': higher_risk
            }
            st.session_state.show_result = True
            st.rerun()
    
    with col2:
        st.markdown("### 🅱️ Camino B")
        st.markdown('<div class="scenario-card">', unsafe_allow_html=True)
        st.markdown(RoadVisualizer.get_scenario_description(scenario2))
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🎯 Seleccionar Camino B", key="btn_b", type="primary", use_container_width=True):
            # Make prediction
            risk1, risk2, higher_risk = predictor.compare_scenarios(scenario1, scenario2)
            user_choice = 1  # User chose scenario B
            correct = (user_choice == higher_risk)
            
            # Update game state
            st.session_state.games_played += 1
            
            if correct:
                st.session_state.games_won += 1
                st.session_state.streak += 1
                points_earned = GameScoring.calculate_points(st.session_state.streak, True)
                st.session_state.score += points_earned
                message = GameScoring.get_streak_message(st.session_state.streak)
            else:
                st.session_state.streak = 0
                points_earned = 0
                message = f"El Camino {'A' if higher_risk == 0 else 'B'} tenía mayor riesgo."
            
            # Store result
            st.session_state.last_result = {
                'correct': correct,
                'points_earned': points_earned,
                'message': message,
                'risk1': risk1,
                'risk2': risk2,
                'higher_risk': higher_risk
            }
            st.session_state.show_result = True
            st.rerun()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>🚗 Desarrollado con Streamlit y Machine Learning</p>
    <p>Modelo: Gradient Boosting Regressor (R² = 0.884)</p>
    <p>Basado en <a href="https://www.kaggle.com/competitions/playground-series-s5e10" target="_blank">Kaggle Competition</a></p>
</div>
""", unsafe_allow_html=True)
