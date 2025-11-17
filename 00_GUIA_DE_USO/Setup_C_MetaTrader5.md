# 📖 SETUP C: METATRADER 5 - GUÍA PASO A PASO

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 📊 Setup MetaTrader 5**

---

**⏱️ Tiempo estimado:** 60-90 minutos  
**🎯 Nivel de detalle:** Paso a paso para traders MT5  
**📅 Última actualización:** Noviembre 2025  
**🎓 Dificultad:** ⭐⭐⭐ (3/5 estrellas)

---

## 🎯 ¿PARA QUIÉN ES ESTA GUÍA?

### ✅ Esta Guía es PERFECTA si:

- 📊 **Ya usas MetaTrader 5** para trading manual (abrir/cerrar órdenes)
- 🤖 Quieres **automatizar tus estrategias** sin aprender MQL5 desde cero
- 🐍 Prefieres usar **Python** (que ya conoces del workshop) en vez de MQL5
- 💼 Operas con **AvaTrade** o quieres empezar con ellos
- 🔄 Necesitas **backtesting profesional** en Strategy Tester de MT5
- ⚡ Quieres **combinar Python + MT5** para lo mejor de ambos mundos

### ❌ Esta Guía NO es Ideal si:

- 🆕 **Nunca usaste MetaTrader** 5  
  → Esta guía asume que sabes navegar MT5 básicamente
  
- 📝 Quieres aprender **MQL5 nativo** (lenguaje de MT5)  
  → Esta guía usa Python, no MQL5 puro
  
- 🏦 Operas con **otro broker** que no soporta MT5  
  → Necesitas un broker compatible con MT5
  
- ⏱️ Solo quieres **prototipar rápido**  
  → Usa [Colab](Setup_A_Guiado.md) - Es más rápido para testear ideas

---

## 📑 TABLA DE CONTENIDOS

### 🚀 Quick Links
- [⚡ Mapa de Progreso](#-mapa-de-progreso)
- [🤔 ¿Por Qué MT5 + Python?](#-por-qué-metatrader-5--python)
- [🚨 ¿Problemas?](#-troubleshooting-por-paso)
- [📞 Soporte](#-soporte-y-contacto)

### 📖 Pasos Detallados
1. [Paso 1: Instalar MetaTrader 5](#paso-1-instalar-metatrader-5-10-min)
2. [Paso 2: Crear Cuenta Demo en AvaTrade](#paso-2-crear-cuenta-demo-en-avatrade-15-min)
3. [Paso 3: Instalar Librería MetaTrader5 de Python](#paso-3-instalar-librería-metatrader5-de-python-10-min)
4. [Paso 4: Conectar Python con MT5](#paso-4-conectar-python-con-mt5-15-min)
5. [Paso 5: Ejecutar Primera Operación desde Python](#paso-5-ejecutar-primera-operación-desde-python-15-min)
6. [Paso 6: Crear Expert Advisor Básico](#paso-6-crear-expert-advisor-básico-20-min)
7. [Paso 7: Backtesting en Strategy Tester](#paso-7-backtesting-en-strategy-tester-15-min)

### 🔗 Navegación
- [Diferencias Python vs MQL5](#-diferencias-python-vs-mql5-en-mt5)
- [Mejores Prácticas MT5](#-mejores-prácticas-mt5--python)
- [Troubleshooting por Paso](#-troubleshooting-por-paso)
- [Próximos Pasos](#-próximos-pasos)

---

## 🗺️ MAPA DE PROGRESO

**Sigue este camino durante el setup:**

```
RUTA METATRADER 5 + PYTHON:

├─ ✅ Paso 1: Instalar MetaTrader 5 (10 min)
├─ ⏳ Paso 2: Crear Cuenta Demo AvaTrade (15 min)
├─ ⬜ Paso 3: Instalar MetaTrader5 Library (10 min)
├─ ⬜ Paso 4: Conectar Python con MT5 (15 min)
├─ ⬜ Paso 5: Primera Operación Python (15 min)
├─ ⬜ Paso 6: Crear Expert Advisor (20 min)
└─ ⬜ Paso 7: Backtesting (15 min)

TOTAL: 60-90 minutos
```

---

## 🤔 ¿POR QUÉ METATRADER 5 + PYTHON?

### 📍 Entendiendo la Combinación

**💡 Analogía del Trader:**

> **MetaTrader 5 solo** es como **operar manualmente con una plataforma profesional**:
> - ✅ Excelente para análisis visual
> - ✅ Herramientas de charting potentes
> - ❌ Trading manual = lento y emocional
>
> **Python solo** es como **tener un analista brillante sin acceso al mercado**:
> - ✅ Puedes analizar datos y crear estrategias
> - ✅ Flexible y fácil de programar
> - ❌ No puede ejecutar órdenes directamente en MT5
>
> **MT5 + Python juntos** es como **tener un trader automático profesional**:
> - ✅ Python analiza y toma decisiones
> - ✅ MT5 ejecuta las órdenes al mercado
> - ✅ Lo mejor de ambos mundos

---

### 🆚 Comparación: MQL5 vs Python en MT5

| Característica | MQL5 Nativo | Python + MT5 |
|---------------|-------------|--------------|
| **Lenguaje** | MQL5 (específico MT5) | Python (universal) |
| **Curva aprendizaje** | ⚠️ Empinada | ✅ Gradual |
| **Velocidad ejecución** | ✅ Máxima | ⚠️ Buena (suficiente) |
| **Librerías disponibles** | ⚠️ Limitadas | ✅ Miles (pandas, numpy, etc.) |
| **Desarrollo estrategias** | ⚠️ Más lento | ✅ Más rápido |
| **Backtesting** | ✅ Strategy Tester nativo | ✅ Strategy Tester + Python |
| **Integración IA** | ❌ Difícil | ✅ Fácil (ChatGPT, Claude) |
| **Portabilidad** | ❌ Solo MT5 | ✅ Multi-plataforma |

**💡 Recomendación del Instructor:**

> Usa **Python para desarrollar** la lógica de trading (es más rápido y flexible).
> 
> Usa **MT5 para ejecutar** (conexión directa al broker y backtesting profesional).

---

### 🎯 Casos de Uso Ideales para MT5 + Python

**Usa esta combinación cuando:**
- 🌍 Operas **Forex, CFDs, o Commodities** (especialidad de MT5)
- 📊 Necesitas **charting profesional** de MT5
- 🔄 Quieres **backtesting riguroso** con datos tick reales
- 🐍 Prefieres **programar en Python** vs. aprender MQL5
- 🤖 Quieres **automatizar estrategias** existentes de MT5
- 📈 Necesitas **indicadores personalizados** fáciles de crear

**NO uses esta combinación cuando:**
- 💻 Solo operas **US Stocks** → Mejor Alpaca/IB con Python directo
- ⚡ Necesitas **ejecución ultra-rápida** (HFT) → Mejor MQL5 nativo
- 🧪 Solo quieres **prototipar** ideas → Mejor Google Colab
- 📱 Operas desde **móvil** principalmente → MT5 app es suficiente

---

## PASO 1: INSTALAR METATRADER 5 (10 min)

### 🎯 Objetivo del Paso
Descargar e instalar MetaTrader 5 en tu PC con Windows.

---

### 📍 ¿Qué es MetaTrader 5?

**💡 Analogía del Trader:**

> MetaTrader 5 es como **TradingView + tu broker + automatización** todo en uno:
>
> - **TradingView** → Solo gráficos (no puedes operar directamente)
> - **MT5** → Gráficos + ejecución de órdenes + automatización + backtesting
>
> Es la "suite completa" para trading profesional, especialmente Forex.

---

### 🚀 Acción: Instalar MT5

**Paso 1.1 - Descargar MetaTrader 5:**

1. **Abre tu navegador**
2. **Ve a:** https://www.metatrader5.com/en/download
3. **Click en:** "Download MetaTrader 5 for Windows"

**Alternativa - Desde AvaTrade (recomendado):**
1. **Ve a:** https://www.avatrade.com/trading-platforms/metatrader-5
2. **Click en:** "Download MT5"

**🔍 Verificación:**
- El archivo descargado: `mt5setup.exe` (o similar)
- Tamaño aproximado: 15-20 MB

---

**Paso 1.2 - Ejecutar el Instalador:**

1. **Doble click** en `mt5setup.exe`
2. **Acepta** los términos y condiciones
3. **Click:** "Siguiente" (deja opciones por defecto)
4. **Espera** 2-3 minutos mientras se instala

**Se instalarán:**
- MetaTrader 5 (aplicación principal)
- MetaEditor (para editar código MQL5)
- Conexión a servidores de demo

5. **Al finalizar:** Se abrirá automáticamente MT5

---

**Paso 1.3 - Primer Vistazo a la Interfaz:**

**Cuando se abre MT5 por primera vez, verás:**

```
┌─────────────────────────────────────────────────┐
│ 🔝 BARRA DE MENÚ                                │
│    File  View  Insert  Charts  Tools  Window   │
├─────────────────────────────────────────────────┤
│ 📊 GRÁFICO PRINCIPAL                            │
│                                                 │
│    [Gráfico de EURUSD o similar]                │
│                                                 │
├─────────────────────────────────────────────────┤
│ 📂 NAVEGADOR (izquierda)  | 📈 TERMINAL (abajo) │
│    - Accounts              |   - Trade           │
│    - Indicators            |   - History         │
│    - Expert Advisors       |   - News            │
└─────────────────────────────────────────────────┘
```

**💡 No te preocupes si te abruma.** Solo necesitas familiarizarte con:
- **Market Watch** (panel izquierdo) → Lista de símbolos
- **Navigator** (panel izquierdo) → Expert Advisors
- **Terminal** (panel abajo) → Historial de órdenes

---

**Paso 1.4 - Habilitar Conexión Python:**

**⚠️ MUY IMPORTANTE:** Para que Python pueda conectarse, debes habilitar "Algo Trading".

1. **En MT5, click en:** `Tools` → `Options`
2. **Pestaña:** `Expert Advisors`
3. **✅ Marca las siguientes opciones:**
   - ☑ Allow automated trading
   - ☑ Allow DLL imports
   - ☑ Allow WebRequest for listed URL

4. **Click:** "OK"

**Sin esto, Python NO podrá conectarse a MT5.**

---

### ✅ Checkpoint de Validación - Paso 1

Antes de continuar, verifica:

- [ ] Descargaste MT5 (mt5setup.exe)
- [ ] Instalaste MT5 correctamente
- [ ] Se abrió la aplicación MT5
- [ ] Ves la interfaz con gráficos
- [ ] Habilitaste "Allow automated trading" en Options

**Si marcaste todos ✅ → Continúa al Paso 2**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 1](#error-paso-1-mt5-no-se-instala)**

---

## PASO 2: CREAR CUENTA DEMO EN AVATRADE (15 min)

### 🎯 Objetivo del Paso
Crear una cuenta demo gratuita en AvaTrade para poder operar en MT5 sin riesgo.

---

### 📍 ¿Por Qué AvaTrade?

**💡 Analogía del Trader:**

> AvaTrade es como **un banco que te da una cuenta de práctica** con dinero virtual:
>
> - 💰 $100,000 USD virtuales para practicar
> - ✅ Datos de mercado reales
> - ✅ Ejecución realista de órdenes
> - ❌ CERO riesgo (es solo simulación)

**Otras opciones de brokers MT5:**
- AvaTrade (recomendado para principiantes)
- XM Global
- IC Markets
- Pepperstone
- FXTM

**Esta guía usa AvaTrade, pero el proceso es similar en otros brokers.**

---

### 🚀 Acción: Crear Cuenta Demo

**Paso 2.1 - Registrarse en AvaTrade:**

1. **Abre tu navegador**
2. **Ve a:** https://www.avatrade.com/
3. **Click en:** "Try Free Demo" o "Abrir Cuenta Demo"

4. **Completa el formulario:**
   - Nombre completo
   - Email
   - Teléfono
   - País

5. **Selecciona plataforma:** MetaTrader 5
6. **Click:** "Open Demo Account"

---

**Paso 2.2 - Verificar Email:**

1. **Revisa tu email** (el que registraste)
2. **Busca email de AvaTrade:**
   - Asunto: "Your Demo Account Details" o similar

3. **En el email verás:**
   ```
   Login: 123456789
   Password: AbCdEfGh123
   Server: AvaTradeDemo-MT5
   ```

**⚠️ GUARDA ESTOS DATOS** - Los necesitarás para conectarte.

---

**Paso 2.3 - Conectar MT5 a AvaTrade:**

1. **Abre MetaTrader 5**
2. **Click en:** `File` → `Login to Trade Account`

3. **En la ventana que se abre:**
   - **Login:** (el número que te enviaron por email)
   - **Password:** (la contraseña del email)
   - **Server:** Busca "AvaTrade" en la lista desplegable
     - Selecciona: `AvaTradeDemo-MT5` o similar

4. **Click:** "Login"

**✅ Si la conexión fue exitosa:**
- Verás en la esquina inferior derecha: **velocidad de conexión** (ej: "128/64 kb/s")
- Color verde en el indicador de conexión

---

**Paso 2.4 - Verificar Balance de Cuenta Demo:**

1. **En MT5, click en:** `View` → `Toolbox` (o presiona Ctrl+T)
2. **Panel inferior se abrirá**
3. **Pestaña:** `Trade`

**Deberías ver:**
```
Balance: $100,000.00
Equity: $100,000.00
Margin: 0.00
Free Margin: $100,000.00
```

**🎉 ¡Perfecto! Tienes $100,000 USD virtuales para operar.**

---

**Paso 2.5 - Descargar Datos de Mercado:**

**Para que Python pueda acceder a datos históricos:**

1. **En MT5, click en:** `View` → `Market Watch` (o Ctrl+M)
2. **Panel izquierdo se abrirá con lista de símbolos**
3. **Click derecho** en cualquier lugar → `Symbols`
4. **Busca estos símbolos populares:**
   - EURUSD
   - GBPUSD
   - USDJPY
   - XAUUSD (Gold)
   - US30 (Dow Jones)

5. **Para cada uno:**
   - Click en el símbolo
   - Click en "Show" (abajo)
   - ✅ Se agregará a Market Watch

**💡 ¿Por qué esto es importante?**
Solo los símbolos visibles en Market Watch se pueden acceder desde Python.

---

### ✅ Checkpoint de Validación - Paso 2

Antes de continuar, verifica:

- [ ] Te registraste en AvaTrade (cuenta demo)
- [ ] Recibiste email con Login/Password/Server
- [ ] Conectaste MT5 a AvaTrade
- [ ] Ves balance de $100,000 USD en pestaña Trade
- [ ] Agregaste símbolos a Market Watch (EURUSD, etc.)
- [ ] Ves conexión activa (esquina inferior derecha)

**Si marcaste todos ✅ → Continúa al Paso 3**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 2](#error-paso-2-no-puedo-conectar-mt5-a-avatrade)**

---

## PASO 3: INSTALAR LIBRERÍA METATRADER5 DE PYTHON (10 min)

### 🎯 Objetivo del Paso
Instalar la librería oficial MetaTrader5 de Python que permite conectar Python con MT5.

---

### 📍 ¿Qué es la Librería MetaTrader5?

**💡 Analogía del Trader:**

> La librería MetaTrader5 es como **un traductor** entre Python y MT5:
>
> - **Python** habla "lenguaje de programación Python"
> - **MT5** habla "lenguaje de trading MT5"
> - **Librería MT5** traduce entre ambos en tiempo real

**Con esta librería puedes:**
- Obtener datos de precios desde Python
- Enviar órdenes de trading desde Python
- Leer información de cuenta desde Python
- Controlar MT5 completamente con código Python

---

### 🚀 Acción: Instalar Librería

**Paso 3.1 - Abrir CMD con Python:**

**Opción A - Si hiciste Setup B (Python Local):**

1. **Abre CMD** en `C:\TradingAlgo\`
2. **Activa virtual environment:**
   ```bash
   venv_trading\Scripts\activate
   ```

**Opción B - Si NO hiciste Setup B:**

1. **Abre CMD** (Windows + R → `cmd` → Enter)
2. **Verifica Python instalado:**
   ```bash
   python --version
   ```

**Deberías ver:** `Python 3.11.X` o superior

---

**Paso 3.2 - Instalar MetaTrader5:**

1. **En CMD, ejecuta:**
   ```bash
   pip install MetaTrader5
   ```

2. **Espera 20-30 segundos**

**✅ Al finalizar verás:**
```
Successfully installed MetaTrader5-5.X.X
```

---

**Paso 3.3 - Verificar Instalación:**

1. **En CMD, ejecuta:**
   ```bash
   python -c "import MetaTrader5; print(MetaTrader5.__version__)"
   ```

**✅ Deberías ver:**
```
5.0.X
```

**Si ves la versión, ¡perfecto! La librería está instalada.**

---

**Paso 3.4 - Test de Conexión Rápido:**

1. **Crea un archivo de prueba** (test_mt5.py):

**Opción A - Usando Jupyter:**
- Abre Jupyter: `jupyter notebook`
- Crea notebook nuevo
- Copia el código de abajo

**Opción B - Usando editor de texto:**
- Abre Notepad
- Copia el código de abajo
- Guarda como: `C:\TradingAlgo\test_mt5.py`

**Código de prueba:**
```python
import MetaTrader5 as mt5

print("MetaTrader5 package version:", mt5.__version__)
print("\n🔍 Intentando conectar con MT5...")

# Inicializar MT5
if mt5.initialize():
    print("✅ MT5 inicializado correctamente")
    
    # Obtener info de cuenta
    account_info = mt5.account_info()
    if account_info != None:
        print(f"\n📊 Información de cuenta:")
        print(f"   Balance: ${account_info.balance:,.2f}")
        print(f"   Server: {account_info.server}")
        print(f"   Company: {account_info.company}")
    
    # Cerrar conexión
    mt5.shutdown()
    print("\n✅ Test completado exitosamente")
else:
    print("❌ Error al inicializar MT5")
    print(f"   Código de error: {mt5.last_error()}")
```

2. **Ejecuta el código:**

**Si usas Jupyter:**
- Shift + Enter

**Si usas archivo .py:**
```bash
python test_mt5.py
```

**✅ Deberías ver:**
```
MetaTrader5 package version: 5.0.X

🔍 Intentando conectar con MT5...
✅ MT5 inicializado correctamente

📊 Información de cuenta:
   Balance: $100,000.00
   Server: AvaTradeDemo-MT5
   Company: AvaTrade

✅ Test completado exitosamente
```

**🎉 ¡Perfecto! Python está conectado con MT5.**

---

### ⚠️ Advertencias Importantes

**1. MT5 debe estar ABIERTO:**
- Python no puede conectarse si MT5 está cerrado
- Deja MT5 corriendo mientras usas Python

**2. Solo funciona en Windows:**
- La librería MetaTrader5 solo funciona en Windows
- Mac/Linux: Usa Wine o máquina virtual

**3. Permisos de DLL:**
- Ya lo configuramos en Paso 1.4
- Si olvidaste: Tools → Options → Expert Advisors → ☑ Allow DLL imports

---

### ✅ Checkpoint de Validación - Paso 3

Antes de continuar, verifica:

- [ ] Instalaste MetaTrader5 con `pip install MetaTrader5`
- [ ] Verificaste versión con `python -c "import MetaTrader5..."`
- [ ] Ejecutaste test_mt5.py (o código en Jupyter)
- [ ] Viste balance de tu cuenta ($100,000)
- [ ] El test se completó sin errores

**Si marcaste todos ✅ → Continúa al Paso 4**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 3](#error-paso-3-librería-mt5-no-se-instala)**

---

## PASO 4: CONECTAR PYTHON CON MT5 (15 min)

### 🎯 Objetivo del Paso
Aprender a conectar, obtener datos, y operar en MT5 desde Python de manera profesional.

---

### 📍 Conceptos Fundamentales

**💡 Analogía del Trader:**

> Conectar Python con MT5 es como **configurar tu API de broker**:
>
> - Estableces conexión (login)
> - Obtienes permisos (símbolos, datos)
> - Ejecutas acciones (órdenes, consultas)
> - Cierras conexión (shutdown)

---

### 🚀 Acción: Script de Conexión Completo

**Paso 4.1 - Crear Script de Conexión Profesional:**

**Crea un archivo:** `mt5_connection.py` (o celda en Jupyter)

```python
# ═══════════════════════════════════════════════════════════
# 📡 CONEXIÓN PROFESIONAL PYTHON ↔ MT5
# ═══════════════════════════════════════════════════════════

import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

def conectar_mt5():
    """
    Conecta con MetaTrader 5 y verifica estado.
    
    Returns:
        bool: True si conexión exitosa, False si falló
    """
    print("🔄 Conectando con MetaTrader 5...")
    
    # Inicializar MT5
    if not mt5.initialize():
        print(f"❌ Error al inicializar MT5: {mt5.last_error()}")
        return False
    
    print("✅ Conexión establecida con MT5")
    
    # Obtener información de cuenta
    account_info = mt5.account_info()
    
    if account_info is None:
        print("❌ No se pudo obtener info de cuenta")
        return False
    
    # Mostrar información
    print("\n" + "="*60)
    print("📊 INFORMACIÓN DE CUENTA")
    print("="*60)
    print(f"Servidor: {account_info.server}")
    print(f"Número de cuenta: {account_info.login}")
    print(f"Compañía: {account_info.company}")
    print(f"Moneda: {account_info.currency}")
    print(f"Balance: ${account_info.balance:,.2f}")
    print(f"Equity: ${account_info.equity:,.2f}")
    print(f"Margen libre: ${account_info.margin_free:,.2f}")
    print(f"Nivel de margen: {account_info.margin_level:.2f}%")
    print("="*60)
    
    return True

def obtener_simbolos_disponibles():
    """
    Obtiene lista de símbolos disponibles en MT5.
    
    Returns:
        list: Lista de símbolos o None si error
    """
    symbols = mt5.symbols_get()
    
    if symbols is None:
        print("❌ No se pudieron obtener símbolos")
        return None
    
    print(f"\n📋 Símbolos disponibles: {len(symbols)}")
    
    # Mostrar primeros 10 símbolos
    print("\n🔝 Top 10 símbolos:")
    for i, symbol in enumerate(symbols[:10]):
        print(f"   {i+1}. {symbol.name} - {symbol.description}")
    
    return [s.name for s in symbols]

def verificar_simbolo(symbol):
    """
    Verifica si un símbolo específico está disponible.
    
    Args:
        symbol (str): Nombre del símbolo (ej: "EURUSD")
    
    Returns:
        bool: True si está disponible, False si no
    """
    symbol_info = mt5.symbol_info(symbol)
    
    if symbol_info is None:
        print(f"❌ Símbolo {symbol} no encontrado")
        return False
    
    # Si no está visible, hacerlo visible
    if not symbol_info.visible:
        print(f"⚠️  Símbolo {symbol} no visible. Activando...")
        if not mt5.symbol_select(symbol, True):
            print(f"❌ Error al activar {symbol}")
            return False
    
    print(f"✅ Símbolo {symbol} disponible")
    print(f"   Spread: {symbol_info.spread} puntos")
    print(f"   Dígitos: {symbol_info.digits}")
    print(f"   Tamaño de lote: {symbol_info.volume_min} - {symbol_info.volume_max}")
    
    return True

def desconectar_mt5():
    """
    Cierra la conexión con MT5 de manera segura.
    """
    mt5.shutdown()
    print("\n👋 Desconectado de MT5")

# ═══════════════════════════════════════════════════════════
# 🧪 PRUEBA DE CONEXIÓN
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Conectar
    if conectar_mt5():
        
        # Obtener símbolos
        simbolos = obtener_simbolos_disponibles()
        
        # Verificar símbolo específico
        verificar_simbolo("EURUSD")
        verificar_simbolo("XAUUSD")  # Gold
        
        # Desconectar
        desconectar_mt5()
    else:
        print("\n❌ No se pudo establecer conexión con MT5")
        print("💡 Verifica que MT5 esté abierto y conectado")
```

---

**Paso 4.2 - Ejecutar el Script:**

**Si usas archivo .py:**
```bash
python mt5_connection.py
```

**Si usas Jupyter:**
- Copia el código en una celda
- Shift + Enter

**✅ Deberías ver:**
```
🔄 Conectando con MetaTrader 5...
✅ Conexión establecida con MT5

============================================================
📊 INFORMACIÓN DE CUENTA
============================================================
Servidor: AvaTradeDemo-MT5
Número de cuenta: 123456789
Compañía: AvaTrade
Moneda: USD
Balance: $100,000.00
Equity: $100,000.00
Margen libre: $100,000.00
Nivel de margen: 0.00%
============================================================

📋 Símbolos disponibles: 250

🔝 Top 10 símbolos:
   1. EURUSD - Euro vs US Dollar
   2. GBPUSD - British Pound vs US Dollar
   3. USDJPY - US Dollar vs Japanese Yen
   ...

✅ Símbolo EURUSD disponible
   Spread: 15 puntos
   Dígitos: 5
   Tamaño de lote: 0.01 - 500.0

✅ Símbolo XAUUSD disponible
   Spread: 30 puntos
   Dígitos: 2
   Tamaño de lote: 0.01 - 100.0

👋 Desconectado de MT5
```

---

**Paso 4.3 - Obtener Datos Históricos desde Python:**

**Código para descargar datos históricos:**

```python
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

# Conectar
mt5.initialize()

# Configurar símbolo y timeframe
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H1  # 1 hora

# Obtener últimas 1000 velas
rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1000)

# Convertir a DataFrame
df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

print(f"📊 Datos descargados: {len(df)} velas")
print(f"\n📋 Primeras 5 filas:")
print(df.head())

print(f"\n📈 Últimas 5 filas:")
print(df.tail())

# Desconectar
mt5.shutdown()
```

**✅ Deberías ver:**
```
📊 Datos descargados: 1000 velas

📋 Primeras 5 filas:
                 time    open    high     low   close  tick_volume  spread
0 2024-10-15 00:00:00  1.0850  1.0855  1.0848  1.0852        1250      15
1 2024-10-15 01:00:00  1.0852  1.0858  1.0850  1.0856        1180      15
...

📈 Últimas 5 filas:
                   time    open    high     low   close  tick_volume  spread
995 2024-11-14 19:00:00  1.0542  1.0548  1.0540  1.0545        980      15
...
```

---

### 🔑 Funciones Clave de MetaTrader5

**Tabla de referencia:**

| Función | Para Qué Sirve | Ejemplo |
|---------|----------------|---------|
| `mt5.initialize()` | Conectar con MT5 | `mt5.initialize()` |
| `mt5.shutdown()` | Desconectar | `mt5.shutdown()` |
| `mt5.account_info()` | Info de cuenta | `info = mt5.account_info()` |
| `mt5.symbols_get()` | Lista símbolos | `symbols = mt5.symbols_get()` |
| `mt5.symbol_info()` | Info de símbolo | `info = mt5.symbol_info("EURUSD")` |
| `mt5.copy_rates_from_pos()` | Datos históricos | `rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_H1, 0, 100)` |
| `mt5.order_send()` | Enviar orden | (veremos en Paso 5) |
| `mt5.positions_get()` | Obtener posiciones abiertas | `positions = mt5.positions_get()` |

---

### ✅ Checkpoint de Validación - Paso 4

Antes de continuar, verifica:

- [ ] Ejecutaste mt5_connection.py sin errores
- [ ] Viste información de tu cuenta
- [ ] Viste lista de símbolos disponibles
- [ ] Verificaste símbolos (EURUSD, XAUUSD)
- [ ] Descargaste datos históricos con copy_rates_from_pos()
- [ ] Convertiste datos a DataFrame de pandas

**Si marcaste todos ✅ → Continúa al Paso 5**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 4](#error-paso-4-python-no-se-conecta-a-mt5)**

---

## PASO 5: EJECUTAR PRIMERA OPERACIÓN DESDE PYTHON (15 min)

### 🎯 Objetivo del Paso
Enviar tu primera orden de trading a MT5 usando Python (en cuenta demo, sin riesgo).

---

### 📍 ¿Cómo Funcionan las Órdenes en MT5?

**💡 Analogía del Trader:**

> Enviar una orden desde Python es como **usar un asistente de voz para operar**:
>
> - Tú (Python) dices: "Compra 0.01 lotes de EURUSD"
> - El asistente (MT5) ejecuta la orden al mercado
> - Recibes confirmación de la operación

---

### 🚀 Acción: Enviar Primera Orden

**Paso 5.1 - Entender la Estructura de una Orden:**

**En MT5, una orden requiere:**

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `action` | Tipo de acción | `mt5.TRADE_ACTION_DEAL` (orden inmediata) |
| `symbol` | Símbolo a operar | `"EURUSD"` |
| `volume` | Tamaño de lote | `0.01` (micro lote) |
| `type` | Compra o venta | `mt5.ORDER_TYPE_BUY` o `SELL` |
| `price` | Precio (si limit/stop) | `1.0850` |
| `deviation` | Deslizamiento permitido | `20` (20 puntos) |
| `magic` | Número mágico (ID) | `234000` |
| `comment` | Comentario | `"Python order"` |
| `type_time` | Tiempo de orden | `mt5.ORDER_TIME_GTC` (hasta cancelar) |
| `type_filling` | Tipo de relleno | `mt5.ORDER_FILLING_IOC` |

---

**Paso 5.2 - Script para Enviar Orden de Compra:**

```python
# ═══════════════════════════════════════════════════════════
# 🛒 PRIMERA ORDEN DESDE PYTHON
# ═══════════════════════════════════════════════════════════

import MetaTrader5 as mt5

# Conectar
if not mt5.initialize():
    print("❌ Error al inicializar MT5")
    quit()

print("✅ Conectado con MT5\n")

# Configuración de la orden
symbol = "EURUSD"
lot = 0.01  # Micro lote (1,000 unidades)

# Verificar que el símbolo esté disponible
if not mt5.symbol_info(symbol).visible:
    mt5.symbol_select(symbol, True)

# Obtener precio actual
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(f"❌ No se pudo obtener info de {symbol}")
    mt5.shutdown()
    quit()

# Precio de compra (ASK)
price = mt5.symbol_info_tick(symbol).ask

print(f"📊 Información de orden:")
print(f"   Símbolo: {symbol}")
print(f"   Acción: COMPRA (BUY)")
print(f"   Tamaño: {lot} lotes")
print(f"   Precio actual (ASK): {price:.5f}")

# Preparar request de orden
request = {
    "action": mt5.TRADE_ACTION_DEAL,  # Orden inmediata
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,  # COMPRA
    "price": price,
    "deviation": 20,  # Deslizamiento máximo de 20 puntos
    "magic": 234000,  # Número mágico
    "comment": "Orden desde Python",
    "type_time": mt5.ORDER_TIME_GTC,  # Válida hasta cancelar
    "type_filling": mt5.ORDER_FILLING_IOC,  # Fill or Kill
}

# Enviar orden
print("\n🚀 Enviando orden al mercado...")
result = mt5.order_send(request)

# Verificar resultado
print("\n" + "="*60)
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("❌ ORDEN RECHAZADA")
    print(f"   Código de error: {result.retcode}")
    print(f"   Descripción: {result.comment}")
else:
    print("✅ ORDEN EJECUTADA CON ÉXITO")
    print(f"   Ticket: {result.order}")
    print(f"   Volumen: {result.volume}")
    print(f"   Precio: {result.price:.5f}")
    print(f"   Bid: {result.bid:.5f}")
    print(f"   Ask: {result.ask:.5f}")
print("="*60)

# Mostrar posiciones abiertas
print("\n📊 Posiciones abiertas:")
positions = mt5.positions_get(symbol=symbol)

if positions is None or len(positions) == 0:
    print("   No hay posiciones abiertas")
else:
    for pos in positions:
        print(f"   Ticket: {pos.ticket}")
        print(f"   Tipo: {'COMPRA' if pos.type == 0 else 'VENTA'}")
        print(f"   Volumen: {pos.volume}")
        print(f"   Precio de apertura: {pos.price_open:.5f}")
        print(f"   Ganancia/Pérdida: ${pos.profit:.2f}")
        print()

# Desconectar
mt5.shutdown()
```

---

**Paso 5.3 - Ejecutar el Script:**

**⚠️ ANTES DE EJECUTAR:**
- Asegúrate que MT5 esté abierto
- Estás en cuenta DEMO (no live)
- Tienes balance suficiente

**Ejecuta:**
```bash
python primera_orden.py
```

**✅ Si todo sale bien:**
```
✅ Conectado con MT5

📊 Información de orden:
   Símbolo: EURUSD
   Acción: COMPRA (BUY)
   Tamaño: 0.01 lotes
   Precio actual (ASK): 1.05426

🚀 Enviando orden al mercado...

============================================================
✅ ORDEN EJECUTADA CON ÉXITO
   Ticket: 987654321
   Volumen: 0.01
   Precio: 1.05426
   Bid: 1.05424
   Ask: 1.05426
============================================================

📊 Posiciones abiertas:
   Ticket: 987654321
   Tipo: COMPRA
   Volumen: 0.01
   Precio de apertura: 1.05426
   Ganancia/Pérdida: $0.05
```

**🎉 ¡Felicitaciones! Enviaste tu primera orden desde Python.**

---

**Paso 5.4 - Cerrar la Posición desde Python:**

**Código para cerrar la posición que acabas de abrir:**

```python
import MetaTrader5 as mt5

# Conectar
mt5.initialize()

symbol = "EURUSD"

# Obtener posiciones abiertas
positions = mt5.positions_get(symbol=symbol)

if positions is None or len(positions) == 0:
    print("❌ No hay posiciones para cerrar")
else:
    # Tomar la primera posición
    position = positions[0]
    
    print(f"📊 Cerrando posición:")
    print(f"   Ticket: {position.ticket}")
    print(f"   Tipo: {'COMPRA' if position.type == 0 else 'VENTA'}")
    print(f"   Volumen: {position.volume}")
    
    # Precio de cierre (opuesto al tipo de posición)
    if position.type == mt5.ORDER_TYPE_BUY:
        price = mt5.symbol_info_tick(symbol).bid  # Cerrar compra con BID
        order_type = mt5.ORDER_TYPE_SELL
    else:
        price = mt5.symbol_info_tick(symbol).ask  # Cerrar venta con ASK
        order_type = mt5.ORDER_TYPE_BUY
    
    # Request de cierre
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": position.volume,
        "type": order_type,
        "position": position.ticket,  # Cerrar esta posición específica
        "price": price,
        "deviation": 20,
        "magic": 234000,
        "comment": "Cierre desde Python",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    # Enviar orden de cierre
    result = mt5.order_send(request)
    
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print("✅ Posición cerrada exitosamente")
        print(f"   Ganancia/Pérdida: ${result.profit:.2f}")
    else:
        print(f"❌ Error al cerrar: {result.comment}")

# Desconectar
mt5.shutdown()
```

**Ejecuta:**
```bash
python cerrar_posicion.py
```

---

### ⚠️ Advertencias Críticas

**1. Siempre usa cuenta DEMO primero:**
- Practica hasta dominar el código
- Solo pasa a live cuando estés 100% seguro

**2. Gestión de riesgo:**
- Usa tamaños pequeños (0.01 lotes al principio)
- Siempre setea Stop Loss y Take Profit
- Nunca arriesgues más del 1-2% de tu capital por operación

**3. Errores comunes:**
- Symbol not found → Activa el símbolo en Market Watch
- Invalid volume → Verifica volume_min del símbolo
- No connection → Asegúrate que MT5 esté abierto

---

### ✅ Checkpoint de Validación - Paso 5

Antes de continuar, verifica:

- [ ] Ejecutaste script de primera orden
- [ ] La orden se ejecutó exitosamente (retcode == DONE)
- [ ] Viste la posición abierta en MT5
- [ ] Ejecutaste script de cierre de posición
- [ ] La posición se cerró correctamente
- [ ] Entiendes estructura de request de orden

**Si marcaste todos ✅ → Continúa al Paso 6**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 5](#error-paso-5-orden-no-se-ejecuta)**

---

## PASO 6: CREAR EXPERT ADVISOR BÁSICO (20 min)

### 🎯 Objetivo del Paso
Crear tu primer Expert Advisor (EA) que opera automáticamente en MT5 usando una estrategia simple.

---

### 📍 ¿Qué es un Expert Advisor?

**💡 Analogía del Trader:**

> Un Expert Advisor es como **un trader robot**:
>
> - **Tú (trader manual)** analizas gráficos y decides cuándo comprar/vender
> - **EA (trader automático)** analiza datos y ejecuta órdenes solo, 24/7
>
> El EA sigue reglas que TÚ defines.

---

### 🚀 Acción: Crear EA Simple (Estrategia SMA Crossover)

**Estrategia que vamos a programar:**

```
ESTRATEGIA: Cruce de Medias Móviles (SMA Crossover)

REGLAS:
- COMPRA cuando: SMA rápida (20) cruza arriba de SMA lenta (50)
- VENTA cuando: SMA rápida (20) cruza abajo de SMA lenta (50)
- Stop Loss: 50 pips
- Take Profit: 100 pips
- Tamaño: 0.01 lotes
```

---

**Paso 6.1 - Código Completo del EA:**

**Crea archivo:** `ea_sma_crossover.py`

```python
# ═══════════════════════════════════════════════════════════
# 🤖 EXPERT ADVISOR: SMA CROSSOVER
# ═══════════════════════════════════════════════════════════
# Estrategia: Cruce de medias móviles
# Autor: Workshop Trading Algorítmico
# Fecha: Noviembre 2025
# ═══════════════════════════════════════════════════════════

import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# CONFIGURACIÓN DE LA ESTRATEGIA
# ═══════════════════════════════════════════════════════════

SYMBOL = "EURUSD"           # Par a operar
TIMEFRAME = mt5.TIMEFRAME_M15  # 15 minutos
LOT_SIZE = 0.01             # Tamaño de posición
STOP_LOSS = 50              # Stop Loss en pips
TAKE_PROFIT = 100           # Take Profit en pips
SMA_FAST = 20               # Período SMA rápida
SMA_SLOW = 50               # Período SMA lenta
MAGIC_NUMBER = 234000       # Identificador único del EA
CHECK_INTERVAL = 60         # Chequear cada 60 segundos

# ═══════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════════

def obtener_datos(symbol, timeframe, n_velas):
    """
    Obtiene datos históricos de MT5.
    
    Args:
        symbol (str): Símbolo
        timeframe: Timeframe de MT5
        n_velas (int): Número de velas
    
    Returns:
        DataFrame: Datos OHLCV
    """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_velas)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def calcular_sma(df, period):
    """
    Calcula Simple Moving Average.
    
    Args:
        df (DataFrame): Datos OHLCV
        period (int): Período de la SMA
    
    Returns:
        Series: SMA
    """
    return df['close'].rolling(window=period).mean()

def hay_posicion_abierta(symbol, magic):
    """
    Verifica si hay posición abierta de este EA.
    
    Args:
        symbol (str): Símbolo
        magic (int): Magic number
    
    Returns:
        bool: True si hay posición
    """
    positions = mt5.positions_get(symbol=symbol)
    
    if positions is None:
        return False
    
    for pos in positions:
        if pos.magic == magic:
            return True
    
    return False

def enviar_orden(symbol, order_type, lot, sl_pips, tp_pips, magic):
    """
    Envía orden al mercado.
    
    Args:
        symbol (str): Símbolo
        order_type: Tipo (BUY/SELL)
        lot (float): Tamaño
        sl_pips (int): Stop Loss en pips
        tp_pips (int): Take Profit en pips
        magic (int): Magic number
    
    Returns:
        bool: True si orden exitosa
    """
    # Obtener info del símbolo
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"❌ No se pudo obtener info de {symbol}")
        return False
    
    # Precio
    if order_type == mt5.ORDER_TYPE_BUY:
        price = mt5.symbol_info_tick(symbol).ask
    else:
        price = mt5.symbol_info_tick(symbol).bid
    
    # Calcular SL y TP
    point = symbol_info.point
    
    if order_type == mt5.ORDER_TYPE_BUY:
        sl = price - sl_pips * point * 10
        tp = price + tp_pips * point * 10
    else:
        sl = price + sl_pips * point * 10
        tp = price - tp_pips * point * 10
    
    # Request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 20,
        "magic": magic,
        "comment": "EA SMA Crossover",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    # Enviar
    result = mt5.order_send(request)
    
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        tipo = "COMPRA" if order_type == mt5.ORDER_TYPE_BUY else "VENTA"
        print(f"✅ {tipo} ejecutada")
        print(f"   Precio: {price:.5f}")
        print(f"   SL: {sl:.5f}")
        print(f"   TP: {tp:.5f}")
        return True
    else:
        print(f"❌ Error: {result.comment}")
        return False

# ═══════════════════════════════════════════════════════════
# LÓGICA PRINCIPAL DEL EA
# ═══════════════════════════════════════════════════════════

def ejecutar_ea():
    """
    Loop principal del Expert Advisor.
    """
    print("="*60)
    print("🤖 EXPERT ADVISOR: SMA CROSSOVER")
    print("="*60)
    print(f"Símbolo: {SYMBOL}")
    print(f"Timeframe: M15")
    print(f"SMA Rápida: {SMA_FAST}")
    print(f"SMA Lenta: {SMA_SLOW}")
    print(f"Tamaño: {LOT_SIZE} lotes")
    print(f"SL: {STOP_LOSS} pips | TP: {TAKE_PROFIT} pips")
    print("="*60)
    
    # Variables para detectar cruces
    ultimo_cruce = None  # 'buy' o 'sell'
    
    while True:
        try:
            # Timestamp
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Obtener datos
            df = obtener_datos(SYMBOL, TIMEFRAME, SMA_SLOW + 10)
            
            # Calcular SMAs
            df['sma_fast'] = calcular_sma(df, SMA_FAST)
            df['sma_slow'] = calcular_sma(df, SMA_SLOW)
            
            # Obtener últimas 2 velas (actual y anterior)
            actual = df.iloc[-1]
            anterior = df.iloc[-2]
            
            # Detectar cruce
            cruce_alcista = (anterior['sma_fast'] <= anterior['sma_slow'] and 
                            actual['sma_fast'] > actual['sma_slow'])
            
            cruce_bajista = (anterior['sma_fast'] >= anterior['sma_slow'] and 
                           actual['sma_fast'] < actual['sma_slow'])
            
            print(f"\n[{ahora}] Chequeando señales...")
            print(f"  SMA Fast: {actual['sma_fast']:.5f}")
            print(f"  SMA Slow: {actual['sma_slow']:.5f}")
            
            # Ejecutar si hay cruce y no hay posición
            if not hay_posicion_abierta(SYMBOL, MAGIC_NUMBER):
                
                if cruce_alcista and ultimo_cruce != 'buy':
                    print("\n🔔 SEÑAL DE COMPRA (Cruce Alcista)")
                    enviar_orden(SYMBOL, mt5.ORDER_TYPE_BUY, LOT_SIZE, 
                               STOP_LOSS, TAKE_PROFIT, MAGIC_NUMBER)
                    ultimo_cruce = 'buy'
                
                elif cruce_bajista and ultimo_cruce != 'sell':
                    print("\n🔔 SEÑAL DE VENTA (Cruce Bajista)")
                    enviar_orden(SYMBOL, mt5.ORDER_TYPE_SELL, LOT_SIZE, 
                               STOP_LOSS, TAKE_PROFIT, MAGIC_NUMBER)
                    ultimo_cruce = 'sell'
                
                else:
                    print("  ⏸️  Sin señales (esperando)")
            
            else:
                print("  📊 Posición abierta (esperando cierre)")
            
            # Esperar antes del próximo chequeo
            time.sleep(CHECK_INTERVAL)
        
        except KeyboardInterrupt:
            print("\n\n⏹️  EA detenido manualmente")
            break
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            time.sleep(CHECK_INTERVAL)

# ═══════════════════════════════════════════════════════════
# INICIO DEL EA
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Conectar MT5
    if not mt5.initialize():
        print("❌ Error al inicializar MT5")
        quit()
    
    # Verificar símbolo
    if not mt5.symbol_info(SYMBOL).visible:
        mt5.symbol_select(SYMBOL, True)
    
    # Ejecutar EA
    try:
        ejecutar_ea()
    except Exception as e:
        print(f"❌ Error crítico: {e}")
    finally:
        # Desconectar
        mt5.shutdown()
        print("\n👋 EA finalizado")
```

---

**Paso 6.2 - Ejecutar el EA:**

**⚠️ IMPORTANTE:**
- Ejecuta en cuenta DEMO primero
- MT5 debe estar abierto
- Observa cómo funciona antes de modificar

**Ejecuta:**
```bash
python ea_sma_crossover.py
```

**✅ Deberías ver:**
```
============================================================
🤖 EXPERT ADVISOR: SMA CROSSOVER
============================================================
Símbolo: EURUSD
Timeframe: M15
SMA Rápida: 20
SMA Lenta: 50
Tamaño: 0.01 lotes
SL: 50 pips | TP: 100 pips
============================================================

[2024-11-15 14:23:45] Chequeando señales...
  SMA Fast: 1.05420
  SMA Slow: 1.05435
  ⏸️  Sin señales (esperando)

[2024-11-15 14:24:45] Chequeando señales...
  SMA Fast: 1.05438
  SMA Slow: 1.05432

🔔 SEÑAL DE COMPRA (Cruce Alcista)
✅ COMPRA ejecutada
   Precio: 1.05440
   SL: 1.05390
   TP: 1.05540

[2024-11-15 14:25:45] Chequeando señales...
  📊 Posición abierta (esperando cierre)
...
```

**El EA está corriendo! 🎉**

**Para detenerlo:** Presiona `Ctrl+C` en el CMD

---

**Paso 6.3 - Personalizar el EA:**

**Puedes modificar fácilmente los parámetros al inicio del código:**

```python
# Cambiar par:
SYMBOL = "GBPUSD"  # En vez de EURUSD

# Cambiar timeframe:
TIMEFRAME = mt5.TIMEFRAME_H1  # 1 hora en vez de 15 min

# Cambiar tamaño:
LOT_SIZE = 0.05  # Más grande (más riesgo)

# Cambiar SMAs:
SMA_FAST = 10
SMA_SLOW = 30

# Cambiar SL/TP:
STOP_LOSS = 30
TAKE_PROFIT = 90
```

---

### ✅ Checkpoint de Validación - Paso 6

Antes de continuar, verifica:

- [ ] Creaste el archivo ea_sma_crossover.py
- [ ] Ejecutaste el EA sin errores
- [ ] El EA está chequeando señales cada 60 segundos
- [ ] Viste el cálculo de SMAs en tiempo real
- [ ] (Opcional) El EA ejecutó una operación
- [ ] Entiendes cómo modificar parámetros

**Si marcaste todos ✅ → Continúa al Paso 7**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 6](#error-paso-6-ea-no-funciona)**

---

## PASO 7: BACKTESTING EN STRATEGY TESTER (15 min)

### 🎯 Objetivo del Paso
Probar tu estrategia con datos históricos para ver cómo habría performado en el pasado.

---

### 📍 ¿Qué es el Backtesting?

**💡 Analogía del Trader:**

> Backtesting es como **una máquina del tiempo para tu estrategia**:
>
> - ¿Cómo habría funcionado tu EA en 2023?
> - ¿Cuántas operaciones habría hecho?
> - ¿Cuánto habría ganado o perdido?
>
> Todo sin arriesgar dinero real.

---

### 🚀 Acción: Backtesting con Python

**Paso 7.1 - Crear Script de Backtesting:**

**Archivo:** `backtest_sma.py`

```python
# ═══════════════════════════════════════════════════════════
# 📈 BACKTESTING: SMA CROSSOVER
# ═══════════════════════════════════════════════════════════

import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt

# Conectar
if not mt5.initialize():
    print("❌ Error al inicializar MT5")
    quit()

# ═══════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════

SYMBOL = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_H1  # 1 hora
SMA_FAST = 20
SMA_SLOW = 50
INITIAL_BALANCE = 10000  # $10,000 iniciales
LOT_SIZE = 0.01
STOP_LOSS = 50  # pips
TAKE_PROFIT = 100  # pips

# ═══════════════════════════════════════════════════════════
# OBTENER DATOS HISTÓRICOS
# ═══════════════════════════════════════════════════════════

print("📥 Descargando datos históricos...")

# Últimos 5000 velas (aproximadamente 7 meses en H1)
rates = mt5.copy_rates_from_pos(SYMBOL, TIMEFRAME, 0, 5000)
df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

print(f"✅ Descargados: {len(df)} velas")
print(f"   Desde: {df['time'].iloc[0]}")
print(f"   Hasta: {df['time'].iloc[-1]}")

# ═══════════════════════════════════════════════════════════
# CALCULAR INDICADORES
# ═══════════════════════════════════════════════════════════

df['sma_fast'] = df['close'].rolling(window=SMA_FAST).mean()
df['sma_slow'] = df['close'].rolling(window=SMA_SLOW).mean()

# ═══════════════════════════════════════════════════════════
# GENERAR SEÑALES
# ═══════════════════════════════════════════════════════════

df['signal'] = 0  # 0 = sin señal, 1 = compra, -1 = venta

# Detectar cruces
for i in range(1, len(df)):
    # Cruce alcista (compra)
    if (df['sma_fast'].iloc[i-1] <= df['sma_slow'].iloc[i-1] and 
        df['sma_fast'].iloc[i] > df['sma_slow'].iloc[i]):
        df.loc[df.index[i], 'signal'] = 1
    
    # Cruce bajista (venta)
    elif (df['sma_fast'].iloc[i-1] >= df['sma_slow'].iloc[i-1] and 
          df['sma_fast'].iloc[i] < df['sma_slow'].iloc[i]):
        df.loc[df.index[i], 'signal'] = -1

# ═══════════════════════════════════════════════════════════
# SIMULAR OPERACIONES
# ═══════════════════════════════════════════════════════════

balance = INITIAL_BALANCE
trades = []
posicion_abierta = None

point = mt5.symbol_info(SYMBOL).point

for i in range(SMA_SLOW, len(df)):
    
    # Si hay señal y NO hay posición abierta
    if df['signal'].iloc[i] != 0 and posicion_abierta is None:
        
        # Abrir posición
        tipo = "BUY" if df['signal'].iloc[i] == 1 else "SELL"
        precio_entrada = df['close'].iloc[i]
        
        if tipo == "BUY":
            sl = precio_entrada - STOP_LOSS * point * 10
            tp = precio_entrada + TAKE_PROFIT * point * 10
        else:
            sl = precio_entrada + STOP_LOSS * point * 10
            tp = precio_entrada - TAKE_PROFIT * point * 10
        
        posicion_abierta = {
            'tipo': tipo,
            'precio_entrada': precio_entrada,
            'sl': sl,
            'tp': tp,
            'time_entrada': df['time'].iloc[i]
        }
    
    # Si hay posición abierta, verificar SL/TP
    elif posicion_abierta is not None:
        
        precio_actual = df['close'].iloc[i]
        cerrar = False
        resultado = ""
        
        # Verificar Stop Loss
        if posicion_abierta['tipo'] == "BUY":
            if df['low'].iloc[i] <= posicion_abierta['sl']:
                precio_cierre = posicion_abierta['sl']
                cerrar = True
                resultado = "SL"
            elif df['high'].iloc[i] >= posicion_abierta['tp']:
                precio_cierre = posicion_abierta['tp']
                cerrar = True
                resultado = "TP"
        else:  # SELL
            if df['high'].iloc[i] >= posicion_abierta['sl']:
                precio_cierre = posicion_abierta['sl']
                cerrar = True
                resultado = "SL"
            elif df['low'].iloc[i] <= posicion_abierta['tp']:
                precio_cierre = posicion_abierta['tp']
                cerrar = True
                resultado = "TP"
        
        # Cerrar posición si se alcanzó SL o TP
        if cerrar:
            if posicion_abierta['tipo'] == "BUY":
                profit = (precio_cierre - posicion_abierta['precio_entrada']) * 100000 * LOT_SIZE
            else:
                profit = (posicion_abierta['precio_entrada'] - precio_cierre) * 100000 * LOT_SIZE
            
            balance += profit
            
            trades.append({
                'time_entrada': posicion_abierta['time_entrada'],
                'time_salida': df['time'].iloc[i],
                'tipo': posicion_abierta['tipo'],
                'precio_entrada': posicion_abierta['precio_entrada'],
                'precio_salida': precio_cierre,
                'profit': profit,
                'balance': balance,
                'resultado': resultado
            })
            
            posicion_abierta = None

# ═══════════════════════════════════════════════════════════
# RESULTADOS
# ═══════════════════════════════════════════════════════════

trades_df = pd.DataFrame(trades)

print("\n" + "="*60)
print("📊 RESULTADOS DEL BACKTESTING")
print("="*60)

if len(trades_df) > 0:
    ganadores = trades_df[trades_df['profit'] > 0]
    perdedores = trades_df[trades_df['profit'] < 0]
    
    print(f"\n💼 General:")
    print(f"   Balance inicial: ${INITIAL_BALANCE:,.2f}")
    print(f"   Balance final: ${balance:,.2f}")
    print(f"   Ganancia/Pérdida: ${balance - INITIAL_BALANCE:,.2f}")
    print(f"   Retorno: {((balance / INITIAL_BALANCE - 1) * 100):.2f}%")
    
    print(f"\n📈 Operaciones:")
    print(f"   Total: {len(trades_df)}")
    print(f"   Ganadoras: {len(ganadores)} ({len(ganadores)/len(trades_df)*100:.1f}%)")
    print(f"   Perdedoras: {len(perdedores)} ({len(perdedores)/len(trades_df)*100:.1f}%)")
    
    print(f"\n💰 Rentabilidad:")
    print(f"   Ganancia promedio: ${ganadores['profit'].mean():.2f}")
    print(f"   Pérdida promedio: ${perdedores['profit'].mean():.2f}")
    print(f"   Mayor ganancia: ${trades_df['profit'].max():.2f}")
    print(f"   Mayor pérdida: ${trades_df['profit'].min():.2f}")
    
    # Calcular Drawdown
    trades_df['peak'] = trades_df['balance'].cummax()
    trades_df['drawdown'] = trades_df['balance'] - trades_df['peak']
    max_dd = trades_df['drawdown'].min()
    
    print(f"\n⚠️  Riesgo:")
    print(f"   Drawdown máximo: ${abs(max_dd):,.2f} ({abs(max_dd)/INITIAL_BALANCE*100:.2f}%)")
    
    # Calcular Sharpe Ratio (simplificado)
    retornos = trades_df['profit'] / INITIAL_BALANCE
    sharpe = retornos.mean() / retornos.std() * (252 ** 0.5) if retornos.std() > 0 else 0
    
    print(f"   Sharpe Ratio: {sharpe:.2f}")
    
    print("\n" + "="*60)
    
    # Graficar curva de equity
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 1, 1)
    plt.plot(trades_df['time_salida'], trades_df['balance'], linewidth=2)
    plt.title('Curva de Equity', fontsize=14, fontweight='bold')
    plt.ylabel('Balance ($)')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.bar(trades_df['time_salida'], trades_df['profit'], 
           color=['green' if p > 0 else 'red' for p in trades_df['profit']])
    plt.title('Ganancia/Pérdida por Operación', fontsize=14, fontweight='bold')
    plt.ylabel('Profit ($)')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('backtest_results.png', dpi=300, bbox_inches='tight')
    print("\n📊 Gráfico guardado como: backtest_results.png")
    plt.show()
    
else:
    print("\n❌ No se generaron operaciones en el backtest")
    print("   Verifica los parámetros de la estrategia")

# Desconectar
mt5.shutdown()
```

---

**Paso 7.2 - Ejecutar el Backtesting:**

```bash
python backtest_sma.py
```

**✅ Deberías ver:**
```
📥 Descargando datos históricos...
✅ Descargados: 5000 velas
   Desde: 2024-04-15 00:00:00
   Hasta: 2024-11-15 14:00:00

============================================================
📊 RESULTADOS DEL BACKTESTING
============================================================

💼 General:
   Balance inicial: $10,000.00
   Balance final: $10,450.00
   Ganancia/Pérdida: $450.00
   Retorno: 4.50%

📈 Operaciones:
   Total: 45
   Ganadoras: 25 (55.6%)
   Perdedoras: 20 (44.4%)

💰 Rentabilidad:
   Ganancia promedio: $32.50
   Pérdida promedio: -$15.80
   Mayor ganancia: $98.50
   Mayor pérdida: -$49.20

⚠️  Riesgo:
   Drawdown máximo: $320.00 (3.20%)
   Sharpe Ratio: 0.85

============================================================

📊 Gráfico guardado como: backtest_results.png
```

**Y se generará un gráfico mostrando:**
- Curva de equity (balance a lo largo del tiempo)
- Ganancias/pérdidas por operación

---

### 🔍 Interpretando los Resultados

| Métrica | Qué Significa | Valor Bueno |
|---------|---------------|-------------|
| **Retorno** | % ganado/perdido | >10% anual |
| **Win Rate** | % operaciones ganadoras | >50% |
| **Ganancia promedio** | $ promedio por operación ganadora | >2x pérdida promedio |
| **Drawdown máximo** | Peor racha de pérdidas | <20% |
| **Sharpe Ratio** | Retorno ajustado por riesgo | >1.0 |

**💡 Reglas de Oro del Backtesting:**

1. **Nunca confíes en UN solo backtest**
   - Prueba en diferentes períodos
   - Prueba en diferentes símbolos
   
2. **Overfitting es el enemigo**
   - No ajustes parámetros hasta que "funcione perfecto"
   - Menos parámetros = mejor
   
3. **Walk-forward testing**
   - Backtest en 70% de datos
   - Valida en 30% restante (out-of-sample)
   
4. **Paper trading ANTES de live**
   - Aunque el backtest sea excelente
   - Prueba 1-3 meses en demo primero

---

### ✅ Checkpoint de Validación - Paso 7

Antes de finalizar, verifica:

- [ ] Ejecutaste backtest_sma.py sin errores
- [ ] Viste resultados del backtesting
- [ ] Se generaron operaciones (>10)
- [ ] Entiendes las métricas (Retorno, Win Rate, DD)
- [ ] Se creó el gráfico backtest_results.png
- [ ] Sabes cómo modificar parámetros para re-testear

**Si marcaste todos ✅:**  
🎉 **¡FELICIDADES! Has completado el Setup C al 100%**

---

## 📊 DIFERENCIAS: PYTHON VS MQL5 EN MT5

### Comparativa Técnica

| Aspecto | Python + MT5 | MQL5 Nativo |
|---------|--------------|-------------|
| **Setup inicial** | ⚠️ Requiere instalar Python | ✅ Integrado en MT5 |
| **Sintaxis** | ✅ Python estándar | ⚠️ Lenguaje específico |
| **Librerías** | ✅ Acceso a todo Python (pandas, sklearn, etc.) | ⚠️ Limitadas |
| **Speed** | ⚠️ Más lento (suficiente para mayoría) | ✅ Máxima velocidad |
| **Depuración** | ✅ Fácil (print, debugger Python) | ⚠️ Más complejo |
| **Portabilidad** | ✅ Código portable | ❌ Solo MT5 |
| **Integración IA** | ✅ Trivial (APIs, Claude, ChatGPT) | ❌ Muy difícil |
| **Backtesting** | ⚠️ Manual (como en Paso 7) | ✅ Strategy Tester nativo |
| **Optimización** | ⚠️ Manual | ✅ Automática en Tester |
| **Deploy 24/7** | ✅ Fácil (script Python) | ✅ Fácil (EA en MT5) |

---

### Cuándo Usar Cada Opción

**Usa Python + MT5 cuando:**
- 🐍 Ya sabes Python (del workshop)
- 🤖 Quieres usar IA Generativa (Claude, ChatGPT)
- 📊 Necesitas análisis avanzado (pandas, sklearn)
- 🔄 Quieres código portable a otras plataformas
- 🧪 Estás prototipando estrategias nuevas

**Usa MQL5 nativo cuando:**
- ⚡ Necesitas máxima velocidad (HFT, scalping)
- 🔧 Quieres usar Strategy Tester nativo
- 📈 Vas a compartir/vender EAs públicamente
- 🏆 Buscas optimización automática de parámetros

**💡 Mejor Práctica:**

> Desarrolla en **Python** (rápido, flexible).
> 
> Si la estrategia funciona, considera **portar a MQL5** para producción ultra-rápida.

---

## 🎯 MEJORES PRÁCTICAS MT5 + PYTHON

### 1. Gestión de Conexión

```python
# ✅ BUENA PRÁCTICA: Verificar conexión antes de operar
import MetaTrader5 as mt5

def safe_initialize():
    if not mt5.initialize():
        print(f"❌ Error: {mt5.last_error()}")
        return False
    
    # Verificar que estamos conectados
    if mt5.account_info() is None:
        print("❌ No hay cuenta conectada")
        mt5.shutdown()
        return False
    
    return True

# Usar en todos los scripts
if safe_initialize():
    # Tu código aquí
    pass
else:
    quit()
```

---

### 2. Manejo de Errores

```python
# ✅ BUENA PRÁCTICA: Try-except en operaciones críticas

try:
    # Intentar enviar orden
    result = mt5.order_send(request)
    
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print("✅ Orden exitosa")
    else:
        print(f"⚠️  Orden rechazada: {result.comment}")
        # Log del error para análisis
        log_error(result)

except Exception as e:
    print(f"❌ Error crítico: {e}")
    # Notificar (email, Telegram)
    send_alert(f"Error en EA: {e}")
```

---

### 3. Logging Profesional

```python
# ✅ BUENA PRÁCTICA: Log de todas las operaciones

import logging
from datetime import datetime

# Configurar logger
logging.basicConfig(
    filename=f'ea_log_{datetime.now().strftime("%Y%m%d")}.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Usar en el EA
logging.info("EA iniciado")
logging.info(f"Señal de COMPRA en {symbol} a {price}")
logging.error(f"Orden rechazada: {error}")
```

---

### 4. Verificación de Símbolos

```python
# ✅ BUENA PRÁCTICA: Siempre verificar símbolo antes de operar

def setup_symbol(symbol):
    """Asegura que el símbolo esté listo para operar."""
    
    # Verificar que existe
    info = mt5.symbol_info(symbol)
    if info is None:
        print(f"❌ {symbol} no existe")
        return False
    
    # Hacerlo visible si no lo está
    if not info.visible:
        if not mt5.symbol_select(symbol, True):
            print(f"❌ No se pudo activar {symbol}")
            return False
    
    return True

# Usar antes de operar
if setup_symbol("EURUSD"):
    # Operar
    pass
```

---

### 5. Gestión de Posiciones

```python
# ✅ BUENA PRÁCTICA: Verificar posiciones antes de abrir nuevas

def max_positions_reached(max_positions=3):
    """Verifica que no tengamos demasiadas posiciones."""
    positions = mt5.positions_total()
    return positions >= max_positions

# Usar en el EA
if not max_positions_reached():
    # Abrir nueva posición
    send_order()
else:
    print("⚠️  Máximo de posiciones alcanzado")
```

---

## 🔧 TROUBLESHOOTING POR PASO

### Error Paso 1: MT5 No Se Instala

**Síntoma:** Instalador falla o MT5 no abre

**Soluciones:**

**Solución 1 - Verificar requisitos:**
- Windows 7 o superior
- .NET Framework 4.5+
- Mínimo 2GB RAM

**Solución 2 - Descargar versión alternativa:**
- Descarga directamente del broker (AvaTrade, XM)

**Solución 3 - Ejecutar como administrador:**
- Click derecho en instalador → "Ejecutar como administrador"

---

### Error Paso 2: No Puedo Conectar MT5 a AvaTrade

**Síntoma:** Error "Invalid account" o "Connection failed"

**Soluciones:**

**Solución 1 - Verificar credenciales:**
- Login correcto (número, no email)
- Password exacto (case-sensitive)
- Server correcto (buscar "AvaTrade" en lista)

**Solución 2 - Firewall:**
- Permitir MT5 en Firewall de Windows
- Verificar antivirus no bloquea MT5

**Solución 3 - Cuenta expirada:**
- Cuentas demo expiran en 30 días
- Crear cuenta demo nueva

---

### Error Paso 3: Librería MT5 No Se Instala

**Síntoma:** `pip install MetaTrader5` falla

**Soluciones:**

**Solución 1 - Actualizar pip:**
```bash
python -m pip install --upgrade pip
pip install MetaTrader5
```

**Solución 2 - Instalar con --user:**
```bash
pip install --user MetaTrader5
```

**Solución 3 - Verificar Python 64-bit:**
- MT5 library requiere Python 64-bit
- Verifica: `python -c "import platform; print(platform.architecture())"`
- Debe decir: `('64bit', ...)`

---

### Error Paso 4: Python No Se Conecta a MT5

**Síntoma:** `mt5.initialize()` retorna False

**Soluciones:**

**Solución 1 - MT5 debe estar abierto:**
- Abre MT5 ANTES de ejecutar Python
- MT5 debe estar conectado a broker

**Solución 2 - Habilitar DLL:**
- MT5 → Tools → Options → Expert Advisors
- ☑ Allow DLL imports
- ☑ Allow automated trading

**Solución 3 - Cerrar otras instancias:**
- Solo UNA instancia de Python puede conectarse a MT5
- Cierra otros scripts corriendo

---

### Error Paso 5: Orden No Se Ejecuta

**Síntoma:** `result.retcode != TRADE_RETCODE_DONE`

**Soluciones:**

**Error: "Invalid volume"**
```python
# Verificar volumen mínimo del símbolo
info = mt5.symbol_info("EURUSD")
print(f"Volumen mín: {info.volume_min}")
print(f"Volumen máx: {info.volume_max}")
print(f"Volumen step: {info.volume_step}")
```

**Error: "Market is closed"**
- Forex cierra viernes tarde y abre domingo tarde
- Verifica horario de mercado

**Error: "Not enough money"**
- Balance insuficiente
- Reducir lot size

**Error: "Invalid stops"**
- SL/TP demasiado cerca del precio
- Verificar stop level mínimo: `symbol_info.trade_stops_level`

---

### Error Paso 6: EA No Funciona

**Síntoma:** EA no genera señales o no opera

**Soluciones:**

**Solución 1 - Verificar datos:**
```python
# Agregar debug
print(f"Velas descargadas: {len(df)}")
print(f"SMA Fast actual: {df['sma_fast'].iloc[-1]}")
print(f"SMA Slow actual: {df['sma_slow'].iloc[-1]}")
```

**Solución 2 - Reducir timeframe:**
- Usar M15 en vez de H1 para ver resultados más rápido

**Solución 3 - Verificar cruces:**
```python
# Agregar más debug
print(f"Anterior Fast: {anterior['sma_fast']:.5f}")
print(f"Anterior Slow: {anterior['sma_slow']:.5f}")
print(f"Actual Fast: {actual['sma_fast']:.5f}")
print(f"Actual Slow: {actual['sma_slow']:.5f}")
print(f"Cruce alcista: {cruce_alcista}")
print(f"Cruce bajista: {cruce_bajista}")
```

---

## 🎯 PRÓXIMOS PASOS

### ✅ Has Completado el Setup C

**¡Felicitaciones! Ahora tienes:**

✅ MetaTrader 5 instalado  
✅ Cuenta demo en AvaTrade  
✅ Python conectado a MT5  
✅ Capacidad de enviar órdenes desde Python  
✅ Tu primer Expert Advisor funcionando  
✅ Herramientas de backtesting  
✅ Ambiente completo para trading automatizado en MT5

---

### 🚀 Mejoras para Tu EA

**1. Agregar más indicadores:**
- RSI para filtrar sobr ecompra/sobreventa
- MACD para confirmar tendencia
- ATR para SL/TP dinámicos

**2. Mejor gestión de riesgo:**
- Position sizing basado en balance
- Multiple timeframe analysis
- Trailing stop loss

**3. Notificaciones:**
- Email cuando se abre/cierra operación
- Telegram bot para alertas
- Dashboard web para monitoreo

**4. Optimización:**
- Grid search de parámetros
- Walk-forward optimization
- Monte Carlo simulation

---

### 📚 Recursos Complementarios

**Documentación oficial:**
- MT5 Python: https://www.mql5.com/en/docs/python_metatrader5
- MQL5 Reference: https://www.mql5.com/en/docs

**Videos recomendados (español):**
- [MT5 + Python Tutorial](https://www.youtube.com/watch?v=9k7yb7X8P9w) (2h)
- [Expert Advisors con Python](https://www.youtube.com/watch?v=K3hYbH5KgHU) (1.5h)

---

## 🧭 NAVEGACIÓN

**🏠 Inicio:** [README Principal](../README.md)  
**⬅️ Anterior:** [Setup B - Python Local](Setup_B_Python_Local.md)  
**➡️ Siguiente:** [Programa del Workshop](Programa_Detallado_Workshop.md)  
**⬆️ Categoría:** [Guía de Uso](GUIA_INICIO.md)

---

## 📞 SOPORTE Y CONTACTO

### 🆘 Si Necesitas Ayuda

**Antes de contactar:**

1. ✅ Revisa el [Troubleshooting](#-troubleshooting-por-paso)
2. ✅ Verifica que MT5 esté abierto y conectado
3. ✅ Asegúrate de estar en cuenta DEMO
4. ✅ Busca error en Google (muchos ya resueltos)

**Si el problema persiste:**

### 📧 Email

**Asunto:** `[Setup C - MT5] - [Tu problema]`

**Email:** yismaryme@gmail.com

**Tiempo de respuesta:** 24-48 horas

**Incluye:**
1. Descripción del problema
2. Paso que estabas siguiendo
3. Screenshot del error (si aplica)
4. Versión de MT5 y Python
5. Qué soluciones ya probaste

---

### 💬 Telegram

**Para:** Consultas rápidas

**Usuario:** [@yismafx](https://t.me/yismafx)

**Horarios:**
- Lunes a Viernes: 9:00 AM - 6:00 PM (GMT-3)

---

## ❓ FAQ - Preguntas Frecuentes

**P: ¿Funciona con MT4?**  
R: No. Esta guía es específica para MT5. MT4 usa librería diferente.

**P: ¿Puedo usar otro broker que no sea AvaTrade?**  
R: Sí, cualquier broker que soporte MT5. El proceso es similar.

**P: ¿El EA corre si cierro Python?**  
R: No. Python debe estar corriendo para que el EA funcione.

**P: ¿Funciona en Mac o Linux?**  
R: MT5 es solo Windows. En Mac/Linux necesitas Wine o VM.

**P: ¿Cuánto capital necesito para empezar?**  
R: Primero practica en DEMO (gratis). Para live, mínimo $500-1000 USD.

**P: ¿Es mejor que usar MQL5?**  
R: Depende. Python es más fácil. MQL5 es más rápido. Ver [comparativa](#-diferencias-python-vs-mql5-en-mt5).

**P: ¿Puedo optimizar parámetros automáticamente?**  
R: En Python debes hacerlo manualmente (grid search). MQL5 tiene optimizador integrado.

---

## 📌 VERSIÓN

**v1.0 (Noviembre 2025)** - Setup MT5 + Python  
**Última actualización:** Noviembre 15, 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- **v1.0 (Nov 15, 2025):** Guía inicial Setup C
  - Instalación MetaTrader 5
  - Configuración cuenta demo AvaTrade
  - Integración Python + MT5
  - Envío de órdenes desde Python
  - Creación de Expert Advisor SMA Crossover
  - Backtesting completo
  - Troubleshooting exhaustivo

---

## ⚠️ DISCLAIMER LEGAL

**Material educativo para fines de aprendizaje únicamente.**

❌ **NO constituye asesoría de inversión**  
⚠️ **Trading algorítmico implica riesgo de pérdida de capital**  
📊 **Resultados pasados NO garantizan resultados futuros**  
💰 **Nunca operes con dinero que no puedas perder**

**Recordatorios específicos de Forex:**
- Forex tiene alta volatilidad y apalancamiento
- Puedes perder más de tu inversión inicial con apalancamiento
- El 70-80% de traders retail pierden dinero
- SIEMPRE usa Stop Loss
- NUNCA arriesgues más del 1-2% por operación

**Responsabilidad:**
- Este setup es para aprendizaje y práctica
- Usa SOLO cuenta demo hasta dominar completamente
- No somos responsables de pérdidas en cuenta live
- Consulta con asesor financiero certificado antes de operar real

---

**🎉 ¡Felicitaciones por completar el Setup C!**

**Ahora dominas MetaTrader 5 + Python. Puedes automatizar tus estrategias de Forex/CFDs profesionalmente.**

**Nos vemos en el workshop. 🚀**

---

[Fin del documento - Setup C MetaTrader 5 v1.0]
