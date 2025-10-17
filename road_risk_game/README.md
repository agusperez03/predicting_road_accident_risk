# Road Risk Game 🚗🛣️

## Juego Interactivo de Predicción de Riesgo de Accidentes

Este es un juego interactivo basado en Machine Learning donde los jugadores deben identificar qué escenario de carretera tiene mayor riesgo de accidente.

### 🎮 Características del Juego

- **Modo de Juego**: Compara dos escenarios de carreteras y selecciona el de mayor riesgo
- **Sistema de Puntos**: Gana puntos por cada acierto
- **Sistema de Rachas**: Multiplica tus puntos manteniendo rachas de aciertos
- **Niveles de Dificultad**: Fácil, Medio y Difícil
- **Estadísticas en Tiempo Real**: Seguimiento de tu rendimiento

### 🏗️ Arquitectura del Proyecto

```
road_risk_game/
├── app.py                          # Aplicación principal Streamlit
├── api/
│   └── main.py                     # API FastAPI (opcional)
├── utils/
│   ├── game_logic.py               # Lógica del juego y generación de escenarios
│   └── model_utils.py              # Utilidades del modelo ML
├── models/
│   ├── accident_risk_model.joblib  # Modelo entrenado
│   ├── label_encoders.joblib       # Codificadores de variables categóricas
│   └── feature_names.joblib        # Nombres de características
├── .streamlit/
│   └── config.toml                 # Configuración de Streamlit
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo
```

### 🚀 Instalación y Ejecución

#### 1. Instalar Dependencias

```bash
cd road_risk_game
pip install -r requirements.txt
```

#### 2. Ejecutar la Aplicación Streamlit

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

#### 3. (Opcional) Ejecutar la API FastAPI

Si deseas usar la API backend por separado:

```bash
cd api
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

### 🎯 Cómo Jugar

1. **Observa** los dos escenarios de carreteras presentados
2. **Analiza** las condiciones:
   - Tipo de carretera (autopista, rural, urbana)
   - Número de carriles
   - Curvatura del camino
   - Límite de velocidad
   - Condiciones de iluminación
   - Clima
   - Presencia de señales
   - Y más...
3. **Selecciona** el camino que crees tiene MAYOR riesgo de accidente
4. **Gana puntos** por cada acierto (¡los puntos se multiplican con las rachas!)
5. **Pierde la racha** si te equivocas, pero no te rindas

### 📊 Sistema de Puntuación

- **Base**: 10 puntos por acierto
- **Multiplicador de Racha**: +10 puntos adicionales por cada nivel de racha (máx. 10x)
- **Ejemplo**: Con racha de 5, ganarás 10 + (10 × 5) = 60 puntos

### 🎓 Niveles de Dificultad

- **😊 Fácil**: Escenarios muy diferentes, fácil de distinguir
- **😐 Medio**: Diferencias moderadas, requiere análisis
- **😈 Difícil**: Escenarios muy similares, para expertos

### 🤖 Modelo de Machine Learning

El juego utiliza un modelo **Gradient Boosting Regressor** entrenado con:
- **Dataset**: 517,754 escenarios de carreteras
- **Precisión**: R² = 0.8841 (88.4% de varianza explicada)
- **MAE**: 0.0440 (4.4% de error promedio)

#### Factores de Riesgo Principales:
1. **Velocidad × Curvatura** (42.1%)
2. **Iluminación** (25.0%)
3. **Alta Velocidad** (8.7%)
4. **Curvatura** (8.3%)
5. **Clima** (7.6%)

### 🎨 Características Técnicas

#### Backend (FastAPI)
- Endpoints RESTful para predicciones
- Validación de datos con Pydantic
- Carga optimizada del modelo
- CORS habilitado para integración frontend

#### Frontend (Streamlit)
- Interfaz intuitiva y responsive
- CSS personalizado para mejor UX
- Manejo de estado con session_state
- Animaciones y efectos visuales
- Sistema de notificaciones

#### Utilidades
- Generador de escenarios aleatorios
- Sistema de dificultad adaptativo
- Visualizador de carreteras con emojis
- Calculadora de puntos y rachas

### 📈 Estadísticas del Juego

El juego rastrea:
- Puntos totales
- Racha actual
- Partidas jugadas
- Tasa de acierto
- Mejor racha (próximamente)

### 🚢 Despliegue

#### Streamlit Cloud (Recomendado)

1. Sube el proyecto a GitHub
2. Ve a [streamlit.io/cloud](https://streamlit.io/cloud)
3. Conecta tu repositorio
4. ¡Despliega!

#### Otras Opciones

- **Heroku**: Usa `Procfile` con `streamlit run app.py`
- **Docker**: Crea un `Dockerfile` con Streamlit
- **AWS/GCP/Azure**: Usa contenedores o servicios de app

### 🔧 Configuración

Puedes personalizar el juego editando:

- **Dificultad**: Modifica `DIFFICULTY_SETTINGS` en `utils/game_logic.py`
- **Puntuación**: Ajusta `calculate_points()` en `GameScoring`
- **Apariencia**: Edita el CSS en `app.py`
- **Tema**: Modifica `.streamlit/config.toml`

### 🐛 Troubleshooting

#### Error: "Model not found"
```bash
# Asegúrate de que los modelos estén en la carpeta correcta
ls models/
# Deberías ver: accident_risk_model.joblib, label_encoders.joblib, feature_names.joblib
```

#### Error: "Module not found"
```bash
# Reinstala las dependencias
pip install -r requirements.txt
```

#### El juego no carga
```bash
# Limpia el cache de Streamlit
streamlit cache clear
```

### 📝 Desarrollo Futuro

- [ ] Modo multijugador
- [ ] Tabla de clasificación global
- [ ] Desafíos diarios
- [ ] Logros y badges
- [ ] Modo tutorial interactivo
- [ ] Exportar estadísticas
- [ ] Tema oscuro/claro
- [ ] Soporte multiidioma

### 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### 📄 Licencia

Este proyecto está basado en el [Kaggle Playground Series S5E10](https://www.kaggle.com/competitions/playground-series-s5e10).

### 👨‍💻 Autor

Desarrollado como proyecto educativo para demostrar:
- Machine Learning aplicado
- Desarrollo de aplicaciones interactivas
- Buenas prácticas de código
- Arquitectura modular

### 🙏 Agradecimientos

- Dataset de Kaggle Playground Series
- Comunidad de Streamlit
- Scikit-learn y FastAPI

---

**¿Listo para el desafío?** 🎮 ¡Demuestra que puedes identificar los caminos más peligrosos!
