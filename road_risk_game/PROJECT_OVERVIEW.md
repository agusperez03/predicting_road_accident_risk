# 🚗 Road Risk Game - Project Overview 🛣️

## 📋 Resumen del Proyecto

**Road Risk Game** es un juego interactivo web que utiliza Machine Learning para desafiar a los jugadores a identificar qué escenarios de carreteras tienen mayor riesgo de accidentes.

### 🎯 Objetivo

Crear una aplicación gamificada que:
- Eduque sobre factores de riesgo en carreteras
- Demuestre aplicación práctica de ML
- Proporcione una experiencia interactiva y entretenida

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Streamlit)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Game UI      │  │ Scoring      │  │ Stats Panel  │ │
│  │ - Scenarios  │  │ - Points     │  │ - Accuracy   │ │
│  │ - Buttons    │  │ - Streak     │  │ - Games      │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                  GAME LOGIC (Python)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Scenario Gen │  │ Difficulty   │  │ Visualizer   │ │
│  │ - Random     │  │ - Easy/Med/  │  │ - Emojis     │ │
│  │ - Contrast   │  │   Hard       │  │ - Colors     │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              ML MODEL (Gradient Boosting)               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Preprocessor │  │ Model        │  │ Predictor    │ │
│  │ - Encoding   │  │ - GBR        │  │ - Risk Calc  │ │
│  │ - Features   │  │ - Trained    │  │ - Compare    │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              DATA (Saved Models - Joblib)               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Model File   │  │ Encoders     │  │ Features     │ │
│  │ .joblib      │  │ .joblib      │  │ .joblib      │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Estructura del Proyecto

```
road_risk_game/
│
├── 📱 app.py                      # Aplicación principal Streamlit
│   ├── UI Components
│   ├── Game State Management
│   ├── Event Handlers
│   └── Styling (CSS)
│
├── 🔧 api/
│   ├── __init__.py
│   └── main.py                    # FastAPI backend (opcional)
│       ├── Endpoints (/predict, /health)
│       ├── Pydantic Models
│       └── CORS Configuration
│
├── 🛠️ utils/
│   ├── __init__.py
│   ├── game_logic.py              # Lógica del juego
│   │   ├── ScenarioGenerator
│   │   ├── GameScoring
│   │   └── RoadVisualizer
│   └── model_utils.py             # Utilidades del modelo
│       └── RiskPredictor
│
├── 🤖 models/
│   ├── accident_risk_model.joblib # Modelo ML entrenado
│   ├── label_encoders.joblib      # Codificadores
│   └── feature_names.joblib       # Nombres de features
│
├── ⚙️ .streamlit/
│   └── config.toml                # Configuración de tema
│
├── 📄 requirements.txt            # Dependencias Python
├── 📖 README.md                   # Documentación completa
├── 🚀 QUICKSTART.md              # Guía rápida
├── 🎮 run_game.bat               # Launcher Windows
├── 🎮 run_game.sh                # Launcher Unix/Mac
└── 🙈 .gitignore                 # Archivos ignorados
```

---

## 🎮 Mecánicas del Juego

### Flujo del Juego

```
[INICIO] 
   │
   ├─→ Generar 2 escenarios aleatorios
   │    │
   │    ├─→ Aplicar nivel de dificultad
   │    └─→ Asegurar diferencia significativa
   │
   ├─→ Mostrar escenarios al jugador
   │    │
   │    ├─→ Camino A (características)
   │    └─→ Camino B (características)
   │
   ├─→ Jugador elige el de MAYOR riesgo
   │    │
   │    └─→ Click en botón A o B
   │
   ├─→ Predecir riesgos con ML
   │    │
   │    ├─→ Preprocesar escenarios
   │    ├─→ Calcular riesgo A
   │    ├─→ Calcular riesgo B
   │    └─→ Comparar
   │
   ├─→ Evaluar respuesta
   │    │
   │    ├─→ ✅ CORRECTO
   │    │    ├─→ +Puntos (base × multiplicador de racha)
   │    │    ├─→ +Racha
   │    │    └─→ Mostrar resultados + 🎉
   │    │
   │    └─→ ❌ INCORRECTO
   │         ├─→ Racha = 0
   │         ├─→ No puntos
   │         └─→ Mostrar resultados
   │
   └─→ [SIGUIENTE RONDA] o [FIN]
```

### Sistema de Puntuación

```python
Puntos = Base × (1 + min(Racha, 10))

Ejemplos:
- Racha 0: 10 × (1 + 0) = 10 puntos
- Racha 3: 10 × (1 + 3) = 40 puntos
- Racha 5: 10 × (1 + 5) = 60 puntos
- Racha 10+: 10 × (1 + 10) = 110 puntos (máximo)
```

### Niveles de Dificultad

| Nivel | Diferencia Mínima | Diferencia Máxima | Estrategia |
|-------|------------------|-------------------|------------|
| 😊 Fácil | 15% | 100% | Escenarios muy contrastantes |
| 😐 Medio | 10% | 20% | Diferencias moderadas |
| 😈 Difícil | 5% | 15% | Escenarios muy similares |

---

## 🤖 Modelo de Machine Learning

### Especificaciones

```python
Modelo: GradientBoostingRegressor
Hyperparámetros:
  - n_estimators: 100
  - max_depth: 5
  - learning_rate: 0.1
  - random_state: 42

Performance:
  - R² Score: 0.8841 (88.4%)
  - MAE: 0.0440
  - RMSE: 0.0566
  
Dataset:
  - Training: 517,754 muestras
  - Features: 16 (12 originales + 4 engineered)
```

### Feature Engineering

```python
# Features Originales
- road_type (3 categorías)
- num_lanes (1-4)
- curvature (0.0-1.0)
- speed_limit (25-70 mph)
- lighting (3 categorías)
- weather (3 categorías)
- road_signs_present (bool)
- public_road (bool)
- time_of_day (3 categorías)
- holiday (bool)
- school_season (bool)
- num_reported_accidents (0-7)

# Features Engineered
+ speed_curvature = speed_limit × curvature
+ lanes_accidents = num_lanes × num_reported_accidents
+ high_speed = (speed_limit >= 60)
+ sharp_curve = (curvature >= 0.7)
```

### Feature Importance

```
1. speed_curvature    42.1% ████████████████████
2. lighting           25.0% ████████████
3. high_speed          8.7% ████
4. curvature           8.3% ████
5. weather             7.6% ███
6. speed_limit         4.9% ██
7. num_reported_acc    3.3% █
8. Otros               0.1%
```

---

## 💻 Stack Tecnológico

### Frontend
- **Streamlit** 1.29.0
  - UI components
  - Session state management
  - Custom CSS styling
  - Real-time updates

### Backend (Opcional)
- **FastAPI** 0.104.1
  - RESTful API
  - Async endpoints
  - Automatic documentation
- **Uvicorn** 0.24.0
  - ASGI server
  - Hot reload

### Machine Learning
- **Scikit-learn** 1.3.2
  - GradientBoostingRegressor
  - LabelEncoder
  - Preprocessing
- **Joblib** 1.3.2
  - Model serialization
  - Fast loading

### Data Processing
- **Pandas** 2.1.3
  - Data manipulation
  - DataFrame operations
- **NumPy** 1.26.2
  - Numerical computations
  - Array operations

### Validation
- **Pydantic** 2.5.0
  - Data validation
  - Type checking
  - API schemas

---

## 🚀 Deployment Options

### 1. Streamlit Cloud (Recomendado)
```bash
# Más fácil y gratuito
1. Push a GitHub
2. Conectar en streamlit.io/cloud
3. Deploy automático
```

### 2. Heroku
```bash
# Procfile
web: streamlit run app.py --server.port=$PORT
```

### 3. Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### 4. AWS/GCP/Azure
- EC2 + PM2
- App Engine
- Azure App Service
- Kubernetes

---

## 📊 Métricas y Analytics

### Estadísticas Rastreadas

```python
{
    "score": int,              # Puntos totales
    "streak": int,             # Racha actual
    "games_played": int,       # Total jugados
    "games_won": int,          # Total ganados
    "accuracy": float,         # Win rate
    "difficulty": str,         # Nivel actual
    "high_score": int,         # Mejor puntaje (futuro)
    "best_streak": int         # Mejor racha (futuro)
}
```

### Próximas Métricas
- Tiempo promedio por decisión
- Historial de partidas
- Análisis de errores comunes
- Progresión del jugador

---

## 🎨 Diseño y UX

### Color Palette

```css
Primary:    #FF4B4B (Rojo Streamlit)
Background: #FFFFFF (Blanco)
Secondary:  #F0F2F6 (Gris claro)
Text:       #262730 (Gris oscuro)

Risk Colors:
- Muy Bajo:  #28a745 (Verde)
- Bajo:      #90EE90 (Verde claro)
- Moderado:  #ffc107 (Amarillo)
- Alto:      #fd7e14 (Naranja)
- Muy Alto:  #dc3545 (Rojo)
```

### UI Components

- **Cards**: Tarjetas de escenarios con hover effects
- **Progress Bars**: Visualización de riesgo
- **Badges**: Niveles de riesgo con emojis
- **Buttons**: CTAs prominentes y coloridos
- **Metrics**: Grandes y legibles
- **Animations**: Balloons en aciertos

---

## 🔐 Seguridad y Mejores Prácticas

✅ **Código Limpio**
- PEP 8 compliant
- Type hints
- Docstrings
- Modular structure

✅ **Error Handling**
- Try-except blocks
- Graceful degradation
- User-friendly messages

✅ **Performance**
- Model caching
- Lazy loading
- Efficient state management

✅ **Extensibilidad**
- Separated concerns
- Configurable parameters
- Plugin architecture ready

---

## 📈 Roadmap

### Versión 1.0 (Actual) ✅
- [x] Juego básico funcional
- [x] Sistema de puntuación
- [x] 3 niveles de dificultad
- [x] Estadísticas básicas
- [x] UI responsive

### Versión 1.1 (Próximo)
- [ ] Tabla de clasificación
- [ ] Sistema de logros
- [ ] Tutorial interactivo
- [ ] Historial de partidas
- [ ] Exportar estadísticas

### Versión 2.0 (Futuro)
- [ ] Modo multijugador
- [ ] Desafíos diarios
- [ ] Personalización de avatar
- [ ] Tema oscuro
- [ ] Multi-idioma
- [ ] Mobile app

---

## 🤝 Contribuir

### Áreas de Mejora

1. **Features**
   - Nuevos modos de juego
   - Power-ups
   - Achievements system

2. **UX/UI**
   - Animaciones mejoradas
   - Sonidos
   - Temas personalizables

3. **Backend**
   - Base de datos para rankings
   - API REST completa
   - WebSocket para multijugador

4. **ML**
   - Modelos adicionales
   - Explicabilidad (SHAP)
   - Online learning

---

## 📝 Licencia y Créditos

**Proyecto**: Educational & Portfolio
**Dataset**: [Kaggle Playground S5E10](https://www.kaggle.com/competitions/playground-series-s5e10)
**Framework**: Streamlit, FastAPI, Scikit-learn

---

## 🎯 Conclusión

Este proyecto demuestra:
- ✅ Aplicación práctica de ML
- ✅ Desarrollo full-stack
- ✅ Gamificación efectiva
- ✅ Código mantenible y escalable
- ✅ UX centrada en el usuario

**¿Listo para jugar?** 🎮 `streamlit run app.py`

---

*Desarrollado con ❤️ y ☕ para demostrar el poder del Machine Learning aplicado*
