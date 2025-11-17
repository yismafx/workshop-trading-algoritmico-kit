# 🎓 SETUP A: GUIADO (MÁXIMO DETALLE)

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 **Setup A: Guiado**

---

**⏱️ Tiempo estimado:** 60-90 minutos  
**🎓 Dificultad:** ⭐ Principiante (0 experiencia Python requerida)  
**📅 Última actualización:** 17 de noviembre de 2025  
**📌 Versión:** 3.0

---

## 💡 ¿OTRAS RUTAS DE SETUP?

> ⚡ **¿Versión ultra-rápida?**  
> [Setup A: Express →](Setup_A_Express.md) (10-15 min)  
> Solo comandos + validación mínima

> 📚 **¿Versión estándar?** ⭐ RECOMENDADO  
> [Setup A: Colab Completo →](Setup_A_Colab_Rapido.md) (30-45 min)  
> Balance perfecto detalle/velocidad

> 📖 **¿Versión guiada?** ESTÁS AQUÍ  
> Setup A: Guiado (60-90 min)  
> Máximo detalle pedagógico + conceptos fundamentales

---

## 📑 TABLA DE CONTENIDOS

- [🎯 ¿Por Qué Esta Versión?](#-por-qué-esta-versión)
- [🧠 Conceptos Fundamentales](#-conceptos-fundamentales-antes-de-empezar)
- [✅ Pre-Requisitos Detallados](#-pre-requisitos-detallados)
- [🔐 Paso 1: Registro en Alpaca (Paper Trading)](#-paso-1-registro-en-alpaca-paper-trading)
- [☁️ Paso 2: Configuración de Google Colab](#️-paso-2-configuración-de-google-colab)
- [🔗 Paso 3: Conexión Alpaca + Colab](#-paso-3-conexión-alpaca--colab)
- [✅ Paso 4: Validación Completa del Setup](#-paso-4-validación-completa-del-setup)
- [🎓 Paso 5: Primeros Pasos en Colab](#-paso-5-primeros-pasos-en-colab)
- [🚨 Troubleshooting Expandido](#-troubleshooting-expandido)
- [🔗 Ver También](#-ver-también)
- [🧭 Navegación](#-navegación)
- [📞 Soporte](#-soporte)
- [📌 Versión y Changelog](#-versión-y-changelog)

---

## 🎯 ¿Por Qué Esta Versión?

**Esta es la versión MÁS DETALLADA del Setup A, diseñada para:**

✅ **Traders sin experiencia en programación**  
Si nunca has escrito código, esta guía te explica cada concepto desde cero

✅ **Participantes que valoran el entendimiento profundo**  
No solo "qué hacer", sino "por qué lo hacemos" y "cómo funciona"

✅ **Personas que prefieren ir despacio y seguro**  
Tiempo adicional invertido aquí = menos fricción durante el workshop

✅ **Troubleshooting preventivo**  
Cubrimos 20+ casos comunes ANTES de que ocurran

---

### 📊 Comparación con Otras Versiones

| Aspecto | Express | Colab Completo | **Guiado** |
|---------|---------|----------------|------------|
| **Tiempo** | 10-15 min | 30-45 min | **60-90 min** |
| **Conceptos explicados** | ❌ No | ✅ Básicos | **✅ Exhaustivos** |
| **Screenshots** | ❌ No | ✅ 8-10 | **✅ 15-20 referencias** |
| **Troubleshooting** | ⚠️ Mínimo | ✅ Común | **✅ Expandido (20+ casos)** |
| **FAQs inline** | ❌ No | ⚠️ Algunas | **✅ Extensas** |
| **Validación** | ⚠️ Básica | ✅ Completa | **✅ Multi-nivel** |

---

**¿Cuándo NO usar esta versión?**

- ❌ Ya tienes experiencia con Python y Colab → Usa [Setup A: Express](Setup_A_Express.md)
- ❌ Tienes tiempo limitado pre-workshop → Usa [Setup A: Colab Completo](Setup_A_Colab_Rapido.md)
- ❌ Necesitas deployment 24/7 → Esta no es tu ruta, usa Setup B

---

## 🧠 Conceptos Fundamentales (Antes de Empezar)

**⏱️ Tiempo de lectura:** 10-15 minutos  
**Objetivo:** Entender QUÉ vamos a configurar y POR QUÉ

---

### 🤔 ¿Qué es Trading Algorítmico?

**Definición simple:**  
Es la automatización de decisiones de trading usando código (en lugar de ejecutar manualmente).

**En el mundo manual:**
1. Analizas el mercado (charts, noticias)
2. Decides: ¿Compro/vendo/espero?
3. Ejecutas la orden manualmente
4. Gestionas la posición (stop loss, take profit)

**En el mundo algorítmico:**
1. Tu **sistema** analiza datos en tiempo real
2. Tu **sistema** decide según reglas pre-programadas
3. Tu **sistema** ejecuta automáticamente
4. Tu **sistema** gestiona la posición según reglas

**Ventaja clave:** Elimina emociones, ejecuta 24/7, backtesting histórico

**Este workshop NO enseña:**
- ❌ Machine Learning para predecir precios
- ❌ "Bots mágicos" que generan dinero automático
- ❌ Estrategias "santas"

**Este workshop SÍ enseña:**
- ✅ Cómo sistematizar TU estrategia manual existente
- ✅ Cómo usar IA Generativa como copiloto (no piloto)
- ✅ Cómo validar estrategias con backtesting riguroso

---

### 🔌 ¿Qué es una API y Por Qué la Necesitamos?

**Analogía simple:**

Imagina que quieres ordenar comida a domicilio:
- **Método antiguo:** Llamas por teléfono, dictas tu orden, esperas confirmación
- **Método moderno:** Usas app (API), la app "habla" con el restaurante automáticamente

**En trading:**
- **Método antiguo:** Abres plataforma del broker, clicas botones manualmente
- **Método moderno:** Tu código "habla" con el broker vía API

**API = Conector automatizado entre tu código y el broker**

**Lo que la API permite hacer:**
- ✅ Obtener precios en tiempo real
- ✅ Descargar datos históricos
- ✅ Enviar órdenes de compra/venta
- ✅ Consultar tu balance y posiciones
- ✅ Recibir notificaciones de ejecución

**Sin API:**  
Tu código no puede "tocar" el mercado → Solo análisis offline

**Con API:**  
Tu código puede ejecutar trades reales → Trading algorítmico completo

---

### 📊 ¿Qué es un Broker y Por Qué Alpaca?

**Broker = Intermediario entre tú y el mercado**

Cuando compras una acción, no la compras directamente de la empresa.  
El broker ejecuta la orden en el mercado en tu nombre.

**¿Por qué Alpaca para este workshop?**

✅ **Paper Trading gratis ilimitado**  
Puedes practicar sin arriesgar dinero real

✅ **API moderna y simple**  
Diseñada específicamente para trading algorítmico

✅ **Documentación excelente**  
Fácil de aprender vs. brokers tradicionales

✅ **Datos gratuitos**  
15 minutos de delay es suficiente para aprendizaje

✅ **Sin requisitos de capital mínimo**  
No necesitas depositar dinero para usar paper trading

**Otros brokers que veremos en el workshop:**
- **MetaTrader 5:** Forex/CFDs (Setup C)
- **Interactive Brokers:** Multi-mercado profesional (Setup D)

**Hoy configuraremos Alpaca porque es el más rápido para empezar.**

---

### ☁️ ¿Qué es Google Colab y Por Qué lo Usamos?

**Google Colab = Excel para código Python**

**Analogía:**  
Así como Google Sheets te permite crear hojas de cálculo sin instalar Excel:  
**Colab te permite escribir/ejecutar Python sin instalar nada en tu computadora.**

**Ventajas clave para este workshop:**

✅ **Cero instalación local**  
Todo funciona en el navegador

✅ **Librerías pre-instaladas**  
pandas, numpy, etc. ya están disponibles

✅ **Gratis con recursos decentes**  
CPU + 12 GB RAM sin costo

✅ **Compartible fácilmente**  
Un link y listo

✅ **Acceso desde cualquier dispositivo**  
Windows, Mac, Linux, tablet

**Limitaciones importantes:**

⚠️ **Sesiones temporales**  
Tu código se "olvida" si no lo guardas

⚠️ **No es para deployment 24/7**  
Colab es para aprendizaje/backtesting, no para bots en producción

⚠️ **Tiempo límite de ejecución**  
~12 horas continuas máximo

**Para este workshop:** Colab es perfecto.  
**Para deployment real:** Necesitarás Setup B (Python local + VPS).

---

### 🎯 ¿Qué Vamos a Configurar Exactamente?

**Al final de este setup, tendrás:**

1️⃣ **Cuenta Alpaca Paper Trading** (gratis)  
Con API keys para conectar tu código

2️⃣ **Google Colab configurado**  
Con acceso al notebook maestro del workshop

3️⃣ **Conexión validada Alpaca ↔ Colab**  
Tu código puede "hablar" con Alpaca

4️⃣ **Ambiente listo para Sesión 1**  
Librerías instaladas, troubleshooting resuelto

**Tiempo total:** 60-90 minutos (esta versión guiada)

---

## ✅ Pre-Requisitos Detallados

**Antes de empezar, asegúrate de tener:**

---

### 1️⃣ Cuenta de Google (Gmail)

**¿Por qué?**  
Google Colab requiere autenticación con cuenta Google

**¿Ya tienes Gmail?**  
✅ Perfecto, continúa

**¿No tienes Gmail?**  
📧 Crea una cuenta en: https://accounts.google.com/signup  
Tiempo: 5 minutos

**Recomendación:**  
Usa una cuenta de Gmail que revises regularmente (necesitarás acceso al email)

---

### 2️⃣ Navegador Web Moderno

**Navegadores compatibles:**
- ✅ Chrome (recomendado)
- ✅ Firefox
- ✅ Edge
- ✅ Safari

**Navegadores NO recomendados:**
- ⚠️ Internet Explorer (desactualizado)
- ⚠️ Navegadores móviles (experiencia limitada)

**Validación:**  
Abre https://colab.research.google.com  
Si ves la interfaz de Colab → ✅ Tu navegador funciona

---

### 3️⃣ Conexión a Internet Estable

**Velocidad mínima requerida:**
- Download: 5 Mbps
- Upload: 1 Mbps

**¿Cómo verificar tu velocidad?**  
Abre: https://fast.com  
Tiempo de test: 30 segundos

**Si tienes internet lento:**  
⚠️ Colab puede tener lag, pero seguirá funcionando  
Evita descargar archivos grandes durante el setup

---

### 4️⃣ Email de Confirmación Accesible

**¿Por qué?**  
Alpaca enviará un email de verificación que debes confirmar

**Validación:**  
Abre tu bandeja de entrada de Gmail  
Verifica que NO esté en modo "offline"

---

### 5️⃣ 90 Minutos de Tiempo Ininterrumpido

**Recomendación:**  
No hagas este setup "entre reuniones" o con prisa

**Mejor momento:**
- ✅ Fin de semana por la mañana
- ✅ Después del horario laboral
- ✅ Cualquier momento donde puedas concentrarte

**Si te interrumpen:**  
⚠️ Guarda tu progreso (explicaremos cómo) y continúa después

---

## 🔐 Paso 1: Registro en Alpaca (Paper Trading)

**⏱️ Tiempo estimado:** 15-20 minutos  
**Dificultad:** ⭐ Muy fácil

---

### 🎯 Objetivo de Este Paso

Al final, tendrás:
- ✅ Cuenta Alpaca Paper Trading creada
- ✅ Email verificado
- ✅ API Keys generadas (2 claves secretas)
- ✅ Acceso al dashboard de Alpaca

---

### 📝 Paso 1.1: Registro Inicial

**1. Abre el sitio de registro:**  
🔗 https://app.alpaca.markets/signup

**2. Completa el formulario:**

**Campos requeridos:**
- **Email:** Usa tu Gmail
- **Password:** Mínimo 8 caracteres, incluye números y símbolos
- **First Name / Last Name:** Tu nombre real
- **Country:** Selecciona tu país
- **Phone:** Opcional pero recomendado

**⚠️ Importante:**  
Guarda tu contraseña en un lugar seguro (gestor de contraseñas recomendado)

**3. Acepta términos y condiciones:**

Lee (al menos rápidamente) los términos.  
Marca la casilla "I agree to terms"

**4. Click en "Sign Up"**

**[Screenshot esperado: Formulario de registro de Alpaca]**

---

### 📧 Paso 1.2: Verificación de Email

**1. Revisa tu bandeja de entrada:**

Busca email de: `no-reply@alpaca.markets`  
Asunto: "Verify your email address"

**⚠️ ¿No lo ves?**  
Revisa carpeta SPAM/Promociones

**2. Click en el link de verificación:**

El link expira en 24 horas  
Si expira, solicita nuevo link desde login

**3. Serás redirigido al dashboard:**

✅ Si ves el dashboard de Alpaca → Email verificado correctamente

**[Screenshot esperado: Email de verificación de Alpaca]**

---

### 🔑 Paso 1.3: Generar API Keys

**¿Qué son las API Keys?**

Piensa en ellas como "usuario y contraseña para robots":
- **API Key ID:** Usuario (público)
- **Secret Key:** Contraseña (NUNCA compartir)

**Paso a paso:**

**1. En el dashboard de Alpaca:**

Menú lateral izquierdo → Click en "Paper Trading"  
(NO "Live Trading" - eso requiere fondos reales)

**2. Navega a API Keys:**

Busca sección "API Keys" o "Your API Keys"  
Debería estar en la parte superior derecha

**[Screenshot esperado: Ubicación de API Keys en dashboard]**

**3. Click en "Generate New Keys" o "View":**

Si es tu primera vez, verás "Generate API Keys"  
Si ya generaste antes, verás "Regenerate" (cuidado, invalida las anteriores)

**4. Guarda tus keys INMEDIATAMENTE:**

**⚠️ CRÍTICO:**  
La Secret Key se muestra SOLO UNA VEZ  
Si cierras la ventana sin guardarla, deberás regenerar

**Formato de las keys:**

```
API Key ID:     PK...........................
Secret Key:     ................................
```

**Dónde guardar:**

**✅ Recomendado:**
- Gestor de contraseñas (1Password, LastPass, Bitwarden)
- Archivo de texto en carpeta segura (NO en Desktop)
- Nota encriptada

**❌ NUNCA:**
- Email
- WhatsApp/Telegram
- Repositorio público de GitHub
- Screenshot compartido

**5. Copia ambas keys:**

Usa `Ctrl+C` / `Cmd+C` para copiar  
Pega en tu gestor de contraseñas o archivo seguro

**6. Click en "I Saved My Keys" o "Confirm"**

---

### ✅ Paso 1.4: Verificar Cuenta Paper Trading

**1. Vuelve al dashboard principal:**

Click en "Dashboard" en menú lateral

**2. Verifica que estás en modo Paper:**

Busca indicador en la parte superior:  
Debe decir **"Paper Trading"** (no "Live Trading")

**[Screenshot esperado: Indicador Paper Trading]**

**3. Revisa tu balance inicial:**

Deberías ver:
- **Buying Power:** $100,000 (USD virtuales)
- **Portfolio Value:** $100,000
- **Cash:** $100,000

**Si ves estos valores → ✅ Cuenta creada correctamente**

---

### 🚨 Troubleshooting Paso 1

<details>
<summary><strong>❌ "El email de verificación nunca llegó"</strong></summary>

**Solución:**

1. Espera 5-10 minutos (puede demorar)
2. Revisa SPAM/Promociones
3. Agrega `@alpaca.markets` a contactos seguros
4. Solicita reenvío: Click en "Resend verification email" en login
5. Si nada funciona: Crea cuenta con otro email

</details>

<details>
<summary><strong>❌ "No encuentro el botón Generate API Keys"</strong></summary>

**Solución:**

1. Verifica que estás en sección "Paper Trading" (menú izquierdo)
2. Busca "API Keys" o "Settings" en la parte superior
3. Si no aparece: Cierra sesión y vuelve a entrar
4. Intenta desde navegador incógnito (puede ser problema de cache)

**Ubicación típica:**  
Dashboard → Paper Trading → API Keys (esquina superior derecha)

</details>

<details>
<summary><strong>❌ "Cerré la ventana sin guardar la Secret Key"</strong></summary>

**Solución:**

1. Vuelve a la sección API Keys
2. Click en "Regenerate Keys" o "Revoke and Regenerate"
3. ⚠️ Esto invalida las keys anteriores
4. Guarda las nuevas keys INMEDIATAMENTE

**Prevención:**  
Abre un archivo de texto ANTES de generar las keys

</details>

<details>
<summary><strong>❌ "Me pide verificar identidad con documento"</strong></summary>

**Explicación:**

Paper Trading NO requiere verificación de identidad.  
Si te lo pide, estás intentando activar "Live Trading"

**Solución:**

1. Ignora la verificación de identidad
2. Asegúrate de estar en sección "Paper Trading"
3. El balance virtual de $100k debe aparecer automáticamente

</details>

<details>
<summary><strong>⚠️ "Veo balance $0 en vez de $100k"</strong></summary>

**Causas comunes:**

1. Estás viendo "Live Trading" en vez de "Paper Trading"
2. Cuenta recién creada (espera 1-2 minutos)

**Solución:**

1. Menú izquierdo → Click en "Paper Trading"
2. Refresh la página (F5)
3. Cierra sesión y vuelve a entrar
4. Si persiste: Contacta soporte Alpaca

</details>

**¿Más problemas?** → [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

### ✅ Checklist Paso 1 Completo

Antes de continuar, verifica:

- ☐ Cuenta Alpaca creada
- ☐ Email verificado (recibiste y clickeaste link)
- ☐ API Keys generadas y guardadas en lugar seguro
- ☐ Estás en modo "Paper Trading"
- ☐ Ves balance de $100,000 virtuales

**Si todos los puntos están marcados → 🎉 ¡Paso 1 completo!**

**Tiempo invertido hasta ahora:** ~15-20 minutos  
**Tiempo restante:** ~40-70 minutos

---

## ☁️ Paso 2: Configuración de Google Colab

**⏱️ Tiempo estimado:** 15-20 minutos  
**Dificultad:** ⭐ Muy fácil

---

### 🎯 Objetivo de Este Paso

Al final, tendrás:
- ✅ Acceso a Google Colab
- ✅ Notebook del workshop cargado
- ✅ Familiaridad básica con la interfaz
- ✅ Primer código ejecutado con éxito

---

### 📝 Paso 2.1: Acceder a Google Colab

**1. Abre Google Colab:**  
🔗 https://colab.research.google.com

**2. Inicia sesión con tu cuenta Google:**

Si ya estás logueado en Gmail → Automático  
Si no → Te pedirá email y contraseña

**3. Verás la página de bienvenida:**

**[Screenshot esperado: Pantalla inicial de Colab]**

Elementos clave:
- **Menú superior:** File, Edit, View, Insert, etc.
- **Panel izquierdo:** Archivos, tabla de contenidos
- **Panel central:** Donde escribirás código

**✅ Si ves esta interfaz → Acceso exitoso**

---

### 📓 Paso 2.2: Cargar el Notebook del Workshop

**Opción A: Link directo (recomendado)**

**1. Abre el link del workshop:**  
🔗 [Link será proporcionado al inicio del workshop]

**2. Click en "Copiar a Drive" o "Copy to Drive":**

Esto crea TU copia personal del notebook  
(No modificarás el original)

**3. Renombra tu copia:**

Nombre sugerido: `WTAA_[TuNombre]_Nov2025.ipynb`  
Ejemplo: `WTAA_Maria_Nov2025.ipynb`

---

**Opción B: Subir archivo manualmente**

**Si el link no funciona:**

**1. Descarga el notebook:**  
[Link de descarga del .ipynb]

**2. En Colab → File → Upload notebook**

**3. Selecciona el archivo descargado**

**4. Espera a que cargue (10-20 segundos)**

---

### 🖥️ Paso 2.3: Entender la Interfaz de Colab

**Estructura del Notebook:**

Un notebook es una combinación de:
- **Celdas de texto:** Explicaciones (como esta)
- **Celdas de código:** Python ejecutable

**Analogía:**  
Un notebook es como un documento de Word donde puedes insertar "calculadoras" (celdas de código) que funcionan de verdad.

---

**Elementos clave de la interfaz:**

```
┌─────────────────────────────────────────────────────┐
│  File  Edit  View  Insert  Runtime  Tools  Help    │ ← Menú principal
├─────────────────────────────────────────────────────┤
│  📁 Files    📑 Table of Contents    🔍 Search      │ ← Panel izquierdo
├─────────────────────────────────────────────────────┤
│                                                     │
│  # 🟦 SESIÓN 1: FUNDAMENTOS                         │ ← Celda de texto
│  Este es el contenido de la Sesión 1...            │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │ # Este es código Python                      │  │ ← Celda de código
│  │ print("Hola Workshop")                       │  │
│  │ ▶️ [Run]                                      │  │ ← Botón ejecutar
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  Hola Workshop  ← Output (resultado del código)    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

**Cómo ejecutar una celda de código:**

**Método 1:** Click en el botón ▶️ a la izquierda de la celda  
**Método 2:** `Shift + Enter` (más rápido)  
**Método 3:** `Ctrl + Enter` (ejecuta sin avanzar)

**Probemos:**

**1. Busca esta celda de código en tu notebook:**

```python
# Celda de prueba inicial
print("✅ Mi setup de Colab funciona correctamente")
print("🎓 Estoy listo para el workshop")
```

**2. Ejecuta la celda (Shift + Enter):**

**Resultado esperado:**
```
✅ Mi setup de Colab funciona correctamente
🎓 Estoy listo para el workshop
```

**✅ Si ves este output → Tu Colab funciona**

---

### 🔧 Paso 2.4: Configuración Inicial del Notebook

**Importante:** Este paso instala las librerías necesarias

**1. Busca la sección "⚙️ SETUP INICIAL":**

Debería estar al inicio del notebook  
Título: "⚙️ Instalación de Librerías"

**2. Ejecuta la celda de instalación:**

```python
# SOLO ejecutar una vez al inicio de cada sesión
!pip install alpaca-py yfinance pandas numpy ta -q
```

**Qué hace esta celda:**
- `!pip install`: Comando para instalar librerías Python
- `alpaca-py`: Librería para conectar con Alpaca
- `yfinance`: Librería para obtener datos históricos gratis
- `pandas`: Librería para análisis de datos
- `numpy`: Librería para cálculos matemáticos
- `ta`: Librería para indicadores técnicos
- `-q`: Modo silencioso (menos output)

**⏱️ Tiempo de ejecución:** 30-60 segundos

**Resultado esperado:**
```
Successfully installed alpaca-py-0.x.x yfinance-0.x.x ...
```

**⚠️ ¿Ves warnings en amarillo?**  
Es normal, ignóralos si termina con "Successfully installed"

**❌ ¿Ves errores en rojo?**  
Continúa al Troubleshooting de este paso

---

### 🧪 Paso 2.5: Validar Instalación de Librerías

**1. Busca la celda "✅ Validación de librerías":**

```python
# Validar que todo está instalado correctamente
import pandas as pd
import numpy as np
import yfinance as yf
from alpaca.data.historical import StockHistoricalDataClient
import ta

print("✅ pandas:", pd.__version__)
print("✅ numpy:", np.__version__)
print("✅ yfinance:", yf.__version__)
print("✅ alpaca-py: Instalado")
print("✅ ta:", ta.__version__)
print("\n🎉 ¡Todas las librerías están listas!")
```

**2. Ejecuta la celda (Shift + Enter):**

**Resultado esperado:**
```
✅ pandas: 2.x.x
✅ numpy: 1.x.x
✅ yfinance: 0.x.x
✅ alpaca-py: Instalado
✅ ta: 0.x.x

🎉 ¡Todas las librerías están listas!
```

**✅ Si ves este output → Instalación exitosa**

---

### 🚨 Troubleshooting Paso 2

<details>
<summary><strong>❌ "ModuleNotFoundError: No module named 'alpaca'"</strong></summary>

**Causa:**  
La librería no se instaló correctamente

**Solución:**

1. Re-ejecuta la celda de instalación (`!pip install ...`)
2. Espera a que termine completamente (no interrumpas)
3. Vuelve a ejecutar la celda de validación
4. Si persiste: Reinicia el runtime (Runtime → Restart runtime)

**Validación:**  
Después de reiniciar, vuelve a ejecutar AMBAS celdas (instalación + validación)

</details>

<details>
<summary><strong>❌ "Session crashed" durante instalación</strong></summary>

**Causa:**  
Colab se quedó sin recursos (raro pero puede pasar)

**Solución:**

1. Cierra pestañas innecesarias del navegador
2. Runtime → Restart runtime
3. Re-ejecuta la celda de instalación
4. Si persiste: Espera 5-10 minutos y reintenta

**Prevención:**  
No ejecutes múltiples notebooks simultáneamente

</details>

<details>
<summary><strong>⚠️ "WARNING: pip is being invoked by an old script wrapper"</strong></summary>

**Explicación:**  
Es un warning, NO un error. Puedes ignorarlo.

**¿Qué significa?**  
La versión de pip podría actualizarse, pero no afecta funcionalidad

**Acción:**  
Ninguna. Continúa normalmente.

</details>

<details>
<summary><strong>❌ "ERROR: Failed building wheel for TA-Lib"</strong></summary>

**Causa:**  
TA-Lib requiere compilación (problema conocido)

**Solución:**

**Opción 1 (recomendada):** Usar `ta` en vez de `TA-Lib`  
La celda de instalación ya usa `ta`, que no requiere compilación

**Opción 2:** Instalar TA-Lib con binarios:
```python
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzf ta-lib-0.4.0-src.tar.gz
!cd ta-lib && ./configure --prefix=/usr && make && make install
!pip install TA-Lib
```

**⚠️ Tiempo:** 5-10 minutos adicionales

**Para el workshop:** `ta` es suficiente, no necesitas TA-Lib

</details>

<details>
<summary><strong>❌ "Cannot connect to GPU backend"</strong></summary>

**Explicación:**  
Este workshop NO requiere GPU, solo CPU

**Solución:**

1. Runtime → Change runtime type
2. Hardware accelerator → **"None"** (no GPU)
3. Click Save
4. Re-ejecuta celdas de instalación

**Beneficio:**  
Sin GPU tendrás más tiempo de sesión (12h vs 8h)

</details>

**¿Más problemas?** → [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

### ✅ Checklist Paso 2 Completo

Antes de continuar, verifica:

- ☐ Google Colab abierto y funcionando
- ☐ Notebook del workshop cargado
- ☐ Ejecutaste la celda de prueba inicial con éxito
- ☐ Librerías instaladas (sin errores rojos)
- ☐ Validación de librerías pasó correctamente

**Si todos los puntos están marcados → 🎉 ¡Paso 2 completo!**

**Tiempo invertido hasta ahora:** ~30-40 minutos  
**Tiempo restante:** ~20-50 minutos

---

## 🔗 Paso 3: Conexión Alpaca + Colab

**⏱️ Tiempo estimado:** 10-15 minutos  
**Dificultad:** ⭐⭐ Media

---

### 🎯 Objetivo de Este Paso

Al final, tendrás:
- ✅ API Keys de Alpaca configuradas en Colab
- ✅ Conexión exitosa Alpaca ↔ Colab
- ✅ Primera descarga de datos históricos
- ✅ Validación de que puedes operar (paper)

---

### 🔐 Paso 3.1: Configurar API Keys en Colab

**⚠️ SEGURIDAD CRÍTICA:**

**NUNCA hagas esto:**
```python
# ❌ NUNCA escribir las keys directamente en el código
api_key = "PK..."  # Cualquiera que vea tu notebook verá tus keys
secret_key = "..."
```

**Siempre usa este método seguro:**

**1. Busca la sección "🔐 Configuración de API Keys":**

**2. Ejecuta esta celda:**

```python
# Método seguro: Input interactivo
from getpass import getpass
import os

print("🔐 Configuración segura de API Keys")
print("Las keys NO se guardarán en el notebook\n")

api_key = getpass("Pega tu API Key ID y presiona Enter: ")
secret_key = getpass("Pega tu Secret Key y presiona Enter: ")

# Guardar en variables de ambiente (solo esta sesión)
os.environ['ALPACA_API_KEY'] = api_key
os.environ['ALPACA_SECRET_KEY'] = secret_key

print("\n✅ Keys configuradas correctamente")
print("⚠️ Recuerda: Deberás repetir esto cada vez que reinicies Colab")
```

**3. Cuando ejecutes, verás:**

```
🔐 Configuración segura de API Keys
Las keys NO se guardarán en el notebook

Pega tu API Key ID y presiona Enter: ················
Pega tu Secret Key y presiona Enter: ················

✅ Keys configuradas correctamente
⚠️ Recuerda: Deberás repetir esto cada vez que reinicies Colab
```

**4. Pega tus keys:**

- Abre tu gestor de contraseñas / archivo donde guardaste las keys
- Copia tu API Key ID
- Pega en el primer prompt (no verás los caracteres, es normal)
- Presiona Enter
- Copia tu Secret Key
- Pega en el segundo prompt
- Presiona Enter

**✅ Si ves "Keys configuradas correctamente" → Paso exitoso**

---

**¿Por qué este método es seguro?**

✅ Las keys NO aparecen en el código  
✅ Las keys NO se guardan cuando compartes el notebook  
✅ Las keys se borran automáticamente al cerrar sesión  

---

### 🔌 Paso 3.2: Conectar con Alpaca

**1. Busca la celda "🔌 Conexión con Alpaca":**

```python
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
import os

# Crear cliente de trading (paper)
trading_client = TradingClient(
    api_key=os.environ['ALPACA_API_KEY'],
    secret_key=os.environ['ALPACA_SECRET_KEY'],
    paper=True  # ⚠️ CRÍTICO: True = Paper Trading
)

# Crear cliente de datos históricos
data_client = StockHistoricalDataClient(
    api_key=os.environ['ALPACA_API_KEY'],
    secret_key=os.environ['ALPACA_SECRET_KEY']
)

print("✅ Clientes de Alpaca creados correctamente")
print("🔐 Modo: Paper Trading")
```

**2. Ejecuta la celda (Shift + Enter):**

**Resultado esperado:**
```
✅ Clientes de Alpaca creados correctamente
🔐 Modo: Paper Trading
```

**✅ Si ves este output → Conexión exitosa**

---

### 💰 Paso 3.3: Verificar Información de Cuenta

**1. Busca la celda "💰 Información de Cuenta":**

```python
# Obtener información de tu cuenta paper
account = trading_client.get_account()

print("📊 INFORMACIÓN DE TU CUENTA PAPER TRADING")
print("=" * 50)
print(f"Balance: ${float(account.cash):,.2f}")
print(f"Buying Power: ${float(account.buying_power):,.2f}")
print(f"Portfolio Value: ${float(account.portfolio_value):,.2f}")
print(f"Número de posiciones: {account.position_count}")
print(f"Número de órdenes: {account.order_count}")
print("=" * 50)
print("✅ Conexión con broker exitosa")
```

**2. Ejecuta la celda:**

**Resultado esperado:**
```
📊 INFORMACIÓN DE TU CUENTA PAPER TRADING
==================================================
Balance: $100,000.00
Buying Power: $100,000.00
Portfolio Value: $100,000.00
Número de posiciones: 0
Número de órdenes: 0
==================================================
✅ Conexión con broker exitosa
```

**✅ Si ves tu balance de $100k → Conexión validada**

---

### 📊 Paso 3.4: Primera Descarga de Datos

**1. Busca la celda "📊 Descarga de Datos Históricos":**

```python
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta

# Configurar request
request_params = StockBarsRequest(
    symbol_or_symbols=["SPY"],  # ETF del S&P 500
    timeframe=TimeFrame.Day,     # Barras diarias
    start=datetime.now() - timedelta(days=30)  # Últimos 30 días
)

# Descargar datos
bars = data_client.get_stock_bars(request_params)

# Convertir a DataFrame de pandas
df = bars.df

print("📊 DATOS DESCARGADOS:")
print(f"Símbolo: SPY (S&P 500 ETF)")
print(f"Período: Últimos 30 días")
print(f"Número de barras: {len(df)}")
print(f"\nPrimeras 5 filas:")
print(df.head())
print(f"\n✅ Descarga exitosa")
```

**2. Ejecuta la celda:**

**Resultado esperado:**
```
📊 DATOS DESCARGADOS:
Símbolo: SPY (S&P 500 ETF)
Período: Últimos 30 días
Número de barras: 20

Primeras 5 filas:
                             open    high     low   close    volume
symbol timestamp                                                    
SPY    2024-10-18  567.89  570.12  567.45  569.78  45678900
       2024-10-19  569.80  571.23  568.90  570.45  48901234
       ...

✅ Descarga exitosa
```

**✅ Si ves una tabla con datos → Descarga funciona**

---

### 🚨 Troubleshooting Paso 3

<details>
<summary><strong>❌ "Unauthorized: Invalid API key"</strong></summary>

**Causa:**  
Las API keys están incorrectas o mal copiadas

**Solución:**

1. Verifica que copiaste AMBAS keys completas (sin espacios al inicio/final)
2. Re-ejecuta la celda de configuración de keys (Paso 3.1)
3. Copia nuevamente desde tu gestor de contraseñas
4. Verifica que estás usando keys de **Paper Trading** (no Live)

**Validación:**

- API Key ID debe empezar con "PK..." (Paper) no "AK..." (Live)
- Ambas keys deben ser largas (30-40 caracteres)

</details>

<details>
<summary><strong>❌ "KeyError: 'ALPACA_API_KEY'"</strong></summary>

**Causa:**  
No ejecutaste la celda de configuración de keys (Paso 3.1)

**Solución:**

1. Vuelve al Paso 3.1
2. Ejecuta la celda de `getpass`
3. Ingresa tus keys
4. Vuelve a ejecutar la celda de conexión

**⚠️ Importante:**  
DEBES ejecutar las celdas en orden: Configuración → Conexión

</details>

<details>
<summary><strong>❌ "Connection timeout" o "Connection refused"</strong></summary>

**Causa:**  
Problemas de red o firewall bloqueando Alpaca API

**Solución:**

1. Verifica tu conexión a internet (abre google.com)
2. Espera 1-2 minutos y reintenta
3. Si estás en red corporativa: Puede estar bloqueado por firewall
4. Intenta desde red móvil o red doméstica

**Validación:**  
Abre https://api.alpaca.markets en tu navegador  
Si carga → Tu red permite conexión

</details>

<details>
<summary><strong>⚠️ "No data returned" al descargar SPY</strong></summary>

**Causa:**  
Rango de fechas incluye fin de semana o feriado

**Solución:**

1. Cambia el rango a 60 días en vez de 30:
```python
start=datetime.now() - timedelta(days=60)
```

2. O usa fecha fija:
```python
start=datetime(2024, 10, 1)
```

**Explicación:**  
Alpaca solo devuelve días hábiles, si el rango es muy corto puede no haber datos

</details>

<details>
<summary><strong>❌ "You don't have permission for this endpoint"</strong></summary>

**Causa:**  
Estás usando keys de cuenta no verificada o endpoint incorrecto

**Solución:**

1. Verifica que tu email de Alpaca está confirmado
2. Verifica que usas `paper=True` en el cliente
3. Re-ejecuta la celda de conexión

**Validación:**  
La cuenta paper NO requiere verificación de identidad

</details>

**¿Más problemas?** → [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

### ✅ Checklist Paso 3 Completo

Antes de continuar, verifica:

- ☐ API Keys configuradas en Colab (sin errores)
- ☐ Clientes de Alpaca creados correctamente
- ☐ Balance de $100k visible
- ☐ Descarga de datos SPY exitosa (con datos)
- ☐ No hay errores de autenticación

**Si todos los puntos están marcados → 🎉 ¡Paso 3 completo!**

**Tiempo invertido hasta ahora:** ~40-55 minutos  
**Tiempo restante:** ~10-35 minutos

---

## ✅ Paso 4: Validación Completa del Setup

**⏱️ Tiempo estimado:** 10-15 minutos  
**Dificultad:** ⭐ Fácil

---

### 🎯 Objetivo de Este Paso

Al final, tendrás:
- ✅ Validación automatizada de TODO el setup
- ✅ Reporte de estado completo
- ✅ Confirmación de que estás listo para el workshop

---

### 🧪 Paso 4.1: Ejecutar Script de Validación

**1. Busca la sección "✅ VALIDACIÓN COMPLETA DEL SETUP":**

**2. Ejecuta la celda de validación:**

```python
print("🔍 INICIANDO VALIDACIÓN COMPLETA DEL SETUP")
print("=" * 60)

# Lista de verificaciones
checks = {
    "✅ Librerías core": False,
    "✅ Librerías de trading": False,
    "✅ API Keys configuradas": False,
    "✅ Conexión con Alpaca": False,
    "✅ Acceso a cuenta paper": False,
    "✅ Descarga de datos": False
}

# 1. Verificar librerías core
try:
    import pandas as pd
    import numpy as np
    checks["✅ Librerías core"] = True
    print("✅ pandas y numpy: OK")
except:
    print("❌ pandas o numpy: FALLÓ")

# 2. Verificar librerías de trading
try:
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.trading.client import TradingClient
    import yfinance as yf
    checks["✅ Librerías de trading"] = True
    print("✅ alpaca-py y yfinance: OK")
except:
    print("❌ Librerías de trading: FALLÓ")

# 3. Verificar API Keys
try:
    import os
    assert 'ALPACA_API_KEY' in os.environ
    assert 'ALPACA_SECRET_KEY' in os.environ
    checks["✅ API Keys configuradas"] = True
    print("✅ API Keys: Configuradas")
except:
    print("❌ API Keys: NO configuradas")

# 4. Verificar conexión con Alpaca
try:
    trading_client = TradingClient(
        api_key=os.environ['ALPACA_API_KEY'],
        secret_key=os.environ['ALPACA_SECRET_KEY'],
        paper=True
    )
    checks["✅ Conexión con Alpaca"] = True
    print("✅ Conexión con Alpaca: OK")
except:
    print("❌ Conexión con Alpaca: FALLÓ")

# 5. Verificar acceso a cuenta
try:
    account = trading_client.get_account()
    balance = float(account.cash)
    checks["✅ Acceso a cuenta paper"] = True
    print(f"✅ Cuenta paper: OK (Balance: ${balance:,.2f})")
except:
    print("❌ Acceso a cuenta: FALLÓ")

# 6. Verificar descarga de datos
try:
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    from datetime import datetime, timedelta
    
    data_client = StockHistoricalDataClient(
        api_key=os.environ['ALPACA_API_KEY'],
        secret_key=os.environ['ALPACA_SECRET_KEY']
    )
    
    request_params = StockBarsRequest(
        symbol_or_symbols=["SPY"],
        timeframe=TimeFrame.Day,
        start=datetime.now() - timedelta(days=60)
    )
    
    bars = data_client.get_stock_bars(request_params)
    df = bars.df
    
    if len(df) > 0:
        checks["✅ Descarga de datos"] = True
        print(f"✅ Descarga de datos: OK ({len(df)} barras)")
    else:
        print("⚠️ Descarga de datos: Sin datos (verifica fechas)")
except Exception as e:
    print(f"❌ Descarga de datos: FALLÓ ({str(e)[:50]})")

# Resumen final
print("\n" + "=" * 60)
print("📊 RESUMEN DE VALIDACIÓN:")
print("=" * 60)

passed = sum(checks.values())
total = len(checks)

for check, status in checks.items():
    print(f"{check}: {'✅ PASÓ' if status else '❌ FALLÓ'}")

print("=" * 60)
print(f"Resultado: {passed}/{total} verificaciones exitosas")

if passed == total:
    print("\n🎉 ¡FELICIDADES! Tu setup está 100% funcional")
    print("🚀 Estás listo para comenzar el workshop")
    print("\n👉 Próximo paso: Revisa la Sección 'Primeros Pasos en Colab'")
else:
    print("\n⚠️ Algunas verificaciones fallaron")
    print("👉 Revisa el Troubleshooting de las secciones marcadas con ❌")
    print("👉 O consulta: Troubleshooting Maestro")

print("=" * 60)
```

**3. Espera a que termine (20-30 segundos):**

**Resultado esperado:**
```
🔍 INICIANDO VALIDACIÓN COMPLETA DEL SETUP
============================================================
✅ pandas y numpy: OK
✅ alpaca-py y yfinance: OK
✅ API Keys: Configuradas
✅ Conexión con Alpaca: OK
✅ Cuenta paper: OK (Balance: $100,000.00)
✅ Descarga de datos: OK (20 barras)

============================================================
📊 RESUMEN DE VALIDACIÓN:
============================================================
✅ Librerías core: ✅ PASÓ
✅ Librerías de trading: ✅ PASÓ
✅ API Keys configuradas: ✅ PASÓ
✅ Conexión con Alpaca: ✅ PASÓ
✅ Acceso a cuenta paper: ✅ PASÓ
✅ Descarga de datos: ✅ PASÓ
============================================================
Resultado: 6/6 verificaciones exitosas

🎉 ¡FELICIDADES! Tu setup está 100% funcional
🚀 Estás listo para comenzar el workshop

👉 Próximo paso: Revisa la Sección 'Primeros Pasos en Colab'
============================================================
```

**✅ Si ves "6/6 verificaciones exitosas" → Setup completo**

---

### 🚨 Troubleshooting Paso 4

<details>
<summary><strong>⚠️ "5/6 verificaciones exitosas - Falló descarga de datos"</strong></summary>

**Causa:**  
Rango de fechas sin días hábiles o problema temporal

**Solución:**

1. Re-ejecuta solo la celda de descarga de datos (Paso 3.4)
2. Cambia el rango a 90 días
3. Vuelve a ejecutar la validación

**Acción si persiste:**  
Puedes continuar, se resolverá en el workshop

</details>

<details>
<summary><strong>❌ "Menos de 5/6 verificaciones pasaron"</strong></summary>

**Causa:**  
Uno o más pasos anteriores no se completaron correctamente

**Solución:**

1. Identifica cuál verificación falló
2. Vuelve al paso correspondiente:
   - Librerías → Paso 2.4
   - API Keys → Paso 3.1
   - Conexión → Paso 3.2
   - Cuenta → Paso 3.3
3. Re-ejecuta ese paso completo
4. Vuelve a ejecutar la validación

**⚠️ No continúes si tienes menos de 5/6**

</details>

<details>
<summary><strong>❌ "Exception during validation"</strong></summary>

**Causa:**  
Error inesperado en el script

**Solución:**

1. Lee el mensaje de error completo
2. Busca el error específico en Troubleshooting Maestro
3. Si no lo encuentras: Contacta soporte con screenshot

**Workaround:**  
Ejecuta cada validación manualmente (Pasos 2-3)

</details>

**¿Más problemas?** → [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

### ✅ Checklist Paso 4 Completo

Antes de continuar, verifica:

- ☐ Script de validación ejecutado sin errores
- ☐ 6/6 o al menos 5/6 verificaciones exitosas
- ☐ Mensaje "Estás listo para comenzar el workshop"

**Si todos los puntos están marcados → 🎉 ¡Paso 4 completo!**

**Tiempo invertido hasta ahora:** ~50-70 minutos  
**Tiempo restante:** ~10-20 minutos

---

## 🎓 Paso 5: Primeros Pasos en Colab

**⏱️ Tiempo estimado:** 10-20 minutos  
**Dificultad:** ⭐ Fácil

---

### 🎯 Objetivo de Este Paso

Al final, sabrás:
- ✅ Cómo navegar por el notebook del workshop
- ✅ Cómo guardar tu progreso
- ✅ Cómo ejecutar código de forma segura
- ✅ Atajos de teclado útiles
- ✅ Buenas prácticas de uso

---

### 🗺️ Paso 5.1: Navegar por el Notebook

**Estructura del notebook del workshop:**

```
📓 WTAA_Nov2025.ipynb
├── 📋 ÍNDICE GENERAL
├── ⚙️ SETUP INICIAL (ya completado)
├── 🟦 SESIÓN 1: FUNDAMENTOS
│   ├── 1.1 ¿Qué es Trading Algorítmico?
│   ├── 1.2 APIs y Brokers
│   └── 1.3 Primera descarga de datos
├── 🟦 SESIÓN 2: ANÁLISIS TÉCNICO
│   ├── 2.1 Indicadores básicos
│   └── ...
├── 🟦 SESIÓN 3-9: [Resto del contenido]
└── 📚 RECURSOS ADICIONALES
```

**Cómo navegar:**

**Método 1: Tabla de Contenidos (recomendado)**

1. Click en el ícono de tabla de contenidos (panel izquierdo)
2. Verás todos los títulos del notebook
3. Click en cualquier título para saltar a esa sección

**[Screenshot esperado: Panel de tabla de contenidos]**

**Método 2: Buscar con Ctrl+F**

1. Presiona `Ctrl+F` (o `Cmd+F` en Mac)
2. Escribe lo que buscas (ej: "Sesión 3")
3. Enter para navegar entre resultados

**Método 3: Scroll manual**

Simplemente desplázate con la rueda del mouse

---

### 💾 Paso 5.2: Guardar Tu Progreso

**⚠️ IMPORTANTE:**  
Colab NO guarda automáticamente cada segundo como Google Docs

**Cómo guardar manualmente:**

**Método 1: Atajo de teclado (más rápido)**  
`Ctrl+S` (o `Cmd+S` en Mac)

**Método 2: Menú**  
File → Save

**Método 3: Auto-save**  
File → Save automatically every X minutes

**Recomendación:**  
Activa auto-save cada 5 minutos

---

**¿Dónde se guarda?**

- ✅ En tu Google Drive (carpeta "Colab Notebooks")
- ✅ Puedes acceder desde cualquier dispositivo
- ✅ Se sincroniza automáticamente

**Validación:**

1. Abre Google Drive (drive.google.com)
2. Busca carpeta "Colab Notebooks"
3. Deberías ver tu notebook con la fecha de última modificación

---

### ▶️ Paso 5.3: Ejecutar Código de Forma Segura

**Regla de oro: Leer ANTES de ejecutar**

**⚠️ NO hagas esto:**
```python
# ❌ Ejecutar código sin leer
# Podrías borrar datos, enviar órdenes reales, etc.
```

**✅ SÍ haz esto:**

1. **Lee el código completo**
2. **Lee los comentarios** (líneas con #)
3. **Entiende qué hace** (o pregunta)
4. **Ejecuta con Shift+Enter**

---

**Celdas seguras vs. peligrosas:**

**✅ Siempre seguro:**
- Celdas que empiezan con `import`
- Celdas que empiezan con `print`
- Celdas de visualización (gráficos)
- Celdas con comentario "# Seguro de ejecutar"

**⚠️ Requiere atención:**
- Celdas que empiezan con `trading_client.submit_order` (envía órdenes)
- Celdas que modifican archivos
- Celdas que descargan/suben datos

**❌ NUNCA ejecutar sin confirmar:**
- Celdas marcadas con `# PELIGRO`
- Celdas que dicen `paper=False` (modo real, no paper)

---

### ⌨️ Paso 5.4: Atajos de Teclado Útiles

**Atajos esenciales:**

| Acción | Windows/Linux | Mac |
|--------|---------------|-----|
| **Ejecutar celda** | `Shift+Enter` | `Shift+Enter` |
| **Ejecutar y quedarse** | `Ctrl+Enter` | `Cmd+Enter` |
| **Insertar celda arriba** | `Ctrl+M A` | `Cmd+M A` |
| **Insertar celda abajo** | `Ctrl+M B` | `Cmd+M B` |
| **Borrar celda** | `Ctrl+M D` | `Cmd+M D` |
| **Guardar** | `Ctrl+S` | `Cmd+S` |
| **Buscar** | `Ctrl+F` | `Cmd+F` |
| **Deshacer** | `Ctrl+Z` | `Cmd+Z` |
| **Comentar línea** | `Ctrl+/` | `Cmd+/` |

**Práctica:**

1. Crea una nueva celda con `Ctrl+M B`
2. Escribe: `print("Probando atajos")`
3. Ejecuta con `Shift+Enter`
4. Borra la celda con `Ctrl+M D`

---

### 🛡️ Paso 5.5: Buenas Prácticas

**✅ Recomendaciones:**

**1. Ejecuta celdas EN ORDEN**  
No saltes celdas (especialmente al inicio)

**2. Guarda frecuentemente**  
`Ctrl+S` cada 10-15 minutos

**3. Lee los outputs**  
No ignores warnings o mensajes

**4. Comenta tu código**  
Si modificas algo, agrega un comentario explicando por qué

**5. Usa nombres descriptivos**  
Si creas variables, usa nombres claros:
```python
# ✅ Bueno
precio_apertura_spy = 570.50

# ❌ Malo
x = 570.50
```

**6. No compartas notebooks con API Keys**  
Antes de compartir, elimina la celda con tus keys

---

**❌ Evita:**

**1. NO ejecutar todo de golpe**  
Runtime → Run all = riesgo de errores en cadena

**2. NO copiar código externo sin entender**  
Stack Overflow puede tener código desactualizado

**3. NO dejar sesiones abiertas indefinidamente**  
Cierra Colab cuando no lo uses (ahorra recursos)

**4. NO trabajar con múltiples notebooks simultáneamente**  
Riesgo de confundir variables entre notebooks

---

### 🔄 Paso 5.6: ¿Qué Hacer Si Algo Sale Mal?

**Escenario 1: Celda se quedó "ejecutando" por siempre**

**Solución:**

1. Click en el botón "Stop" (cuadrado rojo) al lado de la celda
2. Si no funciona: Runtime → Interrupt execution
3. Si persiste: Runtime → Restart runtime (⚠️ perderás variables en memoria)

---

**Escenario 2: "Session crashed"**

**Solución:**

1. Runtime → Restart runtime
2. Re-ejecuta celdas de setup (instalación + API keys)
3. Continúa desde donde estabas

**Prevención:**  
No ejecutes código muy pesado (millones de filas) en versión gratuita

---

**Escenario 3: Error "Out of Memory"**

**Solución:**

1. Runtime → Restart runtime
2. Reduce tamaño de datos (ej: menos días históricos)
3. Elimina variables grandes:
```python
del variable_grande  # Libera memoria
```

---

**Escenario 4: Código modificado accidentalmente**

**Solución:**

1. File → Revision history
2. Click en versión anterior
3. Restaura o copia el código original

**Prevención:**  
Guarda versiones con nombres diferentes antes de experimentar

---

### ✅ Checklist Paso 5 Completo

Antes de continuar, verifica:

- ☐ Entiendes cómo navegar con tabla de contenidos
- ☐ Guardaste tu notebook (Ctrl+S)
- ☐ Probaste ejecutar una celda con Shift+Enter
- ☐ Conoces los atajos básicos
- ☐ Leíste las buenas prácticas

**Si todos los puntos están marcados → 🎉 ¡Paso 5 completo!**

**Tiempo total invertido:** ~60-90 minutos

---

## 🚨 Troubleshooting Expandido

**Esta sección cubre 20+ casos comunes no cubiertos en secciones anteriores:**

---

<details>
<summary><strong>❌ "Runtime disconnected"</strong></summary>

**Causa:**  
Inactividad prolongada (>90 min sin ejecutar celdas)

**Solución:**

1. Click en "Reconnect" en la parte superior
2. Re-ejecuta celdas de setup (instalación + keys)
3. Continúa desde donde estabas

**Prevención:**  
Ejecuta al menos una celda cada 60 minutos

</details>

<details>
<summary><strong>❌ "Cannot connect to GPU backend"</strong></summary>

**Causa:**  
Intentas usar GPU cuando no es necesario

**Solución:**

1. Runtime → Change runtime type
2. Hardware accelerator → "None"
3. Click Save

**Nota:** Este workshop NO usa GPU

</details>

<details>
<summary><strong>❌ "You are using Colab free tier with limited resources"</strong></summary>

**Explicación:**  
Es un mensaje informativo, no un error

**Recursos gratuitos:**
- 12 GB RAM
- CPU Intel Xeon
- 100 GB disco temporal

**Acción:**  
Ninguna. Es suficiente para el workshop.

</details>

<details>
<summary><strong>⚠️ "WARNING: Running pip as root user"</strong></summary>

**Explicación:**  
Es un warning, NO un error. Puedes ignorarlo.

**Causa:**  
Colab ejecuta comandos como root (admin)

**Acción:**  
Ninguna. Es comportamiento normal.

</details>

<details>
<summary><strong>❌ "NameError: name 'X' is not defined"</strong></summary>

**Causa:**  
Intentas usar una variable que no existe o no se ejecutó

**Solución:**

1. Busca dónde se define la variable X
2. Ejecuta esa celda PRIMERO
3. Vuelve a ejecutar la celda que dio error

**Ejemplo:**
```python
# Celda 1 (debes ejecutar PRIMERO)
balance = 100000

# Celda 2 (fallará si no ejecutaste Celda 1)
print(balance)  # NameError si Celda 1 no se ejecutó
```

</details>

<details>
<summary><strong>❌ "KeyError: 'close'"</strong></summary>

**Causa:**  
DataFrame descargado no tiene la columna esperada

**Solución:**

1. Imprime las columnas del DataFrame:
```python
print(df.columns)
```

2. Verifica el nombre correcto (puede ser 'Close' con mayúscula)

3. Ajusta el código:
```python
# En vez de:
df['close']

# Usa:
df['Close']  # O el nombre que viste en print
```

</details>

<details>
<summary><strong>❌ "TypeError: unsupported operand type(s)"</strong></summary>

**Causa:**  
Intentas hacer operación matemática con tipos incompatibles

**Ejemplo del error:**
```python
precio = "570.50"  # String, no número
comision = precio * 0.001  # Error: no puedes multiplicar string
```

**Solución:**

1. Convierte a número:
```python
precio = float("570.50")  # Ahora es número
comision = precio * 0.001  # ✅ Funciona
```

</details>

<details>
<summary><strong>❌ "IndexError: list index out of range"</strong></summary>

**Causa:**  
Intentas acceder a posición que no existe en lista

**Ejemplo del error:**
```python
precios = [570, 571, 572]
print(precios[10])  # Error: solo hay 3 elementos (0, 1, 2)
```

**Solución:**

1. Verifica longitud de la lista:
```python
print(len(precios))  # Imprime: 3
```

2. Usa índices válidos (0 a len-1):
```python
print(precios[0])   # ✅ Primer elemento
print(precios[2])   # ✅ Último elemento
print(precios[-1])  # ✅ Último elemento (alternativa)
```

</details>

<details>
<summary><strong>⚠️ "FutureWarning" en pandas</strong></summary>

**Explicación:**  
No es error, es aviso de funcionalidad que cambiará en futuro

**Ejemplo:**
```
FutureWarning: The default value of numeric_only...
```

**Acción:**  
Ignora por ahora. El código seguirá funcionando.

**Si quieres eliminarlo:**
```python
import warnings
warnings.filterwarnings('ignore')
```

</details>

<details>
<summary><strong>❌ "RateLimitError" de Alpaca</strong></summary>

**Causa:**  
Demasiadas requests en poco tiempo (límite: 200/min)

**Solución:**

1. Espera 60 segundos
2. Reduce frecuencia de requests:
```python
import time
time.sleep(1)  # Pausa 1 segundo entre requests
```

**Para el workshop:**  
No deberías alcanzar este límite con uso normal

</details>

<details>
<summary><strong>❌ "JSONDecodeError"</strong></summary>

**Causa:**  
Respuesta de API no es JSON válido

**Solución:**

1. Verifica tu conexión a internet
2. Intenta de nuevo (puede ser problema temporal)
3. Si persiste: Verifica que API keys son correctas

</details>

<details>
<summary><strong>❌ "SSLError" o "Certificate verify failed"</strong></summary>

**Causa:**  
Problema con certificados SSL

**Solución:**

1. Verifica tu conexión a internet
2. Si estás en red corporativa: Puede ser firewall
3. Workaround temporal:
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

**⚠️ Solo usa esto si es necesario**

</details>

<details>
<summary><strong>❌ "403 Forbidden"</strong></summary>

**Causa:**  
No tienes permiso para acceder a ese endpoint

**Solución:**

1. Verifica que usas `paper=True` en el cliente
2. Verifica que tu cuenta paper está activa
3. Algunas funcionalidades requieren cuenta Live (ignóralas)

</details>

<details>
<summary><strong>⚠️ Notebook se carga muy lento</strong></summary>

**Causas:**

1. Notebook muy grande (>10 MB)
2. Muchos outputs guardados
3. Conexión lenta

**Solución:**

1. Edit → Clear all outputs
2. Guarda nuevamente
3. Cierra y vuelve a abrir

**Prevención:**  
Limpia outputs regularmente (especialmente gráficos grandes)

</details>

<details>
<summary><strong>❌ "Cannot save changes" al guardar</strong></summary>

**Causa:**  
Problema de sincronización con Google Drive

**Solución:**

1. File → Save a copy in Drive
2. Guarda con nuevo nombre
3. Cierra el notebook original
4. Trabaja con la copia

</details>

<details>
<summary><strong>❌ "Kernel restarting" repetidamente</strong></summary>

**Causa:**  
Código con error crítico o memoria insuficiente

**Solución:**

1. Identifica última celda ejecutada antes del restart
2. Comenta esa celda (Ctrl+/)
3. Runtime → Restart runtime
4. Ejecuta el resto sin esa celda
5. Debug la celda problemática

</details>

<details>
<summary><strong>⚠️ Outputs desaparecen al recargar notebook</strong></summary>

**Explicación:**  
Comportamiento normal de Colab

**Los outputs se guardan SOLO si:**

1. Guardas el notebook después de ejecutar (`Ctrl+S`)
2. No limpias outputs (Edit → Clear outputs)

**Solución:**  
Guarda frecuentemente con `Ctrl+S`

</details>

<details>
<summary><strong>❌ "Module has no attribute X"</strong></summary>

**Causa:**  
Versión incorrecta de librería o nombre mal escrito

**Solución:**

1. Verifica spelling del atributo
2. Consulta documentación oficial:
   - Alpaca: https://docs.alpaca.markets/
   - pandas: https://pandas.pydata.org/

3. Reinstala librería:
```python
!pip install alpaca-py --upgrade
```

</details>

<details>
<summary><strong>❌ "No space left on device"</strong></summary>

**Causa:**  
Llenaste los 100 GB de disco temporal

**Solución:**

1. Runtime → Manage sessions
2. Terminate all
3. Inicia nueva sesión
4. No descargues archivos muy grandes

**Para el workshop:**  
No deberías alcanzar este límite

</details>

<details>
<summary><strong>⚠️ Gráficos no se muestran</strong></summary>

**Causa:**  
Falta `%matplotlib inline` o librería no instalada

**Solución:**

1. Agrega al inicio del notebook:
```python
%matplotlib inline
import matplotlib.pyplot as plt
```

2. Re-ejecuta celda del gráfico

</details>

---

**¿Tu problema no está listado?**

👉 Consulta: [Troubleshooting Maestro](Troubleshooting_Maestro.md)  
👉 O contacta soporte (ver sección final)

---

## 🔗 Ver También

**Documentos relacionados con este setup:**

📚 **[Guía de Inicio](GUIA_INICIO.md)**  
Roadmap completo del workshop - 9 sesiones, 27 horas

📊 **[Guía de Setup Completa](Guia_Setup_Completa.md)**  
Hub de navegación para elegir entre Setup A/B/C/D

⚡ **[Setup A: Express](Setup_A_Express.md)**  
Versión ultra-rápida de este setup (10-15 min)

📘 **[Setup A: Colab Completo](Setup_A_Colab_Rapido.md)**  
Versión estándar recomendada (30-45 min)

🛠️ **[Troubleshooting Maestro](Troubleshooting_Maestro.md)**  
Base de conocimiento completa de problemas y soluciones

📖 **[Programa Detallado del Workshop](Programa_Detallado_Workshop.md)**  
Contenido sesión por sesión con tiempos y objetivos

---

## 🔗 NAVEGACIÓN

**◀️ Anterior:** [Setup A: Express](Setup_A_Express.md)  
**▶️ Siguiente:** [Setup B: Python Local](Setup_B_Python_Local.md)

**🏠 Volver a:**
- [Guía de Setup Completa](Guia_Setup_Completa.md)
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**📖 Ver también:**
- [Setup A Express](Setup_A_Express.md) - Versión rápida (10-15 min)
- [Setup A Colab Completo](Setup_A_Colab_Rapido.md) - Versión estándar (30-45 min)
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

---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
