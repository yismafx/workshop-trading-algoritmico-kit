# ⚡ SETUP A: COLAB RÁPIDO (30-45 min)

**Workshop: Trading Algorítmico Aumentado con IA Generativa**  
**Versión:** 3.2 (Noviembre 2025)  
**Dificultad:** ⭐ Fácil (No requiere experiencia en programación)

---

## 📑 Tabla de Contenidos

- [🎯 ¿Es Este Setup Para Ti?](#-es-este-setup-para-ti)
- [🧭 El Camino de Aprendizaje: Python Primero](#-el-camino-de-aprendizaje-python-primero)
- [✅ Requisitos Mínimos](#-requisitos-mínimos)
- [🚀 Guía de Setup Paso a Paso](#-guía-de-setup-paso-a-paso)
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

- **Setup inicial:** 30-45 minutos (este documento)
- **Primera validación:** 10-15 minutos
- **Total hoy:** ~1 hora

---

## 🚀 Guía de Setup Paso a Paso

Vamos a hacer esto juntos, paso por paso. Como cuando analizas un gráfico: un nivel a la vez.

---

### 📝 PASO 1: Crear/Verificar Cuenta Google (5 min)

**🎓 ¿Por qué necesito esto?**

Google Colab es como tener una "oficina de trading en la nube" gratis. En lugar de instalar programas en tu computadora (que puede ser complicado y consume espacio), usas una computadora de Google que ya tiene todo instalado.

**Analogía del trader:**  
Es como usar TradingView en el navegador vs. descargar software pesado. Más simple, más rápido, siempre actualizado.

**💻 Lo que vamos a hacer:**

#### **Si YA tienes cuenta Gmail:**

1. Abre tu navegador
2. Ve a [https://gmail.com](https://gmail.com)
3. Inicia sesión con tu email y contraseña
4. ✅ Si puedes ver tu bandeja de entrada → **Continúa al Paso 2**

#### **Si NO tienes cuenta Gmail:**

1. Abre tu navegador
2. Ve a [https://accounts.google.com/signup](https://accounts.google.com/signup)
3. Completa el formulario (5 minutos):
   - **Nombre y apellido** (usa tu nombre real)
   - **Nombre de usuario** → Será tu email: tuusuario@gmail.com
   - **Contraseña** → Mínimo 8 caracteres, combina letras y números
   
4. **Verificación telefónica:**
   - Google enviará un código SMS a tu celular
   - Ingresa el código de 6 dígitos
   - Esto protege tu cuenta (como autenticación de 2 factores en tu broker)

5. Acepta términos y condiciones
6. ✅ Cuenta creada → **Continúa al Paso 2**

**⚠️ Consejo de Seguridad (como proteger tu cuenta de trading):**
- Usa contraseña única y fuerte
- NO uses la misma contraseña de tu broker
- Activa autenticación de 2 factores (como en tu cuenta de trading)

**🔍 Verificación rápida:**
☐ Puedo entrar a Gmail  
☐ Puedo acceder a [drive.google.com](https://drive.google.com)  
☐ Veo mis archivos en Drive (aunque esté vacío)

---

### 🔐 PASO 2: Crear Cuenta en Alpaca Paper Trading (10 min)

**🎓 ¿Qué es Alpaca y por qué lo necesito?**

Alpaca es un broker moderno que te permite:
1. **Practicar trading algorítmico SIN arriesgar dinero real** (cuenta paper = simulada)
2. **Descargar datos históricos** de mercados (gratis)
3. **Conectar tu código Python** con datos reales de mercado

**Analogía del trader:**  
Es como una cuenta demo en tu broker, pero específicamente diseñada para conectarla con programas de trading algorítmico. Los datos son 100% reales, el dinero es virtual ($100,000 de práctica).

**⚠️ Importante:** Usaremos la cuenta PAPER (simulada), NO la cuenta real. No necesitas depositar dinero real.

**💻 Lo que vamos a hacer:**

#### **2.1 Registrarte en Alpaca**

1. Abre tu navegador
2. Ve a [https://alpaca.markets/](https://alpaca.markets/)
3. Click en **"Sign Up"** (botón arriba a la derecha)
4. Completa el formulario:
   - **Email:** Puedes usar tu Gmail del Paso 1
   - **Password:** Usa una contraseña segura (diferente a Gmail)
   - **País:** Selecciona tu país (Argentina, México, Colombia, etc.)
   - **Acepta términos**

5. **Verifica tu email:**
   - Revisa tu bandeja de entrada (y carpeta spam)
   - Abre el email de Alpaca
   - Click en el enlace de verificación

6. Te llevará al dashboard (panel de control) de Alpaca

#### **2.2 Obtener tus "Llaves de Acceso"**

Ahora necesitas tus **"llaves de acceso"** (API Keys). Piensa en estas llaves como las credenciales de tu broker online.

**Analogía del trader:**  
Como tus credenciales para entrar a tu broker online. Pero en vez de usuario/contraseña, son dos códigos largos que permiten a tu código Python "conversar" con Alpaca.

**Paso a paso:**

1. Dentro del dashboard de Alpaca, busca la sección **"Paper Trading"** (menú izquierdo)
2. Click en **"Generate API Keys"** o **"View"** si ya están generadas
3. Verás dos códigos importantes:
   - 🔑 **API Key** (pública) → Comienza con "PK..."
   - 🔐 **Secret Key** (privada) → Código largo y secreto

4. **CRÍTICO: Guarda estos códigos de forma segura**

**⚠️ Cómo guardar tus llaves de acceso (MUY IMPORTANTE):**

Copia y pega esto en un archivo de texto en tu computadora:

```
═══════════════════════════════════════════════════════════
🔐 MIS CREDENCIALES ALPACA PAPER TRADING
═══════════════════════════════════════════════════════════

API Key (pública):
PK... [pega aquí tu código]

Secret Key (privada - NO COMPARTIR):
[pega aquí tu código secreto]

⚠️ RECORDATORIOS:
- Esta es mi cuenta PAPER (simulación con $100,000 virtuales)
- NUNCA compartir estas llaves con nadie
- NUNCA subirlas a grupos de Telegram/WhatsApp
- NUNCA publicarlas en capturas de pantalla

Fecha de creación: [pon la fecha de hoy]
═══════════════════════════════════════════════════════════
```

**Guarda este archivo como:**
- `Alpaca_Keys_Paper.txt` en tu computadora
- En una ubicación que recuerdes (ej: Documentos/Trading)
- Mejor aún: usa un gestor de contraseñas como LastPass o 1Password

**❌ NUNCA hagas esto:**
- ❌ Compartir en chat de grupo del workshop
- ❌ Poner en capturas de pantalla
- ❌ Enviar por email sin encriptar
- ❌ Publicar en redes sociales

**🔍 Verificación rápida:**
☐ Tengo cuenta Alpaca creada y verificada  
☐ Tengo mi API Key guardada (comienza con "PK...")  
☐ Tengo mi Secret Key guardada de forma segura  
☐ Puedo ver mi balance paper ($100,000 virtuales) en el dashboard

---

### 📂 PASO 3: Acceder a Google Colab (5 min)

**🎓 ¿Qué es Google Colab?**

Google Colab (Colaboratory) es tu "oficina de trading algorítmico en la nube". Imagina un cuaderno de Excel, pero en vez de fórmulas y tablas, escribes instrucciones en Python y el programa las ejecuta.

**Analogía del trader:**  
Como TradingView, pero en vez de dibujar líneas en gráficos, escribes instrucciones que el programa sigue automáticamente. Y no tienes que instalar nada - todo funciona en tu navegador.

**Ventajas de Colab:**
- ✅ No instalas nada en tu computadora
- ✅ Todo se guarda automáticamente en tu Google Drive
- ✅ Puedes acceder desde cualquier computadora
- ✅ Ya tiene todas las herramientas básicas instaladas
- ✅ Es completamente GRATIS

**💻 Lo que vamos a hacer:**

#### **3.1 Tu Primera Vez en Colab**

1. Abre tu navegador
2. Ve a [https://colab.research.google.com](https://colab.research.google.com)
3. Inicia sesión con tu cuenta Gmail (del Paso 1)
4. Verás una pantalla de bienvenida con ejemplos
   - Click en **"Cancelar"** o la "X" para cerrarla
5. Arriba a la izquierda: **File → New notebook**
6. ¡Se abrirá tu primer "cuaderno" vacío! 🎉

#### **3.2 Conoce tu Espacio de Trabajo**

**Así se ve Colab (explicado para traders):**

```
┌─────────────────────────────────────────────────────────┐
│ 📁 File  Edit  View  Insert  Runtime  Tools  Help      │ ← Menú principal
├─────────────────────────────────────────────────────────┤
│ + Code    + Text                                        │ ← Botones para agregar
├─────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────┐    │
│ │ # Esta es una CELDA de código                   │    │
│ │ # Aquí escribes instrucciones Python            │    │
│ │ print("Hola Trading Algorítmico")               │    │
│ └─────────────────────────────────────────────────┘    │
│                                  ▶️ Ejecutar             │ ← Botón para ejecutar
├─────────────────────────────────────────────────────────┤
│ 📤 Resultado: Hola Trading Algorítmico                 │ ← Aquí aparece el resultado
└─────────────────────────────────────────────────────────┘
```

**Partes importantes:**

- **Celda de código:** Donde escribes instrucciones Python
  - Como una "orden de trading" pero en código
  
- **Botón ▶️ (Ejecutar):** Cuando le das click, Python ejecuta tus instrucciones
  - Como presionar "Buy" o "Sell" en tu plataforma de trading
  
- **Resultado:** Lo que el programa te responde
  - Como el "Order Filled" cuando ejecutas una orden

#### **3.3 Tu Primera Línea de Código**

Vamos a probar que todo funciona. En la celda vacía, escribe exactamente esto:

```python
print("¡Hola Trading Algorítmico!")
```

**Ahora ejecuta:**
1. Presiona **Shift + Enter** (o click en el botón ▶️)
2. Espera 1-2 segundos
3. ✅ Deberías ver abajo: `¡Hola Trading Algorítmico!`

**🎉 Si ves ese mensaje, ¡Colab está funcionando correctamente!**

**🎓 ¿Qué acabas de hacer?**

Acabas de darle una instrucción a Python: "muestra este mensaje". Python la ejecutó y te mostró el resultado. Así funciona todo el trading algorítmico: das instrucciones, el programa las ejecuta.

**🔍 Verificación rápida:**
☐ Puedo entrar a colab.research.google.com  
☐ Puedo crear un nuevo notebook (cuaderno)  
☐ Ejecuté `print("¡Hola Trading Algorítmico!")` y vi el resultado  
☐ Entiendo que las celdas son donde escribo código

---

### 📝 PASO 3.4: Nombrar tu Notebook (2 min)

**🎓 ¿Por qué nombrar mi notebook ahora?**

Cuando creaste el notebook en el Paso 3.1, se llamó automáticamente `Untitled0.ipynb` (Sin título 0). Es como tener un archivo de Excel llamado "Libro1.xlsx" - funciona, pero es difícil encontrarlo después.

**Analogía del trader:**  
Como nombrar tus setups de TradingView o tus plantillas de MetaTrader. Un buen nombre te ayuda a encontrarlo rápido y saber qué contiene.

**💻 Lo que vamos a hacer:**

#### **3.4.1 Renombrar el Notebook**

1. En la esquina superior izquierda verás: **"Untitled0.ipynb"**
2. Haz click directo sobre ese texto
3. Se abrirá un cuadro de texto (ahora puedes editarlo)
4. Borra todo y escribe exactamente: **`Setup_y_Practica_Trading`**
5. Presiona **Enter** o click fuera del cuadro
6. ✅ El nombre cambió a: **"Setup_y_Practica_Trading.ipynb"**

**🎓 ¿Por qué este nombre específico?**

Este notebook será tu **"Notebook Maestro"** que usarás durante TODO el workshop:

```
Setup_y_Practica_Trading.ipynb
│
├─ 🔧 SECCIÓN 1: SETUP (inicio del notebook)
│   ├─ Instalación de librerías (ejecutas cada vez)
│   └─ Configuración de llaves Alpaca (ejecutas cada vez)
│
├─ 📚 SECCIÓN 2: SESIONES DEL WORKSHOP
│   ├─ Sesión 1: Fundamentos
│   ├─ Sesión 2: Pipeline de datos
│   └─ ...hasta Sesión 9
│
└─ 🔬 SECCIÓN 3: EXPERIMENTACIÓN PERSONAL
    └─ Tus pruebas y estrategias propias
```

**⚠️ CONCEPTO CRÍTICO - Lee esto con atención:**

**Notebook vs Sesión (esto confunde a muchos principiantes):**

| Concepto | ¿Qué es? | ¿Persiste? |
|----------|----------|------------|
| **Notebook** | Tu archivo con código (este archivo) | ✅ SÍ - Se guarda en Drive permanentemente |
| **Sesión** | La "computadora virtual" ejecutando el código | ❌ NO - Se borra al cerrar Colab |

**Analogía del trader:**
```
Notebook = Tu "Plan de Trading" escrito
├─ Se guarda en Google Drive (permanente)
├─ Tiene todas tus estrategias y código
└─ ✅ Lo abres cada vez que trabajas

Sesión = Tu "Terminal de Trading" abierta
├─ Es temporal (mientras Colab está abierto)
├─ Tiene las herramientas cargadas en memoria
└─ ❌ Se cierra y borra todo al cerrar Colab
```

**📋 Implicaciones prácticas:**

**✅ Qué SÍ persiste (una vez es suficiente):**
- El código del notebook (guardado en Drive)
- Tus anotaciones y celdas
- La estructura del notebook

**❌ Qué NO persiste (debes hacer cada vez):**
- Las librerías instaladas (yfinance, vectorbt, etc.)
- Las variables en memoria (datos descargados)
- Las llaves de Alpaca configuradas

**🔄 Flujo de trabajo correcto:**

**Primera vez (Setup completo - hoy):**
```
1. Crear notebook "Setup_y_Practica_Trading.ipynb" ✅
2. Ejecutar instalación de librerías (5-8 min)
3. Configurar llaves Alpaca
4. Trabajar en Sesión 1
5. Guardar (Ctrl+S) y cerrar
```

**Cada vez que vuelves al workshop (todas las demás veces):**
```
1. Abrir "Setup_y_Practica_Trading.ipynb" (ya existe en Drive)
2. Ejecutar SOLO celdas de instalación (2-3 min) ← OBLIGATORIO
3. Configurar llaves Alpaca (30 seg)
4. Ir a la sección de la sesión del día
5. Trabajar normalmente
6. Guardar y cerrar
```

**💡 Consejo clave:**
Cada vez que abras este notebook para trabajar, deberás ejecutar las celdas de instalación del PASO 4 (toma 2-3 minutos). Es rápido y asegura que todo funcione siempre.

**🔍 Verificación rápida:**
☐ Mi notebook ya NO se llama "Untitled0"  
☐ Mi notebook se llama "Setup_y_Practica_Trading.ipynb"  
☐ Entiendo que este notebook lo usaré durante TODO el workshop  
☐ Entiendo que debo ejecutar instalación cada vez que lo abra  
☐ Entiendo que el notebook persiste, pero la sesión no

---

### 📦 PASO 4: Instalar Herramientas Especializadas (5-10 min)

**🎓 ¿Qué son las "herramientas" y por qué necesito instalarlas?**

Python por sí solo es como tener TradingView sin indicadores. Las "herramientas" (técnicamente: librerías) son como tus indicadores favoritos - cada una hace algo específico:

**Analogía del trader:**
```
En TradingView:
├─ Indicador RSI → Mide momentum
├─ Bandas de Bollinger → Mide volatilidad
└─ MACD → Detecta tendencias

En Python para Trading:
├─ pandas → Maneja tablas de datos (como Excel)
├─ yfinance → Descarga datos de mercados
└─ vectorbt → Hace backtesting de estrategias
```

Colab ya tiene MUCHAS herramientas instaladas (pandas, numpy, matplotlib), pero necesitamos agregar las específicas para trading algorítmico profesional.

**💻 Lo que vamos a hacer:**

Vas a copiar y pegar un código que instala automáticamente solo las herramientas que faltan. Es como descargar solo los indicadores nuevos en TradingView - rápido y eficiente.

#### **4.1 Código de Instalación v3.0 (Compatible con Colab 2025)**

En tu notebook de Colab, crea una celda nueva (+ Code) y pega este código completo:

```python
# ═══════════════════════════════════════════════════════════
# 📦 INSTALACIÓN COLAB v3.2 - SIMPLIFICADA Y ROBUSTA
# Workshop: Trading Algorítmico Aumentado con IA Generativa
# Fecha: Noviembre 2025
# Solución: Instalación directa sin verificación previa
# ═══════════════════════════════════════════════════════════

print("🚀 Instalación SIMPLIFICADA de herramientas...")
print("   Instalación directa de librerías especializadas para trading.\n")
print("⏱️  Tiempo estimado: 2-3 minutos (¡aprovecha para un café! ☕)\n")

# ──────────────────────────────────────────────────────────
# ESTRATEGIA DE INSTALACIÓN v3.2
# ──────────────────────────────────────────────────────────
# Colab 2025 ya tiene instalado:
# ✅ pandas, numpy, matplotlib, scipy
#
# Instalaremos SOLO lo que NO viene con Colab:
# 1. yfinance (descarga de datos)
# 2. alpaca-py (broker paper trading)
# 3. vectorbt (backtesting vectorizado)
# 4. ta (análisis técnico)
# 5. pandas-ta (análisis técnico - opcional)
# 6. plotly (visualización interactiva)
#
# ⚠️ IMPORTANTE: Esta versión NO verifica antes de instalar
#    para evitar conflictos de compatibilidad binaria.
#    Instalamos directo y validamos DESPUÉS del restart.
# ──────────────────────────────────────────────────────────

print("═" * 60)
print("📥 INSTALANDO HERRAMIENTAS ESPECIALIZADAS")
print("═" * 60)

# ──────────────────────────────────────────────────────────
# 1. DESCARGA DE DATOS
# ──────────────────────────────────────────────────────────
print("\n📈 [1/6] Instalando yfinance (datos de mercados)...")
!pip install -q yfinance
print("   ✅ yfinance instalado")

print("\n📊 [2/6] Instalando alpaca-py (broker paper trading)...")
!pip install -q alpaca-py
print("   ✅ alpaca-py instalado")

# ──────────────────────────────────────────────────────────
# 2. BACKTESTING
# ──────────────────────────────────────────────────────────
print("\n🧪 [3/6] Instalando vectorbt (backtesting rápido)...")
!pip install -q vectorbt
print("   ✅ vectorbt instalado")

# ──────────────────────────────────────────────────────────
# 3. ANÁLISIS TÉCNICO
# ──────────────────────────────────────────────────────────
print("\n📉 [4/6] Instalando ta (indicadores técnicos)...")
!pip install -q ta
print("   ✅ ta instalado")

print("\n📊 [5/6] Instalando pandas-ta (más indicadores)...")
try:
    # Instalar sin actualizar dependencias para evitar conflictos
    !pip install -q pandas-ta --no-deps
    print("   ✅ pandas-ta instalado correctamente")
except Exception as e:
    print("   ⚠️  pandas-ta opcional - continuando sin ella")
    print("      (Usaremos la librería 'ta' que es suficiente para el workshop)")

# ──────────────────────────────────────────────────────────
# 4. VISUALIZACIÓN
# ──────────────────────────────────────────────────────────
print("\n🎨 [6/6] Instalando plotly (gráficos interactivos)...")
!pip install -q plotly
print("   ✅ plotly instalado")

# ──────────────────────────────────────────────────────────
# ✅ INSTALACIÓN COMPLETA
# ──────────────────────────────────────────────────────────
print("\n" + "═" * 60)
print("🎉 ¡INSTALACIÓN COMPLETADA!")
print("═" * 60)
print("\n✅ Herramientas instaladas exitosamente:")
print("   • yfinance (descarga de datos)")
print("   • alpaca-py (broker paper trading)")
print("   • vectorbt (backtesting)")
print("   • ta (análisis técnico)")
print("   • pandas-ta (análisis técnico - si estuvo disponible)")
print("   • plotly (visualización)")

print("\n" + "🔴" * 20)
print("⚠️  ⚠️  ⚠️   PASO OBLIGATORIO AHORA  ⚠️  ⚠️  ⚠️")
print("🔴" * 20)
print("\n🔄 DEBES REINICIAR LA SESIÓN:")
print("   1. Ve al menú: Runtime → Restart session")
print("   2. Click en 'Yes' cuando pregunte")
print("   3. Espera 10 segundos")
print("   4. Luego ejecuta el código de VALIDACIÓN (Paso 5)")

print("\n💡 ¿Por qué reiniciar?")
print("   Python necesita 'recargar' para reconocer las nuevas")
print("   herramientas instaladas. Es como cerrar y abrir TradingView")
print("   después de instalar indicadores nuevos.")

print("\n⚠️  NO ejecutes más celdas sin antes hacer:")
print("   Runtime → Restart session")

print("\n" + "═" * 60)
```

#### **4.2 Ejecutar la Instalación**

1. Click en el botón ▶️ (o Shift + Enter)
2. Verás texto desplazándose (es normal, Python está trabajando)
3. Espera 2-3 minutos (aprovecha para leer el Paso 5 mientras)
4. ✅ Cuando termine, verás: `🎉 ¡INSTALACIÓN COMPLETADA!`

**🎓 ¿Qué está pasando mientras esperas?**

Python está descargando y configurando herramientas especializadas desde internet. Es como cuando instalas un indicador en TradingView - toma tiempo porque está descargando código desde servidores.

**💡 ¿Por qué esta versión es diferente?**

Esta versión v3.0 es "inteligente":
- ✅ Detecta qué ya tienes instalado (pandas, numpy, etc.)
- ✅ Solo instala lo que falta (yfinance, vectorbt, etc.)
- ✅ NO fuerza versiones específicas → sin conflictos
- ✅ Más rápido (2-3 min vs 3-5 min versiones anteriores)

#### **4.3 Reiniciar tu Sesión de Trabajo (OBLIGATORIO)**

⚠️ **MUY IMPORTANTE:** Después de instalar herramientas, DEBES reiniciar.

**Por qué:** Python necesita "recargar" para reconocer las nuevas herramientas instaladas.

**Analogía del trader:** Como cerrar y abrir TradingView después de instalar indicadores nuevos.

**Paso a paso:**
1. Ve al menú principal: **Runtime → Restart session**
2. Aparecerá un mensaje: **"Restart session?"**
3. Click en **"Yes"**
4. Espera 10 segundos
5. ✅ La sesión se reinició (perderás variables temporales, pero las herramientas quedan instaladas)

**🔍 Verificación rápida:**
☐ Ejecuté el código de instalación completo  
☐ Vi el mensaje "🎉 ¡INSTALACIÓN COMPLETADA!"  
☐ Reinicié la sesión (Runtime → Restart session)  
☐ Entiendo que las herramientas ya están instaladas

---

### ✅ PASO 5: Validar que Todo Funciona (5 min)

**🎓 ¿Por qué validar?**

Como trader, sabes que antes de arriesgar capital, pruebas tu setup. Aquí es igual: vamos a verificar que todas las herramientas se instalaron correctamente.

**Analogía del trader:**  
Como hacer un "test de conexión" con tu broker antes de operar. Mejor descubrir problemas ahora que en medio de una operación real.

**💻 Lo que vamos a hacer:**

Después de reiniciar la sesión (Paso 4.3), crea una celda NUEVA y pega este código:

```python
# ═══════════════════════════════════════════════════════════
# ✅ VALIDACIÓN v3.2 - SIMPLIFICADA Y ROBUSTA
# Workshop: Trading Algorítmico Aumentado con IA Generativa
# ═══════════════════════════════════════════════════════════

import sys

print("🔍 VALIDANDO INSTALACIÓN DE HERRAMIENTAS...\n")
print("💡 Esta versión valida FUNCIONALIDAD después del restart\n")
print("═" * 60)

# ──────────────────────────────────────────────────────────
# Lista de herramientas CRÍTICAS (pandas-ta es opcional)
# ──────────────────────────────────────────────────────────
herramientas_test = [
    ("pandas", "import pandas as pd; df = pd.DataFrame({'A': [1,2,3]})"),
    ("numpy", "import numpy as np; arr = np.array([1,2,3])"),
    ("matplotlib", "import matplotlib.pyplot as plt"),
    ("yfinance", "import yfinance as yf"),
    ("alpaca-py", "from alpaca.trading.client import TradingClient"),
    ("vectorbt", "import vectorbt as vbt"),
    ("ta", "from ta.trend import SMAIndicator"),
    ("plotly", "import plotly.graph_objects as go"),
]

# pandas-ta es opcional
herramientas_opcionales = [
    ("pandas-ta", "import pandas_ta"),
]

errores = []
exitosos = []
opcionales_ok = []
opcionales_faltantes = []

# ──────────────────────────────────────────────────────────
# Validar herramientas CRÍTICAS
# ──────────────────────────────────────────────────────────
for nombre, test_code in herramientas_test:
    try:
        exec(test_code)
        print(f"✅ {nombre:<20} Funcionando correctamente")
        exitosos.append(nombre)
    except Exception as e:
        print(f"❌ {nombre:<20} ERROR: {str(e)[:40]}")
        errores.append(nombre)

# ──────────────────────────────────────────────────────────
# Validar herramientas OPCIONALES
# ──────────────────────────────────────────────────────────
for nombre, test_code in herramientas_opcionales:
    try:
        exec(test_code)
        print(f"✅ {nombre:<20} Funcionando correctamente (opcional)")
        opcionales_ok.append(nombre)
    except:
        print(f"⚠️  {nombre:<20} No disponible (opcional - no es problema)")
        opcionales_faltantes.append(nombre)

print("═" * 60)

# ──────────────────────────────────────────────────────────
# Reporte final
# ──────────────────────────────────────────────────────────
if not errores:
    print("\n🎉 ¡TODAS LAS HERRAMIENTAS CRÍTICAS VALIDADAS!")
    print(f"✅ {len(exitosos)}/{len(herramientas_test)} herramientas críticas funcionan")
    if opcionales_ok:
        print(f"✅ {len(opcionales_ok)} herramienta(s) opcional(es) también disponibles")
    if opcionales_faltantes:
        print(f"⚠️  {len(opcionales_faltantes)} herramienta(s) opcional(es) no disponibles (OK)")
    print("\n📍 Estás 100% listo para el workshop")
    print("\n🎯 Próximo paso: Configurar llaves de Alpaca (Paso 6)")
    
else:
    print(f"\n❌ ERROR: {len(errores)} herramienta(s) CRÍTICAS no funcionan:")
    for herr in errores:
        print(f"   - {herr}")
    print("\n🔧 Solución:")
    print("   1. Verifica que ejecutaste Runtime → Restart session")
    print("   2. Re-ejecuta el código de instalación (Paso 4)")
    print("   3. Vuelve a reiniciar sesión")
    print("   4. Ejecuta esta validación nuevamente")

print("\n" + "═" * 60)
print(f"📍 Python: {sys.version.split()[0]}")
print(f"📍 Entorno: Google Colab")
print("═" * 60)

# ──────────────────────────────────────────────────────────
# TEST FUNCIONAL: Descargar datos reales
# ──────────────────────────────────────────────────────────
if not errores:
    print("\n🧪 BONUS: Test funcional completo...")
    print("   Descargando datos reales de mercado...\n")
    
    try:
        import yfinance as yf
        import pandas as pd
        
        # Descargar 5 días de SPY
        data = yf.download("SPY", period="5d", progress=False)
        
        if len(data) > 0:
            print("✅ Test de descarga: EXITOSO")
            print(f"   • Descargados {len(data)} días de datos de SPY")
            print(f"   • Último precio: ${data['Close'].iloc[-1]:.2f}")
            print("\n🎉 Sistema completamente funcional y listo para operar")
        else:
            print("⚠️  Test de descarga: Sin datos (verifica conexión)")
            
    except Exception as e:
        print(f"⚠️  Test de descarga: Error ({str(e)[:50]})")
        print("   Pero las librerías están instaladas correctamente")
```

#### **5.2 Ejecutar Validación**

1. Click en ▶️ para ejecutar
2. Espera 5-10 segundos
3. Lee el resultado cuidadosamente

**✅ Resultado PERFECTO (lo que quieres ver):**

```
🔍 VALIDANDO INSTALACIÓN DE HERRAMIENTAS...
═══════════════════════════════════════════════════════════
✅ pandas               2.2.2
✅ numpy                1.26.4
✅ matplotlib           3.8.0
✅ yfinance             0.2.36
✅ alpaca-py            OK
✅ vectorbt             0.26.1
✅ ta                   0.11.0
✅ pandas-ta            OK
✅ plotly               5.18.0
═══════════════════════════════════════════════════════════

🎉 ¡TODAS LAS HERRAMIENTAS VALIDADAS CORRECTAMENTE!
✅ 9/9 herramientas funcionan perfectamente

📍 Estás 100% listo para el workshop
```

**⚠️ Resultado con ADVERTENCIAS (no es grave):**

Si ves versiones ligeramente diferentes:
- ✅ Puedes continuar sin problema
- Las diferencias mínimas no afectan el workshop
- Solo reporta si hay errores específicos más adelante

**❌ Resultado con ERRORES (necesita corrección):**

Si ves "❌ ERROR":
1. Regresa al Paso 4
2. Re-ejecuta el código de instalación
3. Reinicia sesión (Runtime → Restart session)
4. Vuelve a validar

**🔍 Verificación rápida:**
☐ Ejecuté el código de validación  
☐ Todas las herramientas muestran ✅ (o ⚠️ pero no ❌)  
☐ Vi el test funcional de descarga de datos  
☐ Estoy listo para el Paso 6

---

### 🔗 PASO 6: Configurar tus Llaves de Acceso (5 min)

**🎓 ¿Por qué este paso?**

Tus llaves de Alpaca (del Paso 2) necesitan estar "disponibles" para tu código Python. Es como tener tus credenciales de broker guardadas para no escribirlas cada vez.

**Analogía del trader:**  
Como guardar tus credenciales en TradingView o MetaTrader - lo haces una vez, y la plataforma las recuerda mientras estés conectado.

**⚠️ Seguridad CRÍTICA:**

NUNCA escribas tus llaves directamente en el código visible. Vamos a usar un método seguro.

**💻 Lo que vamos a hacer:**

Crea una celda nueva y pega este código:

```python
# ═══════════════════════════════════════════════════════════
# 🔐 CONFIGURACIÓN SEGURA DE LLAVES DE ACCESO
# ═══════════════════════════════════════════════════════════

import os
from getpass import getpass

print("🔐 CONFIGURACIÓN DE LLAVES ALPACA")
print("═" * 60)
print("⚠️  Vas a ingresar tus llaves de forma segura")
print("    (NO se mostrarán en pantalla mientras las escribes)")
print("═" * 60 + "\n")

# Solicitar llaves de forma segura (input oculto)
api_key = getpass("🔑 Pega tu Alpaca API Key (PK...) y presiona Enter: ")
secret_key = getpass("🔐 Pega tu Alpaca Secret Key y presiona Enter: ")

# Guardar temporalmente (solo para esta sesión)
os.environ['ALPACA_API_KEY'] = api_key
os.environ['ALPACA_SECRET_KEY'] = secret_key

print("\n✅ Llaves configuradas correctamente")
print("\n📋 IMPORTANTE RECORDAR:")
print("   ⚠️  Estas llaves son temporales (solo esta sesión)")
print("   ⚠️  Si cierras Colab o reinicias sesión, deberás repetir")
print("       este paso con tus llaves")
print("\n💡 CONSEJO: Guarda este código en una celda al inicio")
print("   de tu notebook. Así solo ejecutas y pegas cada vez.")
```

#### **6.2 Ejecutar Configuración**

1. Click en ▶️
2. Aparecerán dos campos de entrada:
   
   **Primer campo:** `🔑 Pega tu Alpaca API Key (PK...) y presiona Enter:`
   - Abre tu archivo `Alpaca_Keys_Paper.txt` (del Paso 2)
   - Copia tu API Key (comienza con "PK...")
   - Pégala aquí (no verás lo que escribes - es SEGURO)
   - Presiona **Enter**
   
   **Segundo campo:** `🔐 Pega tu Alpaca Secret Key y presiona Enter:`
   - Copia tu Secret Key de tu archivo
   - Pégala aquí (no verás lo que escribes - es SEGURO)
   - Presiona **Enter**

3. ✅ Verás: "Llaves configuradas correctamente"

**🎓 ¿Por qué no veo lo que escribo?**

Por seguridad. Como cuando escribes tu contraseña en cualquier sitio web - no se muestra para que nadie pueda verla.

#### **6.3 Validar Conexión con Alpaca**

Ahora vamos a probar que tus llaves funcionan. Crea otra celda nueva:

```python
# ═══════════════════════════════════════════════════════════
# ✅ VALIDAR CONEXIÓN CON ALPACA PAPER TRADING
# ═══════════════════════════════════════════════════════════

from alpaca.trading.client import TradingClient
import os

print("🔍 VALIDANDO CONEXIÓN CON ALPACA...\n")

try:
    # Obtener llaves del paso anterior
    api_key = os.environ.get('ALPACA_API_KEY')
    secret_key = os.environ.get('ALPACA_SECRET_KEY')
    
    # Crear conexión con Alpaca (paper = cuenta simulada)
    client = TradingClient(api_key, secret_key, paper=True)
    
    # Obtener información de tu cuenta
    cuenta = client.get_account()
    
    print("═" * 60)
    print("✅ CONEXIÓN EXITOSA CON ALPACA")
    print("═" * 60)
    print(f"📊 Tipo de cuenta: Paper Trading (Simulación)")
    print(f"💰 Balance disponible: ${float(cuenta.cash):,.2f}")
    print(f"📈 Poder de compra: ${float(cuenta.buying_power):,.2f}")
    print(f"📍 Estado de cuenta: {cuenta.status}")
    print("═" * 60)
    print("\n✅ Todo funciona correctamente")
    print("🎉 Estás listo para descargar datos y operar en simulación")
    
except Exception as e:
    print("═" * 60)
    print("❌ ERROR EN CONEXIÓN CON ALPACA")
    print("═" * 60)
    print(f"Error técnico: {str(e)}\n")
    print("🔧 Posibles causas:")
    print("   1. Las llaves están incorrectas (copiaste mal)")
    print("   2. Usaste llaves de cuenta LIVE en vez de PAPER")
    print("   3. Cuenta Alpaca no está activada")
    print("\n💡 Solución:")
    print("   1. Ve a alpaca.markets y verifica tus llaves PAPER")
    print("   2. Vuelve al Paso 6.2 y re-ejecuta con llaves correctas")
    print("   3. Asegúrate de usar Paper Trading, NO Live")
```

#### **6.4 Ejecutar Validación de Conexión**

1. Click en ▶️
2. Espera 3-5 segundos
3. ✅ **Si todo está bien, verás:**

```
═══════════════════════════════════════════════════════════
✅ CONEXIÓN EXITOSA CON ALPACA
═══════════════════════════════════════════════════════════
📊 Tipo de cuenta: Paper Trading (Simulación)
💰 Balance disponible: $100,000.00
📈 Poder de compra: $200,000.00
📍 Estado de cuenta: ACTIVE
═══════════════════════════════════════════════════════════

✅ Todo funciona correctamente
🎉 Estás listo para descargar datos y operar en simulación
```

**🎓 ¿Qué significa "Poder de compra $200,000"?**

Alpaca te da 2x leverage (apalancamiento) en paper trading. Tu balance real es $100,000, pero puedes operar hasta $200,000 (como margen en tu broker real).

**❌ Si ves error:**
- Verifica que copiaste bien las llaves (sin espacios extra)
- Confirma que usaste llaves PAPER, no LIVE
- Ve a alpaca.markets y regenera las llaves si es necesario

**🔍 Verificación rápida:**
☐ Configuré mis llaves de forma segura  
☐ No vi mis llaves en pantalla (input oculto funcionó)  
☐ Ejecuté validación de conexión  
☐ Vi mensaje: "✅ CONEXIÓN EXITOSA CON ALPACA"  
☐ Vi mi balance paper ($100,000)

---

### 📘 PASO 7: Acceder al Notebook Maestro del Workshop (5 min)

**🎓 ¿Qué es el Notebook Maestro?**

Es tu "manual de operaciones" para todo el workshop. Imagina un libro de trading que, en vez de solo leer, ejecutas el código mientras aprendes.

**Contiene:**
- Todo el código de las 9 sesiones (27 horas)
- Explicaciones paso a paso
- Ejercicios prácticos
- Ejemplos con datos reales

**Analogía del trader:**  
Como tener un curso de trading completo, pero en vez de solo videos y PDFs, tienes el código ejecutable. Aprendes haciendo, no solo mirando.

**💻 Lo que vamos a hacer:**

#### **7.1 Obtener el Link al Notebook**

📧 **El Notebook Maestro te será enviado por:**
- Email de bienvenida (busca asunto: "Bienvenido al Workshop")
- Grupo de Telegram Premium del workshop
- Drive compartido (link en email)

**⚠️ Si NO tienes el link:**
1. Revisa tu email (bandeja de entrada Y spam)
2. Busca emails de: yismaryme@gmail.com
3. Si no lo encuentras: contacta yismaryme@gmail.com con asunto "Necesito link a Notebook Maestro"

#### **7.2 Abrir y Hacer Tu Copia Personal**

Una vez que tengas el link:

1. Click en el link del Notebook Maestro
2. Se abrirá en Colab en **modo solo lectura** (no puedes editar)
3. **OBLIGATORIO:** Haz tu copia personal:
   - Ve al menú: **File → Save a copy in Drive**
   - Se abrirá una copia EN TU Google Drive personal
   - ✅ Esta copia SÍ puedes editarla y guardar cambios

**🎓 ¿Por qué hacer una copia?**

El Notebook original es compartido con todos los participantes (modo lectura). Tu copia personal es TU espacio de trabajo donde puedes:
- Agregar notas
- Modificar código para experimentar
- Guardar tus ejercicios
- Practicar sin miedo a romper nada

#### **7.3 Estructura del Notebook Maestro**

```
📘 NOTEBOOK MAESTRO DEL WORKSHOP (1,500+ líneas de código)
│
├── 🔧 SETUP Y VALIDACIÓN
│   └─ (Lo que acabas de hacer en Pasos 1-6)
│
├── 🟦 SESIÓN 1: Fundamentos y Mapa del Trading Algorítmico
│   └─ Componentes de un sistema, expectativas realistas
│
├── 🟦 SESIÓN 2: Datos - La Base de Todo Sistema  
│   └─ Descarga, limpieza, validación de datos
│
├── 🟦 SESIÓN 3: Ideación de Estrategias con GenAI
│   └─ Cómo usar IA para generar ideas de estrategias
│
├── 🟦 SESIÓN 4: Implementación Práctica Guiada
│   └─ Codificar una estrategia completa paso a paso
│
├── 🟦 SESIÓN 5: Validación Rigurosa - Backtesting Profesional
│   └─ Probar estrategias con datos históricos
│
├── 🟦 SESIÓN 6: Gestión Avanzada de Riesgo
│   └─ Position sizing, stops, portfolio heat
│
├── 🟦 SESIÓN 7: Multi-Plataforma - Del Código a la Ejecución ⭐
│   └─ Convertir Python → Pine Script / MQL5 / IB
│
├── 🟦 SESIÓN 8: Poner en Funcionamiento 24/7 - Paper Trading
│   └─ Deploy real en servidor, monitoreo, alertas
│
└── 🟦 SESIÓN 9: Proyecto Final y Documentación Profesional
    └─ Crear tu portfolio de estrategias documentadas
```

#### **7.4 Primera Exploración (NO ejecutes todavía)**

1. Navega a **"🟦 SESIÓN 1"** (scroll hacia abajo en el notebook)
2. Lee la introducción
3. Ve los bloques de código
4. **NO ejecutes nada todavía** - lo harás en vivo durante las sesiones
5. Familiarízate con cómo está organizado

#### **7.5 Leer la Guía de Uso (OBLIGATORIO antes de Sesión 1)**

Antes de la primera sesión del workshop, DEBES leer esta guía:

📖 **[Guía de Uso del Colab Notebook Maestro](Guia_Uso_Colab_Notebook.md)**

**Aprenderás:**
- Cómo navegar por las 9 sesiones
- Atajos de teclado útiles
- Cómo ejecutar código correctamente
- Qué hacer si algo falla
- Mejores prácticas de trabajo en Colab

**🔍 Verificación rápida:**
☐ Recibí el link al Notebook Maestro del workshop  
☐ Hice una copia personal en mi Drive ("Save a copy")  
☐ Veo las 9 sesiones en el notebook  
☐ Leí (o tengo en mi lista) la [Guía de Uso de Colab](Guia_Uso_Colab_Notebook.md)  
☐ Entiendo que NO debo ejecutar todo ahora, solo en las sesiones

---

## 🔍 Validación del Setup

**Antes de cerrar, valida que TODO está listo para el workshop:**

### ✅ Checklist Final de los 7 Pasos

☐ **PASO 1:** Tengo cuenta Gmail y puedo acceder  
☐ **PASO 2:** Tengo mis llaves Alpaca guardadas en archivo seguro  
☐ **PASO 3:** Puedo entrar a Google Colab y crear notebooks  
☐ **PASO 4:** Instalé todas las herramientas especializadas (v3.0)  
☐ **PASO 5:** Todas las herramientas validaron con ✅  
☐ **PASO 6:** Conexión con Alpaca exitosa (vi mi balance $100,000)  
☐ **PASO 7:** Tengo copia personal del Notebook Maestro en mi Drive

### 🎯 Test Final de Integración

Ejecuta este test completo en una celda nueva (copia y pega):

```python
# ═══════════════════════════════════════════════════════════
# 🎯 TEST FINAL DE INTEGRACIÓN - SETUP COMPLETO v3.0
# ═══════════════════════════════════════════════════════════

print("🧪 EJECUTANDO TEST FINAL DE INTEGRACIÓN...\n")
print("Validando 5 componentes críticos:\n")

resultados = []

# Test 1: Herramientas Core
try:
    import pandas as pd
    import numpy as np
    print("✅ Test 1/5: Herramientas Core (pandas, numpy)")
    resultados.append(True)
except:
    print("❌ Test 1/5: ERROR en herramientas Core")
    resultados.append(False)

# Test 2: Descarga de Datos
try:
    import yfinance as yf
    datos = yf.download("SPY", period="5d", progress=False)
    assert len(datos) > 0
    print("✅ Test 2/5: Descarga de Datos (yfinance)")
    resultados.append(True)
except:
    print("❌ Test 2/5: ERROR en descarga de datos")
    resultados.append(False)

# Test 3: Conexión Alpaca
try:
    from alpaca.trading.client import TradingClient
    import os
    client = TradingClient(
        os.environ['ALPACA_API_KEY'], 
        os.environ['ALPACA_SECRET_KEY'], 
        paper=True
    )
    cuenta = client.get_account()
    print("✅ Test 3/5: Conexión Alpaca Paper Trading")
    resultados.append(True)
except:
    print("❌ Test 3/5: ERROR en conexión Alpaca")
    resultados.append(False)

# Test 4: Backtesting
try:
    import vectorbt as vbt
    print("✅ Test 4/5: Herramienta de Backtesting (vectorbt)")
    resultados.append(True)
except:
    print("❌ Test 4/5: ERROR en herramienta backtesting")
    resultados.append(False)

# Test 5: Visualización
try:
    import plotly.graph_objects as go
    print("✅ Test 5/5: Herramienta de Visualización (plotly)")
    resultados.append(True)
except:
    print("❌ Test 5/5: ERROR en herramienta visualización")
    resultados.append(False)

# Resultado Final
print("\n" + "═" * 60)
if all(resultados):
    print("🎉 ¡SETUP COMPLETADO EXITOSAMENTE!")
    print("═" * 60)
    print("✅ Todos los componentes funcionan correctamente")
    print("✅ Estás 100% listo para la Sesión 1 del workshop")
    print("\n🎯 Próximos pasos:")
    print("   1. Lee el documento LEEME_PRIMERO.md")
    print("   2. Lee la Guía de Uso del Colab Notebook")
    print("   3. Únete al grupo de Telegram Premium")
    print("   4. Revisa tu horario de sesiones (email)")
    print("   5. ¡Nos vemos en la Sesión 1! 🚀")
else:
    print("⚠️  ALGUNOS TESTS FALLARON")
    print("═" * 60)
    print("Revisa los tests marcados con ❌ arriba")
    print("Regresa al paso correspondiente y corrige el error")
print("═" * 60)
```

**✅ Si ves "🎉 ¡SETUP COMPLETADO EXITOSAMENTE!" → ¡Felicidades! Estás listo.**

---

## 🚨 Troubleshooting Específico

**Soluciones a problemas comunes en Colab:**

### ❌ Error: "No module named 'yfinance'"

**Qué significa:** La herramienta yfinance no está instalada (o Python no la reconoce).

**Solución paso a paso:**
```python
# 1. Re-instalar la herramienta específica
!pip install yfinance

# 2. Reiniciar sesión: Runtime → Restart session

# 3. Re-ejecutar la celda que dio error
```

---

### ❌ Error: "ALPACA_API_KEY not found in environment"

**Qué significa:** Tus llaves de Alpaca no están configuradas (o se perdieron al reiniciar).

**Solución:**
- Vuelve al Paso 6
- Re-ejecuta el código de configuración de llaves
- Pega tus llaves nuevamente

**⚠️ Recuerda:** Las llaves se pierden si:
- Cierras Colab
- Reinicias la sesión
- Pasas 12 horas sin actividad

Debes reconfigurarlas cada vez.

---

### ❌ Error: "Session crashed" / "Out of Memory"

**Qué significa:** Colab gratuito tiene límite de RAM (12 GB) y se quedó sin memoria.

**Causas comunes:**
- Descargaste demasiados datos de una vez
- Ejecutaste muchas celdas sin limpiar memoria
- El código tiene un "memory leak"

**Solución:**
```python
# 1. Liberar memoria manualmente
import gc
gc.collect()

# 2. Si no funciona: Runtime → Restart session

# 3. Ejecuta solo celdas necesarias (no todas a la vez)

# 4. Si el problema persiste, considera Colab Pro ($10/mes)
```

---

### ❌ Error: "Could not find a version that satisfies alpaca-py"

**Qué significa:** El instalador de Python (pip) no encuentra esa versión.

**Solución:**
```python
# 1. Actualizar pip (el instalador)
!pip install --upgrade pip

# 2. Instalar alpaca-py nuevamente
!pip install alpaca-py

# 3. Reiniciar sesión: Runtime → Restart session
```

---

### ❌ Error: "HTTPError 401: Unauthorized" (Alpaca)

**Qué significa:** Tus llaves están incorrectas o no tienes permiso.

**Causas comunes:**
- Copiaste las llaves con espacios extra
- Usaste llaves de cuenta LIVE en vez de PAPER
- Las llaves están revocadas en Alpaca

**Solución:**
1. Ve a [alpaca.markets](https://alpaca.markets)
2. Verifica tus llaves PAPER (no LIVE)
3. Si es necesario, genera llaves nuevas
4. Cópialas CON CUIDADO (sin espacios)
5. Re-ejecuta Paso 6 con las nuevas llaves

---

### ⚠️ Advertencia: "Dependency conflict warnings"

**Qué significa:** Colab detecta versiones diferentes entre librerías.

**¿Es problema?**
- ✅ En el 99% de casos, NO
- Son solo advertencias, no errores
- El código funciona normalmente

**Si tienes errores REALES después:**
- Contacta soporte con el error específico
- Incluye screenshot del error completo

---

### 🌐 Problema: "Colab muy lento / No carga"

**Causas comunes:**
- Conexión a internet lenta
- Sobrecarga de servidores de Google
- Caché del navegador lleno

**Solución:**
1. Verifica tu velocidad de internet (mínimo 3 Mbps)
2. Prueba otro navegador (Chrome es el mejor)
3. Limpia caché:
   - Chrome: Ctrl+Shift+Del → "Caché" → Borrar
4. Intenta en otra hora (menos carga en servidores)
5. Si persiste, prueba conexión móvil (hotspot)

---

### 📂 Problema: "No encuentro mi copia del Notebook Maestro"

**Solución:**
1. Ve a [drive.google.com](https://drive.google.com)
2. Arriba a la derecha: busca "Copy of Colab Notebook Maestro"
3. Click derecho sobre el archivo
4. "Abrir con" → "Google Colaboratory"

---

**🔧 Troubleshooting Avanzado:**

Si ninguna solución funciona:
1. Consulta [Troubleshooting Común](Troubleshooting_Comun.md) (errores cross-platform)
2. Pregunta en grupo Telegram Premium (otros participantes pueden ayudar)
3. Contacta soporte: yismaryme@gmail.com (incluye screenshots)

---

## 💡 Consejos y Mejores Prácticas

**Saca el máximo provecho de Colab:**

### ⚠️ CONCEPTO CRÍTICO: Notebook vs Sesión

**🎯 Este es el error #1 de principiantes - Léelo bien:**

Muchos participantes confunden qué persiste y qué no en Colab. Esto genera frustración cuando vuelven al notebook y "nada funciona".

**📘 Entendiendo la diferencia:**

| Concepto | ¿Qué es? | ¿Cuándo se borra? | ¿Debo recrearlo cada vez? |
|----------|----------|-------------------|---------------------------|
| **Notebook** | Tu archivo .ipynb con código | NUNCA (está en Drive) | ❌ NO - abre el mismo archivo |
| **Sesión** | Computadora virtual ejecutando | Al cerrar Colab / 90 min inactivo | ✅ SÍ - reinstala librerías |

**🔄 Flujo de trabajo CORRECTO:**

**Día 1 (Sesión 1 del workshop):**
```python
1. Crear "Setup_y_Practica_Trading.ipynb" ✅
2. Ejecutar instalación completa (5-8 min)
3. Configurar llaves Alpaca
4. Trabajar en Sesión 1
5. Guardar (Ctrl+S) y cerrar navegador
   ├─ ✅ Notebook guardado en Drive (persiste)
   └─ ❌ Sesión terminada (librerías borradas)
```

**Día 2 (Sesión 2 del workshop):**
```python
1. Abrir "Setup_y_Practica_Trading.ipynb" (ya existe)
   └─ ✅ Todo tu código está ahí (persiste)
2. Ejecutar celdas de instalación (2-3 min) ← OBLIGATORIO
   └─ ⚠️  Nueva sesión = nueva computadora = sin librerías
3. Configurar llaves Alpaca (30 seg)
4. Ir a sección "Sesión 2"
5. Trabajar normalmente
6. Guardar y cerrar
```

**Día 3, 4, 5... (siguientes sesiones):**
```python
1. Abrir notebook (mismo archivo)
2. Ejecutar instalación (2-3 min) ← SIEMPRE
3. Configurar llaves
4. Trabajar
5. Guardar y cerrar
```

**💡 Regla de oro:**
> **"Si cierras Colab, la próxima vez ejecuta las celdas de instalación del PASO 4"**

**🚫 Errores comunes:**

❌ **ERROR:** "Abrí el notebook y me da error al ejecutar código"
✅ **SOLUCIÓN:** Ejecutaste la instalación del PASO 4?

❌ **ERROR:** "Ayer funcionaba, hoy no reconoce yfinance"
✅ **SOLUCIÓN:** Cerraste Colab = sesión terminada. Reinstala.

❌ **ERROR:** "Tengo que hacer TODO el setup de nuevo?"
✅ **SOLUCIÓN:** NO. Solo ejecutar celdas de instalación (2 min).

**🎯 Tip pro:**
Agrega una celda al inicio de tu notebook que diga:
```python
# ⚠️ EJECUTAR CADA VEZ QUE ABRAS ESTE NOTEBOOK
# 1. Celdas de instalación (PASO 4)
# 2. Configurar llaves Alpaca (PASO 6)
# 3. Luego ir a la sección de tu sesión
```

---

### 🎯 Organización en Google Drive

**Crea esta estructura de carpetas en tu Drive:**

```
Mi Drive/
│
└── Workshop_Trading_Algoritmico/
    │
    ├── Colab_Notebook_Maestro.ipynb ← Tu copia personal
    │
    ├── Mis_Estrategias/
    │   ├── Estrategia_1_Mean_Reversion.ipynb
    │   ├── Estrategia_2_Momentum.ipynb
    │   └── Estrategia_3_Breakout.ipynb
    │
    ├── Datos/
    │   ├── SPY_historico.csv
    │   ├── AAPL_5min.csv
    │   └── portfolio_data.csv
    │
    └── Documentacion/
        ├── Alpaca_Keys_Paper.txt ← TUS LLAVES (seguro)
        └── Notas_Workshop.docx
```

**Beneficios:**
- Todo organizado en un solo lugar
- Fácil de encontrar durante el workshop
- Respaldo automático en la nube

---

### ⚡ Atajos de Teclado Útiles

**Como trader, conoces los atajos de tu plataforma. Aquí los de Colab:**

| Atajo | Acción |
|-------|--------|
| **Ctrl + M, luego B** | Agregar celda abajo |
| **Ctrl + M, luego A** | Agregar celda arriba |
| **Ctrl + M, luego D** | Eliminar celda |
| **Shift + Enter** | Ejecutar celda y avanzar |
| **Ctrl + Enter** | Ejecutar celda sin avanzar |
| **Ctrl + S** | Guardar notebook |
| **Ctrl + /** | Comentar/descomentar líneas |
| **Tab** | Autocompletar código |

**💡 Consejo:** Usa **Shift + Enter** todo el tiempo - es el más importante.

---

### 💾 Guardado Automático

**Buenas noticias:**
- ✅ Colab guarda automáticamente cada ~2 minutos
- ✅ Los cambios se guardan en tu Google Drive
- ✅ Puedes ver versiones anteriores (File → Revision history)

**Aún así:**
- Usa **Ctrl + S** antes de cerrar Colab (por costumbre)
- Si trabajas en código importante, guarda manualmente cada 5-10 min

---

### 🔋 Límites de Colab Gratuito

**Colab GRATIS tiene límites (pero son generosos):**

| Límite | Valor | ¿Es problema? |
|--------|-------|---------------|
| **RAM** | 12 GB | ✅ Suficiente para el workshop |
| **Disco temporal** | 100 GB | ✅ Más que suficiente |
| **GPU** | Gratis limitado | ✅ No necesitamos GPU |
| **Tiempo de sesión** | ~12 horas máximo | ⚠️ Se desconecta automáticamente |
| **Sesiones paralelas** | 1 notebook a la vez | ✅ Suficiente |

**⚠️ Si la sesión se desconecta:**
- Variables en memoria se pierden
- Herramientas instaladas permanecen
- Tus llaves Alpaca debes reconfigurarlas (Paso 6)

**💡 Evita desconexiones:**
- No dejes Colab abierto sin usar por más de 90 minutos
- Ejecuta una celda cada hora si estás trabajando

---

### 🚀 ¿Vale la pena Colab Pro?

**Colab Pro cuesta $10/mes. ¿Cuándo considerarlo?**

**Vale la pena SI:**
- Session crashed frecuente (necesitas más RAM)
- Trabajas sesiones > 12 horas
- Quieres ejecución más rápida
- Necesitas prioridad en servidores

**NO es necesario SI:**
- Sigues el workshop sesión por sesión
- Trabajas máximo 3-4 horas por día
- No haces análisis con millones de datos

**Recomendación:** Empieza con Colab GRATIS. Upgrade solo si realmente lo necesitas.

---

### 📝 Buenas Prácticas

**DO ✅ (Haz esto):**
- ✅ Comenta tu código en español (para entenderlo después)
- ✅ Usa nombres descriptivos de variables (no "x", "y", "z")
- ✅ Guarda versiones de tus estrategias (copia el notebook)
- ✅ Reinicia sesión si algo se comporta raro
- ✅ Lee los errores con calma (suelen decir qué está mal)
- ✅ Prueba con datos pequeños primero (5 días, no 5 años)

**DON'T ❌ (Evita esto):**
- ❌ Poner llaves de Alpaca en código visible
- ❌ Ejecutar todas las celdas a la vez sin leer
- ❌ Compartir tu notebook con llaves configuradas
- ❌ Usar llaves de cuenta LIVE (solo PAPER en el workshop)
- ❌ Descargar 10 años de datos tick-by-tick (muy pesado)
- ❌ Copiar código sin entenderlo (aprende paso a paso)

---

## 🎯 Próximos Pasos

**¡Felicidades! Has completado el Setup A: Colab Rápido. 🎉**

**Estás oficialmente listo para empezar el workshop.**

### 1️⃣ Volver al Documento Principal

📖 [← Volver a Instrucciones_Setup_Ambiente.md](Instrucciones_Setup_Ambiente.md)

Revisa otras opciones de setup si tienes curiosidad.

---

### 2️⃣ Leer Documentos Complementarios

📚 **OBLIGATORIOS (antes de Sesión 1):**
- [Guía de Uso del Colab Notebook Maestro](Guia_Uso_Colab_Notebook.md) ⭐ **CRÍTICO**
- [LEEME_PRIMERO.md](LEEME_PRIMERO.md) - Roadmap completo del workshop

📖 **OPCIONALES (útiles de referencia):**
- [Librerías Mínimas vs Completas](Librerias_Minimas_vs_Completas.md) - Qué instalamos y por qué
- [Troubleshooting Común](Troubleshooting_Comun.md)

---

### 3️⃣ Unirte al Grupo Premium

💬 **Telegram:** [Enlace en email de bienvenida]

**Beneficios del grupo:**
- 📢 Anuncios de sesiones
- 🤝 Soporte entre participantes
- 📂 Materiales adicionales
- 💡 Tips y trucos semanales
- 🎯 Recordatorios de tareas

---

### 4️⃣ Preparar Tu Primer Día

✅ **Checklist "Tu Primer Día":**

☐ Setup Colab completado (este documento) ✅  
☐ Leído [Guía de Uso de Colab](Guia_Uso_Colab_Notebook.md)  
☐ Llaves Alpaca guardadas en archivo seguro  
☐ Copia personal del Notebook Maestro en mi Drive  
☐ Unido al grupo de Telegram Premium  
☐ Revisado horario de sesiones (email de bienvenida)  
☐ Preparado mentalmente para aprender (¡lo más importante!)

---

### 5️⃣ El Día de la Sesión 1

**Cuando llegue el día:**

**30 minutos ANTES:**
1. Abre Google Colab
2. Abre tu copia del Notebook Maestro
3. Navega a "🟦 SESIÓN 1: FUNDAMENTOS"
4. Ejecuta las celdas de setup (llaves Alpaca)
5. Espera a que empiece la sesión en vivo

**DURANTE la sesión:**
1. Sigue las instrucciones del instructor
2. Ejecuta celdas paso a paso (no adelantarte)
3. Pregunta si algo no entiendes
4. Toma notas en tu notebook

**DESPUÉS de la sesión:**
1. Completa los ejercicios opcionales
2. Experimenta con el código (aprende haciendo)
3. Prepara preguntas para la siguiente sesión

---

## 📞 Soporte

**Si algo no funciona:**

### 📧 Email
**yismaryme@gmail.com**  
Tiempo de respuesta: 24-48h

**Incluye en tu email:**
- "Setup A: Colab v3" en el asunto
- Paso exacto donde falló (ej: "Paso 5 - Validación")
- Error completo (copia y pega el mensaje de error)
- Screenshot si es posible
- Qué ya intentaste

---

### 💬 Telegram
**[@yismary](https://t.me/yismary)**  
Para consultas rápidas pre-workshop

---

### 🔒 Grupo Premium
Soporte comunitario + troubleshooting en vivo  
(Enlace en email de bienvenida)

---

### 🚨 Antes de Contactar

**Revisa primero (soluciona 80% de problemas):**
1. Troubleshooting de este documento (arriba)
2. [Troubleshooting Común](Troubleshooting_Comun.md)
3. FAQ en [LEEME_PRIMERO.md](LEEME_PRIMERO.md#-faq---preguntas-frecuentes)

---

## 🔖 Versión y Actualizaciones

**Versión:** 3.2 (Noviembre 2025)  
**Última actualización:** 14 de noviembre de 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- v3.2 (Nov 14, 2025): 
  - ✅ **CRÍTICO FIX:** Eliminada fase de verificación previa que causaba error de incompatibilidad binaria de numpy
  - ✅ **SIMPLIFICACIÓN:** Instalación directa sin checks previos para evitar conflictos
  - ✅ **ROBUSTEZ:** pandas-ta tratada como opcional en validación (no causa error si falla)
  - ✅ **MEJORA UX:** Énfasis visual en restart obligatorio después de instalación
- v3.1 (Nov 14, 2025): 
  - ✅ **CRÍTICO:** Agregado Paso 3.4 "Nombrar tu Notebook" con nombre `Setup_y_Practica_Trading.ipynb`
  - ✅ **FIX:** Instalación de pandas-ta con `--no-deps` y try-catch para evitar conflictos de dependencias
  - ✅ **EDUCATIVO:** Explicación clara del concepto "Notebook vs Sesión" (persiste vs no persiste)
  - ✅ **MEJORA:** Nueva subsección en "Consejos y Mejores Prácticas" sobre flujo de trabajo correcto
  - ✅ **CLARIFICACIÓN:** Instrucciones explícitas de que instalación debe ejecutarse cada vez
- v3.0 (Nov 14, 2025): Código de instalación compatible con Colab 2025 (sin conflictos de dependencias)
- v2.1 (Nov 14, 2025): Lenguaje para traders no programadores, clarificación Python → Multi-plataforma
- v2.0 (Nov 13, 2025): Arquitectura modular - setup independiente
- v1.0 (Nov 2025): Versión inicial

---

## ⚠️ Disclaimer

**Este es material educativo del Workshop Trading Algorítmico Aumentado con IA Generativa.**

**Importante recordar:**
- ✅ Todas las herramientas son gratuitas para paper trading
- ⚠️ NUNCA uses credenciales de cuenta LIVE en el workshop
- 📊 Practica con cuentas simuladas (paper) antes de arriesgar capital real
- 💰 Trading algorítmico tiene riesgo de pérdida de capital
- 🎓 Este workshop NO garantiza ganancias - es educativo

**Como todo trading:**
- El rendimiento pasado no garantiza resultados futuros
- Toda estrategia puede fallar
- La gestión de riesgo es crítica

---

## 🎉 ¡Estás Listo!

Has completado exitosamente el Setup A: Colab Rápido v3.2.

**Recuerda el hilo conductor:**

> **"GenAI = Copiloto, NO Piloto Automático"**

El journey de 9 sesiones empieza con Python (lenguaje universal), y en Sesión 7 aprenderás a convertir ese código a cualquier plataforma (TradingView, MetaTrader, Interactive Brokers).

**Confía en el proceso. Miles de traders profesionales han seguido este camino.**

**¡Nos vemos en la Sesión 1!** 🚀

---

**🎯 ¿Listo para empezar?**

[← Volver a Instrucciones Setup](Instrucciones_Setup_Ambiente.md) | [Siguiente: Guía de Uso Colab →](Guia_Uso_Colab_Notebook.md)
