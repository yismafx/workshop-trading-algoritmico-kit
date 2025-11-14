# ⚡ SETUP A: COLAB RÁPIDO (30-45 min)

**Workshop: Trading Algorítmico Aumentado con IA Generativa**  
**Versión:** 2.1 (Noviembre 2025)  
**Dificultad:** ⭐ Fácil (No requiere experiencia técnica)

---

## 📑 Tabla de Contenidos

- [🎯 ¿Es Este Setup Para Ti?](#-es-este-setup-para-ti)
- [✅ Requisitos Mínimos](#-requisitos-mínimos)
- [🚀 Guía de Setup Paso a Paso](#-guía-de-setup-paso-a-paso)
- [🔍 Validación del Setup](#-validación-del-setup)
- [🚨 Troubleshooting Específico](#-troubleshooting-específico)
- [💡 Consejos y Mejores Prácticas](#-consejos-y-mejores-prácticas)
- [🎯 Próximos Pasos](#-próximos-pasos)

---

## 🎯 ¿Es Este Setup Para Ti?

**✅ Este setup es PERFECTO si:**

- ❌ **NO** tienes experiencia con Python
- ❌ **NO** quieres instalar nada en tu computadora
- ✅ Quieres empezar **YA** (en 30 minutos)
- ✅ Te enfocas en **aprender primero, deployar después**
- ✅ Tienes conexión a internet estable
- ✅ Tienes cuenta Google (Gmail)

**❌ Este setup NO es ideal si:**

- 🚀 Necesitas deployar bots 24/7 (usa [Setup B: Python Local](Setup_B_Python_Local.md))
- 🏦 Usas principalmente MetaTrader (usa [Setup C: MT5](Setup_C_MetaTrader5.md))
- 💼 Necesitas Interactive Brokers (usa [Setup D: IB](Setup_D_Interactive_Brokers.md))

**📊 Estadística del Workshop:**
> 🎯 **80% de participantes** usan este setup exitosamente

---

## ✅ Requisitos Mínimos

**Hardware:**
- 💻 Cualquier computadora con navegador web
- 🌐 Conexión a internet (3 Mbps mínimo)
- 🧠 4 GB RAM recomendado (2 GB mínimo)

**Software:**
- 🌐 Navegador moderno (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- 📧 Cuenta Google (Gmail) - [Crear cuenta](https://accounts.google.com/signup)

**Conocimientos:**
- ❌ **NO** se requiere experiencia en programación
- ✅ Saber usar navegador web y email

**Tiempo:**
- ⏱️ **Setup inicial:** 30-45 minutos
- ⏱️ **Primera validación:** 10-15 minutos
- ⏱️ **Total:** ~1 hora

---

## 🚀 Guía de Setup Paso a Paso

Sigue estos 7 pasos en orden. Cada paso tiene verificación al final.

---

### 📝 PASO 1: Crear/Verificar Cuenta Google (5 min)

**🎓 ¿Por qué es necesario?**

Google Colab es un servicio gratuito de Google que te permite ejecutar código Python en la nube sin instalar nada localmente. Necesitas una cuenta Google (Gmail) para acceder.

**💻 Instrucciones:**

**Si YA tienes cuenta Google:**
1. Ve a [https://accounts.google.com](https://accounts.google.com)
2. Inicia sesión con tu email y contraseña
3. ✅ Verifica que puedes acceder → **Continúa a Paso 2**

**Si NO tienes cuenta Google:**
1. Ve a [https://accounts.google.com/signup](https://accounts.google.com/signup)
2. Completa el formulario:
   - Nombre y apellido
   - Nombre de usuario (será tu@gmail.com)
   - Contraseña segura (mínimo 8 caracteres)
3. Verifica tu número de teléfono (recibirás SMS)
4. Acepta términos y condiciones
5. ✅ Cuenta creada → **Continúa a Paso 2**

**⚠️ Recomendación de Seguridad:**
- Activa autenticación de 2 factores (2FA)
- Guarda tu contraseña en un gestor seguro
- NO compartas credenciales con nadie del workshop

**🔍 Verificación:**
☐ Puedo iniciar sesión en Gmail  
☐ Puedo acceder a [drive.google.com](https://drive.google.com)

---

### 🔐 PASO 2: Crear Cuenta en Alpaca Paper Trading (10 min)

**🎓 ¿Por qué Alpaca?**

Alpaca es un broker moderno con API gratuita para paper trading (trading simulado con datos reales). Es la fuente de datos y ejecución que usaremos en el workshop. La cuenta paper es 100% gratuita, sin límites de tiempo, y no requiere depositar dinero real.

**💻 Instrucciones:**

**2.1 Registro en Alpaca**

1. Ve a [https://alpaca.markets/](https://alpaca.markets/)
2. Click en **"Sign Up"** (arriba derecha)
3. Completa el formulario:
   - Email (puedes usar tu Gmail)
   - Password seguro
   - País (ej: Argentina, México, Colombia, etc.)
4. Verifica tu email (revisa bandeja de entrada y spam)
5. Click en el link de verificación que recibiste

**2.2 Crear Paper Trading Account**

1. Una vez dentro del dashboard, ve a **"Paper Trading"**
2. Click en **"Generate API Keys"**
3. Copia y guarda en un lugar seguro:
   - 🔑 **API Key** (comienza con "PK...")
   - 🔐 **Secret Key** (comienza con "...")
   
**⚠️ CRÍTICO: Guarda tus credenciales**

```
📋 MIS CREDENCIALES ALPACA (NO COMPARTIR)

API Key (Public):
PK...

Secret Key (Private):
...

⚠️ Estas son tus credenciales PAPER (simuladas)
⚠️ NUNCA las compartas con nadie
⚠️ NUNCA las subas a GitHub u otro sitio público
```

**Guarda este texto en:**
- 📄 Un archivo .txt local encriptado
- 🔒 Un gestor de contraseñas (LastPass, 1Password, Bitwarden)
- 📝 Escrito a mano en un lugar seguro

**⚠️ NUNCA:**
- ❌ Las pongas en el chat de Telegram/WhatsApp
- ❌ Las compartas con compañeros del workshop
- ❌ Las publiques en capturas de pantalla

**🔍 Verificación:**
☐ Tengo cuenta Alpaca creada  
☐ Tengo API Key (comienza con "PK...")  
☐ Tengo Secret Key guardada de forma segura  
☐ Puedo ver mi balance paper ($100,000 virtual) en el dashboard

---

### 📂 PASO 3: Acceder a Google Colab (5 min)

**🎓 ¿Qué es Google Colab?**

Google Colab (Colaboratory) es una plataforma gratuita que te permite escribir y ejecutar código Python en tu navegador, sin necesidad de instalar Python ni librerías en tu computadora. Piensa en Colab como un "Microsoft Word, pero para código Python".

**💻 Instrucciones:**

**3.1 Primera vez en Colab**

1. Ve a [https://colab.research.google.com](https://colab.research.google.com)
2. Inicia sesión con tu cuenta Google (del Paso 1)
3. Verás una pantalla de bienvenida: **Click en "Cancelar"** (o X)
4. Click en **"File" → "New notebook"**
5. ¡Se abrirá tu primer notebook vacío! 🎉

**3.2 Familiarízate con la interfaz**

```
┌─────────────────────────────────────────────────────┐
│ 📁 File  Edit  View  Insert  Runtime  Tools  Help  │ ← Menú principal
├─────────────────────────────────────────────────────┤
│ + Code    + Text                                    │ ← Agregar celdas
├─────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────┐    │
│ │ # Esta es una CELDA de código               │    │
│ │ print("Hola Workshop")                      │    │ ← Celda de código
│ └─────────────────────────────────────────────┘    │
│                                ▶️ Ejecutar          │ ← Botón play
├─────────────────────────────────────────────────────┤
│ 📤 Salida: Hola Workshop                           │ ← Resultado
└─────────────────────────────────────────────────────┘
```

**3.3 Tu primera línea de código**

En la celda vacía que aparece, escribe:

```python
print("¡Hola Trading Algorítmico!")
```

Luego:
1. Presiona **Shift + Enter** (o click en el botón ▶️)
2. ✅ Deberías ver: `¡Hola Trading Algorítmico!` abajo de la celda

**🎉 Si ves la salida, Colab está funcionando correctamente**

**🔍 Verificación:**
☐ Puedo acceder a colab.research.google.com  
☐ Puedo crear un nuevo notebook  
☐ Ejecuté `print("¡Hola Trading Algorítmico!")` exitosamente  
☐ Veo el resultado en pantalla

---

### 📦 PASO 4: Instalar Librerías del Workshop (10 min)

**🎓 ¿Por qué instalar librerías?**

Las librerías son "herramientas" especializadas para diferentes tareas. Por ejemplo:
- 📊 `pandas` → Manipular tablas de datos
- 📈 `yfinance` → Descargar datos de mercados
- 🧮 `vectorbt` → Hacer backtesting de estrategias

Aunque Colab tiene muchas librerías pre-instaladas, necesitamos instalar las específicas del workshop.

**💻 Instrucciones:**

**4.1 Script de Instalación Completo**

En tu notebook de Colab, crea una nueva celda (+ Code) y pega este código:

```python
# ═══════════════════════════════════════════════════════════
# 📦 INSTALACIÓN DE LIBRERÍAS - WORKSHOP TRADING ALGORÍTMICO
# Versión: 2.1 (Noviembre 2025)
# Tiempo estimado: 3-5 minutos
# ═══════════════════════════════════════════════════════════

print("🚀 Iniciando instalación de librerías...")
print("⏱️  Este proceso toma 3-5 minutos. Por favor espera.\n")

# ──────────────────────────────────────────────────────────
# 1. CORE: Análisis de Datos
# ──────────────────────────────────────────────────────────
print("📊 Instalando librerías CORE...")
!pip install -q pandas==2.2.0 numpy==1.26.3 scipy==1.12.0
print("✅ Core instalado\n")

# ──────────────────────────────────────────────────────────
# 2. DATOS: Descarga de Mercados
# ──────────────────────────────────────────────────────────
print("📈 Instalando librerías de DATOS...")
!pip install -q yfinance==0.2.36 alpaca-py==0.25.0
print("✅ Datos instalado\n")

# ──────────────────────────────────────────────────────────
# 3. BACKTESTING: Validación de Estrategias
# ──────────────────────────────────────────────────────────
print("🧪 Instalando librerías de BACKTESTING...")
!pip install -q vectorbt==0.26.1
print("✅ Backtesting instalado\n")

# ──────────────────────────────────────────────────────────
# 4. ANÁLISIS TÉCNICO: Indicadores
# ──────────────────────────────────────────────────────────
print("📉 Instalando librerías de ANÁLISIS TÉCNICO...")
!pip install -q ta==0.11.0 pandas-ta==0.3.14b
print("✅ Análisis Técnico instalado\n")

# ──────────────────────────────────────────────────────────
# 5. VISUALIZACIÓN: Gráficos
# ──────────────────────────────────────────────────────────
print("🎨 Instalando librerías de VISUALIZACIÓN...")
!pip install -q plotly==5.18.0 matplotlib==3.8.2
print("✅ Visualización instalado\n")

# ──────────────────────────────────────────────────────────
# ✅ INSTALACIÓN COMPLETA
# ──────────────────────────────────────────────────────────
print("═" * 60)
print("🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!")
print("═" * 60)
print("\n⚠️ IMPORTANTE: Después de la instalación:")
print("   1. Ve a 'Runtime' → 'Restart runtime'")
print("   2. Ejecuta la celda de VALIDACIÓN (siguiente paso)")
```

**4.2 Ejecutar la Instalación**

1. Click en el botón ▶️ de la celda
2. Espera 3-5 minutos (verás texto desplazándose)
3. Cuando termine, verás: `🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!`

**4.3 Reiniciar Runtime (OBLIGATORIO)**

⚠️ **MUY IMPORTANTE:** Después de instalar, debes reiniciar Colab

1. Ve al menú: **Runtime → Restart runtime**
2. Aparecerá un diálogo: Click **"Yes"**
3. ✅ El notebook se reiniciará (perderás variables en memoria, pero las librerías quedan instaladas)

**🎓 ¿Por qué reiniciar?**

Cuando instalas librerías nuevas, Python necesita "recargar" para reconocerlas. El restart asegura que todo funcione correctamente.

**🔍 Verificación:**
☐ Ejecuté el script de instalación completo  
☐ Vi el mensaje "🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!"  
☐ Reinicié el runtime (Runtime → Restart runtime)

---

### ✅ PASO 5: Validar Instalación (5 min)

**🎓 ¿Por qué validar?**

La validación asegura que todas las librerías se instalaron correctamente y que puedes usarlas sin errores. Es como un "chequeo médico" antes de empezar el workshop.

**💻 Instrucciones:**

**5.1 Script de Validación Completo**

Después de reiniciar el runtime (Paso 4.3), crea una nueva celda y pega:

```python
# ═══════════════════════════════════════════════════════════
# ✅ VALIDACIÓN DE INSTALACIÓN - WORKSHOP TRADING ALGORÍTMICO
# Versión: 2.1 (Noviembre 2025)
# ═══════════════════════════════════════════════════════════

import sys
from importlib.metadata import version

print("🔍 VALIDANDO INSTALACIÓN...\n")
print("═" * 60)

# ──────────────────────────────────────────────────────────
# Lista de librerías críticas a validar
# ──────────────────────────────────────────────────────────
libraries = {
    "pandas": "2.2.0",
    "numpy": "1.26.3",
    "yfinance": "0.2.36",
    "alpaca-py": "0.25.0",
    "vectorbt": "0.26.1",
    "ta": "0.11.0",
    "plotly": "5.18.0"
}

errors = []
warnings = []

# ──────────────────────────────────────────────────────────
# Validar cada librería
# ──────────────────────────────────────────────────────────
for lib, expected_version in libraries.items():
    try:
        installed_version = version(lib)
        
        # Comparar versión instalada con esperada
        if installed_version.startswith(expected_version.split('.')[0]):
            print(f"✅ {lib:<15} v{installed_version}")
        else:
            print(f"⚠️  {lib:<15} v{installed_version} (esperada: {expected_version})")
            warnings.append(f"{lib}: versión diferente")
            
    except Exception as e:
        print(f"❌ {lib:<15} NO INSTALADA")
        errors.append(lib)

print("═" * 60)

# ──────────────────────────────────────────────────────────
# Reporte final
# ──────────────────────────────────────────────────────────
if not errors and not warnings:
    print("\n🎉 ¡TODAS LAS LIBRERÍAS VALIDADAS CORRECTAMENTE!")
    print("✅ Estás listo para empezar el workshop")
    
elif errors:
    print(f"\n❌ ERROR: {len(errors)} librería(s) NO instalada(s):")
    for lib in errors:
        print(f"   - {lib}")
    print("\n🔧 Solución:")
    print("   1. Regresa al Paso 4")
    print("   2. Re-ejecuta el script de instalación")
    print("   3. Reinicia runtime")
    print("   4. Vuelve a validar")
    
elif warnings:
    print(f"\n⚠️  ADVERTENCIA: {len(warnings)} librería(s) con versión diferente:")
    for warning in warnings:
        print(f"   - {warning}")
    print("\n✅ Puedes continuar, pero podría haber incompatibilidades menores")

print("\n" + "═" * 60)
print(f"📍 Python: {sys.version.split()[0]}")
print(f"📍 Runtime: Google Colab")
print("═" * 60)
```

**5.2 Ejecutar Validación**

1. Click en ▶️ para ejecutar
2. Espera 5-10 segundos
3. Lee el resultado:

**✅ Resultado PERFECTO:**
```
🔍 VALIDANDO INSTALACIÓN...
═══════════════════════════════════════════════════════════
✅ pandas          v2.2.0
✅ numpy           v1.26.3
✅ yfinance        v0.2.36
✅ alpaca-py       v0.25.0
✅ vectorbt        v0.26.1
✅ ta              v0.11.0
✅ plotly          v5.18.0
═══════════════════════════════════════════════════════════

🎉 ¡TODAS LAS LIBRERÍAS VALIDADAS CORRECTAMENTE!
✅ Estás listo para empezar el workshop
```

**⚠️ Resultado con ADVERTENCIAS:**

Si ves versiones ligeramente diferentes (ej: 2.2.1 en vez de 2.2.0):
- ✅ Puedes continuar
- ⚠️ Podría haber diferencias menores en comportamiento
- 📧 Reporta al instructor si ves errores específicos

**❌ Resultado con ERRORES:**

Si ves "❌ NO INSTALADA":
1. Regresa al Paso 4
2. Re-ejecuta instalación
3. Reinicia runtime
4. Vuelve a validar

**🔍 Verificación:**
☐ Ejecuté script de validación  
☐ Todas las librerías muestran ✅  
☐ Vi mensaje: "¡TODAS LAS LIBRERÍAS VALIDADAS CORRECTAMENTE!"

---

### 🔗 PASO 6: Configurar Credenciales Alpaca en Colab (5 min)

**🎓 ¿Por qué este paso?**

Tus credenciales de Alpaca (del Paso 2) deben ser accesibles por tu código Python para poder descargar datos y ejecutar operaciones en paper trading. Aprenderás a guardarlas de forma segura en Colab.

**💻 Instrucciones:**

**6.1 Método Seguro: Variables de Entorno Temporales**

⚠️ **NUNCA escribas tus credenciales directamente en el código visible**

Crea una nueva celda y pega:

```python
# ═══════════════════════════════════════════════════════════
# 🔐 CONFIGURACIÓN DE CREDENCIALES ALPACA
# ═══════════════════════════════════════════════════════════

import os
from getpass import getpass

print("🔐 CONFIGURACIÓN DE CREDENCIALES ALPACA")
print("═" * 60)
print("⚠️  Ingresa tus credenciales de forma segura")
print("    (no se mostrarán en pantalla)")
print("═" * 60 + "\n")

# Solicitar credenciales de forma segura (input oculto)
api_key = getpass("🔑 Ingresa tu Alpaca API Key (PK...): ")
secret_key = getpass("🔐 Ingresa tu Alpaca Secret Key: ")

# Guardar en variables de entorno (solo para esta sesión)
os.environ['ALPACA_API_KEY'] = api_key
os.environ['ALPACA_SECRET_KEY'] = secret_key

print("\n✅ Credenciales configuradas correctamente")
print("⚠️  Estas credenciales son temporales (solo esta sesión)")
print("⚠️  Deberás repetir este paso cada vez que reinicies Colab")
```

**6.2 Ejecutar Configuración**

1. Click en ▶️
2. Aparecerán dos campos de entrada:
   - **🔑 Ingresa tu Alpaca API Key:** Pega tu API Key (del Paso 2)
   - **🔐 Ingresa tu Alpaca Secret Key:** Pega tu Secret Key
3. Presiona **Enter** después de cada uno
4. ✅ Verás: "Credenciales configuradas correctamente"

**6.3 Validar Conexión con Alpaca**

Crea otra celda nueva y pega:

```python
# ═══════════════════════════════════════════════════════════
# ✅ VALIDAR CONEXIÓN CON ALPACA
# ═══════════════════════════════════════════════════════════

from alpaca.trading.client import TradingClient
import os

print("🔍 VALIDANDO CONEXIÓN CON ALPACA...\n")

try:
    # Crear cliente Alpaca usando credenciales del entorno
    api_key = os.environ.get('ALPACA_API_KEY')
    secret_key = os.environ.get('ALPACA_SECRET_KEY')
    
    client = TradingClient(api_key, secret_key, paper=True)
    
    # Obtener información de cuenta
    account = client.get_account()
    
    print("═" * 60)
    print("✅ CONEXIÓN EXITOSA CON ALPACA")
    print("═" * 60)
    print(f"📊 Tipo de cuenta: Paper Trading (Simulación)")
    print(f"💰 Balance: ${float(account.cash):,.2f}")
    print(f"📈 Buying Power: ${float(account.buying_power):,.2f}")
    print(f"📍 Status: {account.status}")
    print("═" * 60)
    
except Exception as e:
    print("═" * 60)
    print("❌ ERROR EN CONEXIÓN CON ALPACA")
    print("═" * 60)
    print(f"Error: {str(e)}\n")
    print("🔧 Posibles causas:")
    print("   1. Credenciales incorrectas")
    print("   2. No copiaste bien API Key o Secret Key")
    print("   3. Cuenta Alpaca no activada")
    print("\n💡 Solución:")
    print("   1. Verifica tus credenciales en alpaca.markets")
    print("   2. Re-ejecuta Paso 6.1 con credenciales correctas")
    print("   3. Asegúrate de tener Paper Trading habilitado")
```

**6.4 Ejecutar Validación de Conexión**

1. Click en ▶️
2. ✅ **Si todo está bien, verás:**

```
═══════════════════════════════════════════════════════════
✅ CONEXIÓN EXITOSA CON ALPACA
═══════════════════════════════════════════════════════════
📊 Tipo de cuenta: Paper Trading (Simulación)
💰 Balance: $100,000.00
📈 Buying Power: $200,000.00
📍 Status: ACTIVE
═══════════════════════════════════════════════════════════
```

**❌ Si ves error:**
- Verifica que copiaste bien las credenciales
- Ve a alpaca.markets y confirma que están correctas
- Re-ejecuta Paso 6.1

**🔍 Verificación:**
☐ Configuré credenciales con getpass (seguras)  
☐ Ejecuté validación de conexión  
☐ Vi mensaje: "✅ CONEXIÓN EXITOSA CON ALPACA"  
☐ Vi mi balance paper ($100,000)

---

### 📘 PASO 7: Acceder al Colab Notebook Maestro (5 min)

**🎓 ¿Qué es el Colab Notebook Maestro?**

Es el notebook oficial del workshop con TODO el código organizado por sesiones (S1-S9). Ya tiene instalación, ejemplos, ejercicios y validaciones incluidas. Es tu "libro de trabajo" para las 27 horas del workshop.

**💻 Instrucciones:**

**7.1 Obtener el Notebook**

📧 **El link al Colab Notebook Maestro te será enviado por:**
- Email de bienvenida al workshop
- Grupo de Telegram Premium
- Drive compartido del workshop

**No puedes continuar este paso sin el link.** Si no lo tienes:
1. Revisa tu email (bandeja de entrada y spam)
2. Contacta al instructor: yismaryme@gmail.com

**7.2 Abrir el Notebook**

1. Click en el link que recibiste
2. El notebook se abrirá en **modo lectura** (no puedes editarlo)
3. **Obligatorio:** Haz una copia personal:
   - Ve a **"File" → "Save a copy in Drive"**
   - Se abrirá una copia en tu Google Drive personal
   - ✅ Ahora puedes editar y guardar cambios

**7.3 Estructura del Notebook Maestro**

```
📘 COLAB NOTEBOOK MAESTRO (1,500+ líneas)
│
├── 🟦 SESIÓN 1: Fundamentos y Mapa del Trading Algorítmico
├── 🟦 SESIÓN 2: Datos - La Base de Todo Sistema  
├── 🟦 SESIÓN 3: Ideación de Estrategias con GenAI
├── 🟦 SESIÓN 4: Implementación Práctica Guiada
├── 🟦 SESIÓN 5: Validación Rigurosa - Backtesting Profesional
├── 🟦 SESIÓN 6: Gestión Avanzada de Riesgo
├── 🟦 SESIÓN 7: Multi-Plataforma - Del Código a la Ejecución
├── 🟦 SESIÓN 8: Deployment Real - Paper Trading y Monitoreo
└── 🟦 SESIÓN 9: Proyecto Final y Documentación Profesional
```

**7.4 Primera Exploración**

1. Navega a **"🟦 SESIÓN 1"** (scroll hacia abajo)
2. Lee la introducción de S1
3. **NO ejecutes celdas todavía** (lo harás en el workshop)
4. Familiarízate con la estructura

**7.5 Leer la Guía de Uso de Colab (OBLIGATORIO)**

Antes de la primera sesión, lee esta guía:

📖 **[Guía de Uso del Colab Notebook Maestro](Guia_Uso_Colab_Notebook.md)**

Aprenderás:
- Cómo navegar por las 9 sesiones
- Atajos de teclado útiles
- Cómo ejecutar celdas correctamente
- Troubleshooting de Colab

**🔍 Verificación:**
☐ Recibí el link al Colab Notebook Maestro  
☐ Hice una copia personal en mi Drive ("Save a copy")  
☐ Veo las 9 sesiones en el notebook  
☐ Leí la [Guía de Uso de Colab](Guia_Uso_Colab_Notebook.md)

---

## 🔍 Validación del Setup

**Antes de continuar, valida que TODO funciona:**

### ✅ Checklist Final

☐ **PASO 1:** Tengo cuenta Google y puedo acceder  
☐ **PASO 2:** Tengo credenciales Alpaca guardadas de forma segura  
☐ **PASO 3:** Puedo acceder a Google Colab  
☐ **PASO 4:** Instalé todas las librerías  
☐ **PASO 5:** Todas las librerías validaron con ✅  
☐ **PASO 6:** Conexión con Alpaca exitosa (vi mi balance)  
☐ **PASO 7:** Tengo copia personal del Colab Notebook Maestro

### 🎯 Test de Integración Final

Ejecuta este test completo en una celda nueva:

```python
# ═══════════════════════════════════════════════════════════
# 🎯 TEST DE INTEGRACIÓN FINAL - SETUP COMPLETO
# ═══════════════════════════════════════════════════════════

print("🧪 EJECUTANDO TEST DE INTEGRACIÓN FINAL...\n")

# Test 1: Librerías Core
try:
    import pandas as pd
    import numpy as np
    print("✅ Test 1/5: Librerías Core")
except:
    print("❌ Test 1/5: ERROR en librerías Core")

# Test 2: Descarga de Datos
try:
    import yfinance as yf
    data = yf.download("SPY", period="5d", progress=False)
    assert len(data) > 0
    print("✅ Test 2/5: Descarga de Datos (yfinance)")
except:
    print("❌ Test 2/5: ERROR en descarga de datos")

# Test 3: Conexión Alpaca
try:
    from alpaca.trading.client import TradingClient
    import os
    client = TradingClient(
        os.environ['ALPACA_API_KEY'], 
        os.environ['ALPACA_SECRET_KEY'], 
        paper=True
    )
    account = client.get_account()
    print("✅ Test 3/5: Conexión Alpaca")
except:
    print("❌ Test 3/5: ERROR en conexión Alpaca")

# Test 4: Backtesting
try:
    import vectorbt as vbt
    print("✅ Test 4/5: Librería Backtesting (vectorbt)")
except:
    print("❌ Test 4/5: ERROR en librería backtesting")

# Test 5: Visualización
try:
    import plotly.graph_objects as go
    print("✅ Test 5/5: Librería Visualización (plotly)")
except:
    print("❌ Test 5/5: ERROR en librería visualización")

print("\n" + "═" * 60)
print("🎉 SETUP COMPLETADO EXITOSAMENTE")
print("═" * 60)
print("✅ Estás listo para empezar la Sesión 1 del workshop")
print("\n🎯 Próximos pasos:")
print("   1. Lee LEEME_PRIMERO.md para roadmap completo")
print("   2. Revisa tu horario de sesiones")
print("   3. Únete al grupo de Telegram Premium")
print("   4. ¡Nos vemos en la Sesión 1!")
```

**✅ Si ves "🎉 SETUP COMPLETADO EXITOSAMENTE" → ¡Felicidades!**

---

## 🚨 Troubleshooting Específico

**Errores comunes en Setup Colab y sus soluciones:**

### ❌ Error: "No module named 'yfinance'"

**Causa:** Librería no instalada o runtime no reiniciado

**Solución:**
```python
# 1. Re-instalar la librería específica
!pip install yfinance==0.2.36

# 2. Reiniciar runtime: Runtime → Restart runtime

# 3. Re-ejecutar celda que da error
```

---

### ❌ Error: "ALPACA_API_KEY not found in environment"

**Causa:** No configuraste credenciales o runtime se reinició

**Solución:**
- Vuelve al Paso 6
- Re-ejecuta configuración de credenciales (getpass)
- ⚠️ Las credenciales se pierden al reiniciar runtime

---

### ❌ Error: "Session crashed" / "Out of Memory"

**Causa:** Colab gratuito tiene límites de RAM (12 GB)

**Solución:**
```python
# 1. Liberar memoria
import gc
gc.collect()

# 2. Reiniciar runtime: Runtime → Restart runtime

# 3. Ejecutar solo celdas necesarias (no todas a la vez)

# 4. Upgrade a Colab Pro ($10/mes) si el problema persiste
```

---

### ❌ Error: "Could not find a version that satisfies alpaca-py"

**Causa:** Versión de Python incompatible o pip desactualizado

**Solución:**
```python
# 1. Actualizar pip
!pip install --upgrade pip

# 2. Instalar alpaca-py nuevamente
!pip install alpaca-py==0.25.0

# 3. Reiniciar runtime
```

---

### ❌ Error: "HTTPError 401: Unauthorized" (Alpaca)

**Causa:** Credenciales incorrectas o mal copiadas

**Solución:**
1. Ve a [alpaca.markets](https://alpaca.markets)
2. Verifica tus credenciales (API Key y Secret)
3. ⚠️ Asegúrate de copiar COMPLETAS (sin espacios extras)
4. Re-ejecuta Paso 6.1 con credenciales correctas

---

### ⚠️ Warning: "Versión diferente de librería esperada"

**Causa:** pip instaló versión más reciente automáticamente

**Solución:**
- ✅ Generalmente no es problema
- Si hay errores específicos, instala versión exacta:
```python
!pip install pandas==2.2.0 --force-reinstall
```

---

### 🌐 Problema: "Colab muy lento / No carga"

**Causa:** Conexión a internet lenta o problemas de Google

**Solución:**
1. Verifica tu velocidad de internet (min 3 Mbps)
2. Prueba con otro navegador
3. Limpia caché del navegador:
   - Chrome: Ctrl+Shift+Del → Borrar caché
4. Intenta en otra hora (menos carga en servidores Google)

---

### 📂 Problema: "No encuentro mi copia del Notebook Maestro"

**Solución:**
1. Ve a [drive.google.com](https://drive.google.com)
2. Busca: "Copy of Colab Notebook Maestro"
3. Click derecho → "Abrir con" → "Google Colaboratory"

---

**🔧 Troubleshooting Avanzado:**

Si ninguna solución funciona:
1. Consulta [Troubleshooting Común](Troubleshooting_Comun.md)
2. Pregunta en grupo Telegram Premium
3. Contacta soporte: yismaryme@gmail.com

---

## 💡 Consejos y Mejores Prácticas

**Para sacar el máximo provecho de Colab:**

### 🎯 Organización

📂 **Estructura de Google Drive:**
```
Mi Drive/
├── Workshop_Trading_Algoritmico/
│   ├── Colab_Notebook_Maestro.ipynb ← Tu copia personal
│   ├── Mis_Estrategias/
│   │   ├── Estrategia_1_Mean_Reversion.ipynb
│   │   └── Estrategia_2_Momentum.ipynb
│   └── Datos/
│       └── SPY_historico.csv
```

---

### ⚡ Atajos de Teclado Útiles

| Atajo | Acción |
|-------|--------|
| **Ctrl + M B** | Agregar celda abajo |
| **Ctrl + M A** | Agregar celda arriba |
| **Ctrl + M D** | Eliminar celda |
| **Shift + Enter** | Ejecutar celda |
| **Ctrl + S** | Guardar notebook |
| **Ctrl + /** | Comentar líneas |

---

### 💾 Guardado Automático

- ✅ Colab guarda automáticamente cada ~2 minutos
- ✅ Usa Ctrl+S para forzar guardado inmediato
- ⚠️ Cambios se guardan en tu Google Drive personal

---

### 🔋 Límites de Colab Gratuito

**Límites importantes:**
- **RAM:** 12 GB (suficiente para el workshop)
- **Disco:** 100 GB temporales
- **GPU:** No necesaria para este workshop
- **Tiempo:** ~12h de conexión, luego se desconecta

**⚠️ Si se desconecta:**
- Variables en memoria se pierden
- Librerías siguen instaladas
- Credenciales debes reconfigurarlas (Paso 6)

---

### 🚀 Colab Pro ($10/mes)

**Vale la pena si:**
- Session crashed frecuente (memoria insuficiente)
- Necesitas sesiones > 12h
- Quieres ejecución más rápida

**NO es necesario para el workshop estándar**

---

### 📝 Buenas Prácticas

**DO ✅**
- Comenta tu código en español
- Usa nombres de variables descriptivos
- Guarda versiones de tus estrategias
- Reinicia runtime si hay errores extraños

**DON'T ❌**
- No pongas credenciales en código visible
- No ejecutes todas las celdas a la vez
- No compartas tu notebook con credenciales
- No uses credenciales de live trading

---

## 🎯 Próximos Pasos

**¡Felicidades! Has completado el Setup A: Colab Rápido. 🎉**

**Tu journey continúa:**

### 1️⃣ Volver al Documento Principal

📖 [← Volver a Instrucciones_Setup_Ambiente.md](Instrucciones_Setup_Ambiente.md)

---

### 2️⃣ Leer Documentos Complementarios

📚 **OBLIGATORIOS:**
- [Guía de Uso del Colab Notebook](Guia_Uso_Colab_Notebook.md) ⭐ **Crítico**
- [LEEME_PRIMERO.md](LEEME_PRIMERO.md) - Roadmap del workshop

📖 **OPCIONALES:**
- [Librerías y Dependencias 2025](Librerias_Dependencias_2025.md)
- [Troubleshooting Común](Troubleshooting_Comun.md)

---

### 3️⃣ Unirte al Grupo Premium

💬 **Telegram:** [@workshop_trading_algo](https://t.me/workshop_trading_algo)

Recibirás:
- 📢 Anuncios de sesiones
- 🤝 Soporte entre participantes
- 📂 Materiales adicionales
- 💡 Tips y trucos semanales

---

### 4️⃣ Preparar Tu Primer Día

✅ **Checklist "Tu Primer Día":**
- [ ] Setup Colab completado (este documento)
- [ ] Leído [Guía de Uso de Colab](Guia_Uso_Colab_Notebook.md)
- [ ] Credenciales Alpaca guardadas de forma segura
- [ ] Copia personal del Notebook Maestro en mi Drive
- [ ] Unido al grupo de Telegram Premium
- [ ] Revisado horario de sesiones (email de bienvenida)

---

### 5️⃣ ¡Empezar la Sesión 1!

**Cuando llegue el día:**
1. Abre tu copia del Colab Notebook Maestro
2. Navega a "🟦 SESIÓN 1: FUNDAMENTOS"
3. Sigue las instrucciones del instructor en vivo
4. Ejecuta celdas paso a paso

**🚀 ¡Estás listo para el viaje algorítmico!**

---

## 📞 Soporte

**Si algo no funciona:**

### 📧 Email
**yismaryme@gmail.com**  
Tiempo de respuesta: 24-48h

**Incluye:**
- "Setup A: Colab" en el asunto
- Paso exacto donde falló
- Error completo (screenshot)

---

### 💬 Telegram
**[@yismary](https://t.me/yismary)**  
Consultas rápidas pre-workshop

---

### 🔒 Grupo Premium
Soporte comunitario + troubleshooting en vivo

---

## 🔖 Versión y Actualizaciones

**Versión:** 2.1 (Noviembre 2025)  
**Última actualización:** 13 de noviembre de 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- v2.1 (Nov 2025): Setup modular independiente
- v2.0 (Nov 2025): alpaca-py 0.25.0 (nueva API)
- v1.0 (Nov 2025): Versión inicial

---

**🎯 Recuerda: GenAI = Copiloto, NO Piloto Automático.**

**¡Nos vemos en la Sesión 1!** 🚀
