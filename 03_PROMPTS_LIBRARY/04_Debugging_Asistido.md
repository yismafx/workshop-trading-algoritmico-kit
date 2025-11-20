# 🤖 PROMPT 04: Debugging Asistido (Resolver Errores)

> **Categoría:** Resolución de Problemas  
> **Nivel:** Básico-Intermedio  
> **Sesión del Workshop:** S4, S5 (Implementación y Backtesting)  
> **Compatible con:** Claude, ChatGPT, Gemini

---

## 🎯 PROPÓSITO

Resolver errores de código de trading algorítmico de forma sistemática con ayuda de IA:
- Errores de sintaxis (SyntaxError, IndentationError)
- Errores de runtime (ValueError, KeyError, TypeError)
- Errores lógicos (código corre pero resultados incorrectos)
- Errores de datos (NaN, valores infinitos, fechas faltantes)

**⚠️ Importante:** El debugging es una habilidad crítica. Usa IA para aprender el proceso, no solo para "arreglar mágicamente".

---

## 📋 ESTRUCTURA DEL PROMPT

### Template Básico

```markdown
🎭 ROL:
Actúa como un debugger experto en Python para trading algorítmico.
Tu enfoque es PEDAGÓGICO: No solo arregles el error, enséñame POR QUÉ ocurrió 
y CÓMO evitarlo en el futuro.

📊 CONTEXTO:
Estoy implementando [DESCRIPCIÓN BREVE: ej. "backtest de estrategia mean reversion"]
usando [LIBRERÍAS: pandas, numpy, yfinance, etc.].

El código FUNCIONABA antes, pero después de [CAMBIO RECIENTE: ej. "agregar stop-loss"]
empezó a dar error.

Código que genera el error:
```python
[PEGAR CÓDIGO AQUÍ - máximo 50 líneas, enfócate en la parte problemática]
```

Error completo:
```
[PEGAR TRACEBACK COMPLETO - desde primera línea hasta última]
```

🎯 TAREA:
Ayúdame a debuggear siguiendo estos pasos:

1. **Diagnóstico:** ¿Cuál es la causa raíz del error? (no solo el síntoma)
2. **Solución:** Código corregido con comentarios en líneas cambiadas
3. **Explicación:** ¿Por qué mi código original falló?
4. **Prevención:** ¿Cómo evitar este error en el futuro?
5. **Test case:** Dame un mini-test para validar que la corrección funciona

📤 FORMATO:
Estructura tu respuesta en las 5 secciones claramente separadas.

⛔ RESTRICCIONES:
- NO me des solo la línea corregida. Quiero entender el contexto.
- NO asumas que sé qué significa el error técnico (explícalo)
- Si hay múltiples formas de arreglar, muestra la MÁS SIMPLE primero
- Si detectas otros bugs potenciales, señálalos
```

---

## 🔥 EJEMPLO DE USO REAL

### Input (Tu prompt al AI):

```markdown
🎭 ROL:
Actúa como un debugger experto en Python para trading algorítmico.
Enfoque pedagógico: enséñame POR QUÉ falló y CÓMO evitarlo.

📊 CONTEXTO:
Estoy implementando backtest de estrategia SMA crossover usando pandas y yfinance.
El código funcionaba hasta que agregué cálculo de Sharpe Ratio.

Código que genera error:
```python
import pandas as pd
import yfinance as yf

# Descargar datos
df = yf.download('SPY', start='2020-01-01', end='2024-01-01')

# Indicadores
df['SMA_20'] = df['Close'].rolling(20).mean()
df['SMA_50'] = df['Close'].rolling(50).mean()

# Señales
df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1

# Retornos
df['Returns'] = df['Close'].pct_change()
df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)

# AQUÍ EMPIEZA EL PROBLEMA
sharpe = df['Strategy_Returns'].mean() / df['Strategy_Returns'].std()
print(f"Sharpe Ratio: {sharpe:.2f}")
```

Error completo:
```
RuntimeWarning: invalid value encountered in scalar divide
  sharpe = df['Strategy_Returns'].mean() / df['Strategy_Returns'].std()
Sharpe Ratio: nan
```

🎯 TAREA:
[Estructura completa del template...]
```

### Output Esperado (Lo que el AI responderá):

```markdown
# ═══════════════════════════════════════════════════════════════
# 1. DIAGNÓSTICO
# ═══════════════════════════════════════════════════════════════

**Causa raíz:** División por cero (o casi cero) cuando std() = 0

**¿Por qué std() = 0?**
- Primeras 50 filas: NaN (rolling windows aún no completos)
- Siguiente: Signal = 0 (ambas SMAs no han cruzado aún)
- Strategy_Returns = 0 * algo = 0 para muchas filas iniciales

Cuando todos los valores son 0 (o muy similares), std() ≈ 0 → división por ~0 = NaN

**Warning "invalid value":** Python te avisa que estás dividiendo por algo inválido

# ═══════════════════════════════════════════════════════════════
# 2. SOLUCIÓN
# ═══════════════════════════════════════════════════════════════

```python
import pandas as pd
import yfinance as yf
import numpy as np  # AGREGAR: Para manejo de NaN

# Descargar datos
df = yf.download('SPY', start='2020-01-01', end='2024-01-01')

# Indicadores
df['SMA_20'] = df['Close'].rolling(20).mean()
df['SMA_50'] = df['Close'].rolling(50).mean()

# Señales
df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1

# Retornos
df['Returns'] = df['Close'].pct_change()
df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)

# CORRECCIÓN: Filtrar NaN y validar datos antes de calcular
# CAMBIO 1: Eliminar filas con NaN
valid_returns = df['Strategy_Returns'].dropna()

# CAMBIO 2: Validar que hay variabilidad
if valid_returns.std() == 0:
    print("⚠️ Sharpe Ratio: No calculable (sin variabilidad en retornos)")
    sharpe = np.nan
else:
    # CAMBIO 3: Calcular solo con datos válidos
    sharpe = valid_returns.mean() / valid_returns.std()
    
    # OPCIONAL: Anualizar (asumiendo datos diarios)
    sharpe_annual = sharpe * np.sqrt(252)
    
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Sharpe Ratio (anualizado): {sharpe_annual:.2f}")
```

# ═══════════════════════════════════════════════════════════════
# 3. EXPLICACIÓN
# ═══════════════════════════════════════════════════════════════

**¿Por qué tu código original falló?**

1. **NaN en rolling windows:**
   - Primeras 50 filas tienen SMA_50 = NaN (no hay 50 datos previos)
   - Strategy_Returns hereda esos NaN

2. **Signal = 0 al inicio:**
   - Hasta que SMA_20 cruce SMA_50 (puede tardar días/semanas)
   - Signal = 0 → Strategy_Returns = 0
   - Si TODOS los primeros N retornos son 0, std() = 0

3. **División por cero:**
   ```python
   mean / 0 = inf  # Si mean > 0
   0 / 0 = nan     # Si mean = 0 también
   ```

**Analogía:**
Es como intentar calcular "volatilidad" de una serie de precios donde 
todos los días el precio es exactamente $100. ¡No hay volatilidad!

# ═══════════════════════════════════════════════════════════════
# 4. PREVENCIÓN
# ═══════════════════════════════════════════════════════════════

**Checklist para evitar este error en futuro:**

✅ **Siempre dropna() antes de calcular estadísticas:**
```python
# Buena práctica
clean_data = df['Column'].dropna()
result = clean_data.mean() / clean_data.std()
```

✅ **Validar divisores antes de dividir:**
```python
if denominator != 0:
    result = numerator / denominator
else:
    result = np.nan  # O manejar según lógica
```

✅ **Usar funciones seguras:**
```python
# En lugar de:
sharpe = mean / std

# Usar:
sharpe = np.divide(mean, std, out=np.nan, where=std!=0)
```

✅ **Inspeccionar datos intermedios:**
```python
print(f"NaN en Strategy_Returns: {df['Strategy_Returns'].isna().sum()}")
print(f"Zeros en Strategy_Returns: {(df['Strategy_Returns']==0).sum()}")
print(f"Std de Strategy_Returns: {df['Strategy_Returns'].std()}")
```

# ═══════════════════════════════════════════════════════════════
# 5. TEST CASE
# ═══════════════════════════════════════════════════════════════

```python
# Test para validar corrección
def test_sharpe_calculation():
    """Valida que Sharpe no da NaN con datos reales"""
    
    # Simular datos de prueba
    test_returns = pd.Series([0.01, -0.005, 0.02, 0.015, -0.01])
    
    # Calcular como en código corregido
    if test_returns.std() == 0:
        sharpe = np.nan
    else:
        sharpe = test_returns.mean() / test_returns.std()
    
    # Validaciones
    assert not np.isnan(sharpe), "Sharpe no debe ser NaN con datos válidos"
    assert sharpe != np.inf, "Sharpe no debe ser infinito"
    assert -5 < sharpe < 5, "Sharpe debe estar en rango razonable"
    
    print(f"✅ Test passed. Sharpe = {sharpe:.2f}")

# Ejecutar test
test_sharpe_calculation()

# Test con tus datos reales
test_returns_real = df['Strategy_Returns'].dropna()
if len(test_returns_real) > 0:
    print(f"✅ Datos reales: {len(test_returns_real)} retornos válidos")
    print(f"   Mean: {test_returns_real.mean():.6f}")
    print(f"   Std: {test_returns_real.std():.6f}")
else:
    print("❌ No hay retornos válidos para calcular Sharpe")
```

# ═══════════════════════════════════════════════════════════════
# BONUS: OTROS BUGS DETECTADOS
# ═══════════════════════════════════════════════════════════════

⚠️ **Bug potencial 1:** Sharpe no está anualizado
- Tu Sharpe actual es "por día"
- Sharpe Ratio estándar es anualizado
- Multiplicar por sqrt(252) para datos diarios

⚠️ **Bug potencial 2:** No restas risk-free rate
- Fórmula completa: (Return - RiskFreeRate) / Std
- Asumir RiskFreeRate ≈ 0 es común pero no preciso

⚠️ **Mejora sugerida:** Agregar manejo de edge cases
```python
# Validar suficientes datos
if len(valid_returns) < 30:
    print("⚠️ Muy pocos datos para Sharpe confiable (min 30 trades)")
```
```

---

## 💡 VARIACIONES DEL PROMPT

### Variación A: Error Sin Traceback (Lógico)

```markdown
📊 CONTEXTO:
Mi código NO da error de Python, pero los resultados están mal.
Esperaba Sharpe de ~1.2, pero obtengo 8.5 (sospechoso).

🎯 TAREA:
1. Identifica qué puede estar causando resultados inflados
2. Busca lookahead bias, data leakage, o bugs lógicos
3. Sugiere validaciones para detectar estos problemas

[Resto igual...]
```

### Variación B: Error de Instalación/Importación

```markdown
Error completo:
```
ModuleNotFoundError: No module named 'pandas_ta'
```

🎯 TAREA:
1. ¿Por qué no encuentra el módulo?
2. Comando exacto para instalarlo (con versión específica si aplica)
3. ¿Hay alternativas si la instalación falla?
4. ¿Este módulo es necesario o puedo usar otro?

[Resto igual...]
```

### Variación C: Error en Producción (Live Trading)

```markdown
📊 CONTEXTO:
El código funciona perfecto en backtest, pero en live trading (paper) 
a veces da error "Order rejected: Insufficient funds"

Código:
[... código de order placement ...]

🎯 TAREA:
1. ¿Qué diferencias hay entre backtest y live que causan esto?
2. ¿Cómo validar fondos ANTES de enviar orden?
3. ¿Cómo manejar este error gracefully sin detener el bot?

[Resto igual...]
```

---

## ✅ CHECKLIST POST-FIX

Después de aplicar la corrección del AI:

- [ ] ¿El error desapareció completamente?
- [ ] ¿Entiendes POR QUÉ estaba fallando?
- [ ] ¿Ejecutaste el test case provisto?
- [ ] ¿Agregaste print statements para debuggear futuro?
- [ ] ¿Documentaste este bug (para no repetirlo)?
- [ ] ¿El AI detectó otros bugs potenciales?

**Si 5+ checks = ✅:** Bug resuelto, código mejorado  
**Si <5 checks = ✅:** Revisa nuevamente o pide aclaración

---

## 🎓 TIPS DE EXPERTO

### 1. Pega El Traceback COMPLETO

❌ **Malo:**
```
Error: KeyError
```

✅ **Bueno:**
```
Traceback (most recent call last):
  File "backtest.py", line 45, in <module>
    df['SMA'] = df['Close'].rolling(20).mean()
KeyError: 'Close'
```

### 2. Describe Qué Cambió Recientemente

El AI puede debuggear mejor si sabe:
- "Esto funcionaba hasta que agregué X"
- "Solo falla con ticker Y pero no con Z"
- "Solo falla los primeros días del mes"

### 3. Incluye Datos de Muestra

```python
# Agrega esto a tu prompt
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
```

### 4. Pregunta "¿Y Si...?"

Follow-ups útiles después del fix:
```markdown
"¿Este fix funciona si los datos tienen gaps (fines de semana)?"
"¿Qué pasa si el DataFrame está vacío?"
"¿Hay algún edge case que no estamos considerando?"
```

### 5. Aprende El Patrón

Después de resolver 3-5 errores similares:
```markdown
"He resuelto 3 KeyErrors. ¿Hay un patrón común? 
¿Cómo puedo prevenir todos los KeyErrors de una vez?"
```

---

## 🚨 ERRORES COMUNES EN TRADING ALGORÍTMICO

### Error 1: KeyError (Columna No Existe)

```python
# ❌ Falla
df['Close']  # yfinance usa 'Close', Alpaca usa 'close'

# ✅ Solución
df.columns = df.columns.str.lower()  # Normalizar a minúsculas
```

### Error 2: SettingWithCopyWarning

```python
# ⚠️ Warning molesto
subset = df[df['Signal'] == 1]
subset['New_Col'] = 123  # Puede o no modificar df original

# ✅ Solución
subset = df[df['Signal'] == 1].copy()
```

### Error 3: Lookahead Bias (Sin Error de Python)

```python
# ❌ Bug silencioso
df['Signal'] = np.where(df['Close'] > df['High'].shift(-1), 1, 0)
                                              # ↑ FUTURO!

# ✅ Corrección
df['Signal'] = np.where(df['Close'] > df['High'].shift(1), 1, 0)
```

### Error 4: División por Cero

```python
# ❌ Falla
position_size = capital / price  # ¿Y si price = 0?

# ✅ Solución
position_size = capital / max(price, 0.01)  # Mínimo seguro
```

---

## 🔗 PRÓXIMOS PASOS

**Después de resolver el error:**

1. **Documenta:** Agrega comentario explicando el fix
2. **Test:** Crea test case para prevenir regresión
3. **Refactor:** ¿Hay código similar que también necesita fix?
4. **Log:** Agrega logging para detectar futuro problema temprano

```python
# Ejemplo de logging preventivo
import logging
logging.basicConfig(level=logging.INFO)

if df['Strategy_Returns'].std() < 0.0001:
    logging.warning("Std muy bajo, Sharpe puede ser inestable")
```

---

## 📚 RECURSOS ADICIONALES

### En el Workshop Premium:

- 🔒 **Prompt 04B:** Debugging de Estrategias Multi-Activo
- 🔒 **Prompt 04C:** Optimizar Performance (código lento)
- 🔒 **Prompt 04D:** Debugging en Producción (live trading)
- 🔒 **Base de Datos de 100+ Errores Comunes** con soluciones

### Herramientas de Debugging:

- **Python Debugger (pdb):** Debugging interactivo
- **Jupyter %debug magic:** Post-mortem debugging
- **logging:** Mejor que print() para producción
- **pytest:** Testing automatizado

---

## 💬 SOPORTE

**¿Error muy raro que el AI no puede resolver?**

📧 Email: yismaryme@gmail.com  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Debugging sessions en vivo]

**Formato ideal de consulta:**
1. Descripción breve del problema
2. Código mínimo que reproduce el error
3. Traceback completo
4. Qué has intentado ya

---

**Versión:** 1.0 (Público)  
**Última actualización:** 20 de noviembre de 2025  
**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa
