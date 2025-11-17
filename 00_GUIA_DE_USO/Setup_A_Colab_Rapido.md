# ⚡ SETUP A: COLAB COMPLETO

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 Setup A Colab Completo**

---

**⏱️ Tiempo:** 30-45 min | **Dificultad:** ⭐⭐ | **Detalle:** Completo con explicaciones  
**📅 Última actualización:** 17 de noviembre de 2025  
**📌 Versión:** 3.0

---

## 💡 ¿OTRAS RUTAS DE SETUP?

> ⚡ **¿Tienes prisa y ya usaste notebooks antes?**  
> Usa [Setup A: Express →](Setup_A_Express.md) (10-15 min, sin explicaciones extensas)

> 📖 **¿Quieres máximo detalle paso a paso?**  
> Usa [Setup A: Guiado →](Setup_A_Guiado.md) (60-90 min, exhaustivo con screenshots)

---

## 📑 TABLA DE CONTENIDOS

### ⚡ Atajos Rápidos
- [🚀 **¿Para quién es este setup?**](#-para-quién-es-este-setup)
- [✅ **Requisitos mínimos**](#-requisitos-mínimos)
- [🎯 **Empezar setup ahora**](#-paso-1-crear-cuenta-google-si-no-tienes)
- [🚨 **Tengo un problema**](#-troubleshooting-rápido)

### 📖 Contenido Principal
1. [¿Para Quién es Este Setup?](#-para-quién-es-este-setup)
2. [Requisitos Mínimos](#-requisitos-mínimos)
3. [Paso 1: Cuenta Google](#-paso-1-crear-cuenta-google-si-no-tienes)
4. [Paso 2: Abrir Google Colab](#-paso-2-abrir-google-colab)
5. [Paso 3: Crear Notebook de Práctica](#-paso-3-crear-notebook-de-práctica)
6. [Paso 4: Instalar Librerías](#-paso-4-instalar-librerías-de-trading)
7. [Paso 5: Configurar Broker](#-paso-5-configurar-broker-alpaca)
8. [Paso 6: Descargar Datos](#-paso-6-descargar-primer-dataset)
9. [Paso 7: Validación Final](#-paso-7-validación-completa)
10. [Troubleshooting Rápido](#-troubleshooting-rápido)
11. [Próximos Pasos](#-próximos-pasos)

---

## 🎯 ¿PARA QUIÉN ES ESTE SETUP?

### ✅ Este Setup es PERFECTO si:

- 📊 **Eres trader profesional** con años de experiencia, pero...
- ❌ **NO tienes experiencia programando** (nunca has escrito código)
- ✅ Prefieres **empezar rápido** sin instalar programas en tu computadora
- ✅ Tienes **conexión a internet estable** (mínimo 3 Mbps)
- ✅ Tienes o puedes crear una **cuenta Gmail** (gratis)

### ❌ Este Setup NO es Ideal si:

- 🚀 Ya necesitas sistemas funcionando **24/7 en producción**  
  → Mejor usa: Setup B (Python Local) - *Disponible próximamente*

- 📊 Usas principalmente **MetaTrader** y quieres empezar ahí  
  → Mejor usa: Setup C (MT5) - *Disponible próximamente*

- 💼 Ya tienes cuenta **Interactive Brokers** y quieres máxima integración  
  → Mejor usa: Setup D (IB) - *Disponible próximamente*

**Para este workshop:** Setup A (Colab) es la opción recomendada para 80% de participantes. Los otros setups se agregan conforme avance el workshop.

---

## ✅ REQUISITOS MÍNIMOS

### 💻 Hardware (Tu Equipo)

**Necesitas:**

- ✅ **Cualquier computadora** con internet (Mac, Windows, o Linux)
  - Tu laptop vieja funciona si tiene menos de 5 años
  - Tablets NO recomendadas (mejor computadora)

- ✅ **Conexión a internet estable**
  - **Mínimo:** 3 Mbps ([Verifica tu velocidad aquí](https://fast.com))
  - Si es más lenta, puedes seguir, pero videos pueden pausarse
  - **Tip:** Cierra Netflix, YouTube, etc. durante el workshop

- ✅ **RAM recomendada:** 4 GB mínimo (2 GB funciona pero más lento)

**NO necesitas:**
- ❌ Computadora potente ni GPU
- ❌ Instalar Python ni librerías
- ❌ Espacio en disco (todo corre en la nube)

---

### 📱 Software

**Necesitas:**

- ✅ **Navegador web moderno**
  - Google Chrome (recomendado)
  - Firefox, Safari, o Edge (también funcionan)
  - Versión actualizada (última versión disponible)

- ✅ **Cuenta Gmail**
  - Si no tienes: [Crear cuenta Gmail](https://accounts.google.com/signup)
  - Gratis, toma 2 minutos

**NO necesitas:**
- ❌ Python instalado
- ❌ Jupyter Lab
- ❌ IDEs (VS Code, PyCharm, etc.)

---

## 🚀 PASO 1: CREAR CUENTA GOOGLE (Si No Tienes)

### ¿Ya tienes Gmail?

**✅ SÍ tengo Gmail** → [Saltar al Paso 2 →](#-paso-2-abrir-google-colab)

**❌ NO tengo Gmail** → Continúa aquí abajo (2 minutos)

---

### Crear Cuenta Gmail (2 minutos)

**1. Ve a:** [accounts.google.com/signup](https://accounts.google.com/signup)

**2. Completa el formulario:**
- Nombre y apellido
- Elige nombre de usuario (tu-email@gmail.com)
- Crea contraseña segura
- Agrega número de teléfono (opcional pero recomendado)
- Fecha de nacimiento

**3. Acepta términos y condiciones**

**4. Listo!** Ya tienes cuenta Google/Gmail

**⚠️ Guarda bien tu contraseña** - La necesitarás para acceder a Colab

---

## 🚀 PASO 2: ABRIR GOOGLE COLAB

### ¿Qué es Google Colab?

> **Analogía para traders:**  
> Google Colab es como TradingView, pero para código Python.  
> No instalas nada, todo corre en el navegador.

**Características:**
- ✅ Gratis
- ✅ Sin instalación
- ✅ Código Python en la nube
- ✅ Librerías pre-instaladas
- ⚠️ Sesiones de 90 minutos (se desconecta si inactivo)

---

### Abrir Colab (1 minuto)

**1. Ve a:** [colab.research.google.com](https://colab.research.google.com)

**2. Inicia sesión** con tu cuenta Gmail creada en Paso 1

**3. Verás la pantalla de bienvenida** con opciones:
- Recent (notebooks recientes)
- Google Drive (tus notebooks guardados)
- GitHub (importar desde GitHub)
- **Upload** (subir archivo .ipynb)

**✅ Confirmación:** Si ves esta pantalla, Colab está funcionando correctamente

---

## 🚀 PASO 3: CREAR NOTEBOOK DE PRÁCTICA

### ¿Qué es un Notebook?

> **Analogía para traders:**  
> Un notebook es como una hoja de Excel, pero en lugar de fórmulas,  
> escribes código Python. Puedes ejecutar código en "celdas" y ver resultados inmediatos.

---

### Crear Notebook Nuevo (2 minutos)

**1. En Colab, click en:**  
`File` → `New notebook`

**2. Se abre un notebook vacío**

**3. Renombra el notebook:**
- Click en "Untitled0.ipynb" (arriba izquierda)
- Cambia nombre a: `Setup_y_Practica_Trading.ipynb`
- **Enter** para guardar

**4. Verifica que esté guardado:**
- Debe decir "Saved" en lugar de "Saving..."
- El notebook está en tu Google Drive automáticamente

---

### Anatomía de un Notebook

Un notebook tiene **2 tipos de celdas:**

**1. Celdas de Código** (ejecutan Python):
```python
# Ejemplo de celda de código
print("Hola, mundo del trading!")
```

**2. Celdas de Texto** (Markdown, como esta guía):
```markdown
# Este es un título
Este es un párrafo explicativo
```

**Para agregar celda:**
- `+ Code` (botón arriba izquierda) = Celda de código
- `+ Text` (botón arriba izquierda) = Celda de texto

**Para ejecutar celda:**
- Click en ▶️ (botón play a la izquierda de la celda)
- O presiona `Shift + Enter`

---

## 🚀 PASO 4: INSTALAR LIBRERÍAS DE TRADING

### ¿Qué son las Librerías?

> **Analogía para traders:**  
> Librerías son como indicadores en TradingView.  
> No programas el RSI desde cero, usas la librería `ta` que ya lo tiene.

**Librerías que usaremos:**
- `pandas` → Manejo de datos (como Excel con esteroides)
- `numpy` → Cálculos matemáticos
- `yfinance` → Descargar datos de Yahoo Finance
- `alpaca-py` → Conectar con broker Alpaca
- `matplotlib` → Gráficos

---

### Instalar Librerías (5 minutos)

**Copia y pega este código en una celda nueva:**

```python
# 📦 INSTALACIÓN DE LIBRERÍAS (Ejecutar UNA sola vez)

# Librerías core (ya incluidas en Colab, solo actualizamos)
!pip install --upgrade pandas numpy matplotlib

# Librerías de trading
!pip install yfinance --quiet
!pip install alpaca-py --quiet
!pip install ta --quiet

print("✅ Librerías instaladas correctamente")
```

**Ejecutar:**
1. Click en ▶️ o `Shift + Enter`
2. Espera 2-3 minutos (verás líneas de instalación)
3. **Debe terminar con:** `✅ Librerías instaladas correctamente`

**⚠️ IMPORTANTE:**
- Solo ejecuta esta celda **UNA vez** al inicio
- Si desconectas Colab, tendrás que ejecutarla de nuevo
- Cada sesión del workshop, ejecuta esto primero

---

### Verificar Instalación

**Crea nueva celda y copia esto:**

```python
# ✅ VERIFICACIÓN DE INSTALACIÓN

import pandas as pd
import numpy as np
import yfinance as yf
from alpaca.trading.client import TradingClient
import ta

print("✅ pandas versión:", pd.__version__)
print("✅ numpy versión:", np.__version__)
print("✅ yfinance importado OK")
print("✅ alpaca-py importado OK")
print("✅ ta (análisis técnico) importado OK")
print("\n🎉 Todas las librerías funcionan correctamente")
```

**Ejecutar:**
- Debe mostrar versiones y terminar con: `🎉 Todas las librerías funcionan correctamente`

**Si hay error:**
- Vuelve a ejecutar la celda de instalación
- Reinicia runtime: `Runtime` → `Restart runtime`
- Ejecuta ambas celdas de nuevo

---

## 🚀 PASO 5: CONFIGURAR BROKER (ALPACA)

### ¿Por Qué Alpaca?

**Ventajas:**
- ✅ **Paper trading gratis** (dinero simulado, 0 riesgo)
- ✅ API simple y bien documentada
- ✅ No requiere capital inicial para practicar
- ✅ Acceso a acciones US (S&P 500, NASDAQ, etc.)

**Desventajas:**
- ⚠️ Solo acciones US (no Forex, no crypto en API)
- ⚠️ Datos históricos con restricción de 15 minutos (plan gratis)

**Para el workshop:** Alpaca es perfecto para aprender. Después puedes migrar a otro broker si necesitas.

---

### Crear Cuenta Alpaca Paper Trading (5-7 minutos)

**1. Ve a:** [alpaca.markets](https://alpaca.markets)

**2. Click en "Sign Up"** (arriba derecha)

**3. Completa registro:**
- Email (puede ser el mismo Gmail)
- Crear contraseña
- Verificar email (revisa bandeja entrada)

**4. Completar perfil:**
- Nombre completo
- País de residencia
- **IMPORTANTE:** Selecciona **"Paper Trading"** (NO "Live Trading")

**5. Verificación de identidad:**
- Para **Paper Trading:** Solo email (instantáneo)
- Para **Live Trading:** Requiere documentos (NO lo necesitas ahora)

**6. Listo!** Tienes cuenta Alpaca Paper con $100,000 USD simulados

---

### Obtener API Keys (3 minutos)

**Las API Keys son como llaves de tu cuenta para que Python se conecte**

**Paso a paso:**

**1. Inicia sesión en Alpaca** ([app.alpaca.markets](https://app.alpaca.markets))

**2. Verifica que estás en "Paper"** (arriba derecha debe decir "Paper" NO "Live")

**3. Ve a:**  
`Your Account` (menú izquierda) → `API Keys` (tab arriba)

**4. Click en "Generate New Key"**

**5. Verás 2 keys:**
- **API Key ID** (ejemplo: `PKXXX...`)
- **Secret Key** (ejemplo: `xxx...xxx`)

**6. Copia ambas keys** y guárdalas en un lugar seguro

**⚠️ MUY IMPORTANTE:**
- **NUNCA compartas tu Secret Key** (es como la contraseña de tu cuenta)
- Si la compartes por accidente, genera nuevas keys inmediatamente
- Estas keys son SOLO para Paper Trading (dinero simulado)

---

### Configurar Keys en Colab

**Crea nueva celda y copia esto:**

```python
# 🔑 CONFIGURACIÓN DE ALPACA API KEYS

# ⚠️ REEMPLAZA con tus propias keys (las que copiaste arriba)
API_KEY = "PKXXX..."  # ← Pega tu API Key ID aquí
SECRET_KEY = "xxx...xxx"  # ← Pega tu Secret Key aquí

# Conexión con Alpaca Paper Trading
from alpaca.trading.client import TradingClient

client = TradingClient(
    api_key=API_KEY,
    secret_key=SECRET_KEY,
    paper=True  # ← TRUE = Paper Trading (simulado)
)

# Verificar conexión
account = client.get_account()
print(f"✅ Conectado a Alpaca Paper Trading")
print(f"💰 Balance: ${account.cash} USD (simulado)")
print(f"📊 Buying Power: ${account.buying_power} USD")
print(f"🔒 Account Status: {account.status}")
```

**Ejecutar:**
1. **ANTES:** Reemplaza `"PKXXX..."` y `"xxx...xxx"` con TUS keys reales
2. Click en ▶️ o `Shift + Enter`
3. **Debe mostrar:**
```
✅ Conectado a Alpaca Paper Trading
💰 Balance: $100000.0 USD (simulado)
📊 Buying Power: $100000.0 USD
🔒 Account Status: ACTIVE
```

**Si hay error "401 Unauthorized":**
- Verifica que copiaste las keys correctamente (sin espacios extra)
- Verifica que estás en modo "Paper" (NO "Live")
- Regenera keys en Alpaca dashboard si persiste

---

## 🚀 PASO 6: DESCARGAR PRIMER DATASET

### Descargar Datos de SPY (3 minutos)

**SPY = ETF del S&P 500 (las 500 empresas más grandes de US)**

**Crea nueva celda y copia:**

```python
# 📊 DESCARGAR DATOS HISTÓRICOS DE SPY

import yfinance as yf
import pandas as pd

# Descargar datos de SPY (últimos 5 años)
ticker = "SPY"
data = yf.download(ticker, start="2020-01-01", end="2025-01-01")

# Ver primeras 5 filas
print(f"✅ Datos de {ticker} descargados")
print(f"📅 Rango: {data.index[0]} a {data.index[-1]}")
print(f"📊 Total de días: {len(data)}")
print("\n📈 Primeras 5 filas:")
print(data.head())

# Ver estructura
print("\n📋 Columnas disponibles:")
print(data.columns.tolist())
```

**Ejecutar:**
- Debe mostrar tabla con datos OHLCV (Open, High, Low, Close, Volume)
- Aproximadamente 1,260 días de datos

**Output esperado:**
```
✅ Datos de SPY descargados
📅 Rango: 2020-01-02 a 2024-12-31
📊 Total de días: 1260

📈 Primeras 5 filas:
              Open    High     Low   Close  Adj Close     Volume
Date                                                             
2020-01-02  324.87  325.00  322.75  323.50     323.50  85730000
2020-01-03  323.19  325.15  322.57  324.87     324.87  70230000
...
```

---

### Graficar Datos (Opcional)

**Si quieres ver gráfico de SPY:**

```python
# 📈 GRAFICAR PRECIO DE SPY

import matplotlib.pyplot as plt

# Graficar precio de cierre
plt.figure(figsize=(14, 6))
plt.plot(data.index, data['Close'], label='SPY Close Price', linewidth=1.5)
plt.title('SPY - S&P 500 ETF (2020-2024)', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Precio (USD)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("✅ Gráfico generado correctamente")
```

---

## 🚀 PASO 7: VALIDACIÓN COMPLETA

### Script de Validación Automática

**Crea nueva celda y copia todo esto:**

```python
# ✅ VALIDACIÓN COMPLETA DEL SETUP

print("🔍 VALIDANDO SETUP COMPLETO...\n")

# Test 1: Librerías
try:
    import pandas as pd
    import numpy as np
    import yfinance as yf
    from alpaca.trading.client import TradingClient
    import ta
    print("✅ Test 1/4: Librerías importadas correctamente")
except Exception as e:
    print(f"❌ Test 1/4: Error en importación - {e}")

# Test 2: Conexión Alpaca
try:
    account = client.get_account()
    if account.status == "ACTIVE":
        print(f"✅ Test 2/4: Conexión Alpaca OK (Balance: ${account.cash} simulado)")
    else:
        print(f"⚠️ Test 2/4: Cuenta Alpaca no activa - Status: {account.status}")
except Exception as e:
    print(f"❌ Test 2/4: Error de conexión - {e}")

# Test 3: Descarga de datos
try:
    test_data = yf.download("SPY", start="2024-01-01", end="2024-01-10", progress=False)
    if len(test_data) > 0:
        print(f"✅ Test 3/4: Descarga de datos OK ({len(test_data)} días)")
    else:
        print("❌ Test 3/4: No se descargaron datos")
except Exception as e:
    print(f"❌ Test 3/4: Error en descarga - {e}")

# Test 4: Procesamiento básico
try:
    sma_20 = data['Close'].rolling(20).mean()
    if not sma_20.isna().all():
        print(f"✅ Test 4/4: Procesamiento de datos OK (SMA calculada)")
    else:
        print("❌ Test 4/4: Error en cálculo de indicadores")
except Exception as e:
    print(f"❌ Test 4/4: Error en procesamiento - {e}")

print("\n" + "="*50)
print("🎉 SETUP COMPLETADO EXITOSAMENTE")
print("="*50)
print("\n📋 RESUMEN:")
print(f"✅ Google Colab: Funcionando")
print(f"✅ Librerías: Instaladas")
print(f"✅ Broker Alpaca: Conectado")
print(f"✅ Datos históricos: Disponibles")
print(f"\n🚀 ¡Estás listo para empezar el workshop!")
```

**Ejecutar:**
- **Todos los tests deben mostrar ✅**
- Si alguno muestra ❌, revisa esa sección específica

---

## 🚨 TROUBLESHOOTING RÁPIDO

### Top 5 Errores Comunes

#### **ERROR 1: "ModuleNotFoundError: No module named 'yfinance'"**

**Causa:** Librería no instalada o runtime reiniciado

**Solución:**
1. Vuelve a ejecutar la celda de instalación de librerías
2. Si persiste: `Runtime` → `Restart runtime`
3. Ejecuta todas las celdas desde el inicio

---

#### **ERROR 2: "401 Unauthorized" (Alpaca)**

**Causa:** API Keys incorrectas o modo incorrecto

**Solución:**
1. Verifica que copiaste las keys sin espacios extra
2. Confirma que estás en "Paper Trading" (NO "Live") en Alpaca dashboard
3. Regenera keys en Alpaca si es necesario

---

#### **ERROR 3: "Session crashed"**

**Causa:** Colab sin memoria o timeout

**Solución:**
1. `Runtime` → `Disconnect and delete runtime`
2. `Runtime` → `Connect`
3. Ejecuta todas las celdas desde el inicio

---

#### **ERROR 4: "KeyError: 'Close'" en datos**

**Causa:** Descarga de datos falló o ticker incorrecto

**Solución:**
1. Verifica que el ticker es correcto ("SPY" no "spy")
2. Verifica tu conexión a internet
3. Espera 5 minutos y reintenta (APIs a veces tienen rate limits)

---

#### **ERROR 5: Runtime desconectado durante el workshop**

**Causa:** 90 minutos de inactividad

**Solución:**
1. Reconnect: `Runtime` → `Connect`
2. Ejecuta celda de instalación de librerías
3. Ejecuta celda de configuración de Alpaca
4. Continúa donde te quedaste

---

**Más errores:** [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

## 🎯 PRÓXIMOS PASOS

### ✅ Setup Completado

**¡Felicitaciones! Has completado el Setup A en 30-45 minutos.** 🎉

**Ahora tienes:**
- ✅ Google Colab funcionando
- ✅ Librerías instaladas
- ✅ Broker conectado (Alpaca Paper)
- ✅ Primer dataset descargado (SPY)
- ✅ Entorno 100% funcional para el workshop

---

### 📚 Antes de la Sesión 1

**1. Lee estos documentos:**
- [Guía de Inicio](GUIA_INICIO.md) - Roadmap completo del workshop
- [Programa Detallado](Programa_Detallado_Workshop.md) - Qué aprenderás en cada sesión

**2. Guarda tu notebook:**
- El notebook está en tu Google Drive
- Puedes acceder siempre desde [colab.research.google.com](https://colab.research.google.com)
- Carpeta: "Colab Notebooks" en tu Drive

**3. Únete al grupo:**
- Recibirás invitación por email
- Grupo Premium para soporte comunitario

---

### 🚀 ¡Listo para Empezar!

**Próxima parada:** [Sesión 1: Fundamentos del Trading Algorítmico](Programa_Detallado_Workshop.md)

---

## 🔗 VER TAMBIÉN

**Otras rutas de Setup A:**
- [Setup A: Express](Setup_A_Express.md) - Fast track para usuarios experimentados (10-15 min)
- [Setup A: Guiado](Setup_A_Guiado.md) - Exhaustivo con screenshots (60-90 min)

**Siguiente paso:**
- [Guía Setup Completa](Guia_Setup_Completa.md) - Hub de todos los setups

**Si encuentras problemas:**
- [Troubleshooting Maestro](Troubleshooting_Maestro.md) - Hub central de soluciones

---

## 🔗 NAVEGACIÓN

**◀️ Anterior:** [Guía de Inicio](GUIA_INICIO.md)  
**▶️ Siguiente:** [Setup B: Python Local](Setup_B_Python_Local.md)

**🏠 Volver a:**
- [Guía de Setup Completa](Guia_Setup_Completa.md)
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**📖 Ver también:**
- [Setup A Express](Setup_A_Express.md) - Versión rápida (10-15 min)
- [Setup A Guiado](Setup_A_Guiado.md) - Versión exhaustiva (60-90 min)
- [Troubleshooting Maestro](Troubleshooting_Maestro.md)
- [FAQ Completo](FAQ_COMPLETO.md)
- [SITEMAP](SITEMAP.md)

---

## 📞 SOPORTE

**¿Necesitas ayuda?**

- 📧 **Email:** yismaryme@gmail.com
- 💬 **Telegram:** [@yismary](https://t.me/yismary)

**Horario de soporte:**
- Lun-Vie: 9:00 AM - 6:00 PM (GMT-5)
- Respuesta promedio: 24-48 horas

**Nota:** Soporte técnico solo para participantes registrados del workshop.

---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
