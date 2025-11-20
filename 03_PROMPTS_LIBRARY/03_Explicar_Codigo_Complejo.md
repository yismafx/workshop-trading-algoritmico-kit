# 🤖 PROMPT 03: Explicar Código Complejo Línea por Línea

> **Categoría:** Comprensión y Aprendizaje  
> **Nivel:** Básico  
> **Sesión del Workshop:** Todas (herramienta transversal)  
> **Compatible con:** Claude, ChatGPT, Gemini

---

## 🎯 PROPÓSITO

Entender código de trading algorítmico que te parece confuso:
- Estrategias de repos de GitHub que quieres usar
- Ejemplos de libros con sintaxis desconocida
- Código de colegas que no está bien documentado
- Scripts de backtesting con lógica compleja

**⚠️ Importante:** Entender código ajeno es CRÍTICO antes de usarlo con dinero real.

---

## 📋 ESTRUCTURA DEL PROMPT

### Template Básico

```markdown
🎭 ROL:
Actúa como un instructor de trading algorítmico explicando código a un 
estudiante que tiene [NIVEL: principiante/intermedio] en Python y trading.

Tu estilo debe ser:
- Pedagógico y paciente (como si enseñaras a un amigo)
- Usar analogías del mundo del trading manual
- Explicar el "por qué" antes del "cómo"

📊 CONTEXTO:
Encontré este código en [FUENTE: GitHub/libro/curso] de una estrategia 
[NOMBRE ESTRATEGIA]. Entiendo el concepto general pero hay partes que no comprendo.

Código que necesito entender:
```python
[PEGAR CÓDIGO AQUÍ - máximo 50 líneas]
```

Específicamente, NO entiendo:
[PUNTO 1: Ej. "¿Qué hace la línea 23 con .shift(-1)?"]
[PUNTO 2: Ej. "¿Por qué se usa .rolling()?"]
[PUNTO 3: Ej. "¿Qué es 'vectorized' backtest?"]

🎯 TAREA:
Explícame este código haciendo lo siguiente:

1. **Resumen ejecutivo** (2-3 líneas): ¿Qué hace este código en general?
2. **Desglose línea por línea:** Para cada línea:
   - ¿Qué hace técnicamente?
   - ¿Por qué es necesaria para la estrategia?
   - Usa analogía con trading manual si aplica
3. **Responde mis dudas específicas** (las que listé arriba)
4. **Señala riesgos/bugs** si detectas algo problemático
5. **Complejidad:** Califícala (⭐ fácil → ⭐⭐⭐⭐⭐ experto)

📤 FORMATO:
Usa formato de código comentado donde cada línea va seguida de su explicación.

⛔ RESTRICCIONES:
- NO asumas que sé qué significa jerga como "vectorization", "broadcasting", etc.
- NO uses términos técnicos sin explicarlos
- Si hay un concepto avanzado, dale prioridad a explicarlo con analogía
- Evita explicaciones de 1 palabra como "Esto calcula el promedio" (quiero saber PARA QUÉ)
```

---

## 🔥 EJEMPLO DE USO REAL

### Input (Tu prompt al AI):

```markdown
🎭 ROL:
Actúa como un instructor de trading algorítmico explicando código a un 
estudiante que tiene nivel intermedio en Python y principiante en trading algorítmico.

📊 CONTEXTO:
Encontré este código en el libro "Algorithmic Trading" de Ernest Chan (2013) 
de una estrategia de mean reversion. Entiendo que compra cuando el precio 
está "barato" y vende cuando está "caro", pero hay líneas que no comprendo.

Código que necesito entender:
```python
import pandas as pd
import numpy as np

# Descargar datos (supongamos df ya tiene OHLCV)
df['Returns'] = df['Close'].pct_change()
df['Log_Returns'] = np.log(df['Close'] / df['Close'].shift(1))

# Calcular z-score
lookback = 20
df['MA'] = df['Close'].rolling(window=lookback).mean()
df['Std'] = df['Close'].rolling(window=lookback).std()
df['Z_Score'] = (df['Close'] - df['MA']) / df['Std']

# Señales
df['Position'] = -np.sign(df['Z_Score'])
df['Strategy_Returns'] = df['Position'].shift(1) * df['Returns']
```

Específicamente, NO entiendo:
1. ¿Por qué se usan log returns Y returns normales?
2. ¿Qué es exactamente el z-score y por qué se divide por Std?
3. ¿Por qué la posición es el NEGATIVO del signo del z-score?
4. ¿Por qué se usa .shift(1) en 'Position'?

🎯 TAREA:
[Estructura completa del template...]

📤 FORMATO:
Usa código comentado línea por línea.
```

### Output Esperado (Lo que el AI responderá):

```python
# ═══════════════════════════════════════════════════════════════
# RESUMEN EJECUTIVO
# ═══════════════════════════════════════════════════════════════
# Esta estrategia implementa MEAN REVERSION (reversión a la media):
# - Compra cuando el precio está "anormalmente bajo" (z-score negativo)
# - Vende cuando está "anormalmente alto" (z-score positivo)
# - La "anormalidad" se mide estadísticamente con desviación estándar

# ═══════════════════════════════════════════════════════════════
# DESGLOSE LÍNEA POR LÍNEA
# ═══════════════════════════════════════════════════════════════

import pandas as pd
import numpy as np

# --- CÁLCULO DE RETORNOS ---

df['Returns'] = df['Close'].pct_change()
# ¿Qué hace? Calcula retorno porcentual entre precio hoy y ayer
# ¿Para qué? Necesitamos retornos (no precios) para calcular performance
# Analogía: Si AAPL pasó de $100 a $102, el retorno es 2%
# Fórmula: (Precio_hoy - Precio_ayer) / Precio_ayer

df['Log_Returns'] = np.log(df['Close'] / df['Close'].shift(1))
# ¿Qué hace? Calcula logaritmo natural del ratio de precios
# ¿Para qué? Log returns tienen propiedades estadísticas mejores:
#   1. Son aditivos: log_ret(día1) + log_ret(día2) = log_ret(total)
#   2. Simétricos: subir 10% y bajar 10% no dan 0%, pero en log sí
#   3. Se usan en finanzas académicas (Sharpe, Sortino, etc.)
# Analogía: Es como usar escala logarítmica en un gráfico

# RESPUESTA A TU DUDA 1:
# Usamos ambos porque:
# - Returns normales: Fáciles de interpretar ("gané 5%")
# - Log returns: Mejores para matemáticas y estadísticas
# En backtesting usamos returns normales, en análisis académico log returns

# --- CÁLCULO DE Z-SCORE (NÚCLEO DE LA ESTRATEGIA) ---

lookback = 20
# Ventana de tiempo: Usaremos últimos 20 días para calcular "normal"

df['MA'] = df['Close'].rolling(window=lookback).mean()
# ¿Qué hace? Calcula promedio móvil de 20 días
# ¿Para qué? Define qué es "precio normal" en los últimos 20 días
# Analogía: Si AAPL promedió $150 últimos 20 días, ese es nuestro "precio justo"
# Método: .rolling(20) toma ventana deslizante de 20 valores
#         .mean() calcula promedio de esa ventana

df['Std'] = df['Close'].rolling(window=lookback).std()
# ¿Qué hace? Calcula desviación estándar de 20 días
# ¿Para qué? Mide cuánto "se mueve" el precio normalmente
# Analogía: Si AAPL tiene Std = $5, significa que fluctúa ±$5 alrededor del promedio
# Nota: Std alta = activo volátil, Std baja = activo estable

df['Z_Score'] = (df['Close'] - df['MA']) / df['Std']
# ¿Qué hace? Calcula cuántas "desviaciones estándar" está el precio del promedio
# ¿Para qué? Normaliza la distancia para que sea comparable entre activos
# 
# RESPUESTA A TU DUDA 2:
# Z-score responde: "¿Qué tan raro es este precio?"
# - Z-score = 0: Precio está en el promedio (normal)
# - Z-score = +2: Precio está 2 Std ARRIBA del promedio (muy alto)
# - Z-score = -2: Precio está 2 Std ABAJO del promedio (muy bajo)
#
# Dividimos por Std para normalizar:
# - AAPL cae $10 con Std=$20 → Z-score = -0.5 (normal)
# - TSLA cae $10 con Std=$2 → Z-score = -5 (¡anormal!)
#
# Analogía: Es como decir "temperatura 5° arriba de lo normal"
#           En verano (Std=10°) no es raro
#           En invierno (Std=2°) es MUY raro

# --- GENERACIÓN DE SEÑALES ---

df['Position'] = -np.sign(df['Z_Score'])
# ¿Qué hace? Convierte z-score en señal de trading: +1 (long), -1 (short), 0 (neutral)
# 
# RESPUESTA A TU DUDA 3:
# Usamos NEGATIVO porque es mean reversion:
# 
# Si z-score > 0 (precio muy ALTO):
#    np.sign(z_score) = +1
#    -np.sign(z_score) = -1 → ¡VENDER! (esperamos que baje)
# 
# Si z-score < 0 (precio muy BAJO):
#    np.sign(z_score) = -1
#    -np.sign(z_score) = +1 → ¡COMPRAR! (esperamos que suba)
#
# Analogía: Es como comprar cuando hay oferta y vender cuando está caro
# La lógica: "El precio volverá al promedio" (reversión a la media)

df['Strategy_Returns'] = df['Position'].shift(1) * df['Returns']
# ¿Qué hace? Calcula retorno de la estrategia cada día
# 
# RESPUESTA A TU DUDA 4:
# .shift(1) es CRÍTICO para evitar lookahead bias:
# 
# SIN .shift(1) (MALO):
# - Día 1: Veo que precio es bajo (z-score = -2)
# - Día 1: Compro usando precio del cierre del Día 1
# ¡Problema! Usaría información que solo sé AL FINAL del día
#
# CON .shift(1) (CORRECTO):
# - Día 1: Veo que precio es bajo (z-score = -2)
# - Día 2: Compro al abrir del Día 2
# ✓ Realista: Solo actúo con información del DÍA ANTERIOR
#
# Multiplicación:
# - Si Position = +1 (long) y Returns = +2% → Strategy_Returns = +2% ✓
# - Si Position = -1 (short) y Returns = +2% → Strategy_Returns = -2% (perdemos shorteando en alza)
# - Si Position = 0 (fuera) → Strategy_Returns = 0 (sin exposición)

# ═══════════════════════════════════════════════════════════════
# RIESGOS Y BUGS DETECTADOS
# ═══════════════════════════════════════════════════════════════

# ⚠️ RIESGO 1: Lookback period fijo (20 días)
# Problema: En mercados volátiles 20 días puede ser mucho/poco
# Solución: Considerar lookback adaptativo

# ⚠️ RIESGO 2: No hay stop-loss
# Problema: Si mean reversion falla, pérdidas pueden crecer
# Solución: Agregar stop-loss de -5% o -10%

# ⚠️ RIESGO 3: Asume distribución normal
# Problema: Mercados tienen "fat tails" (eventos extremos más frecuentes)
# Solución: Usar percentiles en lugar de z-score para eventos raros

# ✅ NO HAY BUGS TÉCNICOS: El código está correcto
# ✅ .shift(1) está bien usado (no hay lookahead bias)
# ✅ Lógica de mean reversion es sólida

# ═══════════════════════════════════════════════════════════════
# COMPLEJIDAD
# ═══════════════════════════════════════════════════════════════

# Complejidad: ⭐⭐⭐ (Intermedia)
# 
# Fácil (⭐):
# - Cálculo de returns
# - Promedio móvil
# 
# Intermedia (⭐⭐⭐):
# - Concepto de z-score
# - Lógica de mean reversion (invertir señal)
# - Uso correcto de .shift() para evitar lookahead
#
# Si esto es tu primer backtest: ¡Está perfecto para aprender!
# Si ya hiciste backtests simples: Este es buen "segundo paso"
```

---

## 💡 VARIACIONES DEL PROMPT

### Variación A: Enfoque en Bugs/Errores

```markdown
📊 CONTEXTO:
Este código da resultados sospechosos (Sharpe 5.0). 
Creo que tiene lookahead bias u otro bug.

🎯 TAREA:
1. Identifica TODOS los posibles bugs
2. Señala líneas específicas problemáticas
3. Sugiere corrección para cada bug

[Resto igual...]
```

### Variación B: Comparar Dos Implementaciones

```markdown
📊 CONTEXTO:
Tengo DOS versiones del mismo concepto. No sé cuál es mejor.

Versión A:
```python
[CÓDIGO A]
```

Versión B:
```python
[CÓDIGO B]
```

🎯 TAREA:
Compara ambas versiones:
1. ¿Hacen lo mismo o hay diferencias sutiles?
2. ¿Cuál es más eficiente?
3. ¿Cuál tiene menos bugs potenciales?
4. ¿Cuál recomendarías para producción?
```

### Variación C: Profundizar en Concepto Específico

```markdown
📊 CONTEXTO:
En este código hay una línea que usa "vectorización" con numpy.

🎯 TAREA:
Enfócate SOLO en las líneas 15-20 y:
1. Explica qué es vectorización
2. Por qué es importante en trading algorítmico
3. Muestra versión SIN vectorizar (con for loop) para comparar
4. Mide diferencia de performance (tiempo de ejecución)
```

---

## ✅ CHECKLIST POST-EXPLICACIÓN

Después de recibir explicación del AI:

- [ ] ¿Entiendes el propósito general del código?
- [ ] ¿Puedes explicar cada línea con tus propias palabras?
- [ ] ¿Sabes por qué se usó .shift() (si aplica)?
- [ ] ¿Identificaste posibles lookahead bias?
- [ ] ¿El AI usó analogías que te ayudaron?
- [ ] ¿Podrías modificar el código ahora con confianza?

**Si 5+ checks = ✅:** Código entendido, listo para usar/adaptar  
**Si <5 checks = ✅:** Pide aclaración en puntos específicos

---

## 🎓 TIPS DE EXPERTO

### 1. Empieza con Código Pequeño (<50 Líneas)

Si el código es muy largo:
```markdown
Opción A: Divide en secciones y explica una a la vez
Opción B: Pide primero "resumen ejecutivo" y luego profundizar
```

### 2. Pide Analogías Explícitas

Agrega a tu prompt:
```markdown
⛔ RESTRICCIONES:
- Para CADA concepto técnico, incluye una analogía con trading manual
```

### 3. Pregunta "¿Qué Pasaría Si...?"

Follow-up útiles:
```markdown
"¿Qué pasaría si elimino .shift(1)?"
"¿Qué pasaría si cambio rolling(20) a rolling(50)?"
"¿Qué pasaría si este código se ejecuta en live trading?"
```

### 4. Pide Visualización

```markdown
🎯 TAREA:
[... tarea normal ...]
Al final, sugiere cómo visualizar esto en un gráfico de pandas/matplotlib
```

### 5. Valida Con Testing

```python
# Después de entender, escribe test
def test_mi_entendimiento():
    # Si entendí bien, esto debería pasar
    assert df['Z_Score'].mean() == 0  # Por definición del z-score
    assert df['Position'].isin([-1, 0, 1]).all()  # Solo estas señales
```

---

## 🚨 SEÑALES DE CÓDIGO PROBLEMÁTICO

Si el AI señala estas cosas, **NO uses el código sin corregir:**

### 🔴 Lookahead Bias

```python
# ❌ MALO: Usa datos futuros
df['Signal'] = np.where(df['Close'] > df['High'].shift(-1), 1, 0)
                                               # ↑ shift negativo = futuro!
```

### 🔴 Data Snooping

```python
# ❌ MALO: Parámetros "mágicos" sin justificación
if z_score < -2.73:  # ¿Por qué 2.73? ¿Fue optimizado hasta funcionar?
    buy()
```

### 🔴 Survivorship Bias

```python
# ❌ MALO: Solo testa con activos que sobrevivieron
tickers = ['AAPL', 'MSFT', 'GOOGL']  
# ¿Dónde están las empresas que quebraron?
```

### 🔴 Falta de Manejo de Errores

```python
# ❌ MALO: ¿Qué pasa si API falla?
data = yf.download('SPY')  # Sin try/except
```

---

## 🔗 PRÓXIMOS PASOS

**Después de entender el código:**

1. **Docuéntalo:** Agrega comentarios que escribiste con AI
2. **Testa:** Ejecuta con datos pequeños para validar comprensión
3. **Adapta:** Usa Prompt 02 para personalizarlo
4. **Guarda:** Crea notebook con código + explicación

---

## 📚 RECURSOS ADICIONALES

### En el Workshop Premium:

- 🔒 **Prompt 03B:** Explicar Conceptos Matemáticos (Sharpe, Sortino, etc.)
- 🔒 **Prompt 03C:** Debugging Asistido (encuentra bugs automáticamente)
- 🔒 **Prompt 03D:** Optimización de Performance (de lento a rápido)
- 🔒 **50+ Códigos Explicados** (biblioteca de ejemplos anotados)

### Lecturas Recomendadas:

- **VanderPlas, J. (2016)** - Python Data Science Handbook
- **Chan, E. (2013)** - Algorithmic Trading (código bien comentado)
- Stack Overflow: Preguntas sobre pandas, numpy, backtesting

---

## 💬 SOPORTE

**¿Aún no entiendes algo después de la explicación?**

📧 Email: yismaryme@gmail.com (con código + duda específica)  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Code reviews en vivo]

**Recuerda:** No hay preguntas tontas. Si no entiendes, pregunta.

---

**Versión:** 1.0 (Público)  
**Última actualización:** 20 de noviembre de 2025  
**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa
