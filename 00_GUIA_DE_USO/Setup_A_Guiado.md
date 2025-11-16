# 📖 SETUP A: GUÍA PASO A PASO COMPLETA

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 📄 Setup Guiado**

---

**⏱️ Tiempo estimado:** 30-60 minutos  
**🎯 Nivel de detalle:** Exhaustivo - Cada paso explicado  
**📅 Última actualización:** Noviembre 2025  
**🎓 Dificultad:** ⭐⭐ (2/5 estrellas)

---

## 🎯 ¿PARA QUIÉN ES ESTA GUÍA?

### ✅ Esta Guía es PERFECTA si:

- 🆕 **Primera vez** con Google Colab o Jupyter notebooks
- 📚 Quieres **entender cada paso** en detalle
- 🧠 Quieres familiarizarte con el entorno antes del workshop
- 🎓 Eres un **aprendiz metódico** que valora la comprensión profunda
- ⚙️ Quieres **configurar TODO correctamente** desde el principio

### ❌ Esta Guía NO es Ideal si:

- ⏱️ Tienes **menos de 30 minutos**  
  → Ve a [Setup A Express](Setup_A_Express.md) - 10-15 min
  
- 🚀 Ya usaste notebooks antes y solo quieres **validar rápido**  
  → Ve a [Setup Colab Rápido](Setup_Colab_Rapido.md) - 10 min

---

## 📑 TABLA DE CONTENIDOS

### 🚀 Quick Links
- [⚡ Mapa de Progreso](#-mapa-de-progreso)
- [🚨 ¿Problemas?](#-troubleshooting-por-paso)
- [📞 Soporte](#-soporte-y-contacto)

### 📖 Pasos Detallados
1. [Paso 1: Acceder a Google Colab](#paso-1-acceder-a-google-colab-5-min)
2. [Paso 2: Crear Tu Notebook Personal](#paso-2-crear-tu-notebook-personal-5-min)
3. [Paso 3: Instalar Librerías de Trading](#paso-3-instalar-librerías-de-trading-10-min)
4. [Paso 4: Configurar Conexión a Broker](#paso-4-configurar-conexión-a-broker-dual-setup-15-30-min)
5. [Paso 5: Descargar Primer Dataset](#paso-5-descargar-primer-dataset-5-min)
6. [Paso 6: Validación Final Completa](#paso-6-validación-final-completa-5-min)

### 🔗 Navegación
- [Integración con Recursos del Workshop](#-integración-con-recursos-del-workshop)
- [Troubleshooting por Paso](#-troubleshooting-por-paso)
- [Próximos Pasos](#-próximos-pasos)

---

## 🗺️ MAPA DE PROGRESO

**Sigue este camino durante el setup:**

```
RUTA GUIADA COMPLETA:

├─ ✅ Paso 1: Acceder a Google Colab (5 min)
├─ ⏳ Paso 2: Crear Notebook Personal (5 min)
├─ ⬜ Paso 3: Instalar Librerías (10 min)
├─ ⬜ Paso 4: Configurar Broker (15-30 min)
├─ ⬜ Paso 5: Descargar Datos (5 min)
└─ ⬜ Paso 6: Validación Final (5 min)

TOTAL: 30-60 minutos
```

---

## PASO 1: ACCEDER A GOOGLE COLAB (5 min)

### 🎯 Objetivo del Paso
Abrir y entender la plataforma donde trabajaremos durante todo el workshop.

---

### 📍 ¿Qué es Google Colab?

**💡 Analogía del Trader:**

> Google Colab es como **TradingView pero para código de trading**.  
> 
> - **TradingView** → Creas gráficos y scripts en la nube  
> - **Google Colab** → Escribes y ejecutas código Python en la nube
>
> **Lo mejor:** No instalas nada, todo funciona en el navegador

**✅ Ventajas para traders:**
- ❌ No instalas Python en tu computadora
- ✅ Funciona en cualquier dispositivo
- ✅ Google te da una "computadora virtual" gratis
- ✅ Tus notebooks se guardan automáticamente en Google Drive

---

### 🚀 Acción: Abre Google Colab

**Paso 1.1 - Accede a Colab:**

1. Abre tu navegador (Chrome recomendado)
2. Ve a: **https://colab.research.google.com**
3. Si te pide login → Usa tu cuenta Gmail
4. Si no tienes Gmail → [Crea una aquí](https://accounts.google.com/signup) (5 min)

**🔍 Verificación Visual:**

✅ **Si tu pantalla se ve así, estás en el lugar correcto:**

[🔲 SCREENSHOT #1 PLACEHOLDER: Interfaz principal de Google Colab]
- Título: "Welcome to Colaboratory" o pantalla principal vacía
- Barra de menú en la parte superior: File, Edit, View, Insert, Runtime, Tools, Help
- Área central blanca para notebooks
- Opción "New Notebook" visible

❌ **Si NO se ve así:**
- Verifica que estás en `colab.research.google.com`
- Cierra otras pestañas de Google y recarga
- Prueba en modo incógnito (Ctrl+Shift+N)

---

### 📹 Recursos de Apoyo

**Para ver paso a paso en video:**  

🎥 **En Español (2024-2025):**
- [Google Colab: Tutorial Completo para Principiantes](https://www.youtube.com/watch?v=HW29067qVWk) (Platzi, 2024, 15 min)
- [Introducción a Google Colab - Tutorial Práctico](https://dialektico.com/google-colab/) (Guía escrita actualizada 2025)
- [Cómo usar Google Colab desde Cero](https://conceptosclaros.com/como-empezar-con-google-colab-y-python/) (Tutorial 2024)

🎥 **En Inglés (Oficial):**
- [Google Colab - Introducción Oficial](https://www.youtube.com/watch?v=inN8seMm7UI) (Google, 10 min)

**💡 Consejo del Instructor:**

> No necesitas ver los videos completos ahora. Úsalos si te atascas o quieres profundizar después.

---

### ✅ Checkpoint de Validación - Paso 1

Antes de continuar, verifica:

- [ ] Estás en `colab.research.google.com`
- [ ] Iniciaste sesión con tu cuenta Gmail
- [ ] Ves la interfaz principal de Colab
- [ ] Puedes ver el menú: File, Edit, View, etc.

**Si marcaste todos ✅ → Continúa al Paso 2**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 1](#error-paso-1-no-puedo-acceder-a-colab)**

---

## PASO 2: CREAR TU NOTEBOOK PERSONAL (5 min)

### 🎯 Objetivo del Paso
Crear tu espacio de trabajo personal para el workshop.

---

### 📍 ¿Qué es un Notebook?

**💡 Analogía del Trader:**

> Un notebook es como tu **diario de trading**, pero interactivo:
>
> - **Diario de trading** → Escribes notas y análisis
> - **Notebook de Colab** → Escribes notas Y ejecutas código
>
> **La magia:** Puedes mezclar texto explicativo con código ejecutable

**Estructura de un Notebook:**

```
Mi_Notebook.ipynb
│
├─ Celda 1: Texto (Markdown)
│   "Hoy voy a descargar datos de SPY"
│
├─ Celda 2: Código (Python)
│   import pandas as pd
│   data = pd.read_csv("SPY.csv")
│
├─ Celda 3: Resultado (Output)
│   [Tabla con datos de SPY]
│
└─ Celda 4: Texto (Markdown)
    "Análisis: El SPY tiene tendencia alcista"
```

---

### 🚀 Acción: Crea Tu Notebook

**Paso 2.1 - Crear Notebook Nuevo:**

1. En la pantalla principal de Colab
2. Click en: **`File`** → **`New notebook`**
3. Se abrirá un notebook en blanco

**🔍 Verificación Visual:**

✅ **Si ves esto, creaste el notebook correctamente:**
- Título en la esquina superior izquierda: "Untitled0.ipynb"
- Una celda de código vacía en el centro
- Barra de herramientas arriba con botones: + Code, + Text

**Paso 2.2 - Renombrar Notebook:**

1. Click en el título "Untitled0.ipynb" (esquina superior izquierda)
2. Cambia el nombre a: **`Setup_y_Practica_Trading`**
3. Presiona Enter

**💡 ¿Por qué este nombre?**
- **Setup** → Indica que es tu entorno de configuración
- **Practica** → Lo usarás para practicar código del workshop
- **Trading** → Recuerda que es para trading algorítmico

**Paso 2.3 - Verificar Guardado Automático:**

Google Colab guarda automáticamente cada pocos segundos.

**🔍 Verificación:**
- Busca el ícono de "nube" en la barra superior
- Si dice "All changes saved" → ✅ Todo correcto
- Si dice "Saving..." → Espera 3 segundos

---

### 📹 Recursos de Apoyo

**Si necesitas ver el proceso:**  
🎥 [Google Colab - Primeros Pasos y Configuración](https://www.youtube.com/watch?v=i6V_GdR3tPE) (Tutorial 2024, 8 min)  
📖 [Guía Completa de Google Colab](https://neoland.es/google-colab/) (Artículo actualizado 2025)

---

### ✅ Checkpoint de Validación - Paso 2

Antes de continuar, verifica:

- [ ] Creaste un notebook nuevo
- [ ] El nombre del notebook es: `Setup_y_Practica_Trading`
- [ ] Ves una celda de código vacía
- [ ] El notebook se guardó automáticamente (ícono de nube)

**Si marcaste todos ✅ → Continúa al Paso 3**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 2](#error-paso-2-no-puedo-crear-el-notebook)**

---

## PASO 3: INSTALAR LIBRERÍAS DE TRADING (10 min)

### 🎯 Objetivo del Paso
Instalar todas las herramientas que usaremos en el workshop.

---

### 📍 ¿Qué son las Librerías?

**💡 Analogía del Trader:**

> Las librerías son como **indicadores técnicos en TradingView**:
>
> - **En TradingView** → Instalas RSI, MACD, Bandas de Bollinger
> - **En Python** → Instalas pandas (para datos), numpy (para cálculos), matplotlib (para gráficos)
>
> **Diferencia:** En TradingView están pre-instalados. En Python, los instalas una vez.

**Las librerías que instalaremos:**

| Librería | Para Qué Sirve | Analogía |
|----------|---------------|----------|
| **alpaca-py** | Conectar con broker Alpaca | Tu "cable de datos" al broker |
| **ib_insync** | Conectar con Interactive Brokers | Tu "cable de datos" a IB |
| **pandas** | Manejar tablas de datos | Excel pero para código |
| **numpy** | Cálculos matemáticos | Calculadora científica |
| **matplotlib** | Crear gráficos | TradingView pero en Python |
| **pandas-ta** | Indicadores técnicos | RSI, MACD, BB automáticos |

---

### 🚀 Acción: Instalar Librerías

**Paso 3.1 - Crear Celda de Instalación:**

1. En tu notebook `Setup_y_Practica_Trading`
2. Asegúrate de estar en una celda de código (no de texto)
3. Si no hay ninguna celda, click en: **`+ Code`** (botón arriba)

**Paso 3.2 - Copiar Código de Instalación:**

Copia y pega este código exacto en la celda:

```python
# ═══════════════════════════════════════════════════════════
# 📦 INSTALACIÓN AUTOMÁTICA v3.5 CORREGIDA
# Workshop: Trading Algorítmico Aumentado con IA Generativa
# ═══════════════════════════════════════════════════════════
# 
# ⚠️ IMPORTANTE: Este código YA ESTÁ ESCRITO
# Tú NO necesitas entender cada línea
# Solo ejecuta y espera
#
# ═══════════════════════════════════════════════════════════

print("🚀 Instalando herramientas de trading automáticamente...")
print("   No necesitas hacer nada más que esperar.\n")
print("⏱️  Tiempo estimado: 2-3 minutos\n")

print("═" * 60)
print("📥 INSTALANDO HERRAMIENTAS")
print("═" * 60)

# Herramienta 1: Descargar datos de mercados
print("\n1/6 Instalando yfinance (descarga de datos)...")
!pip install -q yfinance

# Herramienta 2: Conectar con broker Alpaca
print("2/6 Instalando alpaca-py (broker Alpaca)...")
!pip install -q alpaca-py

# Herramienta 3: Conectar con Interactive Brokers
print("3/6 Instalando ib_insync (broker IB)...")
!pip install -q ib_insync

# Herramienta 4: Análisis técnico automático
print("4/6 Instalando pandas-ta (indicadores técnicos)...")
!pip install -q pandas-ta

# Herramienta 5: Backtesting avanzado
print("5/6 Instalando vectorbt (backtesting)...")
!pip install -q vectorbt

# Herramienta 6: Actualizar dependencias críticas
print("6/6 Actualizando pandas y numpy...")
!pip install -q --upgrade pandas numpy

print("\n" + "═" * 60)
print("✅ INSTALACIÓN COMPLETADA")
print("═" * 60)

# ═══════════════════════════════════════════════════════════
# 🔍 VERIFICACIÓN AUTOMÁTICA
# ═══════════════════════════════════════════════════════════

print("\n🔍 Verificando que todo se instaló correctamente...\n")

import sys
verification_passed = True

# Lista de herramientas a verificar
tools = [
    ("yfinance", "Descarga de datos históricos"),
    ("alpaca", "Conexión con broker Alpaca"),
    ("ib_insync", "Conexión con Interactive Brokers"),
    ("pandas_ta", "Indicadores técnicos automáticos"),
    ("vectorbt", "Backtesting avanzado"),
    ("pandas", "Análisis de datos"),
    ("numpy", "Cálculos matemáticos")
]

for tool_name, description in tools:
    try:
        __import__(tool_name)
        print(f"✅ {tool_name:20} → {description}")
    except ImportError:
        print(f"❌ {tool_name:20} → ERROR en instalación")
        verification_passed = False

print("\n" + "═" * 60)

if verification_passed:
    print("🎉 ¡ÉXITO! Todas las herramientas están listas")
    print("═" * 60)
    print("\n✅ Puedes continuar al Paso 4")
else:
    print("⚠️  ATENCIÓN: Hubo problemas en la instalación")
    print("═" * 60)
    print("\n💡 Solución:")
    print("   1. Runtime → Restart runtime")
    print("   2. Vuelve a ejecutar esta celda")
    print("   3. Si persiste, ve a Troubleshooting")

print("\n" + "═" * 60)
```

**Paso 3.3 - Ejecutar la Instalación:**

1. **Click en el botón ▶️** (play) a la izquierda de la celda
2. **O presiona:** `Shift + Enter`
3. **Espera 2-3 minutos** mientras se instala todo

---

### 🔍 Interpretación de Resultados

**✅ INSTALACIÓN EXITOSA - Verás:**

```
═══════════════════════════════════════════════════════════
📥 INSTALANDO HERRAMIENTAS
═══════════════════════════════════════════════════════════

1/6 Instalando yfinance (descarga de datos)...
2/6 Instalando alpaca-py (broker Alpaca)...
3/6 Instalando ib_insync (broker IB)...
4/6 Instalando pandas-ta (indicadores técnicos)...
5/6 Instalando vectorbt (backtesting)...
6/6 Actualizando pandas y numpy...

═══════════════════════════════════════════════════════════
✅ INSTALACIÓN COMPLETADA
═══════════════════════════════════════════════════════════

🔍 Verificando que todo se instaló correctamente...

✅ yfinance             → Descarga de datos históricos
✅ alpaca               → Conexión con broker Alpaca
✅ ib_insync            → Conexión con Interactive Brokers
✅ pandas_ta            → Indicadores técnicos automáticos
✅ vectorbt             → Backtesting avanzado
✅ pandas               → Análisis de datos
✅ numpy                → Cálculos matemáticos

═══════════════════════════════════════════════════════════
🎉 ¡ÉXITO! Todas las herramientas están listas
═══════════════════════════════════════════════════════════

✅ Puedes continuar al Paso 4
```

**🎊 ¡Perfecto! Continúa al Paso 4**

---

**❌ SI VES ERRORES - Verás:**

```
❌ vectorbt            → ERROR en instalación

⚠️  ATENCIÓN: Hubo problemas en la instalación
═══════════════════════════════════════════════════════════

💡 Solución:
   1. Runtime → Restart runtime
   2. Vuelve a ejecutar esta celda
   3. Si persiste, ve a Troubleshooting
```

→ Ve a [Troubleshooting - Paso 3](#error-paso-3-fallo-en-instalación)

---

### ⚠️ Advertencias Importantes

**1. No cierres la pestaña durante la instalación**
- Espera a ver el mensaje "✅ INSTALACIÓN COMPLETADA"

**2. Es normal ver warnings naranjas**
- Solo preocúpate si ves "ERROR" en rojo

**3. Esta instalación solo se hace UNA vez**
- Si cierras y vuelves a abrir el notebook otro día, RE-ejecuta esta celda
- Toma solo 30 segundos la segunda vez

---

### ✅ Checkpoint de Validación - Paso 3

Antes de continuar, verifica:

- [ ] Ejecutaste la celda de instalación
- [ ] Viste el mensaje: "✅ INSTALACIÓN COMPLETADA"
- [ ] Todas las herramientas muestran ✅ en la verificación
- [ ] Viste el mensaje: "🎉 ¡ÉXITO! Todas las herramientas están listas"

**Si marcaste todos ✅ → Continúa al Paso 4**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 3](#error-paso-3-fallo-en-instalación)**

---

## PASO 4: CONFIGURAR CONEXIÓN A BROKER (Dual Setup) (15-30 min)

### 🎯 Objetivo del Paso
Conectar tu notebook con un broker para poder descargar datos reales y (eventualmente) operar.

---

### 📍 ¿Qué es un Broker en Trading Algorítmico?

**💡 Analogía del Trader:**

> Un broker es tu "intermediario" para acceder a los mercados:
>
> - **Trading Manual** → Entras a la plataforma del broker y clickeas "Buy/Sell"
> - **Trading Algorítmico** → Tu código se conecta al broker vía API y envía órdenes automáticamente
>
> **API = Conector eléctrico** que une tu código con el broker

---

### 🔑 ¿Cuál Broker Debo Usar?

**En este workshop soportamos 2 brokers:**

| Broker | Ventajas | Desventajas | Recomendado Para |
|--------|----------|-------------|------------------|
| **Alpaca** | ✅ Fácil de configurar<br>✅ Paper trading gratis<br>✅ Solo necesitas email | ❌ Solo US stocks<br>❌ No crypto, no forex | Principiantes, prototipos rápidos |
| **Interactive Brokers** | ✅ Todos los mercados<br>✅ Datos de alta calidad<br>✅ Comisiones bajas | ❌ Configuración más compleja<br>❌ Requiere instalar TWS | Traders avanzados, producción |

**💡 Recomendación del Instructor:**

> - **¿Primera vez con trading algorítmico?** → Empieza con **Alpaca**
> - **¿Ya tienes cuenta en IB?** → Usa **Interactive Brokers**
> - **¿Quieres lo mejor de ambos?** → Configura AMBOS (toma 30 min total)

---

### 🚀 RUTA A: Configurar Alpaca (Recomendado) (15 min)

**Ventaja:** Funciona 100% en Google Colab, sin instalar nada localmente.

#### Paso 4A.1 - Crear Cuenta en Alpaca

1. **Ve a:** https://alpaca.markets/
2. **Click en:** "Sign Up" (esquina superior derecha)
3. **Completa el formulario:**
   - Email
   - Contraseña
   - Acepta términos
4. **Verifica tu email** (revisa spam si no llega)

**⏱️ Tiempo:** 3 minutos

#### Paso 4A.2 - Crear API Keys (Paper Trading)

1. **Inicia sesión** en Alpaca
2. **Ve a:** Paper Trading (menú izquierdo)
3. **Click en:** "API Keys" o "Generate New Key"
4. **Nombra tu key:** `Workshop_Trading_Colab`
5. **Click:** "Generate"

**⚠️ CRÍTICO:**
- **Copia INMEDIATAMENTE** tu `API Key` y `Secret Key`
- Solo se muestran UNA vez
- Guárdalas en un lugar seguro (Notepad, Google Keep)

**Verás algo así:**
```
API Key:     PKxxxxxxxxxxxxxxxxxxxxxx
Secret Key:  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**⏱️ Tiempo:** 2 minutos

#### Paso 4A.3 - Configurar Keys en el Notebook

1. **Crea una nueva celda de código** en tu notebook
2. **Copia y pega este código:**

```python
# ═══════════════════════════════════════════════════════════
# 🔑 CONFIGURACIÓN DE ALPACA
# ═══════════════════════════════════════════════════════════
# 
# ⚠️ IMPORTANTE: Reemplaza los valores de abajo con TUS keys
# 
# ═══════════════════════════════════════════════════════════

# 1. Pega TU API Key aquí (entre las comillas)
ALPACA_API_KEY = "PKxxxxxxxxxxxxxxxxxxxxxx"

# 2. Pega TU Secret Key aquí (entre las comillas)
ALPACA_SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 3. Esto indica que usaremos Paper Trading (modo simulación)
ALPACA_PAPER = True

print("═" * 60)
print("🔑 CONFIGURACIÓN DE ALPACA")
print("═" * 60)

# Verificación básica
if ALPACA_API_KEY == "PKxxxxxxxxxxxxxxxxxxxxxx":
    print("❌ ERROR: No reemplazaste tu API Key")
    print("   → Copia tu API Key de Alpaca y pégala arriba")
elif ALPACA_SECRET_KEY == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx":
    print("❌ ERROR: No reemplazaste tu Secret Key")
    print("   → Copia tu Secret Key de Alpaca y pégala arriba")
else:
    print("✅ Keys configuradas correctamente")
    print(f"✅ Modo: {'Paper Trading (Simulación)' if ALPACA_PAPER else 'Live Trading (REAL)'}")
    print("\n💡 Consejo: NUNCA compartas este notebook con las keys dentro")

print("═" * 60)
```

3. **Reemplaza los valores:**
   - Cambia `PKxxxxxxxxxxxxxxxxxxxxxx` por TU API Key
   - Cambia `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` por TU Secret Key

4. **Ejecuta la celda** (Shift + Enter)

**✅ Deberías ver:**
```
✅ Keys configuradas correctamente
✅ Modo: Paper Trading (Simulación)
```

**⏱️ Tiempo:** 2 minutos

#### Paso 4A.4 - Probar la Conexión

1. **Crea otra celda de código**
2. **Copia este código:**

```python
# ═══════════════════════════════════════════════════════════
# 🧪 PRUEBA DE CONEXIÓN CON ALPACA
# ═══════════════════════════════════════════════════════════

print("🔍 Probando conexión con Alpaca...\n")

try:
    from alpaca.trading.client import TradingClient
    
    # Crear cliente de trading
    trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY, paper=ALPACA_PAPER)
    
    # Obtener información de la cuenta
    account = trading_client.get_account()
    
    print("═" * 60)
    print("✅ CONEXIÓN EXITOSA CON ALPACA")
    print("═" * 60)
    
    print(f"\n📊 Información de tu cuenta:")
    print(f"   - Saldo: ${float(account.cash):,.2f} USD")
    print(f"   - Poder de compra: ${float(account.buying_power):,.2f} USD")
    print(f"   - Estado: {account.status}")
    
    print("\n🎉 ¡Todo funciona! Puedes descargar datos y operar (paper trading)")
    print("═" * 60)
    
except Exception as e:
    print("═" * 60)
    print("❌ ERROR EN LA CONEXIÓN")
    print("═" * 60)
    print(f"\nError: {e}")
    print("\n💡 Posibles causas:")
    print("   1. API Key o Secret Key incorrectas")
    print("   2. Keys de Live Trading en vez de Paper Trading")
    print("   3. Cuenta de Alpaca no verificada")
    print("\n→ Ve a Troubleshooting - Alpaca")
```

3. **Ejecuta la celda**

**✅ ÉXITO - Verás:**
```
✅ CONEXIÓN EXITOSA CON ALPACA
═══════════════════════════════════════════════════════════

📊 Información de tu cuenta:
   - Saldo: $100,000.00 USD
   - Poder de compra: $400,000.00 USD
   - Estado: ACTIVE

🎉 ¡Todo funciona! Puedes descargar datos y operar (paper trading)
```

**⏱️ Tiempo:** 2 minutos

---

### ✅ Checkpoint - Configuración Alpaca Completada

- [ ] Creaste cuenta en Alpaca
- [ ] Generaste API Keys (Paper Trading)
- [ ] Configuraste las keys en el notebook
- [ ] La prueba de conexión fue exitosa
- [ ] Viste tu saldo de paper trading ($100,000 USD)

**Si marcaste todos ✅:**
🎉 **¡Excelente! Alpaca está configurado.**

**→ Puedes:**
- **Opción A:** Ir directo al [Paso 5](#paso-5-descargar-primer-dataset-5-min)
- **Opción B:** Configurar también Interactive Brokers (opcional) - continúa abajo

**Si hay algún ❌:**  
→ Ve a [Troubleshooting - Alpaca](#troubleshooting-alpaca)

---

### 🚀 RUTA B: Configurar Interactive Brokers (Avanzado) (15-30 min)

**⚠️ Advertencia:** Esta configuración es más compleja. Solo hazla si:
- Ya tienes cuenta en IB
- Ya usas TWS (Trader Workstation)
- Necesitas operar crypto, forex, o futuros

**Si NO cumples lo anterior → SALTA esta sección y ve al [Paso 5](#paso-5-descargar-primer-dataset-5-min)**

---

#### Paso 4B.1 - Instalar TWS o IB Gateway

**Interactive Brokers requiere tener corriendo localmente:**
- **TWS (Trader Workstation)** - Plataforma completa
- **IB Gateway** - Versión ligera solo para API

**Descarga:**
1. Ve a: https://www.interactivebrokers.com/en/trading/tws.php
2. Descarga TWS o IB Gateway
3. Instala en tu computadora
4. Inicia sesión con tu cuenta IB

**⏱️ Tiempo:** 10-15 minutos (primera vez)

#### Paso 4B.2 - Habilitar API en TWS

1. **Abre TWS o IB Gateway**
2. **Ve a:** `Global Configuration` → `API` → `Settings`
3. **✅ Habilita:** "Enable ActiveX and Socket Clients"
4. **✅ Agrega:** `127.0.0.1` a "Trusted IP addresses"
5. **Puerto:** Deja en 7497 (Paper) o 7496 (Live)
6. **Guarda cambios** y **reinicia TWS**

**⏱️ Tiempo:** 3 minutos

#### Paso 4B.3 - Configurar en el Notebook

1. **Crea una nueva celda de código**
2. **Copia este código:**

```python
# ═══════════════════════════════════════════════════════════
# 🔑 CONFIGURACIÓN DE INTERACTIVE BROKERS
# ═══════════════════════════════════════════════════════════

# Configuración de conexión
IB_HOST = "127.0.0.1"  # Localhost (TWS en tu computadora)
IB_PORT = 7497         # 7497 = Paper Trading, 7496 = Live Trading
IB_CLIENT_ID = 1       # ID único para tu conexión

print("═" * 60)
print("🔑 CONFIGURACIÓN DE INTERACTIVE BROKERS")
print("═" * 60)
print(f"✅ Host: {IB_HOST}")
print(f"✅ Puerto: {IB_PORT} ({'Paper Trading' if IB_PORT == 7497 else 'Live Trading'})")
print(f"✅ Client ID: {IB_CLIENT_ID}")
print("\n⚠️  IMPORTANTE: TWS debe estar corriendo en tu computadora")
print("═" * 60)
```

3. **Ejecuta la celda**

**⏱️ Tiempo:** 1 minuto

#### Paso 4B.4 - Probar la Conexión

**⚠️ ANTES DE CONTINUAR:**
- ✅ TWS o IB Gateway debe estar **ABIERTO**
- ✅ Debes estar **logged in**
- ✅ API debe estar **habilitada** (Paso 4B.2)

1. **Crea una nueva celda**
2. **Copia este código:**

```python
# ═══════════════════════════════════════════════════════════
# 🧪 PRUEBA DE CONEXIÓN CON INTERACTIVE BROKERS
# ═══════════════════════════════════════════════════════════

print("🔍 Probando conexión con Interactive Brokers...\n")

try:
    from ib_insync import IB
    
    # Crear cliente IB
    ib = IB()
    
    # Intentar conectar
    ib.connect(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)
    
    print("═" * 60)
    print("✅ CONEXIÓN EXITOSA CON INTERACTIVE BROKERS")
    print("═" * 60)
    
    # Obtener información de la cuenta
    account_values = ib.accountValues()
    
    # Buscar saldo
    for value in account_values:
        if value.tag == 'NetLiquidation':
            print(f"\n📊 Información de tu cuenta:")
            print(f"   - Saldo: ${float(value.value):,.2f} {value.currency}")
    
    print("\n🎉 ¡Todo funciona! IB está conectado correctamente")
    print("═" * 60)
    
    # Desconectar
    ib.disconnect()
    
except Exception as e:
    print("═" * 60)
    print("❌ ERROR EN LA CONEXIÓN")
    print("═" * 60)
    print(f"\nError: {e}")
    print("\n💡 Posibles causas:")
    print("   1. TWS no está corriendo")
    print("   2. API no habilitada en TWS")
    print("   3. Puerto incorrecto")
    print("   4. Firewall bloqueando conexión")
    print("\n→ Ve a Troubleshooting - Interactive Brokers")
```

3. **Ejecuta la celda**

**✅ ÉXITO - Verás:**
```
✅ CONEXIÓN EXITOSA CON INTERACTIVE BROKERS
═══════════════════════════════════════════════════════════

📊 Información de tu cuenta:
   - Saldo: $1,000,000.00 USD

🎉 ¡Todo funciona! IB está conectado correctamente
```

**⏱️ Tiempo:** 2 minutos

---

### ✅ Checkpoint - Configuración IB Completada

- [ ] TWS o IB Gateway instalado
- [ ] API habilitada en TWS
- [ ] Configuraste host/puerto/clientId en notebook
- [ ] La prueba de conexión fue exitosa
- [ ] Viste la información de tu cuenta

**Si marcaste todos ✅:**
🎉 **¡Perfecto! Interactive Brokers está configurado.**

**→ Continúa al [Paso 5](#paso-5-descargar-primer-dataset-5-min)**

**Si hay algún ❌:**  
→ Ve a [Troubleshooting - Interactive Brokers](#troubleshooting-interactive-brokers)

---

## PASO 5: DESCARGAR PRIMER DATASET (5 min)

### 🎯 Objetivo del Paso
Descargar datos históricos reales de un activo para verificar que todo funciona.

---

### 📍 ¿Por Qué Descargar Datos?

**💡 Analogía del Trader:**

> Descargar datos históricos es como **obtener el historial de precios de un activo**:
>
> - **En TradingView** → Ves el gráfico de precios históricos
> - **En Python** → Descargas los datos en una tabla para analizarlos
>
> **Ventaja:** Puedes hacer cálculos, backtesting, y análisis que TradingView no permite

---

### 🚀 Acción: Descargar Datos de SPY

**Vamos a descargar datos de SPY (S&P 500 ETF) - el activo más líquido del mundo.**

#### Opción A: Usando Alpaca (Si configuraste Alpaca)

1. **Crea una nueva celda de código**
2. **Copia este código:**

```python
# ═══════════════════════════════════════════════════════════
# 📊 DESCARGA DE DATOS HISTÓRICOS - ALPACA
# ═══════════════════════════════════════════════════════════

print("📥 Descargando datos de SPY desde Alpaca...\n")

try:
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    from datetime import datetime, timedelta
    
    # Crear cliente de datos
    data_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
    
    # Configurar request
    request_params = StockBarsRequest(
        symbol_or_symbols="SPY",
        timeframe=TimeFrame.Day,
        start=datetime.now() - timedelta(days=365*5),  # Últimos 5 años
        end=datetime.now()
    )
    
    # Descargar datos
    bars = data_client.get_stock_bars(request_params)
    
    # Convertir a DataFrame
    df = bars.df
    
    print("═" * 60)
    print("✅ DESCARGA COMPLETADA")
    print("═" * 60)
    
    print(f"\n📊 Dataset descargado:")
    print(f"   - Ticker: SPY")
    print(f"   - Filas: {len(df):,}")
    print(f"   - Fecha inicio: {df.index[0]}")
    print(f"   - Fecha fin: {df.index[-1]}")
    
    print(f"\n📋 Primeras 5 filas:")
    print(df.head())
    
    print("\n🎉 ¡Datos listos para análisis!")
    print("═" * 60)
    
except Exception as e:
    print("═" * 60)
    print("❌ ERROR EN LA DESCARGA")
    print("═" * 60)
    print(f"\nError: {e}")
    print("\n→ Ve a Troubleshooting - Descarga de Datos")
```

3. **Ejecuta la celda**

---

#### Opción B: Usando Interactive Brokers (Si configuraste IB)

**⚠️ RECUERDA: TWS debe estar corriendo**

1. **Crea una nueva celda de código**
2. **Copia este código:**

```python
# ═══════════════════════════════════════════════════════════
# 📊 DESCARGA DE DATOS HISTÓRICOS - INTERACTIVE BROKERS
# ═══════════════════════════════════════════════════════════

print("📥 Descargando datos de SPY desde Interactive Brokers...\n")

try:
    from ib_insync import IB, Stock
    import pandas as pd
    
    # Conectar a IB
    ib = IB()
    ib.connect(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)
    
    # Definir el contrato (SPY)
    contract = Stock('SPY', 'SMART', 'USD')
    
    # Descargar datos (últimos 5 años, diarios)
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='5 Y',
        barSizeSetting='1 day',
        whatToShow='TRADES',
        useRTH=True
    )
    
    # Convertir a DataFrame
    df = pd.DataFrame(bars)
    df.set_index('date', inplace=True)
    
    print("═" * 60)
    print("✅ DESCARGA COMPLETADA")
    print("═" * 60)
    
    print(f"\n📊 Dataset descargado:")
    print(f"   - Ticker: SPY")
    print(f"   - Filas: {len(df):,}")
    print(f"   - Fecha inicio: {df.index[0]}")
    print(f"   - Fecha fin: {df.index[-1]}")
    
    print(f"\n📋 Primeras 5 filas:")
    print(df.head())
    
    print("\n🎉 ¡Datos listos para análisis!")
    print("═" * 60)
    
    # Desconectar
    ib.disconnect()
    
except Exception as e:
    print("═" * 60)
    print("❌ ERROR EN LA DESCARGA")
    print("═" * 60)
    print(f"\nError: {e}")
    print("\n→ Ve a Troubleshooting - Descarga de Datos")
```

3. **Ejecuta la celda**

---

### 🔍 Interpretación de Resultados

**✅ DESCARGA EXITOSA - Verás:**

```
═══════════════════════════════════════════════════════════
✅ DESCARGA COMPLETADA
═══════════════════════════════════════════════════════════

📊 Dataset descargado:
   - Ticker: SPY
   - Filas: 1,260
   - Fecha inicio: 2019-11-15
   - Fecha fin: 2024-11-15

📋 Primeras 5 filas:
                 open   high    low  close     volume
date                                                  
2019-11-15  308.12  308.45  307.89  308.33  45234567
2019-11-18  308.50  309.12  308.31  308.95  52341234
...

🎉 ¡Datos listos para análisis!
```

**Lo importante:**
- ✅ Ves una tabla con datos (open, high, low, close, volume)
- ✅ Los datos tienen fechas recientes
- ✅ Hay más de 1000 filas de datos
- ✅ No hay errores rojos

---

### ✅ Checkpoint de Validación - Paso 5

Antes de continuar al Paso 6, verifica:

- [ ] Ejecutaste el código de descarga de tu broker
- [ ] Viste el mensaje: "✅ DESCARGA COMPLETADA"
- [ ] Viste una tabla con datos de SPY
- [ ] Los datos tienen fechas recientes (últimos 5 años)
- [ ] No hay errores críticos

**Si marcaste todos ✅ → Continúa al [Paso 6](#paso-6-validación-final-completa-5-min)**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 5](#error-paso-5-no-puedo-descargar-datos)**

---

## PASO 6: VALIDACIÓN FINAL COMPLETA (5 min)

### 🎯 Objetivo del Paso
Verificar que TODO el setup funciona correctamente.

---

### 📍 ¿Qué Vamos a Validar?

Este paso ejecuta un **script de validación automática** que verifica:

✅ Librerías instaladas  
✅ Conexión al broker  
✅ Capacidad de descargar datos  
✅ Funcionalidad de análisis básico  
✅ Todo listo para el workshop

---

### 🚀 Acción: Ejecutar Validación Final

1. **Crea una nueva celda de código**

2. **Copia y pega este código:**

```python
# ════════════════════════════════════════════════════════════
# 🔍 VALIDACIÓN COMPLETA DEL SETUP
# ════════════════════════════════════════════════════════════
# Este script verifica que todo esté funcionando correctamente
# ════════════════════════════════════════════════════════════

print("🔍 VALIDACIÓN COMPLETA DEL SETUP")
print("=" * 60)

validation_results = []

# ════════════════════════════════════════════════════════════
# 1. Verificar Librerías
# ════════════════════════════════════════════════════════════
print("\n📦 Verificando librerías instaladas...")

required_libraries = [
    "pandas",
    "numpy",
    "matplotlib",
    "pandas_ta"
]

for lib in required_libraries:
    try:
        __import__(lib)
        validation_results.append((lib.capitalize(), "✅ OK"))
    except ImportError:
        validation_results.append((lib.capitalize(), "❌ NO INSTALADA"))

# ════════════════════════════════════════════════════════════
# 2. Verificar Broker
# ════════════════════════════════════════════════════════════
print("\n🔑 Verificando configuración de broker...")

# Detectar qué broker está configurado
broker_configured = False

# Verificar Alpaca
try:
    if 'ALPACA_API_KEY' in globals() and ALPACA_API_KEY != "PKxxxxxxxxxxxxxxxxxxxxxx":
        from alpaca.data.historical import StockHistoricalDataClient
        test_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
        validation_results.append(("Alpaca Configurado", "✅ OK"))
        broker_configured = True
except:
    pass

# Verificar Interactive Brokers
try:
    if 'IB_HOST' in globals():
        from ib_insync import IB
        test_ib = IB()
        test_ib.connect(IB_HOST, IB_PORT, clientId=999)
        test_ib.disconnect()
        validation_results.append(("IB Configurado", "✅ OK"))
        broker_configured = True
except:
    pass

if not broker_configured:
    validation_results.append(("Broker", "❌ NO CONFIGURADO"))

# ════════════════════════════════════════════════════════════
# 3. Verificar Datos
# ════════════════════════════════════════════════════════════
print("\n🌐 Verificando capacidad de análisis de datos...")

try:
    # Verificar que tenemos datos descargados
    if 'df' in globals() and len(df) > 0:
        validation_results.append(("Datos Históricos", "✅ OK"))
        validation_results.append((f"Filas de Datos: {len(df)}", "✅ OK"))
    else:
        validation_results.append(("Datos Históricos", "❌ NO DESCARGADOS"))
except:
    validation_results.append(("Datos Históricos", "❌ ERROR"))

# ════════════════════════════════════════════════════════════
# 4. Imprimir Resultados
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("📊 RESULTADOS DE LA VALIDACIÓN")
print("=" * 60)

for item, status in validation_results:
    print(f"{item:.<40} {status}")

# ════════════════════════════════════════════════════════════
# 5. Veredicto Final
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)

failed = [item for item, status in validation_results if "❌" in status]

if len(failed) == 0:
    print("🎉 ¡TODO PERFECTO! SETUP COMPLETADO AL 100%")
    print("=" * 60)
    print("\n✅ Estás listo para empezar el workshop")
    print("✅ Todas las herramientas están funcionando")
    print("✅ Tu conexión al broker está activa")
    print("✅ Puedes descargar y analizar datos")
    print("\n🎓 Próximos pasos:")
    print("   1. Guarda este notebook (ya se guardó automáticamente)")
    print("   2. Revisa la sección 'Integración con Recursos'")
    print("   3. Espera el inicio del workshop")
else:
    print("⚠️  HAY PROBLEMAS EN EL SETUP")
    print("=" * 60)
    print(f"\n❌ Componentes con error ({len(failed)}):")
    for item in failed:
        print(f"   - {item}")
    print("\n💡 Solución:")
    print("   - Revisa el Troubleshooting de cada paso con error")
    print("   - Vuelve a ejecutar los pasos que fallaron")
    print("   - Contacta soporte si persiste el problema")

print("\n" + "=" * 60)
```

3. **Ejecuta la celda** (Shift + Enter)

---

### 🔍 Interpretación de Resultados

**✅ SETUP EXITOSO - Verás:**

```
🔍 VALIDACIÓN COMPLETA DEL SETUP
============================================================
...
============================================================
📊 RESULTADOS DE LA VALIDACIÓN
============================================================
Pandas............................... ✅ OK
Numpy................................ ✅ OK
Matplotlib........................... ✅ OK
Pandas_ta............................ ✅ OK
Alpaca Configurado................... ✅ OK
Datos Históricos..................... ✅ OK
Filas de Datos: 1260................. ✅ OK
============================================================

🎉 ¡TODO PERFECTO! SETUP COMPLETADO AL 100%
============================================================

✅ Estás listo para empezar el workshop
✅ Todas las herramientas están funcionando
✅ Tu conexión al broker está activa
✅ Puedes descargar y analizar datos

🎓 Próximos pasos:
   1. Guarda este notebook (ya se guardó automáticamente)
   2. Revisa la sección 'Integración con Recursos'
   3. Espera el inicio del workshop
```

**🎊 ¡FELICIDADES! Has completado el Setup A exitosamente.**

---

**❌ SETUP CON ERRORES - Verás:**

```
============================================================
⚠️  HAY PROBLEMAS EN EL SETUP
============================================================

❌ Componentes con error (2):
   - Broker
   - Datos Históricos

💡 Solución:
   - Revisa el Troubleshooting de cada paso con error
   - Vuelve a ejecutar los pasos que fallaron
   - Contacta soporte si persiste el problema
```

→ Ve a la sección de [Troubleshooting](#-troubleshooting-por-paso) correspondiente

---

### ✅ Checklist Final de Completación

**Marca todos los items que completaste:**

- [ ] Accediste a Google Colab (Paso 1)
- [ ] Creaste tu notebook personal (Paso 2)
- [ ] Instalaste todas las librerías (Paso 3)
- [ ] Configuraste tu broker (Paso 4A o 4B)
- [ ] Descargaste datos de SPY (Paso 5)
- [ ] Ejecutaste la validación final (Paso 6)
- [ ] Todos los resultados muestran ✅ OK
- [ ] Viste el mensaje: "🎉 ¡TODO PERFECTO!"

**Si marcaste TODOS ✅:**

🎉 **¡FELICIDADES! Has completado el Setup A al 100%**

→ Continúa a [Integración con Recursos del Workshop](#-integración-con-recursos-del-workshop)

**Si hay algún ❌:**

→ Ve a [Troubleshooting](#-troubleshooting-por-paso)

---

## 🔗 INTEGRACIÓN CON RECURSOS DEL WORKSHOP

### 🎯 ¿Qué Hacer Ahora?

Has completado el setup técnico. Ahora es el momento de familiarizarte con los recursos que usarás durante el workshop.

---

### 📚 Recursos Principales del Kit

**1. Prompts Library (Biblioteca de Prompts)**

**¿Qué es?**  
Colección de +35 prompts probados para interactuar con IA Generativa en contexto de trading algorítmico.

**Ubicación:**  
[03_PROMPTS_LIBRARY/](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)

**Ejemplos de prompts:**
- `P01_Explicar_Codigo.md` - Para entender código que no escribiste
- `P05_Debuggear_Error.md` - Para encontrar y corregir bugs
- `P10_Optimizar_Estrategia.md` - Para mejorar estrategias existentes
- `P15_Generar_Backtest.md` - Para crear scripts de backtesting

**💡 Recomendación:**  
Lee al menos 5 prompts antes de la Sesión 1 para familiarizarte con la estructura.

---

**2. Template Pack (Paquete de Templates)**

**¿Qué es?**  
Plantillas reutilizables para acelerar tu desarrollo de estrategias.

**Ubicación:**  
[02_TEMPLATE_PACK/](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/02_TEMPLATE_PACK)

**Templates disponibles:**
- **Estrategias:** Mean Reversion, Momentum, Pairs Trading
- **Backtesting:** Vectorbt, Backtrader
- **Gestión de Riesgo:** Position Sizing, Stop Loss
- **Reportes:** Performance Analysis, Risk Metrics

**💡 Recomendación:**  
No intentes entender todo ahora. Úsalos como referencia durante el workshop.

---

**3. Scripts de Python Auxiliares**

**¿Qué son?**  
Utilidades pre-escritas para tareas comunes.

**Ubicación:**  
[04_SCRIPTS/](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/04_SCRIPTS)

**Scripts útiles:**
- `data_pipeline.py` - Descarga y limpieza de datos
- `backtest_runner.py` - Ejecutar backtests en batch
- `risk_calculator.py` - Cálculo de métricas de riesgo
- `report_generator.py` - Generar reportes automáticos

**💡 Recomendación:**  
Familiarízate con `data_pipeline.py` - lo usaremos en la Sesión 2.

---

**4. Colab Notebook Maestro**

**¿Qué es?**  
Notebook con TODO el código del workshop (Sesiones 1-9) organizado y comentado.

**Ubicación:**  
[00_GUIA_DE_USO/Colab_Notebook_Maestro.ipynb](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/00_GUIA_DE_USO)

**Contenido:**
- Código de las 9 sesiones
- Ejercicios resueltos
- Casos de estudio completos
- Notas del instructor

**⚠️ Advertencia:**  
NO abras este notebook antes del workshop. Está diseñado como referencia post-sesiones.

---

### 🎓 Programa Detallado del Workshop

**Revisa la estructura completa:**  
[Programa_Detallado_Workshop.md](https://github.com/yismafx/workshop-trading-algoritmico-kit/blob/main/00_GUIA_DE_USO/Programa_Detallado_Workshop.md)

**Encontrarás:**
- Objetivos de cada sesión
- Contenido teórico y práctico
- Entregables esperados
- Pre-requisitos por sesión

**💡 Recomendación:**  
Lee la descripción de las Sesiones 1-3 para tener contexto.

---

### 📞 Únete al Grupo de Telegram

**Grupo Premium del Workshop:**
- Soporte comunitario
- Anuncios importantes
- Material complementario
- Networking con otros participantes

**Recibirás la invitación por email después de tu inscripción.**

**Mientras tanto:**
- Puedes contactar al instructor en: [@yismafx](https://t.me/yismafx)

---

### ✅ Checklist de Preparación Final

**Antes de la Sesión 1:**

- [ ] Exploré la [Prompts Library](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)
- [ ] Revisé el [Template Pack](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/02_TEMPLATE_PACK)
- [ ] Leí el [Programa Detallado](https://github.com/yismafx/workshop-trading-algoritmico-kit/blob/main/00_GUIA_DE_USO/Programa_Detallado_Workshop.md)
- [ ] Me uní al grupo de Telegram (si recibí invitación)
- [ ] Tengo mi notebook de setup guardado y funcional
- [ ] Probé ejecutar al menos una celda de código

**Estado de Preparación:**
- ✅ Completado: Listo para el workshop
- 🟡 En progreso: Completar checklist
- ⬜ No iniciado: Empezar ahora

---

## 🚨 TROUBLESHOOTING POR PASO

### Error Paso 1: No Puedo Acceder a Colab

**Síntoma:** No puedo abrir `colab.research.google.com`

**Causa:** Problema de conexión o navegador

**Soluciones:**

**Solución 1 - Verificar URL:**
- Asegúrate de escribir: `https://colab.research.google.com`
- NO uses: `colab.google.com` o `google.colab.com`

**Solución 2 - Cambiar navegador:**
1. Prueba con Chrome (recomendado)
2. Si usas Chrome, actualiza a la última versión
3. Prueba en modo incógnito (Ctrl+Shift+N)

**Solución 3 - Limpiar cache:**
1. Ctrl+Shift+Del (Chrome)
2. Selecciona "Cached images and files"
3. Click "Clear data"
4. Vuelve a intentar

**Prevención:** Usa siempre Chrome actualizado

---

### Error Paso 2: No Puedo Crear el Notebook

**Síntoma:** No veo la opción "New notebook" o no se crea

**Causa:** Problema con cuenta de Google o permisos

**Soluciones:**

**Solución 1 - Verificar login:**
1. Verifica que iniciaste sesión correctamente
2. Busca tu foto/inicial en la esquina superior derecha
3. Si no aparece → Vuelve a hacer login

**Solución 2 - Permisos de Google Drive:**
1. Ve a: https://drive.google.com
2. Verifica que puedas crear archivos
3. Si hay error → Revisa el espacio de almacenamiento

**Solución 3 - Usar template:**
1. Descarga: [Setup_y_Practica_Trading.ipynb](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/00_GUIA_DE_USO)
2. En Colab: File → Upload notebook
3. Selecciona el archivo descargado

**Prevención:** Verifica que tienes espacio en Google Drive

---

### Error Paso 3: Fallo en Instalación

**Síntoma:** Alguna librería muestra ❌ en la verificación

**Causas comunes:**
1. Conflicto de versiones
2. Límite de memoria
3. Conexión interrumpida

**Soluciones:**

**Solución 1 - Restart Runtime:**
1. Click en: `Runtime` → `Restart runtime`
2. Confirma el restart
3. Vuelve a ejecutar la celda de instalación

**Solución 2 - Instalación individual:**
```python
# Si falló vectorbt, instálalo solo:
!pip install -q vectorbt

# Verifica:
import vectorbt
print("✅ vectorbt instalado")
```

**Solución 3 - Versión específica:**
```python
# Instala versión específica si hay conflicto:
!pip install -q vectorbt==0.25.4
```

**Solución 4 - Desde cero:**
1. File → New notebook (crear nuevo)
2. Copia solo la celda de instalación
3. Ejecuta en notebook limpio

**Prevención:** Siempre restart runtime antes de empezar el workshop

---

### Troubleshooting Alpaca

**Problema: No puedo conectarme a Alpaca**

**Error común:**
```
Could not authenticate with Alpaca
```

**Soluciones:**

**Solución 1 - Verificar keys:**
1. Ve a Alpaca → Paper Trading → API Keys
2. Verifica que copiaste correctamente:
   - API Key completa (empieza con "PK")
   - Secret Key completa
3. NO debe haber espacios al inicio/final
4. Deben estar entre comillas: `"PK..."`

**Solución 2 - Regenerar keys:**
1. En Alpaca: Delete API Key actual
2. Generate New Key
3. Copia las nuevas keys
4. Actualiza el notebook

**Solución 3 - Verificar modo Paper:**
```python
# Asegúrate de que esto sea True:
ALPACA_PAPER = True
```

**Solución 4 - Verificar cuenta activa:**
1. Login en https://alpaca.markets
2. Verifica que tu cuenta esté "ACTIVE"
3. Si está "PENDING" → Completa verificación de email

---

**Problema: Error al descargar datos**

**Error común:**
```
No data returned
```

**Causas:**
1. Ticker incorrecto
2. Broker no soporta ese activo
3. Límite de API alcanzado

**Soluciones:**

**Solución 1 - Verificar ticker:**
```python
# Prueba con SPY (siempre funciona)
ticker = "SPY"
```

**Solución 2 - Verificar mercado:**
- Alpaca solo soporta: US Stocks
- NO soporta: Crypto, Forex, Futuros

**Solución 3 - Verificar horario:**
```python
# Usa rango de fechas válido
from datetime import datetime, timedelta
start = datetime.now() - timedelta(days=365)
end = datetime.now()
```

**Solución 4 - Esperar:**
- APIs tienen límites (ej: 200 requests/minuto)
- Espera 1 minuto y vuelve a intentar

---

### Troubleshooting Interactive Brokers

**Problema: No puedo conectarme a IB**

**Error común:**
```
Could not connect to TWS
```

**Soluciones:**

**Solución 1 - Verificar TWS está corriendo:**
1. Abre TWS o IB Gateway
2. Inicia sesión
3. Deja TWS abierto MIENTRAS usas el notebook

**Solución 2 - Verificar puerto:**
- Paper Trading: Puerto 7497
- Live Trading: Puerto 7496

En el notebook:
```python
IB_PORT = 7497  # Debe coincidir con la configuración en TWS
```

**Solución 3 - Habilitar API:**
1. En TWS: `Global Configuration` → `API` → `Settings`
2. ✅ Enable ActiveX and Socket Clients
3. ✅ Trusted IP: Agrega `127.0.0.1`
4. Guarda cambios
5. Reinicia TWS

**Solución 4 - Firewall:**
1. Windows: Permite TWS en Firewall
2. Mac: System Preferences → Security → Allow TWS

---

### Troubleshooting Datos

**Problema: No se descargan datos**

**Error común:**
```
No data returned
```

**Causas comunes:**
1. Ticker incorrecto
2. Rango de fechas inválido
3. Broker no soporta ese activo
4. Límite de API alcanzado

**Soluciones:**

**Solución 1 - Verificar ticker:**
```python
# Prueba con SPY (siempre funciona)
ticker = "SPY"
```

**Solución 2 - Ajustar fechas:**
```python
# Usa rango seguro
start_date = "2020-01-01"
end_date = "2024-11-15"
```

**Solución 3 - Verificar activo soportado:**
- Alpaca: Solo US stocks
- IB: Stocks, crypto, forex, futuros

**Solución 4 - Esperar y reintentar:**
- APIs tienen límites (ej: 200 requests/minuto)
- Espera 1 minuto y vuelve a intentar

---

### Troubleshooting Gráficos

**Problema: No se muestra el gráfico**

**Soluciones:**

**Solución 1 - Forzar inline plotting:**
```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(data['Close'])
plt.show()
```

**Solución 2 - Reiniciar kernel:**
1. Runtime → Restart runtime
2. Vuelve a ejecutar celdas desde el inicio

**Solución 3 - Verificar datos:**
```python
print(data.head())  # ¿Los datos están cargados?
print(len(data))    # ¿Hay datos suficientes?
```

---

## 🎯 PRÓXIMOS PASOS

### ✅ Has Completado el Setup A

**¡Felicitaciones! Ahora tienes:**

✅ Google Colab configurado  
✅ Notebook personal funcional  
✅ Librerías de trading instaladas  
✅ Conexión a broker establecida  
✅ Capacidad de descargar datos  
✅ Entorno 100% listo para el workshop

---

### 🗓️ Preparación para el Workshop

**Antes de la Sesión 1:**

**1. Revisa los recursos:**
- [ ] Explora la [Prompts Library](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)
- [ ] Revisa el [Template Pack](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/02_TEMPLATE_PACK)
- [ ] Lee el [Programa Detallado](https://github.com/yismafx/workshop-trading-algoritmico-kit/blob/main/00_GUIA_DE_USO/Programa_Detallado_Workshop.md)

**2. Únete al grupo de Telegram:**
- [ ] Recibirás invitación por email
- [ ] Preséntate brevemente
- [ ] Activa notificaciones

**3. Opcional - Familiarízate con Colab:**
- [ ] Mira videos tutoriales de Google Colab
- [ ] Experimenta creando celdas
- [ ] Prueba ejecutar código simple de Python

---

### 📚 Lecturas Previas Opcionales

**Si quieres adelantar teoría (opcional):**

- 📖 Chan, E. (2013). "Algorithmic Trading", Capítulos 1-2
- 📖 Carver, R. (2015). "Systematic Trading", Introducción
- 📖 López de Prado, M. (2018). "Advances in Financial ML", Prefacio

**NO es obligatorio leer nada antes del workshop.** Todo se explicará desde cero.

---

### 🔗 Explora Otros Setups (Opcional)

**Si quieres ver alternativas:**

- 📄 [Setup B: Python Local](Setup_B_Python_Local.md) - Para deployment 24/7
- 📄 [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md) - Para usuarios de MT5
- 📄 [Setup D: Interactive Brokers](Setup_D_Interactive_Brokers.md) - Para máxima integración

**Recomendación:** Mantén este Setup A como principal durante el workshop. Los otros setups son para después.

---

## 🧭 NAVEGACIÓN

**🏠 Inicio:** [README Principal](../README.md)  
**⬅️ Anterior:** [Guía de Setup Completa](Guia_Setup_Completa.md)  
**➡️ Siguiente:** [Mejores Prácticas](Mejores_Practicas_Setup_A.md)  
**⬆️ Categoría:** [Guía de Uso](GUIA_INICIO.md)

---

## 📞 SOPORTE Y CONTACTO

### 🆘 Si Necesitas Ayuda

**Antes de contactar, intenta:**

1. ✅ Revisar el [Troubleshooting](#-troubleshooting-por-paso) de este documento
2. ✅ Buscar en el grupo de Telegram (probablemente alguien tuvo el mismo problema)
3. ✅ Reiniciar el runtime de Colab (Runtime → Disconnect and delete runtime)

**Si el problema persiste:**

### 📧 Email

**Asunto:** `[Setup A Guiado] - [Tu problema en 5 palabras]`

**Email:** yismaryme@gmail.com

**Tiempo de respuesta:** 24-48 horas

**Incluye en tu email:**
1. Descripción del problema
2. Qué paso estabas siguiendo
3. Screenshot del error (si aplica)
4. Qué soluciones de troubleshooting ya probaste

---

### 💬 Telegram

**Para:** Consultas rápidas y urgentes

**Usuario:** [@yismafx](https://t.me/yismafx)

**Horarios de respuesta rápida:**
- Lunes a Viernes: 9:00 AM - 6:00 PM (GMT-3)
- Fines de semana: Respuestas limitadas

---

### 🔒 Grupo Premium del Workshop

**Disponible para participantes inscritos**

- Soporte comunitario
- Respuestas de otros participantes
- Material complementario compartido
- Anuncios importantes

**Recibirás invitación por email después de tu inscripción**

---

## ❓ FAQ - Preguntas Frecuentes

**P: ¿Cuánto tiempo dura este setup guiado?**  
R: 30-60 minutos, dependiendo de si configuras 1 o 2 brokers.

**P: ¿Puedo usar otro broker que no sea Alpaca o IB?**  
R: Sí, pero tendrás que adaptar el código. Recomendamos empezar con Alpaca o IB.

**P: ¿Necesito pagar algo?**  
R: No. Google Colab es gratis, y ambos brokers ofrecen paper trading gratuito.

**P: ¿Colab es seguro para mis API keys?**  
R: Razonablemente seguro si sigues las mejores prácticas. NUNCA compartas tu notebook públicamente sin eliminar las keys primero.

**P: ¿Qué hago si mi runtime se desconecta?**  
R: Normal después de 12 horas de inactividad. Simplemente reconecta y re-ejecuta la celda de instalación.

**P: ¿Puedo hacer el setup desde mi celular?**  
R: Técnicamente sí, pero NO es recomendado. Usa una computadora para mejor experiencia.

**P: ¿Tengo que repetir el setup antes de cada sesión?**  
R: No completo. Solo ejecuta la celda de instalación y configuración si pasó más de un día.

---

## 📌 VERSIÓN

**v2.0 (Noviembre 2025)** - Versión corregida con contenido de Guia_paso_a_paso_completa.md  
**Última actualización:** Noviembre 15, 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- **v2.0 (Nov 15, 2025):** Contenido actualizado desde Guia_paso_a_paso_completa.md
  - Estructura pedagógica mejorada
  - Analogías para traders añadidas en cada sección
  - Checkpoints de validación en cada paso
  - Recursos de video agregados
  - Código corregido y actualizado para 2025
  - Troubleshooting expandido
- **v1.0 (Nov 2025):** Versión inicial guiada paso a paso

---

## ⚠️ DISCLAIMER LEGAL

**Material educativo para fines de aprendizaje únicamente.**

❌ **NO constituye asesoría de inversión**  
⚠️ **Trading algorítmico implica riesgo de pérdida de capital**  
📊 **Resultados pasados NO garantizan resultados futuros**  
💰 **Nunca operes con dinero que no puedas perder**

**Recordatorios importantes:**
- El trading algorítmico requiere conocimiento, práctica y gestión de riesgo
- El 90% de las estrategias fallan en validación rigurosa
- Paper trading NO es exactamente igual a live trading (slippage real)

**Responsabilidad:**
- Tú eres 100% responsable de tus decisiones de trading
- Este material es educativo, no predictivo
- Siempre valida estrategias exhaustivamente antes de usar capital real
- Considera consultar con un asesor financiero certificado

---

**🎉 ¡Felicitaciones por completar el Setup A Guiado!**

**Estás listo para comenzar tu journey en Trading Algorítmico Aumentado con IA Generativa.**

**Nos vemos en la Sesión 1 del workshop. 🚀**

---

[Fin del documento - Setup A Guiado v2.0]
