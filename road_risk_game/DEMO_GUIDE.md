# 🎮 Road Risk Game - Demo & Screenshots

## 🎯 Gameplay Demo

### Pantalla Principal

```
╔══════════════════════════════════════════════════════════════════╗
║                  🚗 ROAD RISK GAME 🛣️                           ║
║          ¿Cuál camino tiene mayor riesgo de accidente?          ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌─────────────────────────┐  ┌─────────────────────────┐      ║
║  │    🅰️ CAMINO A          │  │    🅱️ CAMINO B          │      ║
║  ├─────────────────────────┤  ├─────────────────────────┤      ║
║  │ 🛣️ Highway              │  │ 🌾 Rural                │      ║
║  │ 2 carriles              │  │ 3 carriles              │      ║
║  │ 🌀 Curva cerrada (0.85) │  │ 🌀 Recta (0.15)         │      ║
║  │ ⚡ Límite: 70 mph       │  │ ⚡ Límite: 35 mph       │      ║
║  │ 🌫️ Clima: foggy         │  │ ☀️ Clima: clear         │      ║
║  │ 🌙 Iluminación: night   │  │ ☀️ Iluminación: daylight│      ║
║  │ 🌆 Momento: evening     │  │ 🌅 Momento: morning     │      ║
║  │ 🚸 Sin señales          │  │ 🚸 Con señales          │      ║
║  │ 📊 Accidentes: 3        │  │ 📊 Accidentes: 0        │      ║
║  │                         │  │                         │      ║
║  │ [ Seleccionar A ]       │  │ [ Seleccionar B ]       │      ║
║  └─────────────────────────┘  └─────────────────────────┘      ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  SIDEBAR:                                                        ║
║  ┌──────────────────┐                                           ║
║  │  📊 Estadísticas │                                           ║
║  │                  │                                           ║
║  │  Puntos: 250     │  ← Score box con gradiente                ║
║  │                  │                                           ║
║  │  Racha: 5 🔥🔥🔥  │  ← Streak box con gradiente               ║
║  │  ¡Excelente!     │                                           ║
║  │                  │                                           ║
║  │  Partidas: 8     │                                           ║
║  │  Aciertos: 75%   │                                           ║
║  │                  │                                           ║
║  │  ⚙️ Dificultad:   │                                           ║
║  │  [😐 Medio ▼]    │                                           ║
║  │                  │                                           ║
║  │  [🔄 Reiniciar]  │                                           ║
║  └──────────────────┘                                           ║
╚══════════════════════════════════════════════════════════════════╝
```

### Pantalla de Resultado (Correcto)

```
╔══════════════════════════════════════════════════════════════════╗
║  ┌────────────────────────────────────────────────────────────┐ ║
║  │  ✅ ¡CORRECTO!                                             │ ║
║  │  Has ganado 60 puntos                                      │ ║
║  │  ¡Excelente! ¡5 aciertos! 🔥🔥🔥                           │ ║
║  │                                                            │ ║
║  │  🎉 ¡Felicitaciones! 🎉                                    │ ║
║  └────────────────────────────────────────────────────────────┘ ║
║                                                                  ║
║  ┌──────────────────────┐  ┌──────────────────────┐            ║
║  │  Camino A            │  │  Camino B            │            ║
║  │  🔴 Riesgo: 78.5%    │  │  🟢 Riesgo: 22.1%    │            ║
║  │  ███████████████▓░░  │  │  ████▓░░░░░░░░░░░░░  │            ║
║  └──────────────────────┘  └──────────────────────┘            ║
║                                                                  ║
║              [ ➡️ Siguiente Ronda ]                              ║
╚══════════════════════════════════════════════════════════════════╝
```

### Pantalla de Resultado (Incorrecto)

```
╔══════════════════════════════════════════════════════════════════╗
║  ┌────────────────────────────────────────────────────────────┐ ║
║  │  ❌ INCORRECTO                                             │ ║
║  │  El Camino A tenía mayor riesgo                            │ ║
║  │  Tu racha se ha reiniciado. ¡Sigue intentando!             │ ║
║  └────────────────────────────────────────────────────────────┘ ║
║                                                                  ║
║  ┌──────────────────────┐  ┌──────────────────────┐            ║
║  │  Camino A            │  │  Camino B            │            ║
║  │  🟠 Riesgo: 65.3%    │  │  🟡 Riesgo: 48.7%    │            ║
║  │  █████████████▓░░░░  │  │  █████████▓░░░░░░░░  │            ║
║  └──────────────────────┘  └──────────────────────┘            ║
║                                                                  ║
║              [ ➡️ Siguiente Ronda ]                              ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🎨 Elementos Visuales

### Iconos y Emojis Utilizados

#### Tipos de Carretera
- 🛣️ **Highway** - Autopistas de alta velocidad
- 🌾 **Rural** - Caminos rurales
- 🏙️ **Urban** - Calles urbanas

#### Clima
- ☀️ **Clear** - Despejado
- 🌫️ **Foggy** - Neblina
- 🌧️ **Rainy** - Lluvia

#### Iluminación
- ☀️ **Daylight** - Día claro
- 🌤️ **Dim** - Luz tenue
- 🌙 **Night** - Noche

#### Momento del Día
- 🌅 **Morning** - Mañana
- ☀️ **Afternoon** - Tarde
- 🌆 **Evening** - Atardecer

#### Indicadores de Riesgo
- ✅ **Muy Bajo** (< 20%) - Verde oscuro
- 🟢 **Bajo** (20-40%) - Verde claro
- 🟡 **Moderado** (40-60%) - Amarillo
- 🟠 **Alto** (60-80%) - Naranja
- 🔴 **Muy Alto** (> 80%) - Rojo

#### Otros
- 🎯 Botón de selección
- 🔥 Racha activa
- 📊 Estadísticas
- ⚙️ Configuración
- 🔄 Reiniciar
- 🎉 Celebración de acierto

---

## 💡 Ejemplos de Escenarios

### Escenario Fácil (Gran Diferencia)

**Camino A - ALTO RIESGO (≈75%)**
```
🛣️ Highway, 1 carril
🌀 Curva cerrada (0.92)
⚡ 70 mph
🌫️ Foggy
🌙 Night
🌆 Evening
🚸 Sin señales
📊 3 accidentes previos
```

**Camino B - BAJO RIESGO (≈18%)**
```
🏙️ Urban, 4 carriles
🌀 Recta (0.08)
⚡ 25 mph
☀️ Clear
☀️ Daylight
🌅 Morning
🚸 Con señales
📊 0 accidentes previos
```

### Escenario Medio

**Camino A - RIESGO MODERADO (≈48%)**
```
🌾 Rural, 2 carriles
🌀 Curva moderada (0.55)
⚡ 45 mph
🌧️ Rainy
🌤️ Dim
🌅 Morning
🚸 Con señales
📊 1 accidente previo
```

**Camino B - RIESGO MODERADO-ALTO (≈58%)**
```
🛣️ Highway, 2 carriles
🌀 Curva moderada (0.65)
⚡ 60 mph
☀️ Clear
🌙 Night
🌆 Evening
🚸 Sin señales
📊 2 accidentes previos
```

### Escenario Difícil (Pequeña Diferencia)

**Camino A - RIESGO (≈42%)**
```
🏙️ Urban, 3 carriles
🌀 Curva leve (0.35)
⚡ 35 mph
☀️ Clear
🌤️ Dim
☀️ Afternoon
🚸 Sin señales
📊 1 accidente previo
```

**Camino B - RIESGO (≈38%)**
```
🏙️ Urban, 3 carriles
🌀 Curva leve (0.32)
⚡ 35 mph
☀️ Clear
☀️ Daylight
☀️ Afternoon
🚸 Con señales
📊 1 accidente previo
```

---

## 📱 Flujo de Usuario

```
1. INICIO
   │
   ├─→ Usuario ve dos escenarios
   │   │
   │   ├─→ Lee características del Camino A
   │   └─→ Lee características del Camino B
   │
   ├─→ Usuario analiza factores de riesgo
   │   │
   │   ├─→ Curvatura + Velocidad
   │   ├─→ Clima + Iluminación
   │   ├─→ Señalización
   │   └─→ Historial de accidentes
   │
   ├─→ Usuario hace su elección
   │   │
   │   ├─→ Click "Seleccionar Camino A"
   │   └─→ Click "Seleccionar Camino B"
   │
   ├─→ Sistema procesa
   │   │
   │   ├─→ Preprocesa escenarios
   │   ├─→ Calcula riesgos con ML
   │   ├─→ Compara resultados
   │   └─→ Evalúa respuesta
   │
   ├─→ Muestra resultado
   │   │
   │   ├─→ ✅ Correcto
   │   │    ├─→ Actualiza puntos
   │   │    ├─→ Incrementa racha
   │   │    ├─→ Muestra celebración
   │   │    └─→ Revela riesgos reales
   │   │
   │   └─→ ❌ Incorrecto
   │        ├─→ Reinicia racha
   │        ├─→ Muestra explicación
   │        └─→ Revela riesgos reales
   │
   └─→ Usuario decide
       │
       ├─→ "Siguiente Ronda" → Genera nuevos escenarios
       ├─→ Cambiar dificultad → Ajusta parámetros
       └─→ "Reiniciar" → Reset completo
```

---

## 🎯 Consejos para Jugadores

### Factores de Alto Riesgo 🔴

1. **Combinación Mortal**: Alta velocidad + Curva cerrada
   - Speed × Curvature es el factor #1 (42%)
   
2. **Visibilidad Pobre**: Noche + Neblina
   - Lighting es el factor #2 (25%)
   
3. **Trifecta Peligrosa**:
   - Alta velocidad (≥60 mph)
   - Curva cerrada (≥0.7)
   - Mal clima (foggy/rainy)

### Factores de Bajo Riesgo 🟢

1. **Carretera Segura**:
   - Baja velocidad (≤35 mph)
   - Recta o curva leve (<0.3)
   - Buena iluminación
   
2. **Condiciones Ideales**:
   - Clima despejado
   - Día claro
   - Con señalización
   - Múltiples carriles

### Estrategias por Dificultad

**😊 Modo Fácil**
- Busca los extremos obvios
- Compara velocidad + curvatura primero
- Clima suele ser determinante

**😐 Modo Medio**
- Analiza combinaciones de factores
- Iluminación es clave
- Considera historial de accidentes

**😈 Modo Difícil**
- Todo importa, analiza con cuidado
- Pequeños detalles hacen la diferencia
- Confía en tu intuición + análisis

---

## 🏆 Logros y Objetivos

### Hitos de Puntuación
- 🥉 **Principiante**: 100 puntos
- 🥈 **Intermedio**: 500 puntos
- 🥇 **Experto**: 1,000 puntos
- 💎 **Maestro**: 2,500 puntos
- 👑 **Leyenda**: 5,000 puntos

### Rachas
- 🔥 **Inicio**: Racha 1-2
- 🔥🔥 **Caliente**: Racha 3-4
- 🔥🔥🔥 **Imparable**: Racha 5-9
- 🏆 **Leyenda**: Racha 10+

### Precisión
- 📊 **Novato**: <50% aciertos
- 📈 **Competente**: 50-69% aciertos
- 📊 **Experto**: 70-84% aciertos
- 🎯 **Maestro**: 85-94% aciertos
- 💯 **Perfecto**: 95-100% aciertos

---

## 📊 Ejemplos de Estadísticas

### Sesión Típica

```
┌─────────────────────────────────┐
│  ESTADÍSTICAS DE SESIÓN         │
├─────────────────────────────────┤
│  Puntos Totales: 450            │
│  Mejor Racha: 7 🔥🔥🔥           │
│  Partidas Jugadas: 12           │
│  Partidas Ganadas: 9            │
│  Tasa de Acierto: 75.0%         │
│  Dificultad: Medio              │
│  Tiempo Jugado: 15 min          │
└─────────────────────────────────┘
```

### Sesión Experta

```
┌─────────────────────────────────┐
│  ESTADÍSTICAS DE SESIÓN         │
├─────────────────────────────────┤
│  Puntos Totales: 1,850          │
│  Mejor Racha: 12 👑             │
│  Partidas Jugadas: 25           │
│  Partidas Ganadas: 22           │
│  Tasa de Acierto: 88.0%         │
│  Dificultad: Difícil            │
│  Tiempo Jugado: 30 min          │
└─────────────────────────────────┘
```

---

## 🎮 ¡Empieza a Jugar!

```bash
cd road_risk_game
streamlit run app.py
```

**O simplemente haz doble click en:**
- Windows: `run_game.bat`
- Mac/Linux: `run_game.sh`

---

*¿Puedes identificar los caminos más peligrosos? ¡Demuéstralo! 🚗💨*
