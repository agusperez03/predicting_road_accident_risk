# Quick Start Guide 🚀

## Opción 1: Usando Windows (Más Fácil)

1. **Doble clic** en `run_game.bat`
2. ¡El juego se abrirá automáticamente en tu navegador!

## Opción 2: Línea de Comandos

```bash
# 1. Navega a la carpeta del juego
cd road_risk_game

# 2. Instala dependencias (solo la primera vez)
pip install -r requirements.txt

# 3. Ejecuta el juego
streamlit run app.py
```

## Opción 3: Usando Linux/Mac

```bash
# Dale permisos de ejecución
chmod +x run_game.sh

# Ejecuta
./run_game.sh
```

## URL del Juego

Una vez iniciado, el juego estará disponible en:
- **Local**: http://localhost:8501
- **Red Local**: http://[tu-ip]:8501

## Troubleshooting

### Error: "streamlit command not found"
```bash
pip install streamlit
```

### Error: "Model not found"
Asegúrate de que la carpeta `models/` contenga los archivos:
- accident_risk_model.joblib
- label_encoders.joblib
- feature_names.joblib

### El navegador no se abre automáticamente
Copia y pega esta URL en tu navegador: http://localhost:8501

## Controles del Juego

- **Seleccionar Camino**: Click en los botones "Seleccionar Camino A/B"
- **Cambiar Dificultad**: Usa el selector en la barra lateral
- **Reiniciar**: Botón "🔄 Reiniciar Juego" en la barra lateral
- **Siguiente Ronda**: Aparece después de cada respuesta

## ¡Disfruta el juego! 🎮🚗
