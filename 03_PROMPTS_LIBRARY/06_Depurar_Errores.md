# 🐛 PROMPT 06: Depurar Errores de Trading Code

> **Categoría:** Debugging  
> **Sesión del Workshop:** Todas (herramienta transversal)  
> **Dificultad:** ⭐⭐ (Básico-Intermedio)  
> **Plataformas:** Claude, ChatGPT (Claude recomendado para debugging)

---

## 🎯 Propósito del Prompt

Resolver errores (bugs) en tu código de trading cuando:
- ❌ El código no ejecuta (errores de sintaxis, imports, etc.)
- ❌ El código ejecuta pero da resultados incorrectos (lógica errónea)
- ❌ El código es lento o ineficiente
- ❌ Hay warnings que no entiendes

**Objetivo:** Pasar de "no funciona" a "funciona correctamente" de manera sistemática

---

## 📋 Template del Prompt

```markdown
CONTEXTO:
Estoy implementando [descripción breve de tu estrategia] en Python y  
tengo un error que no puedo resolver. [Describe qué esperabas vs qué obtienes]

ROL:
Actúa como un Senior Python Developer especializado en debugging de código  
financiero. Eres metódico, explicas el error, la causa raíz, y das solución  
paso a paso.

CÓDIGO CON ERROR:
```python
[Pega aquí el código completo que genera el error]
```

MENSAJE DE ERROR (si aplica):
```
[Pega aquí el traceback completo del error]
```

COMPORTAMIENTO ESPERADO vs ACTUAL:
- **Esperado:** [Ej: "Debería generar 50 señales de compra"]
- **Actual:** [Ej: "Genera 0 señales"]
- **Datos de entrada:** [Ej: "DataFrame con 1000 filas de SPY 2020-2024"]

TAREA:
1. **DIAGNOSTICA** el error:
   - ¿Qué línea específica causa el problema?
   - ¿Por qué está fallando?
   - ¿Cuál es la causa raíz?

2. **SOLUCIONA** el error:
   - Código corregido completo
   - Explicación de CADA cambio realizado
   - Por qué el cambio soluciona el problema

3. **PREVENCIÓN:**
   - Cómo evitar este error en el futuro
   - Validaciones que deberías agregar

FORMATO:
Usa secciones claras:
- 🔴 DIAGNÓSTICO
- ✅ SOLUCIÓN (código corregido)
- 📝 EXPLICACIÓN DE CAMBIOS
- 🛡️ PREVENCIÓN FUTURA

RESTRICCIONES:
- NO des soluciones genéricas ("revisa los datos")
- SÍ identifica la línea exacta del problema
- NO cambies más código del necesario
- SÍ explica POR QUÉ funcionaba mal y POR QUÉ la solución funciona
```

---

## 💡 Ejemplo de Uso Real

### Código Buggy:

```python
import pandas as pd
import yfinance as yf

ticker = 'SPY'
data = yf.download(ticker, start='2020-01-01', end='2024-01-01')

# Calcular SMA
data['SMA20'] = data['Close'].rolling(20).mean()

# Generar señales
data['Signal'] = 0
data['Signal'][data['Close'] > data['SMA20']] = 1

print(f"Señales generadas: {data['Signal'].sum()}")
```

### Error Recibido:

```
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame
```

### Tu Prompt:

```markdown
CONTEXTO:
Estoy implementando una estrategia simple de cruce de SMA. 
Recibo un SettingWithCopyWarning y no entiendo qué está mal.

[Incluir template completo + código + error]

COMPORTAMIENTO ESPERADO vs ACTUAL:
- **Esperado:** Señales de compra donde Close > SMA20
- **Actual:** El código funciona pero genera warning molesto
```

### Output Esperado de la IA:

```markdown
## 🔴 DIAGNÓSTICO

### Error Identificado:
```python
data['Signal'][data['Close'] > data['SMA20']] = 1  # ❌ Línea problemática
```

### ¿Qué está pasando?
Estás usando **chained indexing**, que pandas desaconseja porque:
1. Primero seleccionas `data['Signal']` (crea una vista o copia, ambiguo)
2. Luego intentas modificar con `[data['Close'] > data['SMA20']]`
3. Pandas no sabe si modificar el original o la copia → Warning

### ¿Por qué es problemático?
Aunque el código "funciona", puede:
- No modificar el DataFrame original (bug silencioso)
- Comportamiento inconsistente entre versiones de pandas
- Ser más lento que la forma correcta

---

## ✅ SOLUCIÓN

### Código Corregido:

```python
import pandas as pd
import yfinance as yf

ticker = 'SPY'
data = yf.download(ticker, start='2020-01-01', end='2024-01-01')

# Calcular SMA
data['SMA20'] = data['Close'].rolling(20).mean()

# Generar señales (MÉTODO CORRECTO)
data['Signal'] = 0
data.loc[data['Close'] > data['SMA20'], 'Signal'] = 1  # ✅ Usa .loc[]

print(f"Señales generadas: {data['Signal'].sum()}")
```

---

## 📝 EXPLICACIÓN DE CAMBIOS

### Cambio realizado:
```python
# ANTES (incorrecto):
data['Signal'][condición] = valor

# DESPUÉS (correcto):
data.loc[condición, 'Signal'] = valor
```

### ¿Por qué funciona?
`.loc[row_indexer, column_indexer]` es el método **oficial de pandas** para:
- Seleccionar filas (con boolean mask)
- Seleccionar columnas (por nombre)
- Asignar valores

Es explícito y no ambiguo → pandas sabe exactamente qué modificar.

### Equivalencias comunes:
```python
# ❌ MALO (chained indexing):
df['col'][df['col'] > 5] = 0
df['col'][0:10] = 0

# ✅ BUENO (usando .loc):
df.loc[df['col'] > 5, 'col'] = 0
df.loc[0:10, 'col'] = 0

# ✅ ALTERNATIVA (usando .loc con slice):
df.loc[:, 'col'] = df['col'].where(df['col'] <= 5, 0)
```

---

## 🛡️ PREVENCIÓN FUTURA

### Regla de oro:
> **Siempre usa `.loc[]` o `.iloc[]` cuando asignes valores con condiciones**

### Checklist para evitar este error:
- [ ] ¿Estoy haciendo `df['col'][condición] = valor`? → Cambiar a `.loc`
- [ ] ¿Tengo warnings en mi código? → Resolverlos (no ignorarlos)
- [ ] ¿Uso `pd.options.mode.chained_assignment = None`? → NO HACER (oculta problemas)

### Configuración recomendada:
```python
import pandas as pd

# Hacer que warnings sean errors (debugging mode)
pd.options.mode.chained_assignment = 'raise'  # Detiene ejecución

# O solo logging (producción)
pd.options.mode.chained_assignment = 'warn'  # Default
```

### Testing:
```python
# Después de cada modificación, valida:
assert data['Signal'].sum() > 0, "No se generaron señales!"
assert data['Signal'].isin([0, 1]).all(), "Señales fuera de rango!"
```

---

## 📊 VALIDACIÓN DE LA SOLUCIÓN

```python
# Agrega al final de tu código para validar:

print("\\n=== VALIDACIÓN ===")
print(f"Total filas: {len(data)}")
print(f"Señales de compra (1): {(data['Signal'] == 1).sum()}")
print(f"Señales neutrales (0): {(data['Signal'] == 0).sum()}")
print(f"Primer señal en fila: {data[data['Signal'] == 1].index[0] if (data['Signal'] == 1).any() else 'N/A'}")

# Verificar lógica
sample = data[['Close', 'SMA20', 'Signal']].dropna().head(30)
print("\\n=== SAMPLE (primeras 30 filas con datos válidos) ===")
print(sample)
```

**Output esperado:**
```
=== VALIDACIÓN ===
Total filas: 1006
Señales de compra (1): 503
Señales neutrales (0): 503
Primer señal en fila: 2020-01-30

=== SAMPLE ===
            Close     SMA20  Signal
2020-01-30  324.87  320.45       1
2020-01-31  321.45  320.68       1
[...]
```
```

---

## 🔧 Variaciones del Prompt

### Variación A: Error de Lógica (Sin Traceback)
```markdown
CÓDIGO CON ERROR:
[Tu código]

NO HAY MENSAJE DE ERROR, pero:
- **Problema:** El código genera 0 señales cuando debería generar ~50
- **Sospecha:** La condición de entrada nunca se cumple

TAREA:
Debuggea la lógica. Imprime valores intermedios para encontrar dónde falla.
```

### Variación B: Error de Performance
```markdown
PROBLEMA:
El código tarda 5 minutos en ejecutar con 10 años de datos.

TAREA:
1. Identifica operaciones lentas (profile el código)
2. Sugiere optimizaciones vectorizadas
3. Estima mejora de velocidad
```

### Variación C: Error de Datos
```markdown
ERROR AL EJECUTAR:
"KeyError: 'Close'"

CONTEXTO:
Funciona con datos de yfinance pero falla con datos de Alpaca.

TAREA:
Identifica diferencias en estructura de datos entre ambas fuentes.
Haz el código compatible con ambas.
```

---

## 🎓 Errores Comunes en Trading Code

### 1. Look-Ahead Bias (El Más Peligroso)

```python
# ❌ MALO: Usa datos del futuro
data['Signal'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
#                                      ^ Futuro!

# ✅ BUENO: Solo usa datos pasados
data['Signal'] = np.where(data['Close'] > data['Close'].shift(1), 1, 0)
#                                                      ^ Pasado
```

**Impacto:** Backtest perfecto, live trading desastroso

---

### 2. Forward-Filling de Datos (Silencioso)

```python
# Datos con NaN
data = pd.DataFrame({'Close': [100, np.nan, 102, np.nan, 105]})

# ❌ Malo (ffill oculta problemas):
data['Close'].fillna(method='ffill', inplace=True)
# [100, 100, 102, 102, 105] → Señales en días sin trading!

# ✅ Bueno (dropna o validar):
data = data.dropna()
# O: assert not data['Close'].isna().any()
```

---

### 3. Tipo de Datos Incorrecto

```python
# ❌ Fechas como string
data['Date'] = '2024-01-15'  # String, no datetime

# Falla al usar:
data[data['Date'] > '2024-01-01']  # Comparación de strings (malo)

# ✅ Convertir a datetime:
data['Date'] = pd.to_datetime(data['Date'])
data[data['Date'] > pd.to_datetime('2024-01-01')]  # Comparación correcta
```

---

### 4. División por Cero en Indicadores

```python
# ❌ Crash si volatilidad = 0
sharpe = returns.mean() / returns.std()  # std() puede ser 0

# ✅ Validar:
std = returns.std()
sharpe = returns.mean() / std if std > 0 else 0
```

---

## ⚠️ Cuando la IA NO Puede Ayudar

### Casos difíciles:
1. **Errores de datos externos:** Si la API de tu broker cambió estructura
2. **Race conditions:** Si usas multithreading
3. **Errores de estado:** Si tu estrategia guarda estado entre ejecuciones

### Solución alternativa:
```markdown
Usa "PROMPT 05: Explicar Código" primero
→ Entiende cada línea del código
→ Agrega print() para debuggear manualmente
→ Luego vuelve a este prompt con info específica
```

---

## 📚 Recursos para Debugging

### Herramientas:
- **pdb:** Python debugger (breakpoints)
- **jupyter %debug:** Magic command para post-mortem debugging
- **logging:** Mejor que print() para producción

### Lecturas:
- **Effective Python (Slatkin):** Items sobre debugging
- **Python Cookbook:** Sección de testing y debugging

---

## ✅ Checklist de Debugging Sistemático

Antes de usar el prompt, intenta:
- [ ] Leer el error completo (no solo última línea)
- [ ] Agregar print() en línea sospechosa
- [ ] Validar tipo de datos (`.dtypes`, `.head()`)
- [ ] Revisar documentación de la función que falla
- [ ] Google el error exacto (a veces es bug conocido)

Si nada funciona → Usa este prompt

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Autor:** Workshop Trading Algorítmico Aumentado con IA Generativa
