# 📖 PROMPT 05: Explicar Código Complejo Línea por Línea

> **Categoría:** Aprendizaje  
> **Sesión del Workshop:** Todas (herramienta transversal)  
> **Dificultad:** ⭐ (Básico)  
> **Plataformas:** Claude, ChatGPT, Gemini

---

## 🎯 Propósito del Prompt

Entender código de trading algorítmico que encontraste en:
- Papers académicos
- Repositorios de GitHub
- Estrategias compartidas por otros traders
- Documentación de librerías (backtesting.py, zipline, etc.)

**Objetivo:** Pasar de "no entiendo nada" a "puedo explicarlo a otra persona"

---

## 📋 Template del Prompt

```markdown
CONTEXTO:
Soy trader [con X experiencia] aprendiendo trading algorítmico. Encontré 
este código que implementa [tipo de estrategia] pero no entiendo cómo funciona.

ROL:
Actúa como un profesor de programación especializado en enseñar a traders 
que NO tienen background técnico. Usas analogías del mundo del trading manual 
para explicar conceptos de programación.

CÓDIGO A EXPLICAR:
```python
[Pega aquí el código completo que no entiendes]
```

TAREA:
Explica este código de la siguiente manera:

1. **OVERVIEW (2-3 líneas):** ¿Qué hace este código en términos generales?

2. **EXPLICACIÓN LÍNEA POR LÍNEA:**
   - Para cada línea (o bloque lógico), explica:
     * Qué hace técnicamente
     * Por qué es necesaria
     * Analogía con trading manual (cuando aplique)
   
3. **CONCEPTOS CLAVE:** Lista y explica términos técnicos usados
   (ej: ".rolling()", ".shift()", np.where, etc.)

4. **FLUJO DE DATOS:** Describe cómo fluye la información desde input hasta output

5. **PUNTOS CRÍTICOS:** Identifica las 3-5 líneas MÁS importantes (el "core" de la lógica)

FORMATO:
Usa markdown con:
- Bloques de código con comentarios inline
- Secciones claras por paso
- Emojis para highlighting (⚠️ para warnings, 🔑 para key concepts)

RESTRICCIONES:
- NO asumas que entiendo términos técnicos (explica CADA uno)
- SÍ usa analogías de trading manual (stop loss, take profit, señales)
- NO uses jerga de programación sin explicar
- SÍ incluye ejemplos numéricos concretos cuando ayude
```

---

## 💡 Ejemplo de Uso Real

### Código Misterioso:

```python
import pandas as pd
import numpy as np

def calculate_signals(df, window=20):
    df['returns'] = df['close'].pct_change()
    df['volatility'] = df['returns'].rolling(window).std()
    df['z_score'] = (df['close'] - df['close'].rolling(window).mean()) / df['volatility']
    df['signal'] = np.where(df['z_score'] < -2, 1, np.where(df['z_score'] > 2, -1, 0))
    return df
```

### Tu Prompt:

```markdown
CONTEXTO:
Soy trader con 2 años de experiencia manual. Este código calcula señales 
de trading pero no entiendo qué es "z_score" ni por qué -2 y 2.

[Copiar template completo + código arriba]
```

### Output Esperado de la IA:

```markdown
## 1. OVERVIEW

Este código implementa una **estrategia de mean reversion** basada en 
Z-Score. Identifica cuándo el precio se alejó "demasiado" de su promedio 
y genera señales para apostar al retorno.

**Analogía trading manual:**  
Imagina que observas que AAPL normalmente oscila entre $170-$180. 
Si un día cae a $160 sin razón fundamental, compras esperando el rebote. 
Este código automatiza esa lógica.

---

## 2. EXPLICACIÓN LÍNEA POR LÍNEA

```python
def calculate_signals(df, window=20):
```
**Qué hace:** Define una función que recibe un DataFrame con precios 
y un parámetro `window` (ventana de 20 días por defecto)

**Analogía:** Window = "cuántos días hacia atrás miro para calcular el promedio"  
Si window=20, miras los últimos 20 días. Si window=50, los últimos 50.

---

```python
df['returns'] = df['close'].pct_change()
```
**Qué hace:** Calcula el retorno porcentual día a día

**Técnicamente:**  
`.pct_change()` = (Precio_hoy - Precio_ayer) / Precio_ayer

**Ejemplo numérico:**  
- Ayer: $100  
- Hoy: $102  
- Return: (102 - 100) / 100 = 0.02 = 2%

**Por qué importa:** Necesitamos returns para calcular volatilidad

---

```python
df['volatility'] = df['returns'].rolling(window).std()
```
🔑 **KEY CONCEPT:** Volatilidad = "qué tan salvaje se mueve el precio"

**Técnicamente:**  
`.rolling(20)` = ventana móvil de 20 días  
`.std()` = desviación estándar (medida de dispersión)

**Analogía trading:**  
- Volatilidad baja: Precio se mueve $1-$2 por día (estable)
- Volatilidad alta: Precio se mueve $10-$15 por día (salvaje)

**Ejemplo:**  
Si en 20 días los returns fueron: [1%, -0.5%, 2%, -1%, ...]  
La desviación estándar podría ser 0.015 (1.5% volatilidad diaria)

---

```python
df['z_score'] = (df['close'] - df['close'].rolling(window).mean()) / df['volatility']
```
🔑 **KEY CONCEPT:** Z-Score = "¿Qué tan lejos está el precio de su promedio, medido en unidades de volatilidad?"

**Fórmula:**  
Z-Score = (Precio_actual - Promedio_20días) / Volatilidad_20días

**Ejemplo numérico:**
- Precio actual: $100  
- Promedio 20 días: $105  
- Volatilidad: $2  
- Z-Score = (100 - 105) / 2 = **-2.5**

**Interpretación:**  
- Z-Score = 0: Precio en su promedio (normal)  
- Z-Score = -2: Precio está 2 desviaciones estándar ABAJO (barato)
- Z-Score = +2: Precio está 2 desviaciones estándar ARRIBA (caro)

**⚠️ Estadística:**  
En distribución normal:
- 68% de datos están entre -1 y +1
- 95% están entre -2 y +2
- 99.7% están entre -3 y +3

Por eso -2 y +2 son umbrales "extremos"

---

```python
df['signal'] = np.where(df['z_score'] < -2, 1, np.where(df['z_score'] > 2, -1, 0))
```
🔑 **KEY CONCEPT:** Lógica de señales (nested conditional)

**Traducción a español:**
```
SI z_score < -2:
    signal = 1 (COMPRAR - precio muy bajo)
SINO, SI z_score > 2:
    signal = -1 (VENDER - precio muy alto)
SINO:
    signal = 0 (NO HACER NADA - precio normal)
```

**Analogía trading:**
- Z-Score < -2: "Precio en descuento extremo → COMPRA"
- Z-Score > +2: "Precio en premium extremo → VENDE (o short)"
- Z-Score entre -2 y +2: "Precio normal → ESPERA"

---

```python
return df
```
**Qué hace:** Devuelve el DataFrame completo con las nuevas columnas agregadas  
(returns, volatility, z_score, signal)

---

## 3. CONCEPTOS CLAVE

### `.pct_change()`
Calcula retorno porcentual entre valores consecutivos.  
Equivale a: (valor_actual - valor_anterior) / valor_anterior

### `.rolling(window)`
Ventana móvil: calcula estadísticas sobre los últimos N valores.  
Rolling(20).mean() = promedio de últimos 20 valores.

### `.std()`
Desviación estándar: mide "dispersión" o "volatilidad".  
Valores más dispersos = std más alta = más riesgo.

### `np.where(condición, si_true, si_false)`
Operador condicional vectorizado (aplica a toda la columna a la vez).  
Es el IF-ELSE de numpy/pandas.

### Z-Score
Normalización estadística: expresa "qué tan lejos de la media" en unidades de desviación estándar.  
Permite comparar activos con diferentes escalas de precio.

---

## 4. FLUJO DE DATOS

```
INPUT: DataFrame con columna 'close' (precios de cierre)
  ↓
Calcular returns día a día
  ↓
Calcular volatilidad (rolling std de returns)
  ↓
Calcular z-score (distancia del precio vs. promedio, normalizada)
  ↓
Generar signal (-1, 0, 1) basado en umbrales de z-score
  ↓
OUTPUT: DataFrame con columnas adicionales (returns, volatility, z_score, signal)
```

---

## 5. PUNTOS CRÍTICOS (El Core)

### 🔑 Línea MÁS importante:
```python
df['z_score'] = (df['close'] - df['close'].rolling(window).mean()) / df['volatility']
```
**Por qué:** Aquí se calcula el "edge" de la estrategia.  
Todo lo demás es preparación (returns, volatility) o decisión (signal).

### 🔑 Segunda línea más importante:
```python
df['signal'] = np.where(df['z_score'] < -2, 1, np.where(df['z_score'] > 2, -1, 0))
```
**Por qué:** Convierte el z-score en acción concreta (comprar/vender/esperar).  
Los umbrales -2 y +2 definen cuándo la estrategia "ve oportunidad".

### 🔑 Parámetro crítico:
```python
window=20
```
**Por qué:** Define el horizonte temporal de la estrategia.  
window=20 → estrategia de corto plazo (3-4 semanas)  
window=200 → estrategia de largo plazo (10 meses)

---

## ⚠️ LIMITACIONES DE ESTA ESTRATEGIA

1. **Asume mean reversion:** Solo funciona si el precio REALMENTE revierte  
   Si hay tendencia fuerte, generará pérdidas.

2. **Asume distribución normal:** Z-score asume que returns son normales  
   En realidad, mercados tienen "fat tails" (colas gordas)

3. **No considera costos:** Cada señal implica comisiones + slippage

4. **No tiene stop loss:** Si precio sigue cayendo, estrategia sigue comprado

---

## 📚 PARA PROFUNDIZAR

**Conceptos estadísticos:**
- Z-Score: [Khan Academy - Z-Score](https://www.khanacademy.org/math/statistics-probability)
- Mean Reversion: Chan (2013), Cap. 3

**Funciones de pandas:**
- `.rolling()`: [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
- `.pct_change()`: [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html)

**Papers originales:**
- Bollinger, J. (2002) - "Bollinger on Bollinger Bands" (concepto similar)

---

## ✅ AUTOEVALUACIÓN

¿Entendiste el código? Responde sin mirar arriba:

1. ¿Qué mide el z-score?
2. ¿Por qué -2 y +2 son umbrales especiales?
3. ¿Qué pasa si cambias window de 20 a 5?
4. ¿En qué tipo de mercado esta estrategia funcionaría MEJOR?
5. ¿En qué tipo de mercado FALLARÍA?

[Ver respuestas](RESPUESTAS_AUTOEVALUACION.md)
```

---

## 🔧 Variaciones del Prompt

### Variación A: Para Código MUY Complejo (>100 líneas)
```markdown
TAREA ADICIONAL:
En lugar de explicar línea por línea, divide el código en "bloques funcionales"  
y explica cada bloque (setup, procesamiento de datos, lógica de señales, output).

Luego profundiza SOLO en el bloque de "lógica de señales" línea por línea.
```

### Variación B: Enfoque en Performance
```markdown
TAREA ADICIONAL:
Después de explicar el código, identifica:
- Operaciones lentas (loops, .apply())
- Cómo vectorizarlo para mayor velocidad
- Estimación: ¿Cuánto tardaría con 10 años de datos diarios?
```

### Variación C: Enfoque en Errores Potenciales
```markdown
TAREA ADICIONAL:
Identifica 3 formas en las que este código podría FALLAR en producción:
- Datos faltantes (NaN)
- División por cero
- Look-ahead bias
- Cambios en estructura de datos
```

---

## ⚠️ Advertencias

### IA Puede Explicar Código INCORRECTO con Confianza

```python
# Código con bug sutil:
df['signal'] = np.where(df['z_score'] < -2, 1, -1)  # ❌ Siempre compra o vende

# IA podría explicar:
"Esta línea genera señal de compra (1) si z-score < -2,  
 y señal de venta (-1) en todos los demás casos"

# El problema: NO HAY SEÑAL NEUTRA (0)
# Estrategia operaría 100% del tiempo (sobretrading)
```

**Solución:**  
→ Después de la explicación, EJECUTA el código  
→ Valida con print() que hace lo que IA dice  
→ Si hay discrepancia, pregunta: "¿Por qué el output no coincide con tu explicación?"

---

## 📚 Recursos Complementarios

### Para Mejorar Lectura de Código:
- **PEP 8:** Guía de estilo de Python
- **Clean Code (Martin):** Principios de código legible
- **Workshop S4:** Implementación Práctica (video con live coding)

### Otros Prompts Relacionados:
- [PROMPT 04: Adaptar Código](04_Adaptar_Codigo_Existente.md)
- [PROMPT 06: Depurar Errores](06_Depurar_Errores.md)

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Autor:** Workshop Trading Algorítmico Aumentado con IA Generativa
