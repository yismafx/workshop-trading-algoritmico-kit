# 🐍 SCRIPTS AUXILIARES - Versión Pública

> **Workshop:** Trading Algorítmico Aumentado con IA Generativa  
> **Versión:** 1.0 (Público)  
> **Última actualización:** 20 de noviembre de 2025

---

## 🎯 ¿Qué es esto?

Colección de **scripts Python reutilizables** para tareas comunes en trading algorítmico.

**Filosofía:** No reinventes la rueda. Usa código probado y adáptalo.

---

## 📂 Contenido Disponible (1 Script Público)

### ✅ data_pipeline_simple.py

**¿Para qué?**  
Descargar, limpiar y validar datos históricos de mercado.

**Características:**
- 📥 Descarga datos de acciones/ETFs/criptos (yfinance)
- 🧹 Limpia datos (elimina NaN, duplicados, outliers)
- ✅ Valida calidad de datos
- 💾 Guarda en CSV para reutilización
- 🛡️ Maneja errores comunes

**Compatible con:**
- Acciones/ETFs: SPY, AAPL, MSFT, etc.
- Criptos: BTC-USD, ETH-USD, etc.
- Forex: EURUSD=X, GBPUSD=X, etc.

**Timeframes soportados:**
- Intraday: 1m, 5m, 15m, 30m, 1h
- Daily+: 1d, 1wk, 1mo

**Instalación:**
```bash
pip install yfinance pandas numpy
```

**Uso básico:**
```bash
python data_pipeline_simple.py
```

**Personalización:**
```python
# Editar clase DataConfig en el script
class DataConfig:
    TICKERS = ['AAPL', 'MSFT', 'GOOGL']  # Tus activos
    START_DATE = '2023-01-01'
    END_DATE = '2024-01-01'
    INTERVAL = '1h'  # Cambiar timeframe
```

---

## 🔧 Funciones Principales del Script

### 1. download_data()

Descarga datos usando yfinance.

```python
df = download_data(
    ticker='SPY',
    start_date='2020-01-01',
    end_date='2024-01-01',
    interval='1d'
)
```

**Output:** DataFrame con columnas OHLCV

---

### 2. clean_data()

Limpia datos eliminando problemas comunes.

**Limpieza automática:**
- ✅ Elimina filas duplicadas
- ✅ Forward fill para gaps pequeños (max 2 días)
- ✅ Elimina filas con precio = 0 (datos corruptos)
- ✅ Valida lógica OHLC (High >= Low, etc.)
- ✅ Elimina NaN persistentes

```python
df_clean = clean_data(df, ticker='SPY')
```

---

### 3. validate_data()

Valida calidad de datos y genera reporte.

**Validaciones:**
- ✅ Cantidad mínima de datos (default: 100 registros)
- ✅ Porcentaje de NaN aceptable (default: <5%)
- ✅ Detecta gaps grandes en fechas
- ✅ Identifica volatilidad extrema (>50% cambio/día)

```python
report = validate_data(df_clean, ticker='SPY')
# report['is_valid'] = True/False
```

---

### 4. run_pipeline()

Ejecuta pipeline completo para múltiples tickers.

```python
results = run_pipeline(
    tickers=['SPY', 'QQQ', 'TLT'],
    start_date='2020-01-01',
    end_date='2024-01-01'
)

# Acceder a datos de un ticker
spy_data = results['SPY']['data']
```

---

## 🚀 Casos de Uso

### Caso 1: Descargar Datos para Backtest

```python
# En tu script de backtesting
from data_pipeline_simple import download_data, clean_data

# Descargar y limpiar
df = download_data('SPY', '2015-01-01', '2024-01-01')
df = clean_data(df, 'SPY')

# Usar en backtest
# ... tu código de estrategia aquí ...
```

---

### Caso 2: Actualizar Dataset Diariamente

```python
# Script cron que ejecutas cada día
import schedule
import time
from data_pipeline_simple import run_pipeline
from datetime import datetime, timedelta

def daily_update():
    # Descargar último día
    today = datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    results = run_pipeline(
        tickers=['SPY', 'QQQ'],
        start_date=yesterday,
        end_date=today
    )
    print(f"✅ Actualizado {today}")

# Ejecutar diariamente a las 5 PM
schedule.every().day.at("17:00").do(daily_update)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

### Caso 3: Validar Datos Antes de Backtest

```python
from data_pipeline_simple import validate_data

# Cargar CSV existente
df = pd.read_csv('./data/SPY_20241120.csv')

# Validar calidad
report = validate_data(df, 'SPY', min_points=252)

if not report['is_valid']:
    print("⚠️ Datos no válidos:")
    for error in report['errors']:
        print(f"   - {error}")
    # No ejecutar backtest
else:
    print("✅ Datos validados, proceder con backtest")
    # Ejecutar backtest...
```

---

## 🔒 Scripts Premium (No Incluidos)

En el **workshop completo** recibes:

### 1. data_pipeline_advanced.py

**Features adicionales:**
- 🔄 Caching inteligente (no re-descargar datos)
- ⚡ Multi-threading (descargar 10+ tickers en paralelo)
- 🔀 Integración multi-fuente (yfinance + Alpaca + Polygon)
- 📊 Auto-detección de splits/dividendos
- 💾 Soporte para bases de datos (SQLite, PostgreSQL)
- 🔧 Normalización automática entre fuentes

### 2. backtest_analyzer.py

**Features:**
- 📊 Calcular 20+ métricas automáticamente
- 📈 Generar equity curve, drawdown chart
- 🎯 Comparar con benchmark (SPY, QQQ, etc.)
- 📉 Analizar por régimen de mercado (alcista/bajista)
- 📝 Exportar report PDF automático

### 3. risk_calculator.py

**Features:**
- 💰 Position sizing (Kelly, Fixed Fractional, Volatility-based)
- 🛑 Stop-loss dinámico (ATR-based, % de capital)
- 📊 Diversificación de portfolio (correlaciones)
- ⚠️ Circuit breakers (detener bot si drawdown >X%)
- 💸 Cálculo de slippage esperado

### 4. order_manager.py

**Features:**
- 📤 Enviar órdenes a múltiples brokers (Alpaca, IB)
- 🔄 Retry logic si orden falla
- 📝 Logging detallado de cada operación
- ⚡ Validación pre-orden (fondos, liquidez, horario)
- 📊 Tracking de posiciones abiertas

### 5. webhook_handler.py

**Features:**
- 🔗 Recibir señales de TradingView
- 🚀 Ejecutar órdenes automáticamente
- 🔐 Validación de autenticidad (signatures)
- 📝 Log de señales recibidas
- ⚠️ Rate limiting (evitar spam)

### 6. monitoring_dashboard.py

**Features:**
- 📊 Dashboard web en tiempo real (Flask/Dash)
- 📈 Gráficos de performance live
- 🔔 Alertas configurables (Email, Telegram, SMS)
- 💰 Estado de cuenta en tiempo real
- 📋 Historial de trades

---

## 📖 Cómo Adaptar Los Scripts

### Método 1: Modificar Directamente

```python
# Copiar script
cp data_pipeline_simple.py my_data_pipeline.py

# Editar funciones según necesidad
# - Agregar nuevos validadores
# - Cambiar fuente de datos
# - Personalizar limpieza
```

### Método 2: Importar y Extender

```python
# En tu propio script
from data_pipeline_simple import download_data, clean_data

# Agregar tu propia lógica
def my_custom_clean(df):
    df = clean_data(df, 'SPY')  # Usar función base
    
    # Tu limpieza adicional
    df['custom_indicator'] = ...
    df = df[df['volume'] > 1000000]  # Filtrar volumen bajo
    
    return df
```

### Método 3: Usar con Prompts de GenAI

```python
# Usar Prompt 02 (Adaptar Código Existente)

"""
🎭 ROL: Desarrollador Python senior

📊 CONTEXTO:
Tengo el script data_pipeline_simple.py del workshop.
Funciona con yfinance pero quiero usar Alpaca API.

🎯 TAREA:
Adapta la función download_data() para usar Alpaca API
en lugar de yfinance, manteniendo la misma estructura.
"""

# Pegar en Claude/ChatGPT → Recibir código adaptado
```

---

## 🎓 Mejores Prácticas

### ✅ DO (Haz esto):

1. **Valida datos SIEMPRE antes de backtest**
   ```python
   # Nunca asumas que datos están limpios
   df = download_data(...)
   df = clean_data(...)
   report = validate_data(...)
   
   if report['is_valid']:
       # Proceder con backtest
   ```

2. **Guarda datasets intermedios**
   ```python
   # Evita re-descargar mismo dataset
   df.to_csv(f'./data/{ticker}_{date}.csv')
   ```

3. **Usa try/except para manejar errores**
   ```python
   try:
       df = download_data('INVALID_TICKER', ...)
   except ValueError as e:
       print(f"Error: {e}")
       # Usar datos por defecto o continuar con otro ticker
   ```

4. **Loguea operaciones importantes**
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   
   logging.info(f"Descargados {len(df)} registros de {ticker}")
   ```

### ❌ DON'T (Evita esto):

1. **No asumas que yfinance siempre funciona**
   ```python
   # ❌ MALO: Sin manejo de error
   df = yf.download('SPY')
   df['SMA'] = df['Close'].rolling(20).mean()
   
   # ✅ BUENO: Con validación
   df = yf.download('SPY')
   if df.empty:
       raise ValueError("No se descargaron datos")
   ```

2. **No ignores advertencias del validador**
   ```python
   # Si el script dice "Detectados 5 gaps >10 días"
   # NO lo ignores. Investiga qué pasó esos días.
   ```

3. **No mezcles timeframes sin normalizar**
   ```python
   # ❌ MALO: Mezclar 1d y 1h sin ajustar
   df_daily = download_data('SPY', interval='1d')
   df_hourly = download_data('SPY', interval='1h')
   df_combined = pd.concat([df_daily, df_hourly])  # ¡Índices incompatibles!
   ```

4. **No uses datos sin ajustar por splits**
   ```python
   # yfinance con auto_adjust=True ya lo hace
   # Pero si usas otra fuente, valida que esté ajustado
   ```

---

## 📊 Ejemplo de Flujo Completo

### Semana 1: Setup de Datos

```python
# Día 1: Descargar datos históricos
from data_pipeline_simple import run_pipeline

results = run_pipeline(
    tickers=['SPY', 'QQQ', 'TLT', 'GLD'],
    start_date='2015-01-01',
    end_date='2024-01-01'
)

# Validar que todos descargaron bien
for ticker, result in results.items():
    if result['status'] != 'success':
        print(f"⚠️ {ticker} falló: {result.get('error')}")
```

### Semana 2: Desarrollo de Estrategia

```python
# Día 2-5: Usar datos para backtest
import pandas as pd

# Cargar dataset guardado
spy = pd.read_csv('./data/SPY_20241120.csv', index_col=0, parse_dates=True)

# Implementar estrategia
spy['SMA_20'] = spy['close'].rolling(20).mean()
spy['SMA_50'] = spy['close'].rolling(50).mean()
spy['Signal'] = (spy['SMA_20'] > spy['SMA_50']).astype(int)

# Calcular retornos
spy['Returns'] = spy['close'].pct_change()
spy['Strategy_Returns'] = spy['Returns'] * spy['Signal'].shift(1)

# Métricas
total_return = (1 + spy['Strategy_Returns']).prod() - 1
sharpe = spy['Strategy_Returns'].mean() / spy['Strategy_Returns'].std() * (252**0.5)

print(f"Total Return: {total_return:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")
```

---

## 🔗 Integración con Otros Recursos

### Con Templates:

```
Paso 1: data_pipeline_simple.py → Descargar datos
        ↓
Paso 2: Documentar en Strategy_Memo_Template.md
        Sección: "Datos utilizados" (fuente, periodo, limpieza)
```

### Con Prompts:

```
Paso 1: Ejecutar data_pipeline_simple.py
        ↓
Paso 2: Si hay error → Prompt 04 (Debugging)
        ↓
Paso 3: Adaptar script → Prompt 02 (Adaptar Código)
```

---

## 💬 Soporte

**¿Script no funciona o necesitas ayuda?**

📧 Email: yismaryme@gmail.com (adjunta traceback completo)  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Code reviews + scripts avanzados]

**Errores comunes:**

- "ModuleNotFoundError: No module named 'yfinance'"  
  → Solución: `pip install yfinance`

- "ValueError: No data found for ticker"  
  → Solución: Verifica que ticker existe (ej: 'SPY' no 'spy')

- "KeyError: 'Close'"  
  → Solución: Script normaliza a minúsculas, usa 'close' no 'Close'

---

## 📝 Changelog

### v1.0 (Nov 2025)
- ✅ Script data_pipeline_simple.py incluido
- 🔒 6 scripts adicionales en versión premium

---

## ⚠️ Disclaimer

Estos scripts son herramientas educativas. El uso de scripts NO garantiza:
- Datos 100% precisos (fuentes externas pueden tener errores)
- Ausencia de bugs (testing extensivo recomendado)
- Performance óptimo (código prioriza claridad sobre velocidad)

**Pero SÍ te ayuda a:**
- Automatizar tareas repetitivas
- Evitar errores comunes (validación incorporada)
- Acelerar desarrollo (no partir de cero)
- Aprender mejores prácticas (código comentado)

**Regla de oro:**
> "Testa scripts con capital pequeño antes de usar en producción."

---

**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa  
**Versión:** 1.0 (Público)  
**Licencia:** Uso libre para participantes. No redistribuir sin permiso.
