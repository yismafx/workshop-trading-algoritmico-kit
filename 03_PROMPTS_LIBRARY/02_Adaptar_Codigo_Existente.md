# 🤖 PROMPT 02: Adaptar Código Existente de Estrategia

> **Categoría:** Implementación y Modificación  
> **Nivel:** Básico-Intermedio  
> **Sesión del Workshop:** S4 - Implementación Práctica  
> **Compatible con:** Claude, ChatGPT, Gemini

---

## 🎯 PROPÓSITO

Modificar código de estrategias existentes (ejemplos de libros, repos de GitHub, o del workshop) para adaptarlo a:
- Tus activos específicos (cambiar de SPY a criptos, por ejemplo)
- Tu horizonte temporal (de intraday a swing)
- Tus indicadores preferidos (cambiar RSI por MACD)
- Tu plataforma de trading (de Alpaca a Interactive Brokers)

**⚠️ Importante:** Siempre valida el código adaptado con backtesting antes de usar con dinero real.

---

## 📋 ESTRUCTURA DEL PROMPT

### Template Básico

```markdown
🎭 ROL:
Actúa como un desarrollador senior especializado en Python para trading algorítmico.
Tienes expertise en librerías como pandas, numpy, pandas-ta, yfinance, y 
APIs de brokers (Alpaca, Interactive Brokers).

📊 CONTEXTO:
Tengo el siguiente código de una estrategia [NOMBRE ESTRATEGIA] que encontré en 
[FUENTE: libro/GitHub/curso]. Funciona correctamente para [ACTIVO ORIGINAL] 
en timeframe [TIMEFRAME ORIGINAL].

Código original:
```python
[PEGAR CÓDIGO AQUÍ - máximo 100 líneas]
```

🎯 TAREA:
Necesito adaptar este código para:

**Cambios requeridos:**
1. [Ej: Cambiar de activo SPY a BTC-USD]
2. [Ej: Modificar timeframe de diario a 4 horas]
3. [Ej: Reemplazar indicador RSI por MACD]
4. [Ej: Agregar stop-loss de -3%]
5. [Ej: Cambiar fuente de datos de yfinance a Alpaca API]

**Manténer intacto:**
- [Ej: La lógica de entrada basada en cruce de medias]
- [Ej: El sistema de logging]

📤 FORMATO:
1. Muestra el código COMPLETO adaptado (no solo fragmentos)
2. Comenta SOLO las líneas que cambiaron (con # CAMBIO:)
3. Al final, lista los 5 cambios principales en formato bullet point
4. Incluye un bloque de "Testing sugerido" con 3 casos de prueba

⛔ RESTRICCIONES:
- NO cambies la estructura general si no es necesario
- NO agregues funcionalidades que no pedí explícitamente
- NO uses librerías exóticas que requieran instalación complicada
- SIEMPRE mantén los comentarios originales del código
- Si detectas un bug en el código original, señálalo pero arréglalo
```

---

## 🔥 EJEMPLO DE USO REAL

### Input (Tu prompt al AI):

```markdown
🎭 ROL:
Actúa como un desarrollador senior especializado en Python para trading algorítmico.
Tienes expertise en pandas, numpy, pandas-ta, yfinance, y APIs de brokers.

📊 CONTEXTO:
Tengo el siguiente código de una estrategia "Simple Moving Average Crossover" 
que encontré en el libro "Algorithmic Trading" de Ernest Chan (2013). 
Funciona correctamente para SPY en timeframe diario.

Código original:
```python
import yfinance as yf
import pandas as pd
import pandas_ta as ta

# Descargar datos
ticker = yf.Ticker("SPY")
df = ticker.history(period="5y", interval="1d")

# Calcular indicadores
df['SMA_20'] = ta.sma(df['Close'], length=20)
df['SMA_50'] = ta.sma(df['Close'], length=50)

# Señales
df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1  # Buy
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1  # Sell

# Retornos
df['Returns'] = df['Close'].pct_change()
df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)

# Performance
total_return = (1 + df['Strategy_Returns']).prod() - 1
print(f"Total Return: {total_return:.2%}")
```

🎯 TAREA:
Necesito adaptar este código para:

**Cambios requeridos:**
1. Cambiar de activo SPY a BTC-USD (Bitcoin)
2. Modificar timeframe de diario a 4 horas
3. Usar Alpaca API en lugar de yfinance (ya tengo API key configurada)
4. Agregar stop-loss de -5% por trade
5. Calcular también Sharpe Ratio al final

**Mantener intacto:**
- La lógica del cruce SMA 20/50
- La estructura general del código

📤 FORMATO:
1. Muestra el código COMPLETO adaptado
2. Comenta SOLO las líneas que cambiaron
3. Lista los 5 cambios principales
4. Incluye "Testing sugerido"

⛔ RESTRICCIONES:
- NO cambies la lógica del cruce de medias
- NO agregues machine learning ni nada avanzado
- NO uses librerías que no sean estándar (pandas, numpy, pandas-ta)
- Mantén comentarios originales
```

### Output Esperado (Lo que el AI responderá):

```python
import pandas as pd
import pandas_ta as ta
from alpaca.data.historical import CryptoHistoricalDataClient  # CAMBIO: Nueva librería
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta

# CAMBIO: Configurar cliente Alpaca para cripto
client = CryptoHistoricalDataClient()

# CAMBIO: Descargar datos BTC-USD en timeframe 4h
request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],  # CAMBIO: De SPY a BTC-USD
    timeframe=TimeFrame.Hour,  # CAMBIO: De diario a 4 horas
    start=datetime.now() - timedelta(days=365*2),  # 2 años de datos
    limit=10000
)

bars = client.get_crypto_bars(request_params)
df = bars.df

# Calcular indicadores (sin cambios)
df['SMA_20'] = ta.sma(df['close'], length=20)  # CAMBIO: 'Close' → 'close' (Alpaca usa minúsculas)
df['SMA_50'] = ta.sma(df['close'], length=50)

# Señales (sin cambios en lógica)
df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1  # Buy
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1  # Sell

# CAMBIO: Implementar stop-loss de -5%
df['Entry_Price'] = df['close'].where(df['Signal'].diff() != 0)
df['Entry_Price'].ffill(inplace=True)
df['Price_Change_Since_Entry'] = (df['close'] - df['Entry_Price']) / df['Entry_Price']

# Si pérdida >= 5%, forzar señal de salida
df.loc[df['Price_Change_Since_Entry'] <= -0.05, 'Signal'] = 0  # CAMBIO: Stop-loss implementado

# Retornos (sin cambios)
df['Returns'] = df['close'].pct_change()  # CAMBIO: 'Close' → 'close'
df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)

# CAMBIO: Performance con Sharpe Ratio
total_return = (1 + df['Strategy_Returns']).prod() - 1
sharpe_ratio = df['Strategy_Returns'].mean() / df['Strategy_Returns'].std() * (252**0.5)  # CAMBIO: Anualizado

print(f"Total Return: {total_return:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")  # CAMBIO: Nueva métrica
```

**Resumen de Cambios Principales:**

1. **Fuente de datos:** yfinance → Alpaca API (CryptoHistoricalDataClient)
2. **Activo:** SPY → BTC/USD (cripto)
3. **Timeframe:** Diario (1d) → 4 horas (TimeFrame.Hour)
4. **Stop-loss:** Implementado lógica para salir si pérdida ≥ -5%
5. **Métricas:** Agregado cálculo de Sharpe Ratio anualizado

**Testing Sugerido:**

```python
# Test 1: Verificar datos descargados
assert len(df) > 100, "Muy pocos datos descargados"
assert 'SMA_20' in df.columns, "Indicador SMA_20 no calculado"

# Test 2: Verificar señales generadas
assert df['Signal'].nunique() >= 2, "No hay señales de compra/venta"

# Test 3: Verificar stop-loss funciona
stopped_trades = df[df['Price_Change_Since_Entry'] <= -0.05]
assert len(stopped_trades) > 0, "Stop-loss nunca se activó (revisar lógica)"

print("✅ Todos los tests pasaron")
```

**⚠️ Notas importantes:**

1. Alpaca API requiere autenticación (API_KEY y SECRET_KEY en variables de entorno)
2. Datos cripto tienen gaps (fines de semana no aplican como en acciones)
3. Stop-loss implementado es simplificado; en producción necesitarías lógica más robusta
4. Sharpe anualizado asume 252 días; para cripto 24/7 usa factor diferente

---

## 💡 VARIACIONES DEL PROMPT

### Variación A: Agregar Funcionalidad Específica

```markdown
🎯 TAREA:
Necesito adaptar este código para:

**Cambios requeridos:**
1. Agregar logging detallado (cada trade en CSV)
2. Enviar notificación por Telegram cuando hay señal de entrada
3. Implementar trailing stop en lugar de stop-loss fijo

[Resto igual...]
```

### Variación B: Corregir Bug en Código Original

```markdown
📊 CONTEXTO:
Tengo este código pero creo que tiene un bug. Cuando ejecuto el backtest, 
me da Sharpe Ratio de 5.8, que es sospechosamente alto. Posible lookahead bias.

Código original:
[PEGAR CÓDIGO]

🎯 TAREA:
1. Identifica el bug (probablemente lookahead bias)
2. Corrígelo
3. Explica qué estaba mal

[Resto igual...]
```

### Variación C: Simplificar Código Complejo

```markdown
📊 CONTEXTO:
Tengo este código de GitHub que funciona pero es súper complejo (200+ líneas, 
muchas funciones anidadas). No entiendo qué hace.

🎯 TAREA:
1. Simplifica el código manteniendo la funcionalidad core
2. Elimina funcionalidades "nice-to-have" innecesarias
3. Agrega comentarios explicativos en cada sección

[Resto igual...]
```

---

## ✅ CHECKLIST POST-ADAPTACIÓN

Después de recibir código adaptado del AI, valida:

- [ ] ¿El código adaptado corre sin errores?
- [ ] ¿Los cambios están claramente comentados?
- [ ] ¿Se mantuvieron las partes que pediste mantener?
- [ ] ¿El AI agregó funcionalidades que NO pediste? (si sí, elimínalas)
- [ ] ¿El AI incluyó casos de prueba/testing?
- [ ] ¿Entiendes cada línea modificada?

**Si 5+ checks = ✅:** Código listo para backtest  
**Si <5 checks = ✅:** Pide iteración al AI o revisa manualmente

---

## 🎓 TIPS DE EXPERTO

### 1. No Pegues Código Gigante (Máx 100 Líneas)

Si tu código original es >100 líneas:
```markdown
Opción A: Pega solo la función/sección que necesitas cambiar
Opción B: Usa múltiples prompts iterativos (cambio 1, luego cambio 2, etc.)
```

### 2. Especifica EXACTAMENTE Qué Mantener

❌ **Malo:** "Adapta este código para Bitcoin"  
✅ **Bueno:** "Adapta para Bitcoin pero MANTÉN la lógica del RSI y el stop-loss actual"

### 3. Pide Tests Específicos

```markdown
⛔ RESTRICCIONES:
[... tus restricciones existentes ...]
- Al final, incluye 3 test cases que yo pueda copiar-pegar para validar
```

### 4. Itera Si El Primer Output No Es Perfecto

```markdown
Prompt inicial: [Adapta este código...]

Follow-up 1: "El código adaptado da error en línea 45. 
             El problema es [EXPLICAR ERROR]. Corrígelo."

Follow-up 2: "Perfecto, ahora agrega manejo de errores 
             por si la API de Alpaca falla."
```

### 5. Guarda Versiones

```python
# Versión original
estrategia_v1.py

# Versión adaptada
estrategia_v2_btc_4h.py

# Versión con stop-loss mejorado
estrategia_v3_btc_4h_trailing_stop.py
```

---

## 🚨 ERRORES COMUNES AL ADAPTAR CÓDIGO

### Error 1: Cambiar Demasiadas Cosas a la Vez

**Problema:**
```markdown
"Quiero cambiar de SPY a Bitcoin, de diario a 1min, 
agregar 5 indicadores nuevos, implementar ML, 
y que envíe tweets automáticos"
```

**Solución:** Haz cambios incrementales. Un prompt por cambio mayor.

---

### Error 2: No Validar Compatibilidad de Datos

**Problema:**
```python
# Código adaptado de acciones a forex
df['Volume']  # ❌ Muchos pares forex no tienen volumen!
```

**Solución:** Especifica en tu prompt:
```markdown
⛔ RESTRICCIONES:
- Si el nuevo activo no tiene volumen, elimina dependencias de volumen
```

---

### Error 3: Lookahead Bias al Adaptar

**Problema original:**
```python
df['Signal'] = np.where(df['Close'] > df['High'].shift(-1), 1, 0)
# ❌ Usa datos del FUTURO (.shift(-1))
```

**Prompt de corrección:**
```markdown
"Revisa si el código adaptado tiene lookahead bias. 
Si lo tiene, corrígelo asegurándote de que solo usa datos pasados."
```

---

## 🔗 PRÓXIMOS PASOS

**Después de adaptar tu código:**

1. **Testing manual:** Ejecuta en notebook con datos pequeños (100 filas)
2. **Backtest:** Usa el código en tu backtest riguroso (Sesión 5)
3. **Documenta:** Actualiza tu [Strategy Memo](../../02_TEMPLATE_PACK/Strategy_Memo_Template.md)
4. **Version control:** Guarda en GitHub con commit descriptivo

---

## 📚 RECURSOS ADICIONALES

### En el Workshop Premium:

- 🔒 **Prompt 02B:** Optimizar Performance de Código (vectorización)
- 🔒 **Prompt 02C:** Migrar Código Entre Plataformas (Python → Pine Script)
- 🔒 **Prompt 02D:** Agregar Risk Management Avanzado
- 🔒 **Biblioteca de 50+ Códigos Base** listos para adaptar

### Lecturas Recomendadas:

- **Chan, E. (2013)** - Algorithmic Trading, Cap. 6
- **Strimpe, J. (2024)** - Python for Algorithmic Trading Cookbook
- Documentación oficial: Alpaca API, pandas-ta

---

## 💬 SOPORTE

**¿Código adaptado no funciona?**

📧 Email: yismaryme@gmail.com  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Code review para participantes]

**Recuerda:** Pega el error completo y el código que da problema.

---

**Versión:** 1.0 (Público)  
**Última actualización:** 20 de noviembre de 2025  
**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa
