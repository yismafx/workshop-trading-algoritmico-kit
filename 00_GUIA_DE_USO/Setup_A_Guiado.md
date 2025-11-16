# 📖 SETUP A: GUÍA PASO A PASO COMPLETA

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 📄 Setup Guiado**

---

**⏱️ Tiempo estimado:** 30-60 minutos  
**🎯 Nivel de detalle:** Exhaustivo - Cada paso explicado  
**📅 Última actualización:** Noviembre 2025

---

## 🎯 ¿PARA QUIÉN ES ESTA GUÍA?

### ✅ Esta Guía es PERFECTA si:

- 🆕 **Primera vez** con Google Colab o Jupyter notebooks
- 📚 Quieres **entender cada paso** en detalle
- ❓ Prefieres explicaciones completas y contexto
- 🎓 Eres un **aprendiz metódico** que valora la comprensión profunda
- ⚙️ Quieres **configurar TODO correctamente** desde el principio

### ❌ Esta Guía NO es Ideal si:

- ⏱️ Tienes **menos de 30 minutos**  
  → Ve a [Setup A Express](Setup_A_Express.md) - 10-15 min
  
- 🚀 Ya usaste notebooks antes y solo quieres **validar rápido**  
  → Ve a [Setup Colab Rápido](Setup_Colab_Rapido.md) - 10 min

---

## 📑 TABLA DE CONTENIDOS

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

## PASO 1: ACCEDER A GOOGLE COLAB (5 min)

### 🎯 Objetivo del Paso
Acceder a la plataforma Google Colab y familiarizarte con su interfaz básica.

---

### 📝 ¿Qué es Google Colab?

**Google Colaboratory (Colab)** es una plataforma gratuita de Google que te permite:

- 🖥️ **Ejecutar código Python** directamente en tu navegador
- 💾 **Sin instalar nada** en tu computadora
- ⚡ **Usar procesadores potentes** de Google (gratis)
- 💰 **Guardar tu trabajo** en Google Drive automáticamente

**💡 Analogía del Trader:**  
Es como tener una "sala de operaciones virtual" donde puedes probar estrategias sin necesidad de montar una infraestructura propia.

---

### ✅ PASO 1.1: Abrir Google Colab

**1. Abre tu navegador** (Chrome recomendado)

**2. Ve a:**  
```
https://colab.research.google.com
```

**3. Inicia sesión con tu cuenta Gmail**

⚠️ **Si NO tienes cuenta Gmail:**
- Crea una gratis en: [https://accounts.google.com/signup](https://accounts.google.com/signup)
- Toma 5 minutos
- Vuelve a este paso después

---

### ✅ PASO 1.2: Familiarízate con la Interfaz

**Al entrar a Colab, verás:**

```
┌─────────────────────────────────────────┐
│  🟦 Google Colaboratory                 │
│                                         │
│  📂 Recent    Examples    Google Drive  │
│  📂 GitHub    Upload                    │
│                                         │
│  [+ New notebook]                       │
│                                         │
└─────────────────────────────────────────┘
```

**Componentes principales:**

- **Recent:** Notebooks que abriste recientemente
- **Examples:** Ejemplos de Google (ignorar por ahora)
- **Google Drive:** Notebooks guardados en tu Drive
- **GitHub:** Importar desde GitHub (usaremos esto después)
- **Upload:** Subir archivos desde tu computadora
- **+ New notebook:** Crear notebook nuevo (NO uses esto aún)

---

### 🧭 NAVEGACIÓN: Orientándote en la Interfaz

**La interfaz de Colab tiene 3 áreas principales:**

```
┌──────────────────────────────────────────┐
│ 🔝 BARRA SUPERIOR                        │ ← Menú, guardar, ejecutar
├──────────────────────────────────────────┤
│ 📄 ÁREA DE CELDAS                        │ ← Aquí escribes y ejecutas código
│                                          │
│   [Code]  print("Hola")                  │
│                                          │
│   [Text]  # Notas en Markdown            │
├──────────────────────────────────────────┤
│ 📊 PANEL LATERAL (opcional)              │ ← Archivos, variables, snippets
└──────────────────────────────────────────┘
```

**No te preocupes por recordar todo ahora.** Lo aprenderás mientras practicas.

---

### ✅ PASO 1.3: Comprender los "Notebooks"

**¿Qué es un Notebook?**

Un notebook es un documento que mezcla:
- 📝 **Código ejecutable** (Python)
- 📖 **Texto explicativo** (Markdown)
- 📊 **Gráficos y resultados** (outputs)

**💡 Analogía del Trader:**  
Es como un "journal de trading inteligente" donde registras tu análisis (texto), ejecutas cálculos (código), y ves resultados (gráficos) - todo en el mismo lugar.

---

### ✅ PASO 1.4: Crear Tu Primer Notebook de Prueba

**Solo para familiarizarte (2 minutos):**

1. **Click en `+ New notebook`** (botón naranja, esquina inferior derecha)

2. **Verás un notebook vacío con una celda:**
   ```python
   # Click aquí para escribir código
   ```

3. **Escribe esto en la celda:**
   ```python
   print("¡Mi primer notebook para trading!")
   ```

4. **Ejecuta la celda:**
   - Click en el botón ▶️ (play) a la izquierda de la celda
   - O presiona `Shift + Enter`

5. **Verás el resultado debajo:**
   ```
   ¡Mi primer notebook para trading!
   ```

🎉 **¡Felicitaciones!** Acabas de ejecutar tu primer código en Colab.

---

### 🧹 PASO 1.5: Limpiar y Preparar

**Ahora que sabes cómo funciona:**

1. **Cierra este notebook de prueba:**
   - File → Close
   - NO guardar (era solo prueba)

2. **Vuelve a la página principal de Colab:**
   - https://colab.research.google.com

**✅ Has completado el Paso 1**

**Validación rápida:**
- [ ] Sé acceder a Google Colab
- [ ] Entiendo qué es un notebook
- [ ] Puedo ejecutar una celda de código básica
- [ ] Estoy listo para crear mi notebook de trading

---

## PASO 2: CREAR TU NOTEBOOK PERSONAL (5 min)

### 🎯 Objetivo del Paso
Crear un notebook personal configurado específicamente para trading algorítmico.

---

### ⚠️ IMPORTANTE: NO Crear un Notebook Vacío

**NO hagas esto:**
- ❌ Click en "+ New notebook"
- ❌ Empezar desde cero

**¿Por qué?**  
Configurar un notebook de trading desde cero toma 2-3 horas. Ya hicimos ese trabajo por ti.

**SÍ haz esto:**
- ✅ Usar nuestro **notebook pre-configurado**
- ✅ Ya tiene todo instalado y configurado
- ✅ Solo necesitas personalizarlo

---

### ✅ PASO 2.1: Descargar el Notebook Pre-Configurado

**Opción A - Descarga Directa (Recomendada):**

1. **Click derecho en este enlace:**  
   [**Setup_y_Practica_Trading.ipynb**](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb)

2. **Selecciona "Guardar enlace como..." o "Save link as..."**

3. **Guarda el archivo** en una carpeta que recuerdes (ej: Escritorio)

4. **Verifica:** El archivo debe llamarse `Setup_y_Practica_Trading.ipynb`
   - ⚠️ Si se descargó como `.txt` o `.html`, ve a [Troubleshooting - Descarga](#troubleshooting-descarga)

---

**Opción B - Desde GitHub:**

**Si la Opción A no funcionó:**

1. Ve a: https://github.com/yismafx/workshop-trading-algoritmico-kit
2. Navega a: `00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb`
3. Click en **"Raw"** (botón arriba derecha)
4. Guarda la página:
   - Windows: `Ctrl + S`
   - Mac: `Cmd + S`
5. Asegúrate de guardar como **"All files"** y con extensión `.ipynb`

---

### ✅ PASO 2.2: Subir el Notebook a Google Colab

**1. Abre Google Colab:**  
https://colab.research.google.com

**2. Click en la pestaña `Upload`:**

```
┌─────────────────────────────────────────┐
│  📂 Recent  Examples  Google Drive      │
│  📂 GitHub  [Upload] ← CLICK AQUÍ       │
│                                         │
└─────────────────────────────────────────┘
```

**3. Arrastra el archivo `.ipynb` que descargaste**

O click en **"Choose File"** y selecciónalo desde tu computadora.

**4. Espera 5-10 segundos** mientras Colab carga el notebook

---

### ✅ PASO 2.3: Verificar que el Notebook Cargó Correctamente

**Deberías ver:**

- ✅ Título: **"Setup A: Trading Algorítmico con Python"**
- ✅ Varias secciones con títulos en español
- ✅ Celdas de código con comentarios explicativos
- ✅ Texto explicativo entre las celdas de código

**Si ves esto, ¡perfecto! Continúa.**

**Si NO ves esto:**
- ⚠️ Puede que el archivo se haya descargado incorrectamente
- Ve a [Troubleshooting - Descarga](#troubleshooting-descarga)

---

### ✅ PASO 2.4: Guardar el Notebook en Google Drive

**Importante para no perder tu trabajo:**

**1. Guarda el notebook:**
- `File` → `Save a copy in Drive`

**2. Renombra tu copia (opcional pero recomendado):**
- Click en el título arriba (donde dice "Copy of Setup_y_Practica_Trading")
- Cámbialo a algo más personal: `[TuNombre]_Trading_Workshop_2024`

**3. Verifica el guardado:**
- Busca el ícono de nube arriba ☁️
- Debe decir "All changes saved" o "Todos los cambios guardados"

---

### 🔍 PASO 2.5: Entender la Estructura del Notebook

**Tu notebook tiene 6 secciones principales:**

```
📓 Setup A: Trading Algorítmico con Python
│
├── 🧰 SECCIÓN 1: Instalación de Librerías (10 min)
│   └─ Instala todas las herramientas que necesitas
│
├── 🔑 SECCIÓN 2: Configuración de Broker (15-30 min)
│   └─ Conecta con Alpaca o Interactive Brokers
│
├── 📊 SECCIÓN 3: Descarga de Datos (5 min)
│   └─ Obtén datos históricos de SPY, BTC, etc.
│
├── 🧪 SECCIÓN 4: Validación del Setup (5 min)
│   └─ Verifica que todo funciona
│
├── 📈 SECCIÓN 5: Ejemplo de Estrategia Simple (10 min)
│   └─ Primera estrategia de trading
│
└── 📚 SECCIÓN 6: Recursos y Próximos Pasos
    └─ Links a templates, prompts, y más
```

---

### ✅ PASO 2.6: Familiarízate con los Controles Básicos

**Ejecutar una celda:**
- Click en ▶️ a la izquierda de la celda
- O `Shift + Enter`

**Agregar una nueva celda:**
- Pasa el mouse entre celdas
- Aparecerán botones `+ Code` y `+ Text`

**Eliminar una celda:**
- Click en el menú de 3 puntos verticales (⋮) arriba derecha de la celda
- Selecciona "Delete cell"

**⚠️ Consejo:** NO elimines celdas del notebook original hasta que domines Colab.

---

### ✅ Has Completado el Paso 2

**Validación rápida:**
- [ ] Tengo el notebook pre-configurado cargado en Colab
- [ ] El notebook está guardado en mi Google Drive
- [ ] Entiendo la estructura básica del notebook
- [ ] Sé cómo ejecutar celdas
- [ ] Estoy listo para instalar librerías

**✅ Continúa al Paso 3**

---

## PASO 3: INSTALAR LIBRERÍAS DE TRADING (10 min)

### 🎯 Objetivo del Paso
Instalar todas las herramientas de Python necesarias para trading algorítmico.

---

### 📚 ¿Qué son las Librerías?

**Librerías (o bibliotecas) son herramientas pre-hechas** que te ahorran escribir código desde cero.

**💡 Analogía del Trader:**  
Es como tener indicadores pre-configurados en TradingView:
- No creas el RSI desde cero → usas el RSI de TradingView
- No creas pandas desde cero → usas pandas de Python

**Las librerías que instalaremos:**

| Librería | Qué Hace | Analogía |
|----------|----------|----------|
| **pandas** | Maneja datos (tablas, series) | Excel para Python |
| **yfinance** | Descarga precios históricos | Data Feed |
| **alpaca-trade-api** | Conecta con broker Alpaca | API de tu broker |
| **backtrader** | Hace backtesting | TradingView Strategy Tester |
| **matplotlib** | Crea gráficos | Gráficos de TradingView |

---

### ⚠️ IMPORTANTE: Concepto de "Runtime"

**¿Qué es un Runtime?**

El "runtime" es la **máquina virtual temporal** que Google te asigna cuando abres un notebook.

**Conceptos clave:**

- 🔄 **Se reinicia cada 12 horas** de inactividad
- 💾 **NO guarda las librerías instaladas** cuando se cierra
- 🔁 **Tendrás que reinstalar** cada vez que abras el notebook después de mucho tiempo

**¿Significa que tengo que instalar CADA vez?**
- ✅ Sí, si pasó más de 12 horas
- ❌ No, si es el mismo día

**¿Por qué?**  
Google Colab es gratis, pero cada sesión es "temporal". Es el precio de no pagar.

---

### ✅ PASO 3.1: Ubicar la Sección de Instalación

**En tu notebook, busca:**

```
🧰 SECCIÓN 1: INSTALACIÓN DE LIBRERÍAS
```

**Deberías ver una celda que empieza con:**

```python
# 🧰 INSTALACIÓN DE LIBRERÍAS DE TRADING
print("🔧 Instalando herramientas de trading...")
```

---

### ✅ PASO 3.2: Ejecutar la Instalación

**1. Click en el botón ▶️** de esa celda

**2. Verás un montón de texto** desplazándose rápido:

```
Collecting yfinance
  Downloading yfinance-0.2.28-py2.py3-none-any.whl...
Successfully installed yfinance-0.2.28
Collecting pandas
  Downloading pandas-2.1.1-cp310-cp310-manylinux...
...
```

**¿Qué está pasando?**  
Python está descargando e instalando cada librería desde internet.

**⏱️ Tiempo:** 2-5 minutos (dependiendo de tu conexión)

**✅ Cuando termine, verás:**

```
✅ INSTALACIÓN COMPLETADA
Todas las librerías están listas para usar
```

---

### ✅ PASO 3.3: Entender los Mensajes de Instalación

**Durante la instalación, verás 3 tipos de mensajes:**

**1. Mensajes normales (ignora):**
```
Collecting pandas
Downloading pandas-2.1.1.whl
Installing...
```
→ **Acción:** Ninguna. Es normal.

**2. Warnings (advertencias - ignora):**
```
WARNING: Package X requires Y>=1.0.0
```
→ **Acción:** Ignora. Google Colab maneja esto automáticamente.

**3. ERRORES (atiende):**
```
ERROR: Could not install packages due to an OSError
```
→ **Acción:** Ve a [Troubleshooting - Instalación](#troubleshooting-instalación)

---

### ✅ PASO 3.4: Verificar la Instalación

**Busca la siguiente celda en el notebook:**

```python
# ✅ VERIFICACIÓN DE INSTALACIÓN
print("Verificando librerías instaladas...")
```

**Ejecútala (▶️ o Shift+Enter)**

**Deberías ver:**

```
✅ pandas: OK (versión 2.1.1)
✅ yfinance: OK (versión 0.2.28)
✅ alpaca-trade-api: OK (versión 3.0.2)
✅ backtrader: OK (versión 1.9.78)
✅ matplotlib: OK (versión 3.8.0)

🎉 TODAS LAS LIBRERÍAS ESTÁN FUNCIONANDO
```

**Si ves todos ✅ OK → Perfecto, continúa.**

**Si ves algún ❌ ERROR → Ve a [Troubleshooting - Librerías](#troubleshooting-librerías)**

---

### 🧠 PASO 3.5: Entender las Versiones (Opcional pero Importante)

**¿Por qué importan las versiones?**

Las librerías se actualizan constantemente. A veces, nuevas versiones **rompen código viejo**.

**Nuestro notebook usa versiones específicas (compatibles con 2024-2025):**

- pandas: `2.1.1` o superior
- yfinance: `0.2.28` o superior
- alpaca-trade-api: `3.0.2` o superior
- backtrader: `1.9.78` o superior

**Si tus versiones son diferentes:**
- ✅ Si son **superiores** (ej: 2.2.0 vs 2.1.1) → Probablemente OK
- ⚠️ Si son **inferiores** (ej: 2.0.0 vs 2.1.1) → Puede haber problemas

**📌 Regla de oro:** Si algo no funciona más adelante, primero verifica que las versiones sean correctas.

---

### ✅ Has Completado el Paso 3

**Validación rápida:**
- [ ] Ejecuté la celda de instalación sin errores críticos
- [ ] Vi el mensaje "✅ INSTALACIÓN COMPLETADA"
- [ ] Ejecuté la verificación y todas las librerías muestran ✅ OK
- [ ] Entiendo que tendré que reinstalar si cierro y abro después de 12h
- [ ] Estoy listo para configurar el broker

**✅ Continúa al Paso 4**

---

## PASO 4: CONFIGURAR CONEXIÓN A BROKER (DUAL SETUP: 15-30 min)

### 🎯 Objetivo del Paso
Conectar tu notebook con un broker para descargar datos en tiempo real y (eventualmente) ejecutar operaciones.

---

### 🤔 ¿Por Qué Necesito un Broker?

**En trading manual:**  
Usas un broker para ejecutar tus órdenes (buy/sell).

**En trading algorítmico:**  
Usas un broker para:
1. **Descargar datos históricos** (precios pasados para backtesting)
2. **Obtener datos en tiempo real** (precios actuales)
3. **Ejecutar órdenes automáticamente** (cuando tu estrategia da señal)

**💡 Para el workshop:**  
Usaremos la cuenta **Paper Trading** (simulada) del broker.  
NO usaremos dinero real.

---

### 🎯 SETUP DUAL: Alpaca + Interactive Brokers

**¿Por qué configurar DOS brokers?**

Cada broker tiene fortalezas diferentes:

| Broker | Mejor Para | Limitación |
|--------|-----------|------------|
| **Alpaca** | Rápido, fácil, gratis | Solo US stocks (no crypto, forex) |
| **Interactive Brokers** | Multi-asset (stocks, crypto, forex) | Más complejo de configurar |

**Estrategia del workshop:**
1. ✅ Configuramos **Alpaca primero** (10 min) → Rápido, para empezar
2. ✅ Configuramos **IB después** (15-20 min) → Para trading completo

**🎯 Si tienes poco tiempo:**  
Configura solo Alpaca ahora, IB lo haces después.

---

### SECCIÓN A: CONFIGURAR ALPACA (10 min)

---

#### ✅ PASO 4A.1: Crear Cuenta en Alpaca

**1. Ve a:** https://alpaca.markets

**2. Click en "Sign Up" (Registrarse)**

**3. Completa el formulario:**
- Email
- Contraseña
- Nombre completo
- País de residencia

**4. Verifica tu email:**  
Revisa tu correo y click en el link de verificación.

**5. Completa el proceso de KYC (Know Your Customer):**

⚠️ **Importante:** Alpaca pedirá información personal:
- SSN o Tax ID (si eres de US)
- Identificación oficial (si NO eres de US)
- Información financiera básica

**¿Por qué piden esto?**  
Aunque usarás Paper Trading, Alpaca cumple regulaciones financieras.

**⏱️ Aprobación:** Instantánea para Paper Trading

---

#### ✅ PASO 4A.2: Obtener API Keys de Alpaca

**Una vez dentro de tu cuenta Alpaca:**

**1. Ve a la sección "Paper Trading":**
- En el menú lateral: `Paper Trading` → `Overview`

**2. Genera tus API Keys:**
- Click en `Generate New Key` o `View API Keys`

**3. Verás dos claves:**

```
API Key ID: PKXXXXXXXXXXXXXXXXXX
Secret Key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**⚠️ CRÍTICO:**
- ✅ **Copia ambas** en un lugar seguro (bloc de notas temporal)
- ❌ **NO cierres** esta ventana hasta copiar las keys
- 🔒 **El Secret Key** solo se muestra UNA vez
- ⛔ **NUNCA** compartas estas keys públicamente

**4. Confirma el tipo de cuenta:**
- Verifica que estás en **"Paper Trading"** (no Live)
- Aparecerá un banner naranja que dice "Paper Trading" arriba

---

#### ✅ PASO 4A.3: Configurar API Keys en el Notebook

**Vuelve a tu notebook de Colab.**

**Busca la celda que dice:**

```python
# 🔑 CONFIGURACIÓN DE ALPACA API
ALPACA_API_KEY = "TU_API_KEY_AQUÍ"
ALPACA_SECRET_KEY = "TU_SECRET_KEY_AQUÍ"
```

**Reemplaza con tus keys:**

```python
# 🔑 CONFIGURACIÓN DE ALPACA API
ALPACA_API_KEY = "PKXXXXXXXXXXXXXXXXXX"  # ← Pega tu API Key ID aquí
ALPACA_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # ← Pega tu Secret Key aquí
```

**⚠️ Importante:**
- ✅ Mantén las comillas `""`
- ❌ NO agregues espacios antes o después de las keys
- ❌ NO elimines las líneas de comentario (las que empiezan con #)

---

#### ✅ PASO 4A.4: Verificar Conexión a Alpaca

**Busca y ejecuta la celda:**

```python
# ✅ VERIFICACIÓN DE CONEXIÓN A ALPACA
print("Verificando conexión con Alpaca...")
```

**Si todo está bien, verás:**

```
✅ CONEXIÓN EXITOSA A ALPACA
✅ Cuenta: Paper Trading
✅ Saldo disponible: $100,000.00 (simulado)
✅ Listo para descargar datos y operar en paper trading
```

**Si ves un error:**
- ⚠️ Verifica que copiaste las keys correctamente
- ⚠️ Confirma que estás usando Paper Trading (no Live)
- ⚠️ Ve a [Troubleshooting - Alpaca](#troubleshooting-alpaca)

---

#### 🎉 ¡Alpaca Configurado!

**✅ Validación del Paso 4A:**
- [ ] Creé cuenta en Alpaca
- [ ] Obtuve mis API Keys (Paper Trading)
- [ ] Configuré las keys en el notebook
- [ ] Verifiqué la conexión exitosamente

---

### SECCIÓN B: CONFIGURAR INTERACTIVE BROKERS (15-20 min)

---

#### 🤔 ¿Configurar IB Ahora o Después?

**Opción 1 - Configurar AHORA:**
- ✅ Si tienes 20 minutos adicionales
- ✅ Si quieres acceso a crypto, forex, futuros
- ✅ Si planeas operar multi-asset

**Opción 2 - Configurar DESPUÉS:**
- ✅ Si ya llevas 30 minutos en este setup
- ✅ Si solo necesitas US stocks por ahora
- ✅ Si prefieres completar el setup básico primero

**→ Si eliges "Después", salta al [Paso 5](#paso-5-descargar-primer-dataset-5-min)**

---

#### ✅ PASO 4B.1: Crear Cuenta en Interactive Brokers

**⚠️ Proceso más largo que Alpaca (15-20 min):**

**1. Ve a:** https://www.interactivebrokers.com

**2. Click en "Open Account" (Abrir Cuenta)**

**3. Selecciona el tipo de cuenta:**
- **Individual** (recomendado para principiantes)
- NO "Joint" o "Corporate" por ahora

**4. Completa el formulario extenso:**

IB pide MUCHA información:
- Información personal (nombre, dirección, SSN/Tax ID)
- Información financiera (ingresos, patrimonio)
- Experiencia de trading
- Objetivos de inversión

**¿Por qué tanto?**  
IB es un broker regulado por múltiples países. Cumple estrictas normas.

**⏱️ Tiempo de formulario:** 10-15 minutos

**5. Verifica tu identidad:**  
Necesitarás subir documentos:
- Identificación oficial (pasaporte, licencia)
- Comprobante de domicilio (recibo de luz, estado de cuenta)

**⏱️ Tiempo de aprobación:** 1-3 días hábiles

---

#### ⚠️ MIENTRAS ESPERAS APROBACIÓN DE IB

**NO tienes que esperar para continuar el workshop.**

**Puedes:**
1. ✅ Usar Alpaca para todas las sesiones
2. ✅ Completar el resto del Setup A
3. ✅ Empezar con las sesiones del workshop
4. ✅ Volver a configurar IB cuando te aprueben

---

#### ✅ PASO 4B.2: Obtener API Keys de IB (DESPUÉS de aprobación)

**Una vez aprobada tu cuenta:**

**1. Descarga TWS (Trader Workstation) o IB Gateway:**
- TWS: Plataforma completa (pesada)
- IB Gateway: Solo API (más liviano) ← Recomendado

**2. Inicia sesión en TWS/Gateway con tus credenciales**

**3. Ve a:** `Global Configuration` → `API` → `Settings`

**4. Configura:**
- ✅ Enable ActiveX and Socket Clients
- ✅ Port: 7497 (para Paper Trading)
- ✅ Trusted IP Addresses: Agrega `127.0.0.1`

**5. Guarda los cambios**

---

#### ✅ PASO 4B.3: Configurar IB en el Notebook

**⚠️ Esto es MÁS complejo que Alpaca.**

**En tu notebook, busca:**

```python
# 🔑 CONFIGURACIÓN DE INTERACTIVE BROKERS
IB_HOST = "127.0.0.1"  # localhost
IB_PORT = 7497  # Paper Trading (7496 para Live)
IB_CLIENT_ID = 1
```

**NO necesitas cambiar nada si:**
- Usas Paper Trading
- Usas configuración estándar

**Si usas configuración personalizada, ajusta según tus settings.**

---

#### ✅ PASO 4B.4: Verificar Conexión a IB

**⚠️ Requisito previo:**  
TWS o IB Gateway debe estar **ejecutándose** en tu computadora.

**Ejecuta la celda:**

```python
# ✅ VERIFICACIÓN DE CONEXIÓN A IB
print("Verificando conexión con Interactive Brokers...")
```

**Si todo está bien, verás:**

```
✅ CONEXIÓN EXITOSA A INTERACTIVE BROKERS
✅ Cuenta: Paper Trading
✅ TWS Build: 10.19.1
✅ Listo para operar multi-asset
```

**Si ves un error:**
- ⚠️ Verifica que TWS/Gateway esté corriendo
- ⚠️ Confirma que el puerto es 7497 (Paper Trading)
- ⚠️ Ve a [Troubleshooting - Interactive Brokers](#troubleshooting-ib)

---

#### 🎉 ¡Interactive Brokers Configurado!

**✅ Validación del Paso 4B:**
- [ ] Creé cuenta en IB (aprobación puede tomar días)
- [ ] Descargué e instalé TWS o IB Gateway
- [ ] Configuré las credenciales en el notebook
- [ ] Verifiqué la conexión exitosamente (cuando TWS esté corriendo)

---

### ✅ Has Completado el Paso 4

**Validación rápida (al menos UNO debe estar ✅):**
- [ ] Alpaca configurado y funcionando ← Mínimo requerido
- [ ] Interactive Brokers configurado y funcionando ← Opcional pero recomendado
- [ ] Entiendo que puedo usar solo Alpaca para el workshop
- [ ] Sé que puedo configurar IB después si quiero

**✅ Continúa al Paso 5**

---

## PASO 5: DESCARGAR PRIMER DATASET (5 min)

### 🎯 Objetivo del Paso
Descargar datos históricos de un activo (ej: SPY) para validar que tu conexión al broker funciona.

---

### 📊 ¿Qué es un Dataset?

**Dataset = Conjunto de datos históricos de precios**

Típicamente incluye:
- **OHLCV:** Open, High, Low, Close, Volume
- **Timeframe:** Diario, 1H, 15M, 1M, etc.
- **Rango de fechas:** ej: 2020-01-01 a 2024-11-15

**💡 Analogía del Trader:**  
Es como descargar el "historial de precios" de TradingView, pero en formato que Python puede procesar.

---

### ✅ PASO 5.1: Elegir un Activo de Prueba

**Recomendación:** Empezar con **SPY** (S&P 500 ETF)

**¿Por qué SPY?**
- ✅ Alta liquidez (mucho volumen)
- ✅ Datos confiables y completos
- ✅ Disponible en Alpaca e IB
- ✅ Todos los traders lo conocen

**Alternativas populares:**
- **QQQ** - Nasdaq 100 ETF
- **AAPL** - Apple Inc.
- **BTC-USD** - Bitcoin (solo IB, no Alpaca)

---

### ✅ PASO 5.2: Ejecutar la Descarga

**En tu notebook, busca:**

```python
# 📊 DESCARGA DE DATOS HISTÓRICOS
ticker = "SPY"
start_date = "2020-01-01"
end_date = "2024-11-15"
```

**Ejecuta la celda (▶️ o Shift+Enter)**

**Verás:**

```
📥 Descargando datos de SPY desde 2020-01-01 hasta 2024-11-15...
✅ Descarga completada: 1,234 barras de datos
```

**⏱️ Tiempo:** 5-10 segundos

---

### ✅ PASO 5.3: Visualizar los Datos

**La siguiente celda mostrará los primeros datos:**

```python
# 📋 MOSTRAR PRIMEROS 5 DATOS
print(data.head())
```

**Salida esperada:**

```
            Open    High     Low   Close      Volume
Date                                                 
2020-01-02  324.87  325.50  323.45  325.12  50234100
2020-01-03  325.25  326.18  324.60  325.98  48561200
2020-01-06  323.94  326.99  323.68  326.64  52089300
...
```

**Componentes:**
- **Date:** Fecha de cada barra
- **Open:** Precio de apertura
- **High:** Precio máximo del día
- **Low:** Precio mínimo del día
- **Close:** Precio de cierre
- **Volume:** Volumen negociado

---

### ✅ PASO 5.4: Crear un Gráfico Simple

**Ejecuta la siguiente celda:**

```python
# 📈 GRÁFICO DE PRECIOS
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 6))
plt.plot(data['Close'])
plt.title('Precio de Cierre de SPY (2020-2024)')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.grid(True)
plt.show()
```

**Deberías ver:**  
Un gráfico de línea mostrando la evolución del precio de SPY desde 2020 hasta 2024.

**✅ Si ves el gráfico → Tu descarga de datos funciona perfectamente.**

---

### ✅ PASO 5.5: Guardar los Datos (Opcional pero Recomendado)

**Guarda los datos en un archivo CSV:**

```python
# 💾 GUARDAR DATOS EN CSV
data.to_csv('SPY_2020_2024.csv')
print("✅ Datos guardados en SPY_2020_2024.csv")
```

**¿Para qué guardar?**
- ✅ No tienes que descargar de nuevo si el runtime se reinicia
- ✅ Puedes usar los datos offline
- ✅ Backup de tu trabajo

---

### ✅ Has Completado el Paso 5

**Validación rápida:**
- [ ] Descargué datos históricos de SPY
- [ ] Vi los primeros datos en formato tabular
- [ ] Creé un gráfico de precios
- [ ] (Opcional) Guardé los datos en CSV
- [ ] Entiendo el formato OHLCV
- [ ] Estoy listo para la validación final

**✅ Continúa al Paso 6**

---

## PASO 6: VALIDACIÓN FINAL COMPLETA (5 min)

### 🎯 Objetivo del Paso
Ejecutar un checklist completo para confirmar que TODO está funcionando.

---

### ✅ PASO 6.1: Ejecutar el Script de Validación

**En tu notebook, busca:**

```python
# ✅ VALIDACIÓN COMPLETA DEL SETUP
print("🔍 Ejecutando validación completa del Setup A...")
```

**Ejecuta esta celda.**

**Verás una serie de checks:**

```
🔍 Ejecutando validación completa del Setup A...

✅ 1/6 - Python: OK (versión 3.10.12)
✅ 2/6 - Pandas: OK (versión 2.1.1)
✅ 3/6 - yfinance: OK (versión 0.2.28)
✅ 4/6 - Alpaca API: OK (conectado a Paper Trading)
✅ 5/6 - Descarga de datos: OK (SPY: 1,234 barras)
✅ 6/6 - Visualización: OK (gráfico generado)

🎉 VALIDACIÓN COMPLETA: TODO ESTÁ FUNCIONANDO
```

---

### ✅ PASO 6.2: Interpretar Resultados

**Si TODOS los checks muestran ✅ OK:**
- 🎉 **¡Felicitaciones!** Tu setup está 100% funcional
- ✅ Estás listo para el workshop
- ✅ Continúa a [Próximos Pasos](#-próximos-pasos)

**Si algún check muestra ❌ ERROR:**

**Identifica cuál falló:**

| Check | Qué Significa | Solución |
|-------|---------------|----------|
| 1/6 - Python | Problema con la versión de Python | [Troubleshooting - Python](#ts-python) |
| 2/6 - Pandas | Librería no instalada correctamente | [Troubleshooting - Librerías](#ts-librerias) |
| 3/6 - yfinance | yfinance no funciona | [Troubleshooting - yfinance](#ts-yfinance) |
| 4/6 - Alpaca API | Problema con las API keys | [Troubleshooting - Alpaca](#ts-alpaca) |
| 5/6 - Descarga de datos | No se pueden descargar datos | [Troubleshooting - Datos](#ts-datos) |
| 6/6 - Visualización | Problema con matplotlib | [Troubleshooting - Gráficos](#ts-graficos) |

---

### ✅ PASO 6.3: Checklist Manual de Validación

**Además del script automático, valida manualmente:**

**1. Google Colab:**
- [ ] Puedo abrir mi notebook sin problemas
- [ ] El notebook se guarda automáticamente
- [ ] Puedo ejecutar celdas sin errores

**2. Librerías:**
- [ ] pandas, yfinance, alpaca-trade-api están instaladas
- [ ] No veo errores críticos al importarlas
- [ ] Las versiones son compatibles (2024-2025)

**3. Broker:**
- [ ] Tengo cuenta en Alpaca (mínimo)
- [ ] Mis API keys funcionan
- [ ] Puedo conectarme a Paper Trading
- [ ] (Opcional) IB configurado

**4. Datos:**
- [ ] Puedo descargar datos de SPY
- [ ] Los datos tienen el formato correcto (OHLCV)
- [ ] Puedo crear gráficos de precios

**5. Workflow:**
- [ ] Entiendo cómo ejecutar celdas
- [ ] Sé cómo guardar mi trabajo
- [ ] Conozco cómo agregar celdas nuevas
- [ ] Puedo hacer troubleshooting básico

---

### ✅ Has Completado el Paso 6

**Si TODOS los checks están ✅:**

**🎉 ¡FELICITACIONES!**

**Has completado exitosamente el Setup A.**

**Ahora tienes:**
- ✅ Google Colab configurado
- ✅ Notebook personal funcional
- ✅ Librerías de trading instaladas
- ✅ Conexión a broker establecida
- ✅ Capacidad de descargar y visualizar datos
- ✅ Entorno 100% listo para el workshop

**✅ Continúa a [Próximos Pasos](#-próximos-pasos)**

---

## 🗺️ INTEGRACIÓN CON RECURSOS DEL WORKSHOP

### 📦 Recursos Disponibles Para Ti

**Ahora que tienes el setup funcionando, puedes explorar:**

**1. 📚 Template Pack:**
- Strategy Memo
- Reporte de Backtesting
- README Técnico

**Ubicación:** [Template Pack](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/02_TEMPLATE_PACK)

---

**2. 🤖 Prompts Library (35+ Prompts):**
- Adaptar código a tu estrategia
- Depurar errores
- Traducir entre plataformas
- Documentar sistemas

**Ubicación:** [Prompts Library](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)

---

**3. 🛠️ Scripts Auxiliares:**
- Descargador de datos
- Calculadora de position sizing
- Generador de reportes

**Ubicación:** [Scripts Auxiliares](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/04_SCRIPTS_AUXILIARES)

---

**4. 📓 Colab Notebook Maestro:**
- **Código completo** de las 9 sesiones
- **Estrategias implementadas**
- **Backtesting completo**

**⚠️ Acceso:** Solo para participantes inscritos  
**Disponibilidad:** Antes de la Sesión 1

---

### 🎓 Cómo Usar los Recursos Durante el Workshop

**Antes de cada sesión:**

1. **Revisa el template correspondiente**
   - Sesión 1 → Template "Strategy Memo"
   - Sesión 5 → Template "Reporte Backtesting"

2. **Carga los prompts relevantes**
   - Úsalos en Claude o ChatGPT durante las sesiones
   - Adapta el código del Notebook Maestro

3. **Explora los scripts auxiliares**
   - Usa el descargador de datos antes de la Sesión 2
   - Prueba el calculador de position sizing en Sesión 6

---

## 🚨 TROUBLESHOOTING POR PASO

### Troubleshooting Descarga

**Problema: Archivo se descarga como `.txt` o `.html`**

**Causas comunes:**
1. Click simple en lugar de "Guardar enlace como"
2. Navegador auto-renombró el archivo
3. Configuración de descargas del navegador

**Soluciones:**

**Solución 1 - Forzar extensión correcta:**
1. Descarga el archivo (aunque esté mal)
2. Ve a tu carpeta de Descargas
3. Click derecho → Renombrar
4. Cambia la extensión a `.ipynb`
5. Confirma el cambio

**Solución 2 - Usar otro navegador:**
- Chrome → Firefox
- Firefox → Chrome
- Cualquiera → Microsoft Edge

**Solución 3 - Método alternativo:**
1. Ve a GitHub: https://github.com/yismafx/workshop-trading-algoritmico-kit
2. Click en "Code" → "Download ZIP"
3. Descomprime el ZIP
4. Busca `Setup_y_Practica_Trading.ipynb` dentro
5. Sube ese archivo a Colab

---

### Troubleshooting Instalación

**Problema: Error durante instalación de librerías**

**Error común:**
```
ERROR: Could not install packages due to an OSError
```

**Soluciones:**

**Solución 1 - Reiniciar runtime:**
1. Runtime → Disconnect and delete runtime
2. Vuelve a ejecutar la celda de instalación

**Solución 2 - Instalar una por una:**

En lugar de instalar todas juntas, ejecuta:

```python
!pip install pandas
!pip install yfinance
!pip install alpaca-trade-api
!pip install backtrader
!pip install matplotlib
```

Una celda a la vez.

**Solución 3 - Versiones específicas:**

```python
!pip install pandas==2.1.1
!pip install yfinance==0.2.28
```

---

### Troubleshooting Librerías {#ts-librerias}

**Problema: Librería no se importa correctamente**

**Error común:**
```
ModuleNotFoundError: No module named 'pandas'
```

**Causa:** La librería no se instaló o el runtime se reinició.

**Soluciones:**

**Solución 1 - Verificar instalación:**
```python
!pip show pandas
```

Si no aparece → No está instalada → Instalarla:
```python
!pip install pandas
```

**Solución 2 - Reinstalar:**
```python
!pip uninstall pandas -y
!pip install pandas
```

**Solución 3 - Verificar importación:**
```python
import pandas as pd
print(pd.__version__)
```

Si imprime la versión → Está funcionando.

---

### Troubleshooting Alpaca {#ts-alpaca}

**Problema: No puedo conectarme a Alpaca**

**Errores comunes:**

**Error 1:**
```
Authentication failed
```

**Causa:** API keys incorrectas.

**Solución:**
1. Ve a Alpaca → Paper Trading → View API Keys
2. Verifica que las keys en el notebook sean EXACTAMENTE las mismas
3. Asegúrate de NO tener espacios extras
4. Confirma que estás usando Paper Trading (no Live)

---

**Error 2:**
```
Market is closed
```

**Causa:** Estás intentando obtener datos en horario no de mercado.

**Solución:**
- ✅ Usar datos históricos (siempre disponibles)
- ⚠️ Datos en tiempo real solo durante horario de mercado (9:30 AM - 4:00 PM EST)

---

**Error 3:**
```
Invalid symbol
```

**Causa:** El ticker no existe o tiene formato incorrecto.

**Solución:**
- Verifica el ticker en https://finance.yahoo.com
- Usa formato correcto (ej: "AAPL", no "Apple")
- Alpaca solo soporta US stocks (no crypto, no forex)

---

### Troubleshooting Interactive Brokers {#ts-ib}

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

---

### Troubleshooting Datos {#ts-datos}

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

### Troubleshooting Gráficos {#ts-graficos}

**Problema: No se muestra el gráfico**

**Error común:**
```
%matplotlib inline
```

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
- [ ] Lee el [Programa Detallado](Programa_Detallado_Workshop.md)

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

**v1.0 (Noviembre 2025)** - Versión guiada paso a paso  
**Última actualización:** Noviembre 2025

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

[Fin del documento - Setup A Guiado v1.0]
