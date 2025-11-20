# 🔧 PROMPT 04: Adaptar Código Existente a Tu Estrategia

> **Categoría:** Implementación  
> **Sesión del Workshop:** S4 - Implementación Práctica Guiada  
> **Dificultad:** ⭐⭐⭐ (Intermedio)  
> **Plataformas:** Claude, ChatGPT, Cursor

---

## 🎯 Propósito del Prompt

Tomar código de ejemplo (del workshop, GitHub, papers) y **adaptarlo a tu estrategia específica** modificando:
- Indicadores técnicos
- Reglas de entrada/salida
- Gestión de riesgo
- Activos y timeframes

**Filosofía del Workshop:**  
> "No programas desde cero. Adaptas código funcionando con ayuda de GenAI."

---

## 📋 Template del Prompt

```markdown
CONTEXTO:
Tengo este código de una estrategia de trading algorítmico [mean reversion / 
momentum / breakout] que funciona en [activo original]. Necesito adaptarlo 
para mi propia estrategia que opera en [mi activo] con [mi lógica].

ROL:
Actúa como un Senior Python Developer especializado en trading algorítmico. 
Tienes experiencia con pandas, numpy, backtesting.py, y APIs de brokers 
(Alpaca, Interactive Brokers). Sigues PEP 8 y escribes código production-ready.

CÓDIGO ORIGINAL:
```python
[Pega aquí el código completo que quieres adaptar]
```

MI ESTRATEGIA:
- Activo: [Ej: QQQ]
- Indicador principal: [Ej: RSI en lugar de Bollinger Bands]
- Regla de entrada: [Ej: Comprar cuando RSI < 30]
- Regla de salida: [Ej: Vender cuando RSI > 70 o después de 5 días]
- Position sizing: [Ej: 2% del capital por trade]

TAREA:
Adapta el código para implementar MI estrategia manteniendo:
1. La estructura general del código original
2. Las funciones de gestión de riesgo
3. El logging y error handling
4. Los comentarios explicativos

FORMATO:
- Código completo modificado con comentarios que expliquen CADA cambio
- Sección al final: "CAMBIOS REALIZADOS" en bullet points
- Sección: "PRÓXIMOS PASOS" (qué deberías revisar/testear)

RESTRICCIONES:
- NO cambies la estructura de clases/funciones sin explicar por qué
- NO elimines el error handling del código original
- SÍ agrega validaciones si introduzco nuevos parámetros
- SÍ mantén o mejora los docstrings
- SÍ usa type hints (Python 3.7+)
```

---

## 💡 Ejemplo de Uso Real

### Código Original (Ejemplo Simplificado):

```python
import pandas as pd
import yfinance as yf

def bollinger_strategy(ticker, start, end):
    """
    Estrategia mean reversion con Bollinger Bands
    """
    # Descargar datos
    data = yf.download(ticker, start=start, end=end)
    
    # Calcular Bollinger Bands
    data['SMA'] = data['Close'].rolling(20).mean()
    data['STD'] = data['Close'].rolling(20).std()
    data['Upper'] = data['SMA'] + (data['STD'] * 2)
    data['Lower'] = data['SMA'] - (data['STD'] * 2)
    
    # Señales
    data['Signal'] = 0
    data.loc[data['Close'] < data['Lower'], 'Signal'] = 1  # Comprar
    data.loc[data['Close'] > data['Upper'], 'Signal'] = -1  # Vender
    
    return data

# Ejecutar
result = bollinger_strategy('SPY', '2020-01-01', '2024-01-01')
```

### Tu Prompt Completo:

```markdown
CONTEXTO:
Tengo este código de estrategia con Bollinger Bands en SPY. Quiero adaptarlo 
para usar RSI en QQQ.

[Incluir todo el template de arriba + el código]

MI ESTRATEGIA:
- Activo: QQQ
- Indicador: RSI (14 periodos)
- Entrada: Comprar cuando RSI < 30
- Salida: Vender cuando RSI > 70
- Stop loss: -5% desde entrada
```

### Output Esperado de la IA:

```python
import pandas as pd
import yfinance as yf
from typing import Tuple

def rsi_strategy(
    ticker: str = 'QQQ',
    start: str = '2020-01-01',
    end: str = '2024-01-01',
    rsi_period: int = 14,
    rsi_oversold: int = 30,
    rsi_overbought: int = 70,
    stop_loss_pct: float = 0.05
) -> pd.DataFrame:
    """
    Estrategia mean reversion con RSI
    
    CAMBIOS vs. código original:
    - Reemplazado Bollinger Bands por RSI
    - Agregado stop loss dinámico
    - Ticker default cambiado a QQQ
    - Agregados type hints
    
    Args:
        ticker: Símbolo del activo (default: QQQ)
        start: Fecha inicio formato 'YYYY-MM-DD'
        end: Fecha fin formato 'YYYY-MM-DD'
        rsi_period: Periodos para calcular RSI (default: 14)
        rsi_oversold: Umbral de sobreventa (default: 30)
        rsi_overbought: Umbral de sobrecompra (default: 70)
        stop_loss_pct: Porcentaje de stop loss (default: 0.05 = 5%)
        
    Returns:
        DataFrame con precios, RSI y señales
    """
    # Descargar datos
    data = yf.download(ticker, start=start, end=end, progress=False)
    
    # Validación de datos
    if data.empty:
        raise ValueError(f"No se pudieron descargar datos para {ticker}")
    
    # Calcular RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()
    
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Señales de trading
    data['Signal'] = 0
    data['Entry_Price'] = 0.0  # NUEVO: Trackear precio de entrada para stop loss
    
    # Lógica de entrada (RSI oversold)
    data.loc[data['RSI'] < rsi_oversold, 'Signal'] = 1  # Comprar
    
    # Lógica de salida (RSI overbought)
    data.loc[data['RSI'] > rsi_overbought, 'Signal'] = -1  # Vender
    
    # NUEVO: Implementar stop loss
    in_position = False
    entry_price = 0
    
    for i in range(1, len(data)):
        if not in_position and data['Signal'].iloc[i] == 1:
            # Entramos a posición
            in_position = True
            entry_price = data['Close'].iloc[i]
            data.loc[data.index[i], 'Entry_Price'] = entry_price
            
        elif in_position:
            current_price = data['Close'].iloc[i]
            # Check stop loss
            if current_price < entry_price * (1 - stop_loss_pct):
                data.loc[data.index[i], 'Signal'] = -1  # Vender por stop loss
                in_position = False
            # Check salida normal
            elif data['Signal'].iloc[i] == -1:
                in_position = False
    
    return data

# Ejecutar estrategia
result = rsi_strategy(
    ticker='QQQ',
    start='2020-01-01',
    end='2024-01-01'
)

print("\\n=== ESTADÍSTICAS ===")
print(f"Total señales de compra: {(result['Signal'] == 1).sum()}")
print(f"Total señales de venta: {(result['Signal'] == -1).sum()}")
print(f"RSI promedio: {result['RSI'].mean():.2f}")

## CAMBIOS REALIZADOS:
- ✅ Reemplazado cálculo de Bollinger Bands por RSI (14 periodos)
- ✅ Cambiado ticker default de SPY a QQQ
- ✅ Modificado umbrales: RSI < 30 (compra), RSI > 70 (venta)
- ✅ Agregado stop loss dinámico (-5% desde entrada)
- ✅ Agregados type hints para mejor documentación
- ✅ Agregada validación de datos descargados
- ✅ Agregado tracking de precio de entrada
- ✅ Agregadas estadísticas básicas en output

## PRÓXIMOS PASOS:
1. ⚠️ VALIDAR: Ejecuta el código y verifica que funciona sin errores
2. 📊 BACKTEST: Usa backtesting.py o similar para métricas completas
3. 🔧 OPTIMIZAR: Prueba diferentes valores de RSI (30/70 vs. 20/80)
4. 📈 VISUALIZAR: Grafica RSI + señales + equity curve
5. ⚠️ REVIEW: Verifica lógica de stop loss (puede generar muchas salidas)
```

---

## ⚠️ Advertencias Críticas

### 1. IA Puede Introducir Bugs Silenciosos
```python
# Bug común que IA podría introducir:
data.loc[data['RSI'] < 30] = 1  # ❌ MALO: Sobrescribe toda la fila

# Correcto:
data.loc[data['RSI'] < 30, 'Signal'] = 1  # ✅ BUENO: Solo columna Signal
```

**Solución:**  
→ SIEMPRE ejecuta el código adaptado  
→ Valida con print() los valores clave  
→ Compara output con tus expectativas

### 2. Lógica de Backtesting Puede Ser Incorrecta
```python
# Look-ahead bias (IA podría no detectarlo):
data['Signal'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
#                                    ^ Usando datos del FUTURO!
```

**Principio:** (López de Prado, 2018)
> "El look-ahead bias es el error más común y costoso en backtesting"

**Solución:**  
→ Revisa MANUALMENTE que no uses .shift(-1) para decisiones  
→ Solo shift() positivo o sin shift está permitido  
→ Pide a la IA: "Revisa que no haya look-ahead bias"

### 3. IA No Optimiza Performance
```python
# IA podría generar código lento:
for i in range(len(data)):  # Loop Python lento
    if data['Close'].iloc[i] > data['SMA'].iloc[i]:
        data.loc[data.index[i], 'Signal'] = 1

# Mejor (vectorizado):
data['Signal'] = np.where(data['Close'] > data['SMA'], 1, 0)
```

**Solución:**  
→ Pide explícitamente: "Usa operaciones vectorizadas con pandas"  
→ Para datasets >100k filas, la velocidad importa

---

## 🔧 Variaciones del Prompt

### Variación A: Adaptar Entre Plataformas
```markdown
TAREA ADICIONAL:
El código original usa backtesting.py. Adáptalo para usar Backtrader.
Mantén la misma lógica de estrategia pero cambia el framework.
```

### Variación B: Agregar Features Avanzados
```markdown
TAREA ADICIONAL:
Además de la adaptación básica, agrega:
- Position sizing dinámico (Kelly Criterion)
- Trailing stop loss
- Filtro de volumen (solo operar si volumen > promedio)
```

### Variación C: Simplificar Código Complejo
```markdown
CONTEXTO ADICIONAL:
El código original tiene 500 líneas y es difícil de entender.

TAREA:
Simplifica el código manteniendo solo:
- La lógica core de la estrategia
- Elimina optimizaciones prematuras
- Hazlo más legible para un principiante
```

---

## 📊 Checklist de Validación Post-Adaptación

Después de recibir código adaptado de la IA:

### Paso 1: Validación Sintáctica
- [ ] El código ejecuta sin errores
- [ ] Todos los imports están presentes
- [ ] No hay variables undefined

### Paso 2: Validación Lógica
- [ ] Las señales de compra/venta son correctas
- [ ] No hay look-ahead bias (revisar .shift(-1))
- [ ] El stop loss se activa correctamente

### Paso 3: Validación de Output
- [ ] El DataFrame resultante tiene las columnas esperadas
- [ ] Los valores de indicadores son razonables (RSI entre 0-100, etc.)
- [ ] El número de señales es realista (no 0, no 10,000)

### Paso 4: Comparación con Original
- [ ] La estructura general se mantiene
- [ ] El error handling no fue eliminado
- [ ] Los docstrings están actualizados

---

## 🎓 Fundamento Teórico

### ¿Por Qué Adaptar en Lugar de Crear?

**Razones pedagógicas:**
1. **Andamiaje:** Código funcionando es tu scaffold (Vygotsky)
2. **Pattern recognition:** Aprendes patrones comunes en trading code
3. **Menor carga cognitiva:** Focus en lógica, no sintaxis

**Razones prácticas:**
1. **Velocidad:** 10x más rápido que escribir desde cero
2. **Menos bugs:** Código probado como base
3. **Best practices:** Hereda estructura profesional

**Cita:** (Chan, 2013)
> "No reinventes la rueda. Adapta estrategias conocidas a tu tesis única."

---

## 📚 Recursos Complementarios

### Código Base Recomendado:
- **Workshop Colab Notebook:** Estrategias de S4-S6
- **GitHub:** [Awesome Quant Trading](https://github.com/topics/algorithmic-trading)
- **Strimpe (2024):** Python for Algorithmic Trading Cookbook

### Otros Prompts Relacionados:
- [PROMPT 05: Explicar Código Complejo](05_Explicar_Codigo_Complejo.md)
- [PROMPT 06: Depurar Errores](06_Depurar_Errores.md)
- [PROMPT 07: Optimizar Performance](07_Optimizar_Performance.md)

---

## 💬 Ejemplo de Conversación Iterativa

**Usuario:**
```
[Pega código adaptado que recibió]

"Este código genera 200 señales de compra en 4 años. 
Es demasiado. ¿Cómo puedo reducir la frecuencia de trades?"
```

**IA (respuesta típica):**
```python
# Agrega filtros adicionales:

# 1. Filtro de volumen
data['Volume_MA'] = data['Volume'].rolling(20).mean()
data['High_Volume'] = data['Volume'] > data['Volume_MA'] * 1.5

# 2. Filtro de tendencia (solo operar con tendencia alcista)
data['SMA_50'] = data['Close'].rolling(50).mean()
data['Uptrend'] = data['Close'] > data['SMA_50']

# 3. Modificar señal de entrada
data.loc[
    (data['RSI'] < 30) &        # Condición original
    (data['High_Volume']) &      # NUEVO filtro
    (data['Uptrend']),           # NUEVO filtro
    'Signal'
] = 1
```

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Autor:** Workshop Trading Algorítmico Aumentado con IA Generativa  
**Licencia:** Uso educativo libre
