# ⚡ SETUP A: COLAB RÁPIDO (30-45 min)


🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 📄 **Setup Colab Rápido**

---

**Workshop: Trading Algorítmico Aumentado con IA Generativa**  
**Versión:** 4.0 (Noviembre 2025)  
**Dificultad:** ⭐ Fácil (No requiere experiencia en programación)

---

## 🎯 Elige Tu Ruta de Setup

**Tienes DOS rutas para completar el setup. Ambas usan código ya funcionando.**

⚠️ **IMPORTANTE:** En ambas rutas, **NO vas a programar**. Todo el código ya está escrito y listo para usar. Solo ejecutas y validas que funcione.

---

### ⚡ RUTA A: EXPRESS (5-10 min)

**Ejecución directa sin explicaciones**

✅ **Para ti si:**
- Tienes prisa antes del workshop
- Ya usaste notebooks de Colab antes
- Solo quieres validar que todo funcione

✅ **Qué harás:**
- Descargas notebook ya hecho
- Lo subes a Colab
- Ejecutas cada celda (código pre-escrito)
- Validación automática

❌ **NO harás:**
- Programar o escribir código
- Modificar nada (código ya correcto)

📥 **DESCARGAR NOTEBOOK:**

**Opción 1 - Descarga Directa (Recomendada):**
[Click derecho → Guardar enlace como... → Setup_y_Practica_Trading.ipynb](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb)

**Opción 2 - Desde GitHub:**
1. Ve a: https://github.com/yismafx/workshop-trading-algoritmico-kit
2. Navega a: `00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb`
3. Click en "Raw" (esquina superior derecha)
4. Ctrl+S para guardar

**Pasos después de descargar:**
1. Ve a: https://colab.research.google.com
2. File → Upload notebook
3. Selecciona el archivo `.ipynb` que descargaste
4. Ejecuta cada celda (Shift+Enter)

**Tiempo:** 5-10 minutos

---

### 📖 RUTA B: GUIADA (15-20 min)

**Ejecución con explicaciones paso a paso**

✅ **Para ti si:**
- Es tu primera vez con notebooks de trading
- Quieres entender QUÉ hace cada herramienta
- Prefieres ver el flujo completo explicado

✅ **Qué harás:**
- Lees explicaciones de cada paso
- Ejecutas código pre-escrito (no lo escribes tú)
- Entiendes QUÉ hace cada componente
- Familiarización con el entorno

❌ **NO harás:**
- Programar o crear código desde cero
- Aprender sintaxis de Python
- Escribir scripts

📋 **Sigue los pasos detallados en este documento** ⬇️

**Tiempo:** 15-20 minutos

---

### 💡 ¿Cuál Ruta Elegir?

**USA RUTA A (EXPRESS) SI:**
- ⏱️ Tienes poco tiempo
- ✅ Ya conoces notebooks
- 🎯 Solo quieres validar y seguir

**USA RUTA B (GUIADA) SI:**
- 📚 Primera vez con notebooks de trading
- 🧠 Quieres entender el flujo
- 📖 Prefieres explicaciones detalladas

**¿AÚN CON DUDAS?**
- 👉 Empieza con **Ruta B** (más contexto)
- 💡 Si te atascas, cambia a **Ruta A**

---

### 🎯 Mensaje Clave del Workshop

> ⚠️ **NO vas a convertirte en programador**  
> ✅ Usarás herramientas **ya funcionando**  
> ✅ En el workshop, IA te ayudará a **ADAPTAR** (no crear desde cero)  
> ✅ Serás **usuario avanzado** de sistemas de trading

**Setup = Instalar y validar herramientas pre-hechas**  
**Workshop = Usar y adaptar con IA como copiloto**

---

**📌 Recomendación del Instructor:**

> Primera vez con notebooks → **Ruta B** (contexto valioso)  
> Ya tienes experiencia → **Ruta A** (eficiencia)

---

## 📑 Tabla de Contenidos

- [🎯 Elige Tu Camino de Setup](#-elige-tu-camino-de-setup)
- [🎯 ¿Es Este Setup Para Ti?](#-es-este-setup-para-ti)
- [🧭 El Camino de Aprendizaje: Python Primero](#-el-camino-de-aprendizaje-python-primero)
- [✅ Requisitos Mínimos](#-requisitos-mínimos)
- [🚀 Guía de Setup Paso a Paso](#-guía-de-setup-paso-a-paso)
- [🎓 Conectar con el Colab Notebook Maestro](#-conectar-con-el-colab-notebook-maestro)
- [🔍 Validación del Setup](#-validación-del-setup)
- [🚨 Troubleshooting Específico](#-troubleshooting-específico)
- [💡 Consejos y Mejores Prácticas](#-consejos-y-mejores-prácticas)
- [🎯 Próximos Pasos](#-próximos-pasos)

---

## 🎯 ¿Es Este Setup Para Ti?

**✅ Este setup es PERFECTO si:**

- 📊 Eres **trader profesional** con años de experiencia
- ❌ **NO** tienes experiencia programando (¡esto es normal!)
- ❌ **NO** quieres instalar programas en tu computadora
- ✅ Quieres empezar a practicar **HOY** (en 30 minutos)
- ✅ Prefieres **aprender primero, automatizar después**
- ✅ Tienes conexión a internet estable
- ✅ Tienes o puedes crear una cuenta Gmail

**❌ Este setup NO es ideal si:**

- 🚀 Ya necesitas poner sistemas funcionando 24/7 (ve a [Setup B: Python Local](Setup_B_Python_Local.md))
- 📊 Usas principalmente MetaTrader y quieres empezar ahí (ve a [Setup C: MT5](Setup_C_MetaTrader5.md))
- 💼 Ya tienes cuenta en Interactive Brokers y quieres usarla (ve a [Setup D: IB](Setup_D_Interactive_Brokers.md))

**📊 Dato del Workshop:**
> 🎯 **8 de cada 10 participantes** usan este setup exitosamente

---

## 🧭 El Camino de Aprendizaje: Python Primero

**🤔 "¿Por qué voy a aprender Python si yo opero en TradingView/MetaTrader?"**

Excelente pregunta. Aquí está la respuesta:

### 📍 Python es el "Lenguaje Universal" del Trading Algorítmico

**Piensa en Python como aprender inglés antes de otros idiomas:**

```
En Trading Manual:
│
├─ TradingView (Pine Script)     ← Limitado a gráficos de TV
├─ MetaTrader (MQL5)              ← Limitado a brokers MT5
└─ Interactive Brokers (TWS)      ← Limitado a IB
│
│
En Trading Algorítmico con Python:
│
Python (Lenguaje Base)            ← Funciona con TODO
│
├─ Descarga datos de CUALQUIER fuente
├─ Testea estrategias rigurosamente
├─ Conecta con CUALQUIER broker
└─ Y luego... (↓ Sesión 7 del workshop)
    │
    ├─→ Traduce a Pine Script (TradingView)
    ├─→ Traduce a MQL5 (MetaTrader)
    ├─→ Traduce a cualquier plataforma
    │
    └─ IA Generativa = Tu "Traductor Automático"
```

### 🎯 El Journey del Workshop (9 Sesiones)

**Sesiones 1-6: Fundamentos en Python** (18 horas)
- Aprendes a descargar datos
- Diseñas estrategias con IA
- Haces backtesting riguroso
- Gestionas riesgo profesionalmente

**→ Sesión 7: Multi-Plataforma** (3 horas) ⭐ **AQUÍ ES LA MAGIA**
- Conviertes tu código Python a Pine Script (TradingView)
- Conviertes tu código Python a MQL5 (MetaTrader)
- IA Generativa hace la traducción automática

**Sesiones 8-9: Producción** (6 horas)
- Pones tu sistema en funcionamiento continuo 24/7
- Documentas profesionalmente

### 💡 Analogía del Trader

**Es como aprender análisis técnico:**

- Primero dominas **indicadores fundamentales** (RSI, MACD, Bandas de Bollinger)
- Luego aplicas esos conceptos en **cualquier plataforma** (TradingView, MT5, ThinkOrSwim)

**Python es tu "indicador fundamental"** del trading algorítmico:
- Lo aprendes UNA VEZ
- Lo usas en TODAS las plataformas
- GenAI traduce por ti

### ⚠️ ¿Y si solo quiero usar TradingView/MetaTrader?

**Puedes, PERO:**

❌ Pine Script y MQL5 son lenguajes "cerrados" (solo funcionan en su plataforma)  
❌ Tienen limitaciones técnicas importantes  
❌ No tienen las herramientas de validación profesional que Python ofrece

✅ Con Python + GenAI, obtienes lo MEJOR de ambos mundos:
- Desarrollo riguroso en Python
- Ejecución en la plataforma que prefieras

**Confía en el proceso. Miles de traders profesionales han seguido este camino.**

---

## ✅ Requisitos Mínimos

**Lo que necesitas para empezar HOY:**

### 💻 Hardware (Equipo)

- Cualquier computadora con internet (no importa si es Mac, Windows o Linux)
- Conexión a internet: mínimo 3 Mbps (lo que usas para ver videos)
- Memoria RAM: 4 GB recomendado (2 GB funciona, pero será más lento)

### 🌐 Software (Programas)

- **Navegador web moderno:**
  - Google Chrome 90 o superior ⭐ Recomendado
  - Firefox 88 o superior
  - Safari 14 o superior
  - Edge 90 o superior
  
- **Cuenta Gmail:**
  - Si ya tienes Gmail → ✅ Listo
  - Si no tienes → La crearemos en Paso 1 (5 minutos)

### 🧠 Conocimientos

**Lo que SÍ necesitas saber:**
- ✅ Cómo usar un navegador web
- ✅ Cómo enviar y recibir emails
- ✅ Fundamentos de trading (esto ya lo dominas)

**Lo que NO necesitas saber:**
- ❌ Programación (empiezas desde cero)
- ❌ Matemáticas avanzadas (usaremos herramientas ya hechas)
- ❌ Inglés técnico (todo está en español)

### ⏱️ Tiempo

**Tiempo total del setup:**
- ⚡ **Ruta Express:** 5-10 minutos
- 📖 **Ruta Guiada:** 15-20 minutos
- 🚀 **Primera práctica:** 10-15 minutos adicionales (opcional)

---

## 🚀 Guía de Setup Paso a Paso

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ⬜ Paso 1: Cuenta Gmail (5 min)
├─ ⬜ Paso 2: Acceder a Colab (2 min)
├─ ⬜ Paso 3: Crear y configurar notebook (5 min)
├─ ⬜ Paso 4: Instalar herramientas (3-4 min)
├─ ⬜ Paso 5: Configurar Alpaca (3 min)
├─ ⬜ Paso 6: Descargar datos (2 min)
└─ ⬜ Paso 7: Validación final (2 min)

⏱️ Tiempo total estimado: 20-25 minutos
```

---

### 🟦 PASO 1: Cuenta Gmail (5 min)

**🎯 Objetivo:** Tener acceso a Google Colab

#### ✅ Si YA tienes cuenta Gmail:

**Verifica que funcione:**
1. Ve a: https://mail.google.com
2. Inicia sesión con tu email y contraseña
3. Si ves tu bandeja → ✅ Listo, salta al [Paso 2](#-paso-2-acceder-a-google-colab-2-min)

#### ❌ Si NO tienes cuenta Gmail:

**Crea una cuenta (5 minutos):**

1. Ve a: https://accounts.google.com/signup
2. Llena el formulario:
   - Nombre y apellido
   - Email deseado (ejemplo: `tu nombre@gmail.com`)
   - Contraseña segura (mínimo 8 caracteres, mezcla letras y números)
3. Verifica tu teléfono (Gmail te enviará un código SMS)
4. Acepta términos y condiciones
5. ¡Listo! Ya tienes Gmail

**💡 Consejo:** Usa una contraseña que recuerdes pero que sea segura. Ejemplo: `TradingAlgo2025!`

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 2:**
- Estás en tu bandeja de entrada de Gmail
- Puedes enviar y recibir correos

❌ Si no puedes iniciar sesión → Ve a [Troubleshooting: Problemas con Gmail](#-error-1-no-puedo-crear-cuenta-gmail)

---

### 🟦 PASO 2: Acceder a Google Colab (2 min)

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ✅ Paso 1: Cuenta Gmail (5 min)
├─ ⏳ Paso 2: Acceder a Colab (2 min) ← ESTÁS AQUÍ (10% completado)
├─ ⬜ Paso 3: Crear y configurar notebook (5 min)
├─ ⬜ Paso 4: Instalar herramientas (3-4 min)
├─ ⬜ Paso 5: Configurar Alpaca (3 min)
├─ ⬜ Paso 6: Descargar datos (2 min)
└─ ⬜ Paso 7: Validación final (2 min)
```

**🎯 Objetivo:** Abrir Google Colab por primera vez

**Pasos:**

1. **Abre tu navegador** (Chrome, Firefox, Safari o Edge)

2. **Ve a la URL de Colab:**  
   https://colab.research.google.com

3. **Inicia sesión con tu Gmail**
   - Usa el email y contraseña que creaste/verificaste en Paso 1
   - Acepta los permisos que Colab pida

4. **¡Listo!** Deberías ver la pantalla de bienvenida de Colab

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 3:**
[🔲 SCREENSHOT PLACEHOLDER: Pantalla de bienvenida de Colab]
- Pantalla de Google Colab con logo naranja/amarillo
- Mensaje "Welcome to Colaboratory"
- Opción de crear un nuevo notebook

❌ Si ves un error o pantalla en blanco → Ve a [Troubleshooting: Problemas con Colab](#-error-2-colab-no-carga-o-pantalla-en-blanco)

**💡 Tip importante:**

> **Guarda este enlace en tus favoritos:**  
> https://colab.research.google.com
>
> Lo usarás TODOS LOS DÍAS del workshop.

---

### 🟦 PASO 3: Crear y Configurar Notebook (5 min)

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ✅ Paso 1: Cuenta Gmail (5 min)
├─ ✅ Paso 2: Acceder a Colab (2 min)
├─ ⏳ Paso 3: Crear y configurar notebook (5 min) ← ESTÁS AQUÍ (25% completado)
├─ ⬜ Paso 4: Instalar herramientas (3-4 min)
├─ ⬜ Paso 5: Configurar Alpaca (3 min)
├─ ⬜ Paso 6: Descargar datos (2 min)
└─ ⬜ Paso 7: Validación final (2 min)
```

**🎯 Objetivo:** Crear tu primer notebook de trading y entender el entorno

---

#### 📝 PASO 3.1: Crear Nuevo Notebook (1 min)

**Estás en:** Pantalla de bienvenida de Colab

**Pasos:**
1. Click en **"New notebook"** (esquina superior izquierda)
   - O usa el atajo: **File → New notebook**

2. Se abrirá un notebook vacío con el nombre "Untitled0.ipynb"

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa:**
[🔲 SCREENSHOT PLACEHOLDER: Notebook vacío recién creado]
- Notebook con nombre "Untitled0.ipynb" en la esquina superior izquierda
- Una celda de código vacía en el centro
- Barra de herramientas en la parte superior

---

#### 🏷️ PASO 3.2: Nombrar tu Notebook (1 min)

**Por qué es importante:**  
> Dar un nombre descriptivo te ayudará a encontrar tu notebook después. Además, seguiremos una convención de nombres estándar para el workshop.

**Pasos:**

1. **Click en "Untitled0.ipynb"** (esquina superior izquierda)

2. **Cambia el nombre a:**  
   `Setup_y_Practica_Trading.ipynb`

3. **Presiona Enter** para guardar el nombre

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa:**
[🔲 SCREENSHOT PLACEHOLDER: Notebook con nombre correcto]
- El nombre del notebook ahora dice "Setup_y_Practica_Trading.ipynb"
- El nombre está en la esquina superior izquierda

**💡 Nota sobre nombres:**
- La extensión `.ipynb` significa "Interactive Python Notebook"
- Colab la agrega automáticamente, no te preocupes si no la ves

---

#### 🎨 PASO 3.3: Entender la Interfaz de Colab (2 min)

**Antes de escribir código, entiende las partes del notebook:**

```
┌──────────────────────────────────────────────────────────┐
│  Setup_y_Practica_Trading.ipynb           [▶ Share] [⚙]│  ← Nombre y controles
├──────────────────────────────────────────────────────────┤
│  File  Edit  View  Insert  Runtime  Tools  Help         │  ← Menú principal
├──────────────────────────────────────────────────────────┤
│  [+ Code]  [+ Text]                                      │  ← Botones para agregar celdas
├──────────────────────────────────────────────────────────┤
│                                                           │
│  [ ]  # Tu código va aquí                       [▶]      │  ← Celda de código
│       print("Hola Trading")                               │
│                                                           │
├──────────────────────────────────────────────────────────┤
│  Output: (aquí aparece el resultado)                     │  ← Resultado de la ejecución
└──────────────────────────────────────────────────────────┘
```

**Elementos clave:**

1. **Celdas de Código**  
   - Donde escribes código Python
   - Se ejecutan con ▶ (play button) o **Shift + Enter**
   - El output aparece abajo de la celda

2. **Celdas de Texto**  
   - Para agregar notas, explicaciones
   - Usan formato Markdown
   - No ejecutan código

3. **Botones principales:**
   - **▶ Run** - Ejecuta la celda actual
   - **+ Code** - Agrega celda de código
   - **+ Text** - Agrega celda de texto

**🔍 Verificación Visual:**

[🔲 SCREENSHOT PLACEHOLDER: Interfaz de Colab con elementos resaltados]
- Menú File/Edit/Runtime resaltado
- Botones +Code y +Text señalados
- Celda de código vacía mostrada
- Botón de ejecución (▶) resaltado

---

#### ⚡ PASO 3.4: Tu Primera Ejecución (1 min)

**Vamos a probar que todo funciona:**

**Pasos:**

1. **En la celda de código vacía, escribe:**

```python
print("¡Hola Trading Algorítmico!")
```

2. **Ejecuta la celda:**
   - Opción A: Click en el botón **▶** (play) a la izquierda de la celda
   - Opción B: Presiona **Shift + Enter** (atajo recomendado)

3. **Espera 2-3 segundos**  
   (La primera ejecución siempre toma un poco más)

4. **Verás el resultado abajo:**

```
¡Hola Trading Algorítmico!
```

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 4:**
[🔲 SCREENSHOT PLACEHOLDER: Celda ejecutada con output visible]
- Código `print("¡Hola Trading Algorítmico!")` en la celda
- Output "¡Hola Trading Algorítmico!" mostrado abajo
- Checkmark verde (✓) junto al botón de play

❌ Si ves un error rojo → Ve a [Troubleshooting: Error al ejecutar primera celda](#-error-3-error-al-ejecutar-primera-celda)

**💡 Concepto clave:**

> **Notebook vs Sesión:**
> - **Notebook** = El archivo (persiste, se guarda en tu Drive)
> - **Sesión** = La "máquina virtual" ejecutando (temporal, se reinicia)
>
> Cuando cierres Colab, el **notebook se guarda**, pero la **sesión se termina**.  
> Esto significa que las variables y las librerías instaladas SE PIERDEN.  
> Por eso instalaremos herramientas cada vez que abramos el notebook.

---

### 🟦 PASO 4: Instalar Herramientas (3-4 min)

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ✅ Paso 1: Cuenta Gmail (5 min)
├─ ✅ Paso 2: Acceder a Colab (2 min)
├─ ✅ Paso 3: Crear y configurar notebook (5 min)
├─ ⏳ Paso 4: Instalar herramientas (3-4 min) ← ESTÁS AQUÍ (50% completado)
├─ ⬜ Paso 5: Configurar Alpaca (3 min)
├─ ⬜ Paso 6: Descargar datos (2 min)
└─ ⬜ Paso 7: Validación final (2 min)
```

**🎯 Objetivo:** Instalar las librerías de trading que usaremos en el workshop

**⚠️ IMPORTANTE:** Estas librerías NO vienen pre-instaladas en Colab. Deberás ejecutar este paso CADA VEZ que abras el notebook (las librerías se instalan en la sesión temporal).

---

#### 📦 PASO 4.1: Entender Qué Vamos a Instalar (1 min)

**Las herramientas del taller:**

| Librería | Para qué sirve | Analogía Trader |
|----------|----------------|-----------------|
| **alpaca-py** | Descargar datos y ejecutar trades | Tu "conector" con el broker |
| **pandas** | Manipular datos (tablas, series de tiempo) | Tu "hoja de Excel" profesional |
| **numpy** | Cálculos matemáticos rápidos | Tu "calculadora científica" |
| **matplotlib** | Graficar precios y estrategias | Tu "TradingView" para análisis |
| **pandas-ta** | Indicadores técnicos (RSI, MACD, BBands) | Tu "biblioteca de indicadores" |

**📊 Dato tranquilizador:**  
> Estas son las librerías estándar que usan traders profesionales en todo el mundo. Están bien probadas y documentadas.

---

#### 💻 PASO 4.2: Ejecutar Instalación (2 min)

**Pasos:**

1. **Agrega una nueva celda de código:**
   - Click en **"+ Code"** (barra superior)
   - O usa el atajo: Hover sobre la celda anterior → Click en "+ Code" que aparece

2. **Copia y pega este código EN UNA SOLA CELDA:**

```python
# ==============================================
# 📦 INSTALACIÓN DE HERRAMIENTAS DE TRADING
# ==============================================
# NOTA: Ejecuta esta celda CADA VEZ que abras el notebook
# Tiempo de instalación: 2-3 minutos

print("🚀 Iniciando instalación de herramientas de trading...")
print("⏱️  Esto tomará 2-3 minutos. Es normal que veas texto de progreso.")
print("=" * 60)

# 1. Instalar alpaca-py (broker API)
print("\n📦 Instalando alpaca-py (API de broker)...")
!pip install alpaca-py --quiet

# 2. Instalar pandas (manipulación de datos)
print("✅ alpaca-py instalado")
print("\n📦 Instalando pandas (datos y tablas)...")
!pip install pandas --quiet
print("✅ pandas instalado")

# 3. Instalar numpy (cálculos matemáticos)
print("\n📦 Instalando numpy (matemáticas)...")
!pip install numpy --quiet
print("✅ numpy instalado")

# 4. Instalar matplotlib (gráficos)
print("\n📦 Instalando matplotlib (gráficos)...")
!pip install matplotlib --quiet
print("✅ matplotlib instalado")

# 5. Instalar pandas-ta (indicadores técnicos)
print("\n📦 Instalando pandas-ta (indicadores técnicos)...")
try:
    !pip install pandas-ta --no-deps --quiet
    print("✅ pandas-ta instalado")
except:
    print("⚠️  pandas-ta no se pudo instalar completamente")
    print("    (No es crítico - lo validaremos en el paso siguiente)")

print("\n" + "=" * 60)
print("✅ INSTALACIÓN COMPLETADA")
print("=" * 60)
print("\n⚠️  IMPORTANTE: REINICIA LA SESIÓN AHORA")
print("    📍 Runtime → Restart session")
print("    (Esto es obligatorio para que las librerías funcionen correctamente)")
```

3. **Ejecuta la celda:**  
   - Presiona **Shift + Enter**
   - O click en **▶** (play)

4. **Espera 2-3 minutos**  
   - Verás MUCHO texto desplazándose (es normal)
   - Líneas de progreso, descargas, instalaciones
   - Al final verás: "✅ INSTALACIÓN COMPLETADA"

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 4.3:**
[🔲 SCREENSHOT PLACEHOLDER: Instalación completada sin errores]
- Mensaje "✅ INSTALACIÓN COMPLETADA" visible
- Texto de advertencia "⚠️ IMPORTANTE: REINICIA LA SESIÓN AHORA"
- No hay mensajes rojos de "ERROR" críticos

⚠️ Si ves advertencias amarillas → **Es normal, continúa**  
❌ Si ves errores rojos que detienen la instalación → Ve a [Troubleshooting: Error en instalación](#-error-4-error-al-instalar-librerías)

---

#### 🔄 PASO 4.3: Reiniciar Sesión (CRÍTICO) (1 min)

**⚠️ MUY IMPORTANTE:** Después de instalar librerías, SIEMPRE debes reiniciar la sesión.

**Por qué es necesario:**
> Cuando instalas librerías nuevas, Python necesita "recargarlas" en memoria. Sin reinicio, algunas librerías podrían no funcionar correctamente o dar errores confusos más adelante.

**Pasos:**

1. **Ve al menú superior:**  
   - Click en **"Runtime"**

2. **Selecciona:**  
   - **"Restart session"**

3. **Confirma en el popup:**  
   - Click en **"Yes"** o **"Restart"**

4. **Espera 5-10 segundos**  
   - La página se refrescará
   - Verás el mensaje "Session restarted"

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 5:**
[🔲 SCREENSHOT PLACEHOLDER: Sesión reiniciada correctamente]
- Mensaje "Your session crashed after using all available RAM" NO debe aparecer
- El notebook sigue abierto
- Las celdas están intactas pero sin output (se limpiaron al reiniciar)

**💡 Recordatorio importante:**

> **Después de reiniciar:**
> - Las librerías están instaladas ✅
> - Las variables/código ejecutado se borró ❌
> - El notebook (archivo) sigue intacto ✅
>
> **Esto significa:** No necesitas volver a ejecutar el código de instalación AHORA.  
> Lo ejecutarás nuevamente la próxima vez que abras el notebook.

---

### 🟦 PASO 5: Configurar Alpaca (3 min)

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ✅ Paso 1: Cuenta Gmail (5 min)
├─ ✅ Paso 2: Acceder a Colab (2 min)
├─ ✅ Paso 3: Crear y configurar notebook (5 min)
├─ ✅ Paso 4: Instalar herramientas (3-4 min)
├─ ⏳ Paso 5: Configurar Alpaca (3 min) ← ESTÁS AQUÍ (75% completado)
├─ ⬜ Paso 6: Descargar datos (2 min)
└─ ⬜ Paso 7: Validación final (2 min)
```

**🎯 Objetivo:** Obtener llaves de API de Alpaca para descargar datos y practicar

---

#### 🤔 PASO 5.1: ¿Qué es Alpaca? (30 seg)

**Alpaca = Tu broker para practicar trading algorítmico**

**Características:**
- ✅ **Gratuito** para paper trading (dinero simulado)
- ✅ **API moderna** (fácil de usar con Python)
- ✅ **Datos en tiempo real** durante horas de mercado
- ✅ **Sin comisiones** en paper trading
- ✅ **No requiere capital real** (usaremos cuenta demo)

**💡 Analogía del Trader:**
> Alpaca es como un "simulador de trading" profesional. Tiene datos reales, pero tu dinero es ficticio. Perfecto para aprender sin riesgos.

---

#### 📝 PASO 5.2: Crear Cuenta en Alpaca (2 min)

**Pasos:**

1. **Ve a Alpaca:**  
   https://alpaca.markets

2. **Click en "Sign Up" o "Get Started"**  
   (esquina superior derecha)

3. **Completa el formulario:**
   - Email (usa tu Gmail)
   - Contraseña segura
   - Nombre completo
   - Acepta términos

4. **Verifica tu email:**
   - Alpaca te enviará un email de confirmación
   - Click en el link de verificación

5. **Inicia sesión** con tu nuevo usuario

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 5.3:**
[🔲 SCREENSHOT PLACEHOLDER: Dashboard de Alpaca después de login]
- Estás en el dashboard de Alpaca
- Ves opciones como "Paper Trading", "API Keys", "Portfolio"

---

#### 🔑 PASO 5.3: Obtener API Keys (Paper Trading) (1 min)

**⚠️ CRÍTICO:** Asegúrate de obtener las llaves de **PAPER TRADING**, NO de cuenta LIVE.

**Pasos:**

1. **En el dashboard de Alpaca:**  
   - Busca el menú lateral izquierdo
   - Click en **"Paper Trading"** o **"View Paper Account"**

2. **Ve a la sección de API:**  
   - Click en **"Your API Keys"** o similar
   - O navega a: https://app.alpaca.markets/paper/dashboard/overview

3. **Genera nuevas llaves:**  
   - Click en **"Generate"** o **"Regenerate API Keys"**
   - Confirma la acción

4. **Copia tus llaves:**  
   - Verás dos llaves:
     - **API KEY** (algo como: `PKA...`)
     - **SECRET KEY** (algo como: `...`)
   
   - ⚠️ **IMPORTANTE:** Copia ambas llaves a un archivo de texto temporal
   - ⚠️ **SECRET KEY solo se muestra UNA VEZ**. Si la pierdes, deberás regenerar ambas.

**🔍 Verificación Visual:**

✅ Si ves esto → **Perfecto, continúa al Paso 5.4:**
[🔲 SCREENSHOT PLACEHOLDER: API Keys de Alpaca (keys ofuscadas)]
- Dos campos con llaves:
  - API Key ID: `PK...` (pública)
  - Secret Key: `...` (privada, ofuscada en screenshot)
- Botón de "Regenerate" visible

**💡 Seguridad de las llaves:**

> **API KEY:** Es "pública" (como tu email). Puede estar visible en código.  
> **SECRET KEY:** Es "privada" (como tu contraseña). NUNCA la compartas públicamente.
>
> En este setup, las guardaremos de forma segura en el notebook.

---

#### 💻 PASO 5.4: Configurar Llaves en el Notebook (1 min)

**Volvamos a tu notebook de Colab:**

**Pasos:**

1. **Agrega una nueva celda de código** (+ Code)

2. **Copia y pega este código:**

```python
# ==============================================
# 🔑 CONFIGURACIÓN DE ALPACA API
# ==============================================
# INSTRUCCIONES:
# 1. Reemplaza "TU_API_KEY_AQUI" con tu API Key de Alpaca
# 2. Reemplaza "TU_SECRET_KEY_AQUI" con tu Secret Key de Alpaca
# 3. Ejecuta esta celda (Shift + Enter)

# ⚠️ IMPORTANTE: Estas son llaves de PAPER TRADING (dinero simulado)
#               NUNCA uses llaves de cuenta LIVE aquí

ALPACA_API_KEY = "TU_API_KEY_AQUI"
ALPACA_SECRET_KEY = "TU_SECRET_KEY_AQUI"
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"  # Paper trading (simulado)

# Validación rápida
if ALPACA_API_KEY == "TU_API_KEY_AQUI" or ALPACA_SECRET_KEY == "TU_SECRET_KEY_AQUI":
    print("❌ ERROR: Debes reemplazar las llaves con tus llaves reales de Alpaca")
    print("    Ve a https://app.alpaca.markets/paper/dashboard/overview")
else:
    print("✅ Llaves de Alpaca configuradas correctamente")
    print(f"   API Key: {ALPACA_API_KEY[:8]}... (primeros 8 caracteres)")
    print(f"   Usando: PAPER TRADING (dinero simulado)")
```

3. **Reemplaza las llaves:**
   - Borra `"TU_API_KEY_AQUI"` y pega tu API Key
   - Borra `"TU_SECRET_KEY_AQUI"` y pega tu Secret Key
   - Deja las comillas (`"..."`)

4. **Ejemplo de cómo debería verse:**

```python
ALPACA_API_KEY = "PKXXXXXXXXXXXXXX"  # Tu llave real
ALPACA_SECRET_KEY = "aBcDeF1234567890aBcDeF1234567890"  # Tu llave real
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"
```

5. **Ejecuta la celda:**  
   - Presiona **Shift + Enter**

6. **Verás:**

```
✅ Llaves de Alpaca configuradas correctamente
   API Key: PKXXXXXX... (primeros 8 caracteres)
   Usando: PAPER TRADING (dinero simulado)
```

**🔍 Verificación Visual:**

✅ Si ves el mensaje de éxito → **Perfecto, continúa al Paso 6**

❌ Si ves "ERROR: Debes reemplazar las llaves" → Revisa que pegaste tus llaves correctamente

---

### 🟦 PASO 6: Descargar Datos (Primera Prueba) (2 min)

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ✅ Paso 1: Cuenta Gmail (5 min)
├─ ✅ Paso 2: Acceder a Colab (2 min)
├─ ✅ Paso 3: Crear y configurar notebook (5 min)
├─ ✅ Paso 4: Instalar herramientas (3-4 min)
├─ ✅ Paso 5: Configurar Alpaca (3 min)
├─ ⏳ Paso 6: Descargar datos (2 min) ← ESTÁS AQUÍ (90% completado)
└─ ⬜ Paso 7: Validación final (2 min)
```

**🎯 Objetivo:** Descargar datos históricos del SPY (S&P 500 ETF) y validar que todo funciona

---

#### 📊 PASO 6.1: Descargar Datos del SPY (1 min)

**SPY = ETF que sigue al S&P 500 (las 500 empresas más grandes de USA)**

**Pasos:**

1. **Agrega una nueva celda de código** (+ Code)

2. **Copia y pega este código:**

```python
# ==============================================
# 📊 DESCARGA DE DATOS HISTÓRICOS (SPY)
# ==============================================
# Vamos a descargar datos del SPY de los últimos 30 días

print("📊 Descargando datos del SPY (S&P 500 ETF)...")
print("⏱️  Esto tomará 5-10 segundos...")
print("=" * 60)

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta

# Crear cliente de datos
client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# Configurar la petición de datos
request_params = StockBarsRequest(
    symbol_or_symbols=["SPY"],  # Símbolo a descargar
    timeframe=TimeFrame.Day,     # Datos diarios
    start=datetime.now() - timedelta(days=30),  # Últimos 30 días
    end=datetime.now()
)

# Descargar datos
try:
    bars = client.get_stock_bars(request_params)
    spy_data = bars.df  # Convertir a DataFrame de pandas
    
    print("✅ DESCARGA EXITOSA")
    print("=" * 60)
    print(f"\n📊 Datos descargados:")
    print(f"   • Símbolo: SPY")
    print(f"   • Filas: {len(spy_data)}")
    print(f"   • Fecha inicial: {spy_data.index[0].strftime('%Y-%m-%d')}")
    print(f"   • Fecha final: {spy_data.index[-1].strftime('%Y-%m-%d')}")
    print(f"\n📈 Precios de cierre (últimos 5 días):")
    print(spy_data['close'].tail())
    
except Exception as e:
    print(f"❌ ERROR al descargar datos: {e}")
    print("\n💡 Posibles causas:")
    print("   1. Llaves de Alpaca incorrectas (revisa Paso 5)")
    print("   2. Sin conexión a internet")
    print("   3. Alpaca temporalmente no disponible (raro)")
```

3. **Ejecuta la celda:**  
   - Presiona **Shift + Enter**

4. **Espera 5-10 segundos**

5. **Verás:**

```
✅ DESCARGA EXITOSA
============================================================

📊 Datos descargados:
   • Símbolo: SPY
   • Filas: 21
   • Fecha inicial: 2025-10-15
   • Fecha final: 2025-11-14

📈 Precios de cierre (últimos 5 días):
timestamp
2025-11-08    590.25
2025-11-11    592.10
2025-11-12    591.85
2025-11-13    593.40
2025-11-14    594.25
Name: close, dtype: float64
```

**🔍 Verificación Visual:**

✅ Si ves "✅ DESCARGA EXITOSA" y precios del SPY → **Perfecto, continúa al Paso 7**

[🔲 SCREENSHOT PLACEHOLDER: Datos descargados correctamente]
- Mensaje "✅ DESCARGA EXITOSA"
- Tabla con fechas y precios del SPY
- No hay errores rojos

❌ Si ves "❌ ERROR al descargar datos" → Ve a [Troubleshooting: Error descargando datos](#-error-5-error-al-descargar-datos-de-alpaca)

---

### 🟦 PASO 7: Validación Final del Setup (2 min)

## 📍 DONDE ESTÁS AHORA

```
SETUP COMPLETO (RUTA GUIADA):
├─ ✅ Paso 1: Cuenta Gmail (5 min)
├─ ✅ Paso 2: Acceder a Colab (2 min)
├─ ✅ Paso 3: Crear y configurar notebook (5 min)
├─ ✅ Paso 4: Instalar herramientas (3-4 min)
├─ ✅ Paso 5: Configurar Alpaca (3 min)
├─ ✅ Paso 6: Descargar datos (2 min)
└─ ⏳ Paso 7: Validación final (2 min) ← ESTÁS AQUÍ (95% completado)
```

**🎯 Objetivo:** Validar que TODAS las herramientas funcionan correctamente

---

#### ✅ PASO 7.1: Script de Validación Completa (2 min)

**Vamos a ejecutar un script que verifica TODO:**

**Pasos:**

1. **Agrega una última celda de código** (+ Code)

2. **Copia y pega este código:**

```python
# ==============================================
# ✅ VALIDACIÓN COMPLETA DEL SETUP
# ==============================================
# Este script verifica que todo esté funcionando correctamente

print("🔍 VALIDACIÓN COMPLETA DEL SETUP")
print("=" * 60)

validation_results = []

# 1. Verificar librerías instaladas
print("\n📦 Verificando librerías instaladas...")
try:
    import alpaca
    validation_results.append(("Alpaca-py", "✅ OK"))
except:
    validation_results.append(("Alpaca-py", "❌ FALTA"))

try:
    import pandas as pd
    validation_results.append(("Pandas", "✅ OK"))
except:
    validation_results.append(("Pandas", "❌ FALTA"))

try:
    import numpy as np
    validation_results.append(("Numpy", "✅ OK"))
except:
    validation_results.append(("Numpy", "❌ FALTA"))

try:
    import matplotlib.pyplot as plt
    validation_results.append(("Matplotlib", "✅ OK"))
except:
    validation_results.append(("Matplotlib", "❌ FALTA"))

try:
    import pandas_ta as ta
    validation_results.append(("Pandas-TA", "✅ OK"))
except:
    validation_results.append(("Pandas-TA", "⚠️  OPCIONAL"))

# 2. Verificar configuración de Alpaca
print("\n🔑 Verificando configuración de Alpaca...")
try:
    if ALPACA_API_KEY != "TU_API_KEY_AQUI" and ALPACA_SECRET_KEY != "TU_SECRET_KEY_AQUI":
        validation_results.append(("Alpaca Keys", "✅ OK"))
    else:
        validation_results.append(("Alpaca Keys", "❌ NO CONFIGURADAS"))
except:
    validation_results.append(("Alpaca Keys", "❌ NO CONFIGURADAS"))

# 3. Verificar conexión a Alpaca
print("\n🌐 Verificando conexión a Alpaca...")
try:
    from alpaca.data.historical import StockHistoricalDataClient
    test_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
    validation_results.append(("Conexión Alpaca", "✅ OK"))
except:
    validation_results.append(("Conexión Alpaca", "❌ ERROR"))

# 4. Imprimir resultados
print("\n" + "=" * 60)
print("📊 RESULTADOS DE LA VALIDACIÓN")
print("=" * 60)

for item, status in validation_results:
    print(f"{item:.<30} {status}")

# 5. Veredicto final
print("\n" + "=" * 60)
failed = [item for item, status in validation_results if "❌" in status]
if len(failed) == 0:
    print("🎉 ¡TODO PERFECTO! SETUP COMPLETADO AL 100%")
    print("=" * 60)
    print("\n✅ Estás listo para empezar el workshop")
    print("✅ Puedes cerrar este notebook y esperar la Sesión 1")
else:
    print("⚠️  HAY PROBLEMAS EN EL SETUP")
    print("=" * 60)
    print(f"\n❌ Componentes con error: {', '.join(failed)}")
    print("\n💡 Revisa la sección de Troubleshooting de este documento")
```

3. **Ejecuta la celda:**  
   - Presiona **Shift + Enter**

4. **Revisa los resultados:**

**Ejemplo de output exitoso:**

```
🔍 VALIDACIÓN COMPLETA DEL SETUP
============================================================

📦 Verificando librerías instaladas...

🔑 Verificando configuración de Alpaca...

🌐 Verificando conexión a Alpaca...

============================================================
📊 RESULTADOS DE LA VALIDACIÓN
============================================================
Alpaca-py..................... ✅ OK
Pandas........................ ✅ OK
Numpy......................... ✅ OK
Matplotlib.................... ✅ OK
Pandas-TA..................... ✅ OK
Alpaca Keys................... ✅ OK
Conexión Alpaca............... ✅ OK

============================================================
🎉 ¡TODO PERFECTO! SETUP COMPLETADO AL 100%
============================================================

✅ Estás listo para empezar el workshop
✅ Puedes cerrar este notebook y esperar la Sesión 1
```

**🔍 Verificación Visual:**

✅ Si ves "🎉 ¡TODO PERFECTO! SETUP COMPLETADO AL 100%" → **¡FELICIDADES! Has terminado el setup**

[🔲 SCREENSHOT PLACEHOLDER: Validación exitosa completa]
- Todos los componentes con "✅ OK"
- Mensaje final "🎉 ¡TODO PERFECTO!"
- No hay "❌ ERROR" en ningún componente crítico

⚠️ Si algún componente muestra "❌" → Ve a la sección de [Troubleshooting](#-troubleshooting-específico) correspondiente

---

## 🎓 CONECTAR CON EL COLAB NOTEBOOK MAESTRO

**🎯 ¿Qué es el Colab Notebook Maestro?**

El **Colab Notebook Maestro** es tu "Manual de Código Completo" del workshop. Contiene TODO el código de las 9 sesiones, listo para usar y ejecutar.

---

### 📚 Setup vs Notebook Maestro: ¿Cuál es la diferencia?

```
Setup_y_Practica_Trading.ipynb = Tu cuaderno de notas personal
├─ Lo creaste tú desde cero (en este setup)
├─ Lo usas para practicar y experimentar
├─ Puedes modificarlo libremente sin miedo
└─ Es tu "sandbox" (caja de arena) para aprender

Colab_Notebook_Maestro.ipynb = El manual oficial del instructor
├─ Tiene TODO el código profesional de las 9 sesiones
├─ Código validado y testeado
├─ Contiene las estrategias guiadas del workshop
└─ Lo copias y adaptas a tu notebook personal
```

**💡 Analogía del Trader:**

> **Setup_y_Practica_Trading** = Tu "demo account" donde pruebas y aprendes  
> **Colab_Notebook_Maestro** = La "biblioteca de estrategias" profesionales

---

### 💻 Cómo Usar Ambos Notebooks Juntos

**Estrategia Recomendada (Durante el Workshop):**

**ANTES de cada sesión:**
1. Abre el **Notebook Maestro** en una pestaña del navegador
2. Abre tu **Setup_y_Practica_Trading** en otra pestaña
3. Durante la sesión, el instructor te dirá qué sección del Maestro usar

**DURANTE la sesión:**
1. Sigue la explicación del instructor en el Notebook Maestro
2. Copia el código relevante a tu notebook personal
3. Experimenta y modifica en tu notebook sin miedo

**DESPUÉS de la sesión:**
1. Practica ejecutando código del Maestro
2. Completa los ejercicios en tu notebook personal
3. Si algo falla, vuelve al Maestro como referencia

---

### 📥 Acceder al Colab Notebook Maestro

**Opción 1 - Abrir Directo en Colab (Recomendado):**

**Link Directo:**  
🔗 [Abrir Colab Notebook Maestro](https://colab.research.google.com/github/yismafx/workshop-trading-algoritmico-kit/blob/main/01_COLAB_NOTEBOOK_MAESTRO/Colab_Notebook_Maestro.ipynb)

**Pasos:**
1. Click en el link de arriba
2. Se abrirá automáticamente en Google Colab
3. **MUY IMPORTANTE:** Haz una copia personal
   - File → Save a copy in Drive
   - Renombra a: `Colab_Notebook_Maestro_[TuNombre].ipynb`

---

**Opción 2 - Descargar y Subir Manualmente:**

**Si el link directo no funciona:**

1. Descarga el notebook:  
   [Descargar Colab_Notebook_Maestro.ipynb](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/01_COLAB_NOTEBOOK_MAESTRO/Colab_Notebook_Maestro.ipynb)

2. Ve a Google Colab: https://colab.research.google.com

3. File → Upload notebook → Selecciona el archivo descargado

---

### 🗂️ Estructura del Notebook Maestro

**El Notebook Maestro está organizado por sesiones:**

```
Colab_Notebook_Maestro.ipynb
│
├─ 📘 INFORMACIÓN GENERAL
│   ├─ Bienvenida
│   ├─ Cómo usar este notebook
│   └─ Configuración inicial
│
├─ 🟦 SESIÓN 1: Fundamentos y Mapa
│   ├─ Código de teoría
│   ├─ Ejemplos prácticos
│   └─ Ejercicios de refuerzo
│
├─ 🟦 SESIÓN 2: Datos - La Base de Todo
│   ├─ Pipeline de datos completo
│   ├─ Validación y limpieza
│   └─ Ejercicios
│
├─ 🟦 SESIÓN 3: Ideación con GenAI
│   ├─ Framework de 5 pasos
│   ├─ Prompts estructurados
│   └─ Casos de uso
│
[... Sesiones 4-9 ...]
│
└─ 📚 APÉNDICES
    ├─ Cheat sheets
    ├─ Glosario
    └─ Referencias
```

---

### 📋 Checklist: ¿Estás Listo con el Notebook Maestro?

Antes de la Sesión 1, asegúrate de:

- [ ] Abriste el Colab Notebook Maestro
- [ ] Hiciste una copia personal en tu Google Drive
- [ ] Ejecutaste la sección "Configuración Inicial" del Maestro
- [ ] Configuraste tus llaves de Alpaca en el Maestro (igual que en el Setup)
- [ ] Puedes navegar entre las 9 sesiones del Maestro
- [ ] Tienes ambos notebooks abiertos (Setup personal + Maestro)

**Si marcaste todos ✅ → Estás 100% listo para el workshop**

---

### 🔄 Workflow Recomendado Durante el Workshop

**Flujo de trabajo ideal:**

```
1. INSTRUCTOR EXPLICA (Notebook Maestro) 
   ↓
2. TÚ COPIAS código relevante
   ↓
3. TÚ PEGAS en tu notebook personal
   ↓
4. TÚ EJECUTAS y experimentas
   ↓
5. TÚ MODIFICAS parámetros para aprender
   ↓
6. Si algo falla → Vuelves al Maestro como referencia
```

**💡 Regla de oro:**

> **Notebook Maestro = Solo lectura** (tu fuente de verdad)  
> **Tu notebook personal = Escritura y experimentación** (tu laboratorio)

---

### ❓ FAQ: Notebook Maestro

**P: ¿Puedo modificar el Notebook Maestro?**  
R: Sí, pero solo si hiciste una copia personal (File → Save a copy). NUNCA modifiques el original del repositorio.

**P: ¿Qué pasa si actualizo el Notebook Maestro?**  
R: Si hay actualizaciones, recibirás un aviso por Telegram. Descarga la nueva versión y haz merge con tus cambios.

**P: ¿Necesito el Notebook Maestro para el Setup?**  
R: No, el setup funciona independientemente. El Maestro se usa durante las sesiones del workshop.

**P: ¿Puedo usar solo el Notebook Maestro sin crear mi propio notebook?**  
R: Puedes, pero NO es recomendado. Necesitas un espacio para experimentar sin miedo a romper cosas.

---

## 🔍 Validación del Setup

[... continúa con la sección original de validación ...]

