# 🚀 Deployment Guide - Streamlit Cloud

## Pasos para Desplegar en Streamlit Cloud

### 1. Preparar el Repositorio

```bash
# 1. Asegúrate de que todos los archivos estén committed
git status

# 2. Si hay cambios, haz commit
git add .
git commit -m "Ready for deployment"

# 3. Push a GitHub
git push origin main
```

### 2. Ir a Streamlit Cloud

1. Ve a https://streamlit.io/cloud
2. Inicia sesión con tu cuenta de GitHub
3. Click en "New app"

### 3. Configurar la Aplicación

**Repository**:
- Selecciona: `agusperez03/predicting_road_accident_risk`

**Branch**:
- `main`

**Main file path**:
- `road_risk_game/app.py`

**App URL** (opcional):
- Personaliza tu URL: `road-risk-game` o el nombre que prefieras

### 4. Advanced Settings (Opcional)

**Python version**:
- `3.9` o `3.10` (recomendado)

**Secrets** (si fuera necesario):
- No se requieren secrets para esta app

### 5. Deploy!

Click en **"Deploy!"**

⏱️ El deployment toma aproximadamente 2-3 minutos

---

## 📋 Checklist Pre-Deployment

### Archivos Necesarios
- [x] `requirements.txt` - Todas las dependencias listadas
- [x] `app.py` - Archivo principal de la app
- [x] `models/` - Carpeta con los modelos (.joblib)
- [x] `utils/` - Módulos de utilidades
- [x] `.streamlit/config.toml` - Configuración de Streamlit

### Verificaciones
- [x] El modelo se carga correctamente
- [x] Todas las rutas son relativas (no absolutas)
- [x] Las dependencias están en requirements.txt
- [x] El código funciona localmente

---

## 🔧 Configuración Específica para Streamlit Cloud

### requirements.txt
Asegúrate de que incluya:
```
streamlit==1.29.0
pandas==2.1.3
numpy==1.26.2
scikit-learn==1.3.2
joblib==1.3.2
```

### .streamlit/config.toml
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
```

---

## 🌐 URLs Post-Deployment

Después del deployment, tu app estará disponible en:

```
https://[tu-app-name].streamlit.app
```

Por ejemplo:
```
https://road-risk-game.streamlit.app
```

---

## 🔄 Actualizar la Aplicación

Para actualizar la app desplegada:

```bash
# 1. Haz cambios en tu código local
# 2. Commit los cambios
git add .
git commit -m "Update: descripción de cambios"

# 3. Push a GitHub
git push origin main

# 4. Streamlit Cloud re-desplegará automáticamente
```

---

## 📊 Monitoreo y Logs

### Ver Logs
1. Ve a tu app en Streamlit Cloud
2. Click en "Manage app"
3. Ver logs en tiempo real

### Metrics
- Número de visitantes
- Tiempo de actividad
- Errores (si los hay)

---

## ⚠️ Troubleshooting

### Error: "Model file not found"
**Causa**: Los archivos .joblib no están en el repo  
**Solución**: 
```bash
git add models/*.joblib
git commit -m "Add model files"
git push
```

### Error: "Module not found"
**Causa**: Falta una dependencia en requirements.txt  
**Solución**: Agregar la dependencia y hacer push

### Error: "Out of memory"
**Causa**: El modelo es muy grande  
**Solución**: Streamlit Cloud tiene límites de recursos. Considera optimizar el modelo.

### App muy lenta
**Causa**: Streamlit Cloud recursos compartidos  
**Solución**: 
- Usa `@st.cache_resource` para cachear el modelo
- Ya implementado en `model_utils.py`

---

## 💰 Costos

### Streamlit Cloud
- **Community Plan**: GRATIS
  - 1 app privada
  - Apps públicas ilimitadas
  - 1GB de RAM por app
  - Perfecto para este proyecto

- **Upgrade a Teams** (opcional):
  - $250/mes por 3 miembros
  - Apps privadas ilimitadas
  - Más recursos

---

## 🎯 Optimizaciones para Production

### 1. Cachear el Modelo
```python
# Ya implementado en model_utils.py
@st.cache_resource
def load_model():
    return RiskPredictor(models_dir="models")
```

### 2. Lazy Loading
```python
# Cargar solo cuando sea necesario
if 'predictor' not in st.session_state:
    st.session_state.predictor = load_model()
```

### 3. Comprimir el Modelo (si es necesario)
```python
import joblib
model = joblib.load('model.joblib', mmap_mode='r')
```

---

## 📱 Compartir tu App

### Links para Compartir
```
Direct link:
https://[tu-app].streamlit.app

GitHub:
https://github.com/agusperez03/predicting_road_accident_risk

LinkedIn:
🚗 He creado un juego interactivo de ML que predice riesgo de accidentes
🎮 Pruébalo: https://[tu-app].streamlit.app
🔧 Código: https://github.com/agusperez03/predicting_road_accident_risk
```

### Embed en Sitio Web
```html
<iframe 
  src="https://[tu-app].streamlit.app/?embed=true" 
  width="100%" 
  height="800">
</iframe>
```

---

## 🎨 Personalización Post-Deployment

### Cambiar Título de Pestaña
```python
# En app.py
st.set_page_config(
    page_title="Road Risk Game",
    page_icon="🚗"
)
```

### Agregar Analytics (opcional)
```python
# Google Analytics
# Agregar en config.toml o usando components
import streamlit.components.v1 as components
```

---

## 📈 Próximos Pasos Post-Deployment

### Inmediato
- [ ] Compartir en redes sociales
- [ ] Agregar link en README principal
- [ ] Incluir en portfolio

### Corto Plazo
- [ ] Recopilar feedback de usuarios
- [ ] Monitorear errores
- [ ] Optimizar performance si es necesario

### Medio Plazo
- [ ] Agregar Google Analytics
- [ ] A/B testing de UI
- [ ] Implementar mejoras basadas en feedback

---

## 🏆 Showcase

Una vez desplegado, incluye en:

### README.md
```markdown
## 🎮 Play the Game
[Play Road Risk Game](https://[tu-app].streamlit.app)
```

### LinkedIn Post
```
🚗 Road Risk Game - ML en Acción 🎮

He desarrollado un juego interactivo que usa Machine Learning 
para predecir riesgo de accidentes en carreteras.

🤖 Modelo: Gradient Boosting (88% accuracy)
🎯 Stack: Python, Streamlit, Scikit-learn
📊 Dataset: 500K+ escenarios de Kaggle

¡Pruébalo y demuestra que puedes identificar los caminos más peligrosos!

🎮 Jugar: https://[tu-app].streamlit.app
💻 Código: https://github.com/agusperez03/predicting_road_accident_risk

#MachineLearning #DataScience #Python #Streamlit #GameDev
```

### Portfolio
```markdown
### Road Risk Game
**Description**: Interactive ML game for accident risk prediction

**Tech Stack**: Python, Streamlit, FastAPI, Scikit-learn

**Features**: 
- Real-time ML predictions
- Gamification system
- 3 difficulty levels
- Educational and fun

**Links**:
- [Play Game](https://[tu-app].streamlit.app)
- [GitHub](https://github.com/agusperez03/predicting_road_accident_risk)
- [Kaggle Competition](https://www.kaggle.com/competitions/playground-series-s5e10)
```

---

## ✅ Deployment Checklist Final

Pre-deployment:
- [x] Código tested localmente
- [x] requirements.txt actualizado
- [x] Models incluidos en repo
- [x] Rutas relativas (no absolutas)
- [x] .gitignore configurado
- [x] README actualizado

Deployment:
- [ ] Push a GitHub
- [ ] Crear app en Streamlit Cloud
- [ ] Configurar settings
- [ ] Deploy
- [ ] Verificar que funciona

Post-deployment:
- [ ] Testear en producción
- [ ] Compartir link
- [ ] Monitorear logs
- [ ] Recopilar feedback

---

## 🎉 ¡Listo para Desplegar!

Tu proyecto está completamente preparado para deployment en Streamlit Cloud.

**Tiempo estimado de deployment**: 5-10 minutos

**URL final**: `https://[tu-nombre-app].streamlit.app`

---

*¡Buena suerte con el deployment! 🚀*
