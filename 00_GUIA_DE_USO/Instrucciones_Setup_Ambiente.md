# 🛠️ INSTRUCCIONES DE SETUP DEL AMBIENTE

**Workshop: Trading Algorítmico Aumentado con IA Generativa**  
**Versión:** 1.0 (Noviembre 2025)  
**Tiempo estimado:** 30 min (Rápido) a 3h (Avanzado)

---

## 📑 Tabla de Contenidos

- [⚡ Quick Start - Elige Tu Camino](#-quick-start---elige-tu-camino)
- [🚀 OPCIÓN A: Setup Rápido (Google Colab)](#-opción-a-setup-rápido-google-colab---30-45-min)
- [💻 OPCIÓN B: Setup Avanzado (Python Local)](#-opción-b-setup-avanzado-python-local---2-3h)
- [📊 OPCIÓN C: MetaTrader 5 Setup](#-opción-c-metatrader-5-setup---1-2h)
- [🏦 OPCIÓN D: Interactive Brokers Setup](#-opción-d-interactive-brokers-setup---2-3h)
- [📦 Librerías y Dependencias](#-librerías-y-dependencias-actualizadas-2025)
- [🚨 Troubleshooting](#-troubleshooting)
- [✅ Validación Final](#-validación-final)
- [📞 Soporte](#-soporte)

---

## ⚡ Quick Start - Elige Tu Camino

**¿Qué setup es mejor para ti?** Usa este diagrama de decisión:

```
                    ┌─────────────────────────────────────┐
                    │ ¿Tienes experiencia con Python?     │
                    └─────────────────────────────────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                      ❌ NO                 ✅ SÍ
                         │                     │
                         ↓                     ↓
              ┌──────────────────┐   ┌──────────────────┐
              │ Setup RÁPIDO     │   │ ¿Vas a deployar  │
              │ (Google Colab)   │   │ bots 24/7?       │
              │ → 30 min         │   └──────────────────┘
              └──────────────────┘            │
                                    ┌─────────┴─────────┐
                                    │                   │
                                 ❌ NO                ✅ SÍ
                                    │                   │
                                    ↓                   ↓
                         ┌──────────────────┐  ┌──────────────────┐
                         │ Setup RÁPIDO     │  │ Setup AVANZADO   │
                         │ (Google Colab)   │  │ (Python Local)   │
                         │ → 30 min         │  │ → 2-3h           │
                         └──────────────────┘  └──────────────────┘
```

### 📋 Tabla Comparativa

| Característica | 🚀 Rápido (Colab) | 💻 Avanzado (Local) | 📊 MetaTrader 5 | 🏦 Interactive Brokers |
|----------------|-------------------|---------------------|-----------------|----------------------|
| **Tiempo setup** | 30 min | 2-3h | 1-2h | 2-3h |
| **Experiencia Python** | No necesaria | Intermedia | Básica | Avanzada |
| **Deployment 24/7** | ❌ No | ✅ Sí (con VPS) | ✅ Sí | ✅ Sí |
| **Costo** | Gratis | Gratis | Gratis | Gratis (paper) |
| **Mercados** | Multi-asset | Multi-asset | Forex/CFDs | Multi-asset global |
| **Dificultad** | ⭐ Fácil | ⭐⭐⭐ Media | ⭐⭐ Media-fácil | ⭐⭐⭐⭐ Alta |
| **Recomendado para** | Principiantes | Desarrollo serio | Traders Forex | Traders profesionales |

---

## 🚀 OPCIÓN A: Setup Rápido (Google Colab) - 30-45 min

**✅ Ideal para:** 80% de los participantes - No requiere instalar nada localmente

### 📋 Paso 1: Cuenta Google (2 min)

**¿Ya tienes cuenta Gmail?**  
✅ Sí → Pasa al Paso 2  
❌ No → Crear cuenta en [google.com/gmail](https://google.com/gmail)

**Validación:**
- [ ] Puedo acceder a [colab.research.google.com](https://colab.research.google.com)
- [ ] Puedo crear un nuevo notebook

---

### 📋 Paso 2: Cuenta Alpaca Paper Trading (5 min)

Alpaca es el broker que usaremos para paper trading (gratis, sin riesgo).

**Pasos:**

1. **Ir a:** [alpaca.markets](https://alpaca.markets)

2. **Registrarse:**
   - Click en "Sign Up"
   - Completar formulario
   - Verificar email

3. **Generar API Keys:**
   - Ir a Dashboard → API Keys
   - Click en "Generate New Keys"
   - **IMPORTANTE:** Seleccionar **"Paper Trading"** (no "Live Trading")
   - Copiar y guardar:
     - `API_KEY` (comienza con "PK...")
     - `SECRET_KEY` (string largo)

**⚠️ CRÍTICO:** Guarda las keys en un lugar seguro. Las necesitarás en el Paso 4.

**Validación:**
- [ ] Tengo API_KEY copiada
- [ ] Tengo SECRET_KEY copiada
- [ ] Las keys son de **Paper Trading** (no Live)

---

### 📋 Paso 3: Abrir Colab Notebook Maestro (2 min)

**Pasos:**

1. **Acceder al notebook:**
   - Si eres participante pago, descarga `Colab_Notebook_Maestro.ipynb` del repositorio premium
   - Sube el archivo a tu Google Drive

2. **Abrir en Colab:**
   - Click derecho en el archivo `.ipynb` en Drive
   - "Abrir con" → "Google Colaboratory"

**Alternativa (si no tienes el notebook aún):**
Crear uno nuevo en [colab.research.google.com](https://colab.research.google.com)

**Validación:**
- [ ] Notebook abierto en Colab
- [ ] Puedo ejecutar celdas (Shift + Enter)

---

### 📋 Paso 4: Configurar API Keys (5 min)

**En la primera celda del notebook, ejecuta:**

```python
# === CONFIGURACIÓN DE AMBIENTE ===
import os
from getpass import getpass

# Solicitar API keys de forma segura (no se guardan en el notebook)
ALPACA_API_KEY = getpass("Ingresa tu Alpaca API Key: ")
ALPACA_API_SECRET = getpass("Ingresa tu Alpaca API Secret: ")

# Configurar como variables de entorno
os.environ['ALPACA_API_KEY'] = ALPACA_API_KEY
os.environ['ALPACA_API_SECRET'] = ALPACA_API_SECRET
os.environ['ALPACA_PAPER'] = 'true'

print("✅ API Keys configuradas correctamente")
```

**Ejecuta la celda (Shift + Enter)** y pega tus keys cuando te las pida.

**⚠️ Seguridad:** Nunca pegues las keys directamente en el código. Usa `getpass()`.

---

### 📋 Paso 5: Instalar Librerías (10 min)

**Ejecuta esta celda para instalar todas las dependencias:**

```python
# === INSTALACIÓN DE LIBRERÍAS (2024-2025 Updated) ===

# Core
!pip install --upgrade pip

# Manejo de datos
!pip install pandas==2.2.0 numpy==1.26.3

# Obtención de datos
!pip install yfinance==0.2.36 alpaca-py==0.25.0

# Backtesting
!pip install vectorbt==0.26.1 backtrader==1.9.78.123

# Análisis técnico
!pip install ta==0.11.0 pandas-ta==0.3.14b

# Visualización
!pip install matplotlib==3.8.2 seaborn==0.13.1 plotly==5.18.0

# Machine Learning (opcional)
!pip install scikit-learn==1.4.0

# Utilities
!pip install python-dotenv==1.0.0 requests==2.31.0

print("✅ Todas las librerías instaladas correctamente")
```

**Tiempo de ejecución:** ~5-8 minutos (Colab descarga e instala todo)

**Validación:**
- [ ] La celda ejecutó sin errores
- [ ] Veo "✅ Todas las librerías instaladas correctamente"

---

### 📋 Paso 6: Validación de Setup (5 min)

**Ejecuta esta celda para validar que todo funciona:**

```python
# === CELDA DE VALIDACIÓN COMPLETA ===

import sys
print("🔍 Validando setup...\n")

# 1. Verificar Python
python_version = sys.version.split()[0]
print(f"✅ Python {python_version}")

# 2. Verificar librerías core
try:
    import pandas as pd
    import numpy as np
    import yfinance as yf
    import vectorbt as vbt
    from alpaca.trading.client import TradingClient
    import ta
    import matplotlib.pyplot as plt
    print("✅ Todas las librerías importadas correctamente")
except ImportError as e:
    print(f"❌ Error importando librerías: {e}")
    sys.exit(1)

# 3. Verificar conexión con Alpaca
try:
    client = TradingClient(
        api_key=os.environ['ALPACA_API_KEY'],
        secret_key=os.environ['ALPACA_API_SECRET'],
        paper=True
    )
    account = client.get_account()
    print(f"✅ Conexión con Alpaca exitosa")
    print(f"   Balance: ${float(account.cash):,.2f} (paper)")
except Exception as e:
    print(f"❌ Error conectando con Alpaca: {e}")
    print("   Verifica tus API keys en el Paso 4")
    sys.exit(1)

# 4. Verificar descarga de datos
try:
    data = yf.download('SPY', period='5d', progress=False)
    print(f"✅ Descarga de datos funcionando")
    print(f"   Datos obtenidos: {len(data)} días")
except Exception as e:
    print(f"❌ Error descargando datos: {e}")
    sys.exit(1)

# 5. Test de indicadores técnicos
try:
    data['SMA_20'] = ta.trend.sma_indicator(data['Close'], window=20)
    data['RSI_14'] = ta.momentum.rsi(data['Close'], window=14)
    print("✅ Cálculo de indicadores técnicos funcionando")
except Exception as e:
    print(f"❌ Error calculando indicadores: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("🎉 ¡SETUP COMPLETADO EXITOSAMENTE!")
print("="*50)
print("\nEstás listo para empezar la Sesión 1.")
print("Guarda este notebook en tu Google Drive.")
```

**Resultado esperado:**

```
✅ Python 3.10.12
✅ Todas las librerías importadas correctamente
✅ Conexión con Alpaca exitosa
   Balance: $100,000.00 (paper)
✅ Descarga de datos funcionando
   Datos obtenidos: 5 días
✅ Cálculo de indicadores técnicos funcionando

==================================================
🎉 ¡SETUP COMPLETADO EXITOSAMENTE!
==================================================

Estás listo para empezar la Sesión 1.
Guarda este notebook en tu Google Drive.
```

**Validación final:**
- [ ] Todos los ✅ aparecen (no hay ❌)
- [ ] Veo el mensaje "¡SETUP COMPLETADO EXITOSAMENTE!"
- [ ] Balance de Alpaca aparece (debería ser $100,000 paper)

---

### 📋 Paso 7: Guardar Notebook en Drive (2 min)

**Para no perder tu trabajo:**

1. `File` → `Save a copy in Drive`
2. Renombrar como: `Workshop_TradingAlgo_[TuNombre].ipynb`
3. Guardar en carpeta `00_Workshop_Trading_Algo/`

**✅ Setup Rápido Completo** - Total: ~30 minutos

---

## 💻 OPCIÓN B: Setup Avanzado (Python Local) - 2-3h

**✅ Ideal para:** Traders con experiencia técnica que quieren desarrollo local y deployment 24/7

### 📋 Paso 1: Instalar Python 3.11+ (15 min)

#### **Opción A: Anaconda (Recomendado para principiantes)**

**Windows:**
1. Descargar: [anaconda.com/download](https://www.anaconda.com/download)
2. Ejecutar instalador (`.exe`)
3. Opciones:
   - ✅ "Add Anaconda to PATH" (importante)
   - ✅ "Register Anaconda as default Python"
4. Reiniciar terminal

**macOS:**
```bash
# Instalar con Homebrew
brew install --cask anaconda

# Agregar al PATH
echo 'export PATH="/usr/local/anaconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Linux (Ubuntu/Debian):**
```bash
# Descargar instalador
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh

# Instalar
bash Anaconda3-2024.02-1-Linux-x86_64.sh

# Seguir instrucciones y agregar al PATH
```

#### **Opción B: Python Directo (Para usuarios avanzados)**

**Windows:**
1. Descargar: [python.org/downloads](https://www.python.org/downloads/)
2. Instalar Python 3.11.x
3. ✅ Marcar "Add Python to PATH"

**macOS:**
```bash
brew install python@3.11
```

**Linux:**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

**Validación:**
```bash
python --version
# Debe mostrar: Python 3.11.x o superior
```

---

### 📋 Paso 2: Crear Ambiente Virtual (10 min)

**¿Por qué un ambiente virtual?**  
Aísla las dependencias del workshop de otros proyectos Python.

#### **Con Anaconda:**

```bash
# Crear ambiente
conda create -n trading-algo python=3.11

# Activar
conda activate trading-algo

# Verificar
python --version  # Debe mostrar 3.11.x
```

#### **Con venv (Python vanilla):**

```bash
# Crear ambiente
python3.11 -m venv ~/envs/trading-algo

# Activar
# Windows:
~/envs/trading-algo/Scripts/activate

# macOS/Linux:
source ~/envs/trading-algo/bin/activate

# Verificar
python --version
```

**Validación:**
- [ ] Ambiente activado (ves `(trading-algo)` en el prompt)
- [ ] Python 3.11+ funcionando

---

### 📋 Paso 3: Instalar Librerías (30 min)

**Crear archivo `requirements.txt`:**

```txt
# requirements.txt - Librerías Trading Algorítmico 2025
# ========================================================

# === Core ===
numpy==1.26.3
pandas==2.2.0
scipy==1.12.0

# === Datos ===
yfinance==0.2.36
alpaca-py==0.25.0
ib-insync==0.9.86
MetaTrader5==5.0.45

# === Backtesting ===
vectorbt==0.26.1
backtrader==1.9.78.123
zipline-reloaded==3.0.4

# === Análisis Técnico ===
ta==0.11.0
pandas-ta==0.3.14b
TA-Lib==0.4.28

# === Visualización ===
matplotlib==3.8.2
seaborn==0.13.1
plotly==5.18.0
mplfinance==0.12.10

# === Machine Learning ===
scikit-learn==1.4.0
xgboost==2.0.3

# === APIs y Web ===
requests==2.31.0
websocket-client==1.7.0
fastapi==0.109.0
uvicorn==0.27.0

# === Utilities ===
python-dotenv==1.0.0
pyyaml==6.0.1
click==8.1.7
loguru==0.7.2

# === Jupyter (opcional) ===
jupyter==1.0.0
notebook==7.0.7
ipykernel==6.29.0
```

**Instalar:**

```bash
# Actualizar pip primero
pip install --upgrade pip

# Instalar todas las dependencias
pip install -r requirements.txt
```

**Tiempo:** ~20-30 minutos (descarga y compilación)

**⚠️ Nota sobre TA-Lib:**
TA-Lib requiere compilación en algunos sistemas:

**Windows:**
```bash
# Descargar wheel pre-compilado
# De: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip install TA_Lib‑0.4.28‑cp311‑cp311‑win_amd64.whl
```

**macOS:**
```bash
brew install ta-lib
pip install TA-Lib
```

**Linux:**
```bash
sudo apt-get install libta-lib-dev
pip install TA-Lib
```

**Validación:**
```bash
pip list | grep -E "pandas|numpy|yfinance|vectorbt|alpaca"
# Deberías ver todas las librerías instaladas
```

---

### 📋 Paso 4: Configurar Jupyter (10 min)

**Instalar Jupyter Lab:**

```bash
pip install jupyterlab==4.0.11
```

**Registrar el kernel:**

```bash
python -m ipykernel install --user --name=trading-algo --display-name="Python (Trading Algo)"
```

**Iniciar Jupyter:**

```bash
jupyter lab
```

Se abrirá en tu navegador: `http://localhost:8888`

**Validación:**
- [ ] Jupyter Lab abre correctamente
- [ ] Puedes crear un nuevo notebook
- [ ] El kernel "Python (Trading Algo)" aparece en la lista

---

### 📋 Paso 5: Configurar Brokers y APIs (15 min)

#### **Alpaca (Recomendado para multi-asset)**

1. **Crear archivo `.env` en tu directorio de trabajo:**

```bash
# .env - Variables de entorno

# Alpaca API (Paper Trading)
ALPACA_API_KEY=PKxxxxxxxxxxxxxxxxxx
ALPACA_API_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ALPACA_PAPER=true

# TradingView Webhook (opcional, para S7)
WEBHOOK_SECRET=tu_secreto_super_seguro

# Telegram Bot (opcional, para alertas)
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

2. **Test de conexión:**

```python
# test_alpaca.py
import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()

client = TradingClient(
    api_key=os.getenv('ALPACA_API_KEY'),
    secret_key=os.getenv('ALPACA_API_SECRET'),
    paper=True
)

account = client.get_account()
print(f"✅ Conexión exitosa")
print(f"Balance: ${float(account.cash):,.2f}")
```

```bash
python test_alpaca.py
```

**Validación:**
- [ ] Test ejecuta sin errores
- [ ] Veo mi balance de paper trading

---

### 📋 Paso 6: Validación Final (10 min)

**Script de validación completo:**

```python
# validate_setup.py
import sys

print("🔍 Validando setup completo...\n")

# 1. Python version
python_version = sys.version.split()[0]
print(f"✅ Python {python_version}")
assert python_version >= "3.11", "❌ Necesitas Python 3.11+"

# 2. Core libraries
try:
    import pandas as pd
    import numpy as np
    import yfinance as yf
    import vectorbt as vbt
    import backtrader as bt
    import ta
    print("✅ Librerías core importadas")
except ImportError as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# 3. Broker APIs
try:
    from alpaca.trading.client import TradingClient
    import MetaTrader5 as mt5
    from ib_insync import IB
    print("✅ APIs de brokers disponibles")
except ImportError as e:
    print(f"⚠️ Advertencia: {e}")
    print("   (Opcional si no usas ese broker)")

# 4. Jupyter
try:
    import notebook
    import ipykernel
    print("✅ Jupyter configurado")
except ImportError:
    print("⚠️ Jupyter no instalado (opcional)")

# 5. Test de datos
try:
    data = yf.download('SPY', period='5d', progress=False)
    assert len(data) > 0
    print(f"✅ Descarga de datos funcionando ({len(data)} días)")
except Exception as e:
    print(f"❌ Error en descarga: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("🎉 SETUP AVANZADO COMPLETADO")
print("="*50)
print("\nPróximos pasos:")
print("1. Configurar tu broker preferido")
print("2. Abrir Jupyter Lab")
print("3. Empezar Sesión 1")
```

```bash
python validate_setup.py
```

**✅ Setup Avanzado Completo** - Total: ~2-3 horas

---

## 📊 OPCIÓN C: MetaTrader 5 Setup - 1-2h

**✅ Ideal para:** Traders de Forex/CFDs que usan MetaTrader

### 📋 Paso 1: Instalar MetaTrader 5 (15 min)

**Windows:**
1. Descargar: [metatrader5.com](https://www.metatrader5.com/en/download)
2. Instalar MT5
3. Crear cuenta demo con tu broker preferido

**macOS:**
```bash
# MT5 no es nativo en macOS, usar alternativas:
# Opción A: Wine + PlayOnMac
# Opción B: Virtual Machine con Windows
# Opción C: Broker con WebTrader (IG, FXCM)
```

**Linux:**
```bash
# Instalar Wine
sudo apt install wine

# Descargar MT5
wget https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe

# Instalar
wine mt5setup.exe
```

**Validación:**
- [ ] MT5 instalado y abierto
- [ ] Cuenta demo configurada
- [ ] Puedo ver gráficos y hacer operaciones demo

---

### 📋 Paso 2: Instalar Python MT5 API (10 min)

**En tu ambiente Python:**

```bash
# Activar ambiente
conda activate trading-algo  # o tu ambiente

# Instalar MetaTrader5 para Python
pip install MetaTrader5==5.0.45
```

**Validación:**
```python
import MetaTrader5 as mt5

# Verificar versión
print(f"MetaTrader5 package version: {mt5.__version__}")
```

---

### 📋 Paso 3: Conectar Python con MT5 (15 min)

**Script de conexión:**

```python
# connect_mt5.py
import MetaTrader5 as mt5
from datetime import datetime

# Inicializar conexión
if not mt5.initialize():
    print("❌ Error: MT5 no inicializado")
    print(f"Error: {mt5.last_error()}")
    quit()

print("✅ Conexión con MT5 exitosa")

# Obtener información de la cuenta
account_info = mt5.account_info()
if account_info is not None:
    print(f"\nCuenta: {account_info.login}")
    print(f"Balance: ${account_info.balance:,.2f}")
    print(f"Equity: ${account_info.equity:,.2f}")
    print(f"Broker: {account_info.company}")
else:
    print("❌ No se pudo obtener info de cuenta")

# Listar símbolos disponibles
symbols = mt5.symbols_get()
print(f"\nSímbolos disponibles: {len(symbols)}")
print("Primeros 5:", [s.name for s in symbols[:5]])

# Test de datos históricos
symbol = "EURUSD"
rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 10)

if rates is not None:
    print(f"\n✅ Descarga de datos históricos funcionando")
    print(f"Símbolo: {symbol}")
    print(f"Últimos 10 días obtenidos")
else:
    print(f"❌ Error obteniendo datos de {symbol}")

# Cerrar conexión
mt5.shutdown()
print("\n✅ MT5 Setup completo")
```

```bash
python connect_mt5.py
```

**Resultado esperado:**
```
✅ Conexión con MT5 exitosa

Cuenta: 12345678
Balance: $10,000.00
Equity: $10,000.00
Broker: Tu Broker

Símbolos disponibles: 200
Primeros 5: ['EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD', 'USDCAD']

✅ Descarga de datos históricos funcionando
Símbolo: EURUSD
Últimos 10 días obtenidos

✅ MT5 Setup completo
```

**Validación:**
- [ ] Conexión exitosa con MT5
- [ ] Veo información de mi cuenta demo
- [ ] Puedo descargar datos históricos

---

### 📋 Paso 4: Integración con Python (20 min)

**Ejemplo de estrategia simple:**

```python
# strategy_mt5_example.py
import MetaTrader5 as mt5
import pandas as pd
import numpy as np

# Inicializar
mt5.initialize()

# Parámetros
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H1
periods = 100

# Obtener datos
rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, periods)
df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

# Calcular indicadores
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()

# Generar señales
df['signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'signal'] = 1  # Buy
df.loc[df['SMA_20'] < df['SMA_50'], 'signal'] = -1  # Sell

# Última señal
last_signal = df['signal'].iloc[-1]

print(f"Símbolo: {symbol}")
print(f"Precio actual: {df['close'].iloc[-1]:.5f}")
print(f"SMA 20: {df['SMA_20'].iloc[-1]:.5f}")
print(f"SMA 50: {df['SMA_50'].iloc[-1]:.5f}")
print(f"Señal: {'BUY' if last_signal == 1 else 'SELL' if last_signal == -1 else 'NEUTRAL'}")

mt5.shutdown()
```

**Validación:**
- [ ] El script ejecuta sin errores
- [ ] Veo señales generadas

**✅ MetaTrader 5 Setup Completo**

---

## 🏦 OPCIÓN D: Interactive Brokers Setup - 2-3h

**✅ Ideal para:** Traders profesionales con acceso a mercados globales

### 📋 Paso 1: Crear Cuenta IB Paper Trading (20 min)

**Pasos:**

1. **Ir a:** [interactivebrokers.com](https://www.interactivebrokers.com)

2. **Registrarse:**
   - Click en "Register"
   - Seleccionar "Individual Account"
   - Completar formulario

3. **Solicitar Paper Trading:**
   - En el portal, ir a "Account Management"
   - "Settings" → "Paper Trading Account"
   - Solicitar activación (aprueban en 24h)

4. **Descargar TWS (Trader Workstation):**
   - [Portal → Downloads](https://www.interactivebrokers.com/en/trading/tws.php)
   - Instalar TWS para tu sistema operativo

**Validación:**
- [ ] Cuenta paper trading aprobada
- [ ] TWS instalado y funcional
- [ ] Puedo hacer login a paper trading

---

### 📋 Paso 2: Instalar IB Gateway (30 min)

**IB Gateway es más ligero que TWS para conexiones API.**

**Windows/macOS/Linux:**
1. Descargar IB Gateway: [ibkr.com/gateway](https://www.interactivebrokers.com/en/trading/ibgateway-stable.php)
2. Instalar
3. Configurar:
   - Puerto API: `4002` (paper) o `4001` (live)
   - ✅ Habilitar "Enable ActiveX and Socket Clients"
   - ✅ Desmarcar "Read-Only API"
   - Socket Port: `7497`

**Validación:**
- [ ] IB Gateway instalado
- [ ] Puedo hacer login
- [ ] API habilitada (puerto 4002 o 7497)

---

### 📋 Paso 3: Instalar ib_insync (15 min)

**En tu ambiente Python:**

```bash
# Activar ambiente
conda activate trading-algo

# Instalar ib_insync (la mejor librería para IB en Python)
pip install ib-insync==0.9.86
```

**Validación:**
```python
from ib_insync import *

print(f"ib_insync version: {util.__version__}")
```

---

### 📋 Paso 4: Conectar Python con IB (20 min)

**Script de conexión:**

```python
# connect_ib.py
from ib_insync import *

# Conectar a IB Gateway
ib = IB()

try:
    # Puerto 4002 = Paper Trading, 4001 = Live Trading
    ib.connect('127.0.0.1', 4002, clientId=1)
    print("✅ Conexión con Interactive Brokers exitosa")
    
    # Obtener información de cuenta
    account_summary = ib.accountSummary()
    
    print("\nResumen de Cuenta:")
    for item in account_summary:
        if item.tag in ['TotalCashValue', 'NetLiquidation', 'BuyingPower']:
            print(f"{item.tag}: {item.currency} {item.value}")
    
    # Obtener posiciones
    positions = ib.positions()
    print(f"\nPosiciones abiertas: {len(positions)}")
    
    if positions:
        for pos in positions:
            print(f"- {pos.contract.symbol}: {pos.position} @ ${pos.avgCost:.2f}")
    
    # Test de datos de mercado
    contract = Stock('AAPL', 'SMART', 'USD')
    ib.qualifyContracts(contract)
    
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='5 D',
        barSizeSetting='1 day',
        whatToShow='TRADES',
        useRTH=True
    )
    
    print(f"\n✅ Descarga de datos funcionando")
    print(f"Símbolo: {contract.symbol}")
    print(f"Datos obtenidos: {len(bars)} días")
    
    # Último precio
    ticker = ib.reqTickers(contract)[0]
    print(f"Último precio: ${ticker.marketPrice():.2f}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nAsegúrate de:")
    print("1. IB Gateway está corriendo")
    print("2. Has hecho login")
    print("3. API está habilitada (puerto 4002)")

finally:
    ib.disconnect()
    print("\n✅ Desconectado de IB")
```

```bash
# IMPORTANTE: Primero inicia IB Gateway
# Luego ejecuta el script
python connect_ib.py
```

**Resultado esperado:**
```
✅ Conexión con Interactive Brokers exitosa

Resumen de Cuenta:
TotalCashValue: USD 1000000.00
NetLiquidation: USD 1000000.00
BuyingPower: USD 4000000.00

Posiciones abiertas: 0

✅ Descarga de datos funcionando
Símbolo: AAPL
Datos obtenidos: 5 días
Último precio: $189.50

✅ Desconectado de IB
```

**Validación:**
- [ ] Conexión exitosa con IB
- [ ] Veo información de mi cuenta paper
- [ ] Puedo descargar datos históricos

---

### 📋 Paso 5: Integración Avanzada (30 min)

**Ejemplo de estrategia con IB:**

```python
# strategy_ib_example.py
from ib_insync import *
import pandas as pd

# Conectar
ib = IB()
ib.connect('127.0.0.1', 4002, clientId=1)

# Definir contrato
contract = Stock('SPY', 'SMART', 'USD')
ib.qualifyContracts(contract)

# Obtener datos históricos
bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='30 D',
    barSizeSetting='1 hour',
    whatToShow='TRADES',
    useRTH=True
)

# Convertir a DataFrame
df = util.df(bars)
df['time'] = pd.to_datetime(df['date'])
df.set_index('time', inplace=True)

# Calcular indicadores
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['RSI'] = ta.momentum.rsi(df['close'], window=14)

# Generar señales
df['signal'] = 0
df.loc[(df['close'] > df['SMA_20']) & (df['RSI'] < 70), 'signal'] = 1
df.loc[(df['close'] < df['SMA_20']) | (df['RSI'] > 70), 'signal'] = -1

# Última señal
last_signal = df['signal'].iloc[-1]

print(f"Símbolo: {contract.symbol}")
print(f"Precio actual: ${df['close'].iloc[-1]:.2f}")
print(f"SMA 20: ${df['SMA_20'].iloc[-1]:.2f}")
print(f"RSI: {df['RSI'].iloc[-1]:.2f}")
print(f"Señal: {'BUY' if last_signal == 1 else 'SELL' if last_signal == -1 else 'NEUTRAL'}")

ib.disconnect()
```

**Validación:**
- [ ] Estrategia ejecuta sin errores
- [ ] Veo señales generadas
- [ ] Puedo analizar datos en DataFrame

**✅ Interactive Brokers Setup Completo**

**📚 Recursos IB:**
- [ib_insync Documentation](https://ib-insync.readthedocs.io/)
- [IB API Reference](https://www.interactivebrokers.com/en/trading/ib-api.php)

---

## 📦 Librerías y Dependencias (Actualizadas 2025)

### 🔵 Librerías Core (Obligatorias)

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **pandas** | 2.2.0 | Manejo de datos (DataFrame) | `pip install pandas==2.2.0` |
| **numpy** | 1.26.3 | Cálculos numéricos | `pip install numpy==1.26.3` |
| **scipy** | 1.12.0 | Estadística avanzada | `pip install scipy==1.12.0` |

---

### 📊 Obtención de Datos

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **yfinance** | 0.2.36 | Datos Yahoo Finance (gratis) | `pip install yfinance==0.2.36` |
| **alpaca-py** | 0.25.0 | API Alpaca (moderna, 2024) | `pip install alpaca-py==0.25.0` |
| **ib-insync** | 0.9.86 | Interactive Brokers | `pip install ib-insync==0.9.86` |
| **MetaTrader5** | 5.0.45 | MetaTrader 5 API | `pip install MetaTrader5==5.0.45` |

**⚠️ Nota:** `alpaca-py` es la librería oficial nueva de Alpaca (reemplaza `alpaca-trade-api`).

---

### 📈 Backtesting

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **vectorbt** | 0.26.1 | Backtesting vectorizado (rápido) | `pip install vectorbt==0.26.1` |
| **backtrader** | 1.9.78.123 | Backtesting event-driven (flexible) | `pip install backtrader==1.9.78.123` |
| **zipline-reloaded** | 3.0.4 | Backtesting institucional | `pip install zipline-reloaded==3.0.4` |

**Comparación:**
- **vectorbt**: Mejor para optimización de parámetros (10-100x más rápido)
- **backtrader**: Mejor para lógica compleja de estrategias
- **zipline-reloaded**: Mejor para análisis estilo hedge fund

---

### 📉 Análisis Técnico

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **ta** | 0.11.0 | 130+ indicadores técnicos | `pip install ta==0.11.0` |
| **pandas-ta** | 0.3.14b | Integración pandas | `pip install pandas-ta==0.3.14b` |
| **TA-Lib** | 0.4.28 | Librería C (más rápida) | Ver instalación especial abajo |

**Instalación TA-Lib (requiere compilación):**

**Windows:**
```bash
# Descargar wheel de: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip install TA_Lib-0.4.28-cp311-cp311-win_amd64.whl
```

**macOS:**
```bash
brew install ta-lib
pip install TA-Lib
```

**Linux:**
```bash
sudo apt-get install libta-lib-dev
pip install TA-Lib
```

---

### 📊 Visualización

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **matplotlib** | 3.8.2 | Gráficos estáticos | `pip install matplotlib==3.8.2` |
| **seaborn** | 0.13.1 | Gráficos estadísticos | `pip install seaborn==0.13.1` |
| **plotly** | 5.18.0 | Gráficos interactivos | `pip install plotly==5.18.0` |
| **mplfinance** | 0.12.10 | Gráficos de velas (candlesticks) | `pip install mplfinance==0.12.10` |

---

### 🤖 Machine Learning (Opcional)

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **scikit-learn** | 1.4.0 | ML clásico | `pip install scikit-learn==1.4.0` |
| **xgboost** | 2.0.3 | Gradient boosting | `pip install xgboost==2.0.3` |
| **tensorflow** | 2.15.0 | Deep Learning | `pip install tensorflow==2.15.0` |

---

### 🔧 Utilities

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **python-dotenv** | 1.0.0 | Variables de entorno (.env) | `pip install python-dotenv==1.0.0` |
| **loguru** | 0.7.2 | Logging mejorado | `pip install loguru==0.7.2` |
| **click** | 8.1.7 | CLI apps | `pip install click==8.1.7` |
| **requests** | 2.31.0 | HTTP requests | `pip install requests==2.31.0` |

---

### 📝 Jupyter (Opcional)

| Librería | Versión | Propósito | Instalación |
|----------|---------|-----------|-------------|
| **jupyter** | 1.0.0 | Jupyter Notebook | `pip install jupyter==1.0.0` |
| **jupyterlab** | 4.0.11 | Jupyter Lab (IDE) | `pip install jupyterlab==4.0.11` |
| **ipykernel** | 6.29.0 | Kernel Python | `pip install ipykernel==6.29.0` |

---

## 🚨 Troubleshooting

### ❌ Error: "No module named 'yfinance'"

**Causa:** Librería no instalada o instalada en ambiente incorrecto.

**Solución (Colab):**
```python
!pip install yfinance
```

**Solución (Local):**
```bash
# Verifica que el ambiente esté activado
conda activate trading-algo  # o tu ambiente

# Instala
pip install yfinance

# Verifica
python -c "import yfinance; print('OK')"
```

---

### ❌ Error: "Alpaca API authentication failed"

**Causa:** API keys incorrectas, no configuradas, o usando keys de Live en Paper.

**Solución:**

1. **Verifica las keys:**
   - ✅ `API_KEY` debe empezar con "PK..."
   - ✅ `SECRET_KEY` es un string largo
   - ✅ Las keys son de **Paper Trading** (no Live)

2. **Regenera las keys:**
   - Ir a Alpaca Dashboard
   - API Keys → "Regenerate"
   - Copiar y reemplazar en tu código

3. **Verifica el código:**
```python
# Debe tener paper=True
client = TradingClient(
    api_key="tu_key",
    secret_key="tu_secret",
    paper=True  # ← IMPORTANTE
)
```

---

### ❌ Error: "IndexError: list index out of range" en backtesting

**Causa:** Datos insuficientes o mal formateados.

**Solución:**

1. **Verifica cantidad de datos:**
```python
print(f"Datos disponibles: {len(df)} días")
# Mínimo recomendado: 252 días (1 año)
```

2. **Verifica formato:**
```python
print(df.head())
# Columnas requeridas: ['Open', 'High', 'Low', 'Close', 'Volume']
```

3. **Descarga más datos:**
```python
data = yf.download('SPY', period='2y')  # 2 años en vez de 5 días
```

---

### ❌ Error: "TA-Lib not found" o "ImportError: DLL load failed"

**Causa:** TA-Lib no está instalada correctamente (requiere compilación).

**Solución Windows:**
```bash
# Descargar wheel pre-compilado de:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib

# Instalar wheel
pip install TA_Lib-0.4.28-cp311-cp311-win_amd64.whl
```

**Solución macOS:**
```bash
brew install ta-lib
pip install TA-Lib
```

**Solución Linux:**
```bash
sudo apt-get install libta-lib-dev
pip install TA-Lib
```

**Alternativa (sin TA-Lib):**
Usa `ta` o `pandas-ta` en su lugar (más fáciles de instalar):
```bash
pip install ta pandas-ta
```

---

### ❌ "Colab se desconecta y pierdo mi trabajo"

**Causa:** Sesiones de Colab expiran después de ~12h de inactividad.

**Solución:**

1. **Guardar frecuentemente:**
   - `Ctrl + S` o `File → Save`

2. **Descargar notebook:**
   - `File → Download → .ipynb`

3. **Usar Google Drive:**
```python
# Montar Drive (ejecutar celda)
from google.colab import drive
drive.mount('/content/drive')

# Guardar notebook en Drive automáticamente
# File → Save a copy in Drive
```

4. **Mantener sesión activa (hack):**
```python
# NO recomendado, pero funciona
# Ejecutar esta celda para mantener conexión
import time
for i in range(100):
    print(f"Manteniendo sesión activa... {i}/100")
    time.sleep(600)  # 10 minutos
```

---

### ❌ MetaTrader5: "initialize() failed"

**Causa:** MT5 no está corriendo o no se puede conectar.

**Solución:**

1. **Verificar que MT5 está abierto:**
   - Abrir MetaTrader 5 desktop app
   - Hacer login con cuenta demo

2. **Verificar ruta de instalación:**
```python
import MetaTrader5 as mt5

# En Windows, especificar ruta si necesario
mt5.initialize(
    path="C:\\Program Files\\MetaTrader 5\\terminal64.exe"
)
```

3. **Verificar que cuenta está activa:**
   - En MT5: Tools → Options → Server
   - Debe mostrar "Connected"

---

### ❌ Interactive Brokers: "Connection refused"

**Causa:** IB Gateway no está corriendo o puerto incorrecto.

**Solución:**

1. **Verificar que IB Gateway está corriendo:**
   - Iniciar IB Gateway
   - Hacer login

2. **Verificar puerto:**
```python
# Paper Trading = puerto 4002
# Live Trading = puerto 4001
ib.connect('127.0.0.1', 4002, clientId=1)
```

3. **Verificar API habilitada:**
   - En IB Gateway: Configure → Settings → API → Settings
   - ✅ "Enable ActiveX and Socket Clients"
   - Socket Port: 7497 (predeterminado)

4. **Firewall:**
   - Asegúrate de que el firewall permite conexiones al puerto 4002

---

### ❌ "Kernel died" o "Out of Memory" en Jupyter

**Causa:** Estrategia está usando demasiada memoria.

**Solución:**

1. **Reducir datos:**
```python
# Cargar menos datos
data = yf.download('SPY', period='1y')  # En vez de '10y'
```

2. **Liberar memoria:**
```python
import gc

# Después de backtests pesados
del data, results
gc.collect()
```

3. **Usar chunks:**
```python
# Para datasets muy grandes
for chunk in pd.read_csv('huge_data.csv', chunksize=10000):
    # Procesar chunk por chunk
    pass
```

---

### ❌ "SSL Certificate Verify Failed"

**Causa:** Problema con certificados SSL (común en redes corporativas).

**Solución temporal (NO recomendado para producción):**
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

**Solución correcta:**
```bash
# Actualizar certifi
pip install --upgrade certifi
```

---

### ❌ "ModuleNotFoundError" después de instalar

**Causa:** Instalaste en un ambiente, pero estás ejecutando en otro.

**Solución:**

1. **Verificar ambiente activo:**
```bash
# Debería mostrar tu ambiente
conda env list
# O
which python
```

2. **Reinstalar en ambiente correcto:**
```bash
conda activate trading-algo
pip install [librería]
```

3. **En Jupyter, verificar kernel:**
   - Kernel → Change Kernel → "Python (Trading Algo)"

---

## ✅ Validación Final

**Antes de empezar la Sesión 1, verifica:**

### 🎯 Setup Rápido (Colab)

- [ ] Puedo abrir Google Colab
- [ ] Tengo API keys de Alpaca configuradas
- [ ] Todas las librerías instaladas (celda ejecuta sin errores)
- [ ] Validación completa pasó (todos los ✅)
- [ ] Balance de Alpaca aparece ($100,000 paper)
- [ ] Puedo descargar datos con yfinance

### 🎯 Setup Avanzado (Local)

- [ ] Python 3.11+ instalado
- [ ] Ambiente virtual creado y activo
- [ ] Todas las librerías instaladas (requirements.txt)
- [ ] Jupyter Lab funciona
- [ ] Puedo conectar con Alpaca API
- [ ] Script de validación pasa (validate_setup.py)

### 🎯 MetaTrader 5

- [ ] MT5 instalado y funcional
- [ ] Cuenta demo configurada
- [ ] Python MT5 package instalado
- [ ] Puedo conectar Python con MT5
- [ ] Puedo descargar datos históricos de MT5

### 🎯 Interactive Brokers

- [ ] Cuenta paper trading aprobada
- [ ] IB Gateway instalado
- [ ] ib_insync instalado
- [ ] Puedo conectar Python con IB
- [ ] Puedo descargar datos históricos de IB

---

## 📞 Soporte

**Si algo no funciona después de seguir esta guía:**

### 📧 Email
**yismaryme@gmail.com**  
Tiempo de respuesta: 24-48h

**Incluye en tu email:**
- Sistema operativo (Windows/macOS/Linux)
- Setup que intentaste (Rápido/Avanzado/MT5/IB)
- Paso exacto donde falló
- Error completo (screenshot o texto)
- Qué ya intentaste

### 💬 Telegram
**[@yismary](https://t.me/yismary)**  
Para consultas rápidas pre-workshop

### 🔒 Grupo Premium
**Solo participantes pagos**  
Soporte comunitario + sesiones de troubleshooting

---

## 🎯 Próximos Pasos

**Una vez completado tu setup:**

1. ✅ **Guarda/bookmark este documento** para referencia futura

2. ✅ **Vuelve a** [LEEME_PRIMERO.md](LEEME_PRIMERO.md)

3. ✅ **Completa el** [Checklist "Tu Primer Día"](LEEME_PRIMERO.md#-checklist-tu-primer-día)

4. ✅ **Revisa el** [Programa Detallado](ESTRUCTURA_COMPLETA.md) para entender las 9 sesiones

5. ✅ **¡Estás listo para la Sesión 1!** 🎉

---

## 🔖 Versión y Actualizaciones

**Versión:** 1.0 (Noviembre 2025)  
**Última actualización:** 13 de noviembre de 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- v1.0 (Nov 2025): Versión inicial con 4 opciones de setup + librerías 2025

---

## ⚠️ Disclaimer

**Este es material educativo.**

- ✅ Todas las herramientas son gratuitas para paper trading
- ⚠️ Nunca uses credenciales de live trading en el workshop
- 📊 Practica con cuentas demo/paper antes de arriesgar capital real
- 💰 Trading algorítmico tiene riesgo de pérdida de capital

---

**¿Listo para empezar?** 🚀

Recuerda: **GenAI = Copiloto, NO Piloto Automático.**  
El setup es el primer paso de un viaje de 3-6 meses.

¡Nos vemos en la Sesión 1! 🎓
