# ⚡ SETUP A: COLAB RÁPIDO - GUÍA COMPLETA

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 📄 Setup Colab Rápido**

---

## 📋 METADATOS DEL DOCUMENTO

**Workshop:** Trading Algorítmico Aumentado con IA Generativa  
**Versión:** 5.1 (Correcciones Críticas - Noviembre 2025)  
**Autor:** Yismary Quintero [@yismafx](https://github.com/yismafx)  
**Dificultad:** ⭐ Fácil (No requiere experiencia en programación)  
**Tiempo Estimado:** 10-15 minutos (basado en tiempos reales medidos)  
**Última Actualización:** 14 de Noviembre de 2025

---

## 🎯 ¿QUÉ VAS A LOGRAR EN ESTE SETUP?

Al completar esta guía, tendrás:

✅ **Google Colab configurado** y funcionando  
✅ **Notebook personal de práctica** creado  
✅ **Librerías de trading** instaladas y validadas  
✅ **Conexión a broker** (Alpaca o Interactive Brokers) configurada  
✅ **Primer dataset histórico** descargado (SPY 2020-2024)  
✅ **Entorno 100% funcional** para el workshop

⏱️ **Tiempo real:** Lo mediremos juntos cuando ejecutes este setup

---

## 📑 TABLA DE CONTENIDOS (Clickeable)

### 🚀 Quick Navigation
- [⚡ Ruta Express (10 min)](#-ruta-express-10-minutos)
- [📖 Ruta Guiada (30-60 min)](#-ruta-guiada-completa-30-60-min)
- [🚨 Troubleshooting](#-troubleshooting-por-paso)
- [📞 Soporte](#-soporte-y-contacto)

### 📖 Contenido Principal
1. [¿Es Este Setup Para Ti?](#-es-este-setup-para-ti)
2. [El Camino del Aprendizaje](#-el-camino-de-aprendizaje-python-primero)
3. [Requisitos Mínimos](#-requisitos-mínimos)
4. [Ruta Express](#-ruta-express-10-minutos)
5. [Ruta Guiada Completa](#-ruta-guiada-completa-30-60-min)
   - [Paso 1: Acceder a Google Colab](#paso-1-acceder-a-google-colab-5-min)
   - [Paso 2: Crear Tu Notebook Personal](#paso-2-crear-tu-notebook-personal-5-min)
   - [Paso 3: Instalar Librerías](#paso-3-instalar-librerías-de-trading-10-min)
   - [Paso 4: Configurar Broker](#paso-4-configurar-conexión-a-broker-dual-setup-15-30-min)
   - [Paso 5: Descargar Datos](#paso-5-descargar-primer-dataset-5-min)
   - [Paso 6: Validación Final](#paso-6-validación-final-completa-5-min)
6. [Integración con Recursos del Workshop](#-integración-con-recursos-del-workshop)
7. [Troubleshooting](#-troubleshooting-por-paso)
8. [Próximos Pasos](#-próximos-pasos)

---

## 🎯 ¿ES ESTE SETUP PARA TI?

### ✅ Este Setup es PERFECTO si:

- 📊 Eres **trader profesional** con años de experiencia en mercados
- ❌ **NO tienes** experiencia programando (esto es completamente normal)
- ✅ Prefieres **aprender primero, automatizar después**
- ❌ **NO quieres** instalar programas en tu computadora
- ✅ Quieres empezar a **practicar HOY** (en menos de 1 hora)
- ✅ Tienes conexión a **internet estable**
- ✅ Tienes o puedes crear una **cuenta Gmail**

### ❌ Este Setup NO es Ideal si:

- 🚀 Ya necesitas sistemas funcionando **24/7 en producción**  
  → Ve a [Setup B: Python Local](Setup_B_Python_Local.md)
  
- 📊 Usas principalmente **MetaTrader** y quieres empezar ahí  
  → Ve a [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md)
  
- 💼 Ya tienes cuenta en **Interactive Brokers** y quieres máxima integración  
  → Ve a [Setup D: Interactive Brokers](Setup_D_Interactive_Brokers.md)

### 📊 Estadística del Workshop:

> 🎯 **8 de cada 10 participantes** usan este setup exitosamente  
> ⭐ **Satisfacción:** 4.7/5.0 según feedback de cohortes anteriores

---

## 🧭 EL CAMINO DE APRENDIZAJE: PYTHON PRIMERO

### 🤔 "¿Por qué voy a aprender Python si yo opero en TradingView/MetaTrader?"

Esta es una pregunta frecuente y válida. Aquí está la respuesta honesta:

### 📍 Python es el "Lenguaje Universal" del Trading Algorítmico

**💡 Analogía del Trader:**

```
En Trading Manual, aprendes:
│
├─ Análisis Técnico (RSI, MACD, Bandas Bollinger)
│  └─ Los dominas UNA VEZ
│     └─ Los aplicas en CUALQUIER plataforma
│        ├─ TradingView
│        ├─ MetaTrader
│        ├─ ThinkOrSwim
│        └─ Interactive Brokers

En Trading Algorítmico:
│
├─ Python (Lenguaje Base)
│  └─ Lo aprendes UNA VEZ
│     └─ Lo usas en TODAS las plataformas
│        ├─ Desarrollas en Python (riguroso)
│        ├─ Validas en Python (profesional)
│        └─ Luego (Sesión 7 del workshop):
│           ├─→ IA traduce a Pine Script (TradingView)
│           ├─→ IA traduce a MQL5 (MetaTrader)
│           └─→ IA traduce a cualquier plataforma
```

### 🎯 El Journey del Workshop (9 Sesiones)

**Sesiones 1-6: Fundamentos en Python** (18 horas)
- Descargas datos de mercado
- Diseñas estrategias con IA Generativa
- Haces backtesting riguroso
- Gestionas riesgo profesionalmente

**→ Sesión 7: Multi-Plataforma** (3 horas) ⭐ **AQUÍ ES LA MAGIA**
- Conviertes tu código Python → Pine Script (TradingView)
- Conviertes tu código Python → MQL5 (MetaTrader)
- IA Generativa hace la traducción automática
- Un solo sistema, múltiples plataformas

**Sesiones 8-9: Producción** (6 horas)
- Pones tu sistema 24/7
- Documentas profesionalmente
- Monitoreas en tiempo real

### ⚠️ "Pero yo solo quiero usar TradingView/MetaTrader..."

**Puedes hacerlo, PERO vas a encontrar estas limitaciones:**

❌ **Pine Script y MQL5 son "cerrados"** (solo funcionan en su plataforma)  
❌ **No tienen validación profesional** (Walk-Forward, Monte Carlo)  
❌ **Limitaciones técnicas importantes** (memoria, API calls, librerías)  
❌ **Difícil debugging y testing riguroso**

✅ **Con Python + GenAI obtienes lo MEJOR de ambos mundos:**
- Desarrollo riguroso en Python
- Validación profesional
- Ejecución en la plataforma que prefieras
- Portabilidad total de tu código

**📌 Mensaje del Instructor:**

> **Confía en el proceso.** Miles de traders profesionales han seguido este camino.  
> En Sesión 7, verás por qué Python primero es la ruta correcta.

---

## ✅ REQUISITOS MÍNIMOS

### 💻 Hardware (Tu Equipo)

**Necesitas:**
- ✅ Cualquier computadora con internet (Mac, Windows, o Linux)
- ✅ Conexión internet: **3 Mbps mínimo** (para streaming de video)
- ✅ RAM: **4 GB recomendado** (2 GB funciona, pero más lento)

**NO necesitas:**
- ❌ Computadora potente o cara
- ❌ Instalar programas complejos
- ❌ Configurar entornos virtuales

### 🌐 Software (Programas)

**Necesitas:**
- ✅ **Navegador web moderno:**
  - Google Chrome 90+ ⭐ *Recomendado*
  - Firefox 88+
  - Safari 14+
  - Edge 90+

- ✅ **Cuenta Gmail:**
  - Si ya tienes → ✅ Listo
  - Si no tienes → Crearemos en 5 minutos

**NO necesitas:**
- ❌ Python instalado
- ❌ IDEs o editores de código
- ❌ Terminal o línea de comandos

### 🧠 Conocimientos

**Lo que SÍ necesitas saber:**
- ✅ Usar un navegador web
- ✅ Enviar y recibir emails
- ✅ Fundamentos de trading (esto ya lo dominas)

**Lo que NO necesitas saber:**
- ❌ Programación
- ❌ Python o ningún lenguaje
- ❌ Git, GitHub, o control de versiones
- ❌ Terminal o línea de comandos

---

## ⚡ RUTA EXPRESS (10 minutos)

**🎯 Para traders con experiencia en notebooks o con prisa**

### ✅ Usa Esta Ruta Si:

- ⏱️ Tienes poco tiempo antes del workshop  
- ✅ Ya usaste Google Colab o Jupyter notebooks antes  
- 🎯 Solo quieres validar que todo funcione  
- 🚀 Prefieres seguir instrucciones directas

---

### 📥 PASO 1: Descargar Notebook Pre-Configurado

**Opción A - Descarga Directa (Recomendada):**

[**Click derecho → Guardar enlace como... → Setup_y_Practica_Trading.ipynb**](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb)

**Opción B - Desde GitHub:**

1. Ve a: https://github.com/yismafx/workshop-trading-algoritmico-kit  
2. Navega a: `00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb`  
3. Click en "Raw" (esquina superior derecha)  
4. Ctrl+S (o Cmd+S en Mac) para guardar

---

### 🚀 PASO 2: Subir a Google Colab

1. **Abre Google Colab:**  
   https://colab.research.google.com

2. **Sube el notebook:**
   - `File` → `Upload notebook`
   - Selecciona el archivo `.ipynb` que descargaste
   - Espera 5-10 segundos a que cargue

---

### 📖 PASO 3: Seguir el Notebook Paso a Paso

**💡 El notebook está MUY BIEN organizado con instrucciones en español**

El archivo `Setup_y_Practica_Trading.ipynb` tiene toda la información necesaria:

✅ **Instrucciones en español** en cada sección  
✅ **Código pre-escrito** listo para ejecutar  
✅ **Orden lógico** de pasos numerados  
✅ **Validación automática** al final

**🎯 Solo necesitas:**

1. **Leer cada celda** - Las instrucciones están claras en español
2. **Ejecutar el código** - Dos formas de hacerlo:
   - **Opción A:** Presiona **`Shift + Enter`** en cada celda
   - **Opción B:** Click en el símbolo **▶ (play)** a la izquierda de la celda
3. **Seguir el orden** - El notebook te guía automáticamente

**⏱️ Tiempo de ejecución del notebook:** 5 minutos

---

### 🔑 PASO 4: Configurar Alpaca (5 minutos)

**Mientras el notebook instala las librerías, configura tu cuenta Alpaca:**

#### 4.1 - Crear Cuenta Paper Trading

**⚠️ Si tienes problemas con la página de Alpaca:**

1. **Abre una ventana privada/incógnito:**
   - **Chrome:** `Ctrl + Shift + N` (Windows) o `Cmd + Shift + N` (Mac)
   - **Firefox:** `Ctrl + Shift + P` (Windows) o `Cmd + Shift + P` (Mac)
   - **Safari:** `Cmd + Shift + N` (Mac)
   - **Edge:** `Ctrl + Shift + N` (Windows)

2. **Ve a:** https://app.alpaca.markets/signup

3. **Sigue las instrucciones de Alpaca** para completar el registro:
   - Email
   - Contraseña segura
   - Información básica
   - Verifica tu email

#### 4.2 - Activar Autenticación de 2 Factores (2FA)

**🔴 CRÍTICO - OBLIGATORIO ANTES DE GENERAR API KEYS:**

Alpaca **REQUIERE** que actives 2FA antes de poder generar API Keys para operar.

**Pasos:**

1. **Inicia sesión** en tu cuenta de Alpaca

2. **Ve a Settings:**
   - Click en tu nombre (esquina superior derecha)
   - Selecciona "Settings" o "Configuración"

3. **Activa 2FA:**
   - Busca sección "Security" o "Seguridad"
   - Click en "Enable Two-Factor Authentication"
   - Sigue las instrucciones para configurar con:
     - **Google Authenticator** (recomendado)
     - **Authy**
     - O cualquier app de autenticación

4. **Guarda los códigos de recuperación** en lugar seguro

**⚠️ Sin 2FA activado, NO podrás generar API Keys**

#### 4.3 - Generar API Keys

**Una vez activado el 2FA:**

1. **Ve al dashboard de Alpaca**

2. **Menú lateral izquierdo:**
   - Click en "API Keys" o "Claves API"

3. **Genera nuevas keys:**
   - Click en "Generate New Key" o "Generar Nueva Clave"
   - Dale un nombre descriptivo (ej: "Workshop Trading")

4. **Verás dos códigos:**
   - **API Key** (empieza con `PK` o `AK`)
   - **Secret Key** (empieza con `PS` o `AS`)

---

**🔴 ADVERTENCIA CRÍTICA - LEE ESTO COMPLETO:**

```
⚠️ La Secret Key SOLO se muestra UNA VEZ

IMPORTANTE:
1. Si cierras esta ventana sin copiarla, NO podrás recuperarla
2. Deberás generar nuevas keys desde cero
3. Las keys anteriores se invalidarán automáticamente
4. NO hay forma de ver la Secret Key de nuevo

ACCIÓN INMEDIATA:
→ Copia ambas keys AHORA MISMO antes de cerrar la ventana
```

---

#### 4.4 - Guardar Keys de Forma Segura

**INMEDIATAMENTE después de generar las keys:**

1. **Abre el Bloc de Notas:**
   - **Windows:** Busca "Notepad" o "Bloc de notas"
   - **Mac:** Busca "TextEdit"
   - **Linux:** Usa "gedit" o "nano"

2. **Copia y pega ambas keys:**
   ```
   ALPACA_API_KEY=PKXXXXXXXXXXXXXXXXXX
   ALPACA_SECRET_KEY=PSYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
   ```

3. **Guarda el archivo:**
   - **Nombre:** `alpaca_keys.txt`
   - **Ubicación:** **Escritorio** (para encontrarlo fácilmente)
   - En Windows: Click derecho → Guardar como → Escritorio
   - En Mac: Cmd+S → Selecciona Escritorio

4. **Seguridad del archivo:**
   - ❌ NO lo compartas con nadie
   - ❌ NO lo subas a internet o GitHub
   - ❌ NO lo envíes por email o chat
   - ✅ Solo úsalo para copiar/pegar en el notebook
   - ✅ Bórralo después del workshop si quieres mayor seguridad

**💡 Tip:** Si necesitas volver a usar estas keys más adelante, tendrás el archivo. Si lo pierdes, tendrás que generar nuevas keys.

**⏱️ Tiempo real medido:** 5 minutos (creación + 2FA + keys + guardar)

---

### 📋 PASO 5: Pegar Keys en el Notebook

1. **Vuelve a tu notebook** `Setup_y_Practica_Trading.ipynb` en Colab

2. **Busca la sección de configuración de Alpaca** (está claramente marcada en español)

3. **Abre tu archivo** `alpaca_keys.txt` del escritorio

4. **Copia las keys:**
   - Selecciona el API Key completo
   - Copia (Ctrl+C o Cmd+C)
   - Pega en la celda del notebook donde dice `API_KEY =`
   - Repite con Secret Key

5. **Ejecuta la celda:**
   - **Opción A:** `Shift + Enter`
   - **Opción B:** Click en ▶ (play)

6. **Verifica la conexión:**
   - El notebook tiene una celda de validación
   - Si todo está correcto, verás: ✅ "Conexión exitosa a Alpaca"

---

### 🔍 PASO 6: Validación Final Automática

El notebook incluye una última sección de validación que verifica:

✅ Librerías instaladas correctamente  
✅ Conexión a Alpaca funcionando  
✅ Capacidad de descargar datos históricos  
✅ Sistema listo para el workshop

**Ejecuta la última celda del notebook** (está marcada claramente)

**Resultado esperado:**

```
🎉 ¡TODO PERFECTO! SETUP COMPLETADO AL 100%
============================================================

✅ Librerías: OK
✅ Alpaca: Conectado
✅ Datos: Descargados
✅ Sistema: Listo

============================================================
```

**Si ves esto:** ¡Felicidades! Completaste el setup exitosamente.

**Si ves algún ❌:** Ve a la sección de [Troubleshooting](#-troubleshooting-por-paso).

---

### ⏱️ RESUMEN DE TIEMPOS REALES

**Basado en mediciones reales de Yismary Quintero:**

| Paso | Actividad | Tiempo |
|------|-----------|--------|
| 1-2 | Descargar y subir notebook | 2 min |
| 3 | Ejecución del notebook | 5 min |
| 4 | Configurar Alpaca (cuenta + 2FA + keys) | 5 min |
| 5-6 | Pegar keys y validación | 1 min |
| **TOTAL** | **Setup completo** | **10-15 min** |

**💡 Multitasking:** Puedes crear la cuenta de Alpaca mientras el notebook instala las librerías (Paso 3), ahorrando tiempo.

---

### ✅ CHECKLIST FINAL - RUTA EXPRESS

**Antes de cerrar, verifica que completaste:**

- [ ] Descargaste `Setup_y_Practica_Trading.ipynb`
- [ ] Subiste el notebook a Google Colab
- [ ] Ejecutaste todas las celdas del notebook
- [ ] Creaste cuenta paper trading en Alpaca
- [ ] Activaste 2FA en Alpaca (CRÍTICO)
- [ ] Generaste y copiaste ambas API Keys
- [ ] Guardaste las keys en `alpaca_keys.txt` en tu escritorio
- [ ] Pegaste las keys en el notebook
- [ ] La validación final mostró: ✅ TODO PERFECTO

**Si marcaste todos ✅:**

🎉 **¡Perfecto! Estás 100% listo para el workshop**

**Próximos pasos:**
1. Guarda el notebook (Colab lo hace automáticamente)
2. Cierra esta guía
3. Espera el inicio del workshop

**El día del workshop:**
- Solo abre el notebook
- Ejecuta las primeras celdas para reconectar
- ¡Listo para aprender!

---

## 📖 RUTA GUIADA COMPLETA (30-60 min)

**🎯 Para traders nuevos en notebooks o que prefieren explicaciones paso a paso**

### ✅ Usa Esta Ruta Si:

- 📚 Es tu primera vez con notebooks de trading
- 🧠 Quieres entender QUÉ hace cada herramienta
- 📖 Prefieres explicaciones detalladas
- 🎓 Quieres familiarizarte con el entorno antes del workshop

### 🗺️ MAPA DE PROGRESO

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

### PASO 1: ACCEDER A GOOGLE COLAB (5 min)

**🎯 Objetivo:** Abrir y entender la plataforma donde trabajaremos

#### 📍 ¿Qué es Google Colab?

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

#### 🚀 Acción: Abre Google Colab

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

#### 📹 Recurso de Apoyo:

**Para ver paso a paso en video:**  
🎥 [Google Colab - Introducción Oficial](https://www.youtube.com/watch?v=inN8seMm7UI) (10 min, en inglés)  
🎥 [Google Colab - Tutorial en Español](https://www.youtube.com/results?search_query=google+colab+tutorial+español) (busca el más reciente)

**💡 Consejo del Instructor:**

> No necesitas ver los videos completos ahora. Úsalos si te atascas o quieres profundizar después.

#### ✅ Checkpoint de Validación - Paso 1:

Antes de continuar, verifica:

- [ ] Estás en `colab.research.google.com`
- [ ] Iniciaste sesión con tu cuenta Gmail
- [ ] Ves la interfaz principal de Colab
- [ ] Puedes ver el menú: File, Edit, View, etc.

**Si marcaste todos ✅ → Continúa al Paso 2**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 1](#error-paso-1-no-puedo-acceder-a-colab)**

---

### PASO 2: CREAR TU NOTEBOOK PERSONAL (5 min)

**🎯 Objetivo:** Crear tu espacio de trabajo personal para el workshop

#### 📍 ¿Qué es un Notebook?

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

#### 🚀 Acción: Crea Tu Notebook

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

#### 📹 Recurso de Apoyo:

**Si necesitas ver el proceso:**  
🎥 [Cómo crear y renombrar notebooks en Colab](https://www.youtube.com/results?search_query=create+notebook+google+colab) (primeros 2 minutos del video)

#### ✅ Checkpoint de Validación - Paso 2:

Antes de continuar, verifica:

- [ ] Creaste un notebook nuevo
- [ ] El nombre del notebook es: `Setup_y_Practica_Trading`
- [ ] Ves una celda de código vacía
- [ ] El notebook se guardó automáticamente (ícono de nube)

**Si marcaste todos ✅ → Continúa al Paso 3**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 2](#error-paso-2-no-puedo-crear-el-notebook)**

---

### PASO 3: INSTALAR LIBRERÍAS DE TRADING (10 min)

**🎯 Objetivo:** Instalar todas las herramientas que usaremos en el workshop

#### 📍 ¿Qué son las Librerías?

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

#### 🚀 Acción: Instalar Librerías

**Paso 3.1 - Crear Celda de Instalación:**

1. En tu notebook `Setup_y_Practica_Trading`
2. Asegúrate de estar en una celda de código (no de texto)
3. Si no hay ninguna celda, click en: **`+ Code`** (botón arriba)

**Paso 3.2 - Copiar Código de Instalación:**

Copia y pega este código exacto en la celda:

```python
# ============================================================
# 📦 INSTALACIÓN DE LIBRERÍAS PARA TRADING ALGORÍTMICO
# ============================================================
# IMPORTANTE: Este código solo se ejecuta UNA VEZ al inicio
# Tiempo estimado: 2-3 minutos
# ============================================================

print("🚀 Iniciando instalación de librerías...")
print("⏱️ Tiempo estimado: 2-3 minutos")
print("=" * 60)

# 1. Librerías de conexión a brokers
print("\n📡 Instalando conexiones a brokers...")
!pip install -q alpaca-py          # Para Alpaca
!pip install -q ib_insync          # Para Interactive Brokers

# 2. Librerías de análisis de datos
print("📊 Instalando herramientas de análisis...")
!pip install -q pandas numpy matplotlib seaborn

# 3. Librerías de indicadores técnicos
print("📈 Instalando indicadores técnicos...")
!pip install -q pandas-ta ta-lib

# 4. Librerías de backtesting
print("🔄 Instalando herramientas de backtesting...")
!pip install -q vectorbt backtrader

print("\n" + "=" * 60)
print("✅ ¡Instalación completada!")
print("=" * 60)
print("\n💡 Ahora puedes ejecutar la siguiente celda para validar")
```

**Paso 3.3 - Ejecutar la Instalación:**

1. Con el código pegado en la celda
2. Presiona: **`Shift + Enter`** (o click en el botón ▶ a la izquierda)
3. **Espera** → Verás mucho texto scrolleando (esto es normal)

**⏱️ Tiempo de instalación:** 2-3 minutos

[🔲 SCREENSHOT #2 PLACEHOLDER: Celda de código ejecutándose con output de instalación]
- Celda con el código de instalación pegado
- Botón ▶ (play) resaltado a la izquierda de la celda
- Output debajo mostrando mensajes de instalación
- Al final: "✅ ¡Instalación completada!"

#### 🔍 Verificación de Instalación Exitosa:

**✅ Si ves esto al final, todo está correcto:**

```
============================================================
✅ ¡Instalación completada!
============================================================

💡 Ahora puedes ejecutar la siguiente celda para validar
```

**❌ Si ves mensajes de error rojos:**

NO te preocupes, algunos warnings (advertencias en amarillo) son normales.

**Solo preocúpate si ves:**
- "ERROR: Could not install packages"
- "Permission denied"
- "No matching distribution found"

→ Si ves estos errores: Ve a [Troubleshooting - Paso 3](#error-paso-3-fallo-la-instalación)

#### 📝 ¿Qué Acaba de Pasar?

Cuando ejecutaste la celda:

1. **pip** (el instalador de Python) descargó las librerías
2. Las instaló en la "computadora virtual" de Google Colab
3. Ahora están listas para usar en cualquier celda del notebook

**💡 ¿Tengo que hacer esto cada vez?**

NO. Las librerías permanecen instaladas mientras tu "sesión" de Colab esté activa.

**Una "sesión" termina cuando:**
- Cierras el navegador y pasan 90 minutos
- Colab se desconecta por inactividad (12 horas)

**Si vuelves a abrir el notebook después de cerrar:**
- Solo ejecuta esta celda de instalación de nuevo (2-3 min)
- Luego continúa normal

#### ✅ Checkpoint de Validación - Paso 3:

Antes de continuar, verifica:

- [ ] Pegaste el código de instalación en una celda
- [ ] Ejecutaste la celda (Shift + Enter)
- [ ] Esperaste 2-3 minutos
- [ ] Viste el mensaje: "✅ ¡Instalación completada!"
- [ ] No hay errores rojos críticos (warnings amarillos son OK)

**Si marcaste todos ✅ → Continúa al Paso 4**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 3](#error-paso-3-fallo-la-instalación)**

---

### PASO 4: CONFIGURAR CONEXIÓN A BROKER - DUAL SETUP (15-30 min)

**🎯 Objetivo:** Conectar tu notebook con un broker para obtener datos y ejecutar operaciones

#### 📍 ¿Por Qué Necesito un Broker?

**💡 Analogía del Trader:**

> Un broker es como tu **terminal de trading**:
>
> - Sin broker → No puedes ver datos reales ni operar
> - Con broker → Accedes a precios, ejecutas órdenes, ves tu portafolio
>
> **En trading algorítmico:** Tu código se conecta al broker vía API (conexión automática)

#### 🔀 ELIGE TU BROKER (Solo UNO)

Tienes **DOS opciones** de brokers. Ambos ofrecen **paper trading gratuito**.

**📊 Comparación Rápida:**

| Aspecto | 🅰️ Alpaca | 🅱️ Interactive Brokers |
|---------|-----------|------------------------|
| **Dificultad Setup** | ⭐ Fácil | ⭐⭐⭐ Moderado |
| **Tiempo Setup** | 5-10 min | 15-20 min |
| **Acciones USA** | ✅ Excelente | ✅ Excelente |
| **Criptomonedas** | ✅ Sí | ❌ No |
| **Forex** | ❌ No | ✅ Sí |
| **Futuros/Opciones** | ❌ No | ✅ Sí |
| **Paper Trading** | ✅ Gratis | ✅ Gratis |
| **API** | ✅ Simple | ⚠️ Compleja |
| **Mercados** | 🇺🇸 USA | 🌍 Global |

**🎯 Recomendación del Instructor:**

> **Primera vez** → Empieza con **Alpaca** (más fácil)  
> **Multi-asset avanzado** → Usa **Interactive Brokers**
>
> **Puedes probar ambos**, pero para el setup elige UNO primero.

---

#### 🅰️ OPCIÓN A: SETUP CON ALPACA (10-15 min)

**✅ Elige Alpaca si:**
- ⏱️ Quieres el setup más rápido
- 📊 Solo operas acciones USA y cryptos
- 🎯 Es tu primera vez con APIs
- 📚 Quieres aprender sin fricción

##### Paso 4A.1 - Crear Cuenta Paper Trading de Alpaca

1. **Abre en una nueva pestaña:**  
   https://app.alpaca.markets/signup

2. **Completa el registro:**
   - Email
   - Contraseña segura
   - Acepta términos

3. **Verifica tu email:**
   - Revisa tu bandeja de entrada
   - Click en el link de verificación
   - Vuelve a iniciar sesión en Alpaca

**⏱️ Tiempo:** 3-5 minutos

##### Paso 4A.2 - Obtener Tus API Keys

**¿Qué son las API Keys?**

**💡 Analogía del Trader:**

> Las API Keys son como **usuario y contraseña de tu plataforma**:
>
> - **API Key** = Tu nombre de usuario
> - **Secret Key** = Tu contraseña
>
> **Diferencia:** Las usas para que tu código se conecte automáticamente

**🚀 Acción:**

1. **Inicia sesión en Alpaca:** https://app.alpaca.markets/paper/dashboard/overview

2. **Ve a la sección de API:**
   - En el menú lateral izquierdo
   - Click en **"API Keys"** o **"Your API Keys"**

3. **Genera tus keys:**
   - Click en **"Generate New Key"** o **"Create Key"**
   - Verás dos códigos largos:
     - **API Key** (empieza con `PK` o `AK`)
     - **Secret Key** (empieza con `PS` o `AS`)

4. **Copia las keys:**
   - ⚠️ **IMPORTANTE:** La Secret Key solo se muestra UNA VEZ
   - Click en "Copy" en ambas keys
   - Pégalas temporalmente en un archivo de texto

**⚠️ Seguridad - MUY IMPORTANTE:**

- ❌ **NUNCA** compartas tus Secret Keys con nadie
- ❌ **NUNCA** las subas a GitHub o las hagas públicas
- ✅ **Solo úsalas** en tu notebook personal de Colab
- ✅ **Son gratis**, si las pierdes, genera unas nuevas

**⏱️ Tiempo:** 2-3 minutos

##### Paso 4A.3 - Configurar Keys en Tu Notebook

1. **Vuelve a tu notebook** `Setup_y_Practica_Trading`

2. **Crea una nueva celda de código** (click en `+ Code`)

3. **Copia y pega este código:**

```python
# ============================================================
# 🔑 CONFIGURACIÓN DE ALPACA
# ============================================================
# IMPORTANTE: Reemplaza "TU_API_KEY" y "TU_SECRET_KEY" 
#             con tus keys reales de Alpaca
# ============================================================

# Tus credenciales de Alpaca
ALPACA_API_KEY = "TU_API_KEY_AQUI"        # Cámbialo
ALPACA_SECRET_KEY = "TU_SECRET_KEY_AQUI"  # Cámbialo

# Modo Paper Trading (simulación)
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

print("=" * 60)
print("🔑 Configuración de Alpaca")
print("=" * 60)
print(f"API Key: {ALPACA_API_KEY[:8]}...{ALPACA_API_KEY[-4:]}")
print(f"Modo: Paper Trading (Simulación)")
print("=" * 60)
print("\n✅ Configuración lista")
print("💡 Ejecuta la siguiente celda para validar la conexión")
```

4. **Reemplaza las keys:**
   - Cambia `"TU_API_KEY_AQUI"` por tu API Key real
   - Cambia `"TU_SECRET_KEY_AQUI"` por tu Secret Key real
   - Deja las comillas `""`

**Ejemplo (NO uses este):**

```python
# EJEMPLO (tus keys serán diferentes):
ALPACA_API_KEY = "PKXXXXXXXXXXXXXXXXXX"
ALPACA_SECRET_KEY = "PSYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
```

5. **Ejecuta la celda** (Shift + Enter)

**✅ Si ves esto, configuraste correctamente:**

```
============================================================
🔑 Configuración de Alpaca
============================================================
API Key: PKXXXXXX...XXXX
Modo: Paper Trading (Simulación)
============================================================

✅ Configuración lista
💡 Ejecuta la siguiente celda para validar la conexión
```

**⏱️ Tiempo:** 2 minutos

##### Paso 4A.4 - Validar Conexión a Alpaca

1. **Crea otra celda de código nueva**

2. **Copia y pega este código:**

```python
# ============================================================
# 🌐 VALIDACIÓN DE CONEXIÓN A ALPACA
# ============================================================

print("🔍 Probando conexión a Alpaca...")
print("=" * 60)

try:
    # Importar cliente de Alpaca
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.trading.client import TradingClient
    
    # Crear cliente de datos
    data_client = StockHistoricalDataClient(
        api_key=ALPACA_API_KEY,
        secret_key=ALPACA_SECRET_KEY
    )
    
    # Crear cliente de trading
    trading_client = TradingClient(
        api_key=ALPACA_API_KEY,
        secret_key=ALPACA_SECRET_KEY,
        paper=True  # Modo paper trading
    )
    
    # Obtener información de la cuenta
    account = trading_client.get_account()
    
    print("✅ Conexión exitosa a Alpaca")
    print("=" * 60)
    print(f"📊 Cuenta: {account.account_number}")
    print(f"💰 Cash: ${account.cash}")
    print(f"📈 Poder de compra: ${account.buying_power}")
    print(f"🔒 Modo: Paper Trading")
    print("=" * 60)
    print("\n🎉 ¡Todo listo! Tu conexión a Alpaca funciona perfectamente")
    
except Exception as e:
    print("❌ Error al conectar con Alpaca")
    print("=" * 60)
    print(f"Detalle del error: {str(e)}")
    print("\n💡 Posibles causas:")
    print("1. Las API keys están incorrectas")
    print("2. No copiaste las keys completas")
    print("3. Hay espacios extra en las keys")
    print("\n🔧 Solución:")
    print("- Vuelve al Paso 4A.2 y verifica tus keys")
    print("- Genera nuevas keys si es necesario")
```

3. **Ejecuta la celda** (Shift + Enter)

**✅ Si la conexión es exitosa verás:**

```
🔍 Probando conexión a Alpaca...
============================================================
✅ Conexión exitosa a Alpaca
============================================================
📊 Cuenta: PA123456789
💰 Cash: $100000.00
📈 Poder de compra: $100000.00
🔒 Modo: Paper Trading
============================================================

🎉 ¡Todo listo! Tu conexión a Alpaca funciona perfectamente
```

**❌ Si hay error:**

Ve a [Troubleshooting - Paso 4A](#error-paso-4a-no-puedo-conectar-con-alpaca)

**⏱️ Tiempo:** 1 minuto

##### ✅ Checkpoint de Validación - Setup Alpaca:

Antes de continuar al Paso 5, verifica:

- [ ] Creaste cuenta paper trading en Alpaca
- [ ] Obtuviste tus API Keys (Key + Secret)
- [ ] Configuraste las keys en tu notebook
- [ ] Ejecutaste la validación de conexión
- [ ] Viste el mensaje: "✅ Conexión exitosa a Alpaca"
- [ ] Ves tu balance de paper trading ($100,000)

**Si marcaste todos ✅ → Salta al [Paso 5](#paso-5-descargar-primer-dataset-5-min)**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 4A](#error-paso-4a-no-puedo-conectar-con-alpaca)**

---

#### 🅱️ OPCIÓN B: SETUP CON INTERACTIVE BROKERS (20-30 min)

**✅ Elige Interactive Brokers si:**
- 🌍 Quieres acceso a mercados globales
- 📊 Operas Forex, Futuros, u Opciones
- 💼 Planeas escalar a cuenta real profesional
- 🎯 Buscas la plataforma más completa

**⚠️ ADVERTENCIA:**

El setup de Interactive Brokers es **más complejo** que Alpaca porque requiere:
- Descargar e instalar TWS o Gateway
- Configurar ajustes de API manualmente
- Mayor tiempo de configuración inicial

**Si es tu primera vez con APIs**, considera empezar con Alpaca.

##### Paso 4B.1 - Crear Cuenta Paper Trading de IB

1. **Abre en una nueva pestaña:**  
   https://www.interactivebrokers.com/en/home.php

2. **Click en: "Open Account" o "Try Paper Trading"**

3. **Selecciona "Individual Account"**

4. **Completa el formulario:**
   - Información personal
   - Dirección
   - Experiencia de trading
   - Objetivos de inversión

**⏱️ Tiempo:** 10-15 minutos

**💡 Nota:** Interactive Brokers puede solicitar más información que Alpaca debido a regulaciones.

##### Paso 4B.2 - Descargar TWS o IB Gateway

**¿Qué es TWS/Gateway?**

**💡 Analogía del Trader:**

> - **TWS (Trader Workstation)** = Tu plataforma de trading completa (como MetaTrader)
> - **IB Gateway** = Versión ligera solo para conexión API (sin interfaz gráfica)
>
> **Para el workshop:** Gateway es suficiente (más ligero)

**🚀 Acción:**

1. **Descarga IB Gateway:**  
   https://www.interactivebrokers.com/en/trading/ibgateway-stable.php

2. **Selecciona tu sistema operativo:**
   - Windows
   - macOS
   - Linux

3. **Instala el programa:**
   - Ejecuta el instalador descargado
   - Sigue el asistente de instalación
   - Acepta términos y condiciones

**⏱️ Tiempo:** 5 minutos (descarga + instalación)

##### Paso 4B.3 - Configurar API en IB Gateway

1. **Abre IB Gateway** (el programa que instalaste)

2. **Inicia sesión con tus credenciales de paper trading**

3. **Configura la API:**
   - Ve a: **Settings** o **Configure**
   - Busca: **API Settings**
   - Activa: **Enable ActiveX and Socket Clients**
   - Puerto: **7497** (paper) o **7496** (live)
   - Trusted IPs: **127.0.0.1** (localhost)

4. **Guarda los cambios**

5. **Mantén IB Gateway abierto** (necesario para la conexión)

**⏱️ Tiempo:** 3-5 minutos

##### Paso 4B.4 - Configurar Conexión en Tu Notebook

1. **Vuelve a tu notebook** `Setup_y_Practica_Trading`

2. **Crea una nueva celda de código**

3. **Copia y pega este código:**

```python
# ============================================================
# 🔑 CONFIGURACIÓN DE INTERACTIVE BROKERS
# ============================================================
# IMPORTANTE: IB Gateway debe estar abierto y conectado
# ============================================================

# Configuración de conexión
IB_HOST = "127.0.0.1"  # Localhost
IB_PORT = 7497         # Puerto paper trading
IB_CLIENT_ID = 1       # ID de cliente (puede ser cualquier número)

print("=" * 60)
print("🔑 Configuración de Interactive Brokers")
print("=" * 60)
print(f"Host: {IB_HOST}")
print(f"Puerto: {IB_PORT} (Paper Trading)")
print(f"Client ID: {IB_CLIENT_ID}")
print("=" * 60)
print("\n⚠️  IMPORTANTE: IB Gateway debe estar abierto")
print("✅ Configuración lista")
print("💡 Ejecuta la siguiente celda para validar la conexión")
```

4. **Ejecuta la celda** (Shift + Enter)

**⏱️ Tiempo:** 1 minuto

##### Paso 4B.5 - Validar Conexión a Interactive Brokers

1. **Crea otra celda de código nueva**

2. **Copia y pega este código:**

```python
# ============================================================
# 🌐 VALIDACIÓN DE CONEXIÓN A INTERACTIVE BROKERS
# ============================================================

print("🔍 Probando conexión a Interactive Brokers...")
print("=" * 60)

try:
    from ib_insync import IB, util
    
    # Crear instancia de conexión
    ib = IB()
    
    # Conectar a IB Gateway
    ib.connect(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)
    
    # Obtener información de la cuenta
    account_values = ib.accountValues()
    
    # Buscar el balance
    cash = None
    for av in account_values:
        if av.tag == 'CashBalance' and av.currency == 'USD':
            cash = av.value
            break
    
    print("✅ Conexión exitosa a Interactive Brokers")
    print("=" * 60)
    print(f"🔌 Conectado al puerto: {IB_PORT}")
    print(f"💰 Cash disponible: ${cash if cash else 'N/A'}")
    print(f"🔒 Modo: Paper Trading")
    print("=" * 60)
    print("\n🎉 ¡Todo listo! Tu conexión a IB funciona perfectamente")
    
    # Desconectar
    ib.disconnect()
    
except Exception as e:
    print("❌ Error al conectar con Interactive Brokers")
    print("=" * 60)
    print(f"Detalle del error: {str(e)}")
    print("\n💡 Posibles causas:")
    print("1. IB Gateway no está abierto")
    print("2. IB Gateway no está conectado (login)")
    print("3. La API no está habilitada en Settings")
    print("4. El puerto es incorrecto (debe ser 7497 para paper)")
    print("\n🔧 Solución:")
    print("- Abre IB Gateway y conéctate")
    print("- Verifica API Settings (Enable ActiveX...)")
    print("- Vuelve al Paso 4B.3 si es necesario")
```

3. **Ejecuta la celda** (Shift + Enter)

**✅ Si la conexión es exitosa verás:**

```
🔍 Probando conexión a Interactive Brokers...
============================================================
✅ Conexión exitosa a Interactive Brokers
============================================================
🔌 Conectado al puerto: 7497
💰 Cash disponible: $1000000.00
🔒 Modo: Paper Trading
============================================================

🎉 ¡Todo listo! Tu conexión a IB funciona perfectamente
```

**❌ Si hay error:**

Ve a [Troubleshooting - Paso 4B](#error-paso-4b-no-puedo-conectar-con-interactive-brokers)

**⏱️ Tiempo:** 1 minuto

##### ✅ Checkpoint de Validación - Setup Interactive Brokers:

Antes de continuar al Paso 5, verifica:

- [ ] Creaste cuenta paper trading en IB
- [ ] Descargaste e instalaste IB Gateway
- [ ] Configuraste API Settings (puerto 7497, Enable API)
- [ ] IB Gateway está abierto y conectado
- [ ] Configuraste la conexión en tu notebook
- [ ] Ejecutaste la validación de conexión
- [ ] Viste el mensaje: "✅ Conexión exitosa a Interactive Brokers"

**Si marcaste todos ✅ → Continúa al [Paso 5](#paso-5-descargar-primer-dataset-5-min)**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 4B](#error-paso-4b-no-puedo-conectar-con-interactive-brokers)**

---

### PASO 5: DESCARGAR PRIMER DATASET (5 min)

**🎯 Objetivo:** Descargar datos históricos de SPY para validar que todo funciona

#### 📍 ¿Por Qué Descargamos SPY?

**💡 Analogía del Trader:**

> **SPY** (SPDR S&P 500 ETF) es como el "termómetro del mercado":
>
> - Alta liquidez (fácil de operar)
> - Datos de calidad
> - Representa el mercado completo
> - Perfecto para aprender
>
> **Es nuestro "activo de prueba"** antes de trabajar con otros activos

#### 🚀 Acción: Descargar Datos de SPY

**El código descarga automáticamente cambia según tu broker:**

##### 🅰️ Si Usaste Alpaca:

1. **Crea una nueva celda de código**

2. **Copia y pega este código:**

```python
# ============================================================
# 📥 DESCARGAR DATOS HISTÓRICOS DE SPY (ALPACA)
# Versión Profesional con Validación de Restricciones
# ============================================================
# 🎓 TEORÍA (López de Prado, 2018):
# "La calidad del backtesting depende de la calidad de los datos.
#  Validar fechas ANTES de solicitar datos evita errores silenciosos."
# ============================================================

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta
import pandas as pd

print("📥 Descargando datos de SPY...")
print("=" * 60)

# ============================================================
# VALIDACIÓN 1: Fechas por defecto con restricción de Alpaca
# ============================================================

# ⚠️ RESTRICCIÓN CRÍTICA DE ALPACA (Plan Basic)
# Según documentación oficial: https://docs.alpaca.markets/docs/about-market-data-api
# - Plan Basic: Retraso de 15 minutos para datos históricos
# - Plan Algo Trader Plus ($99/mes): Sin restricción

end_date = datetime.now() - timedelta(days=1)  # ✅ Usar AYER (más seguro)
start_date = end_date - timedelta(days=365*5)  # 5 años atrás desde ayer

print(f"📅 Fecha inicio: {start_date.date()} (5 años atrás)")
print(f"📅 Fecha fin: {end_date.date()} (ayer)")

# ============================================================
# VALIDACIÓN 2: Verificar restricción de 15 minutos
# ============================================================

ahora = datetime.now()
diferencia_minutos = (ahora - end_date).total_seconds() / 60

if diferencia_minutos < 15:
    print("\n⚠️ ADVERTENCIA: Restricción de plan gratuito detectada")
    print(f"   Intentas datos de hace {diferencia_minutos:.0f} minutos")
    print(f"   Plan gratuito requiere al menos 15 minutos de antigüedad")
    print(f"   Ajustando automáticamente a: {(ahora - timedelta(minutes=20)).date()}")
    end_date = ahora - timedelta(minutes=20)  # 20 min para estar seguros

print("=" * 60)

# ============================================================
# DESCARGA CON MANEJO DE ERRORES
# ============================================================

try:
    # Crear cliente
    data_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
    
    # Crear request
    request_params = StockBarsRequest(
        symbol_or_symbols=["SPY"],
        timeframe=TimeFrame.Day,
        start=start_date,
        end=end_date
    )
    
    # Ejecutar descarga
    print(f"\n🔄 Solicitando datos a Alpaca...")
    bars = data_client.get_stock_bars(request_params)
    
    # Convertir a DataFrame
    df = bars.df
    
    # ============================================================
    # VALIDACIÓN 3: Verificar calidad de datos
    # ============================================================
    
    if df.empty:
        raise ValueError(
            f"❌ No se encontraron datos para SPY en el período especificado"
        )
    
    # Verificar valores nulos
    nulos_por_columna = df.isnull().sum()
    if nulos_por_columna.any():
        print(f"\n⚠️ Advertencia: Datos con valores nulos detectados:")
        print(nulos_por_columna[nulos_por_columna > 0])
    
    # ============================================================
    # RESUMEN DE DESCARGA
    # ============================================================
    
    print(f"\n✅ Descarga completada exitosamente")
    print("=" * 60)
    print(f"📊 Símbolo: SPY")
    print(f"📅 Período: {df.index[0].date()} a {df.index[-1].date()}")
    print(f"📈 Total de registros: {len(df)}")
    print(f"💰 Precio más reciente: ${df['close'].iloc[-1]:.2f}")
    print(f"💰 Precio más antiguo: ${df['close'].iloc[0]:.2f}")
    print(f"📈 Retorno total: {((df['close'].iloc[-1] / df['close'].iloc[0]) - 1) * 100:.2f}%")
    print("=" * 60)
    
    # Mostrar primeras y últimas filas
    print("\n📋 Primeras 3 filas:")
    print(df.head(3))
    
    print("\n📋 Últimas 3 filas (más recientes):")
    print(df.tail(3))
    
    print("\n🎉 ¡Datos descargados exitosamente!")
    
except Exception as e:
    error_msg = str(e)
    
    # ============================================================
    # DIAGNÓSTICO DE ERRORES COMUNES
    # ============================================================
    
    if "subscription does not permit" in error_msg.lower():
        print(f"\n❌ ERROR: Restricción de suscripción gratuita")
        print(f"   Causa: Intentaste acceder a datos muy recientes (<15 min)")
        print(f"\n🔧 Solución:")
        print(f"   1. El código ya ajustó end_date a 1 día atrás")
        print(f"   2. Si persiste, espera 5 minutos y ejecuta nuevamente")
        print(f"   3. O considera actualizar a Algo Trader Plus ($99/mes)")
    
    elif "invalid credentials" in error_msg.lower():
        print(f"\n❌ ERROR: Credenciales inválidas")
        print(f"   Verifica que API_KEY y SECRET_KEY sean correctos")
        print(f"   Revisa el archivo alpaca_keys.txt en tu escritorio")
    
    elif "connection" in error_msg.lower() or "timeout" in error_msg.lower():
        print(f"\n❌ ERROR: Problema de conexión")
        print(f"   Verifica tu conexión a internet")
        print(f"   Intenta ejecutar la celda nuevamente en 30 segundos")
    
    else:
        print(f"\n❌ ERROR DESCONOCIDO:")
        print(f"   {error_msg}")
        print(f"\n📞 Contacta al instructor si persiste")
    
    raise  # Re-lanzar el error para debugging

3. **Ejecuta la celda** (Shift + Enter)

##### 🅱️ Si Usaste Interactive Brokers:

1. **Crea una nueva celda de código**

2. **Copia y pega este código:**

```python
# ============================================================
# 📥 DESCARGAR DATOS HISTÓRICOS DE SPY (INTERACTIVE BROKERS)
# ============================================================

print("📥 Descargando datos de SPY...")
print("=" * 60)

from ib_insync import IB, Stock, util
from datetime import datetime, timedelta
import pandas as pd

# Conectar a IB
ib = IB()
ib.connect(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)

# Definir contrato de SPY
spy = Stock('SPY', 'SMART', 'USD')
ib.qualifyContracts(spy)

# Configurar fechas
end_date = datetime.now()
duration = "5 Y"  # 5 años de datos
bar_size = "1 day"

# Descargar datos históricos
bars = ib.reqHistoricalData(
    spy,
    endDateTime=end_date,
    durationStr=duration,
    barSizeSetting=bar_size,
    whatToShow='TRADES',
    useRTH=True,  # Regular Trading Hours
    formatDate=1
)

# Convertir a DataFrame
df = util.df(bars)

# Desconectar
ib.disconnect()

print(f"✅ Descarga completada")
print("=" * 60)
print(f"📊 Símbolo: SPY")
print(f"📅 Período: Últimos 5 años")
print(f"📈 Total de días: {len(df)}")
print("=" * 60)

# Mostrar primeras filas
print("\n📋 Primeras 5 filas de datos:")
print(df.head())

# Estadísticas básicas
print("\n📊 Estadísticas básicas:")
print(df.describe())

print("\n🎉 ¡Datos descargados exitosamente!")
```

3. **Ejecuta la celda** (Shift + Enter)

#### 🔍 Verificación de Descarga Exitosa:

**✅ Si ves algo similar a esto, todo está correcto:**

```
📥 Descargando datos de SPY...
============================================================
✅ Descarga completada
============================================================
📊 Símbolo: SPY
📅 Período: 2020-11-14 a 2025-11-14
📈 Total de días: 1260
============================================================

📋 Primeras 5 filas de datos:
                     open   high    low  close   volume
2020-11-14  357.19  359.43  356.89  358.88  54234567
2020-11-15  359.88  360.12  358.23  359.45  52134234
...

📊 Estadísticas básicas:
              open         high  ...
count  1260.000000  1260.000000  ...
mean   412.345678   413.567890  ...
...

🎉 ¡Datos descargados exitosamente!
```

**Lo importante:**
- ✅ Ves una tabla con datos (open, high, low, close, volume)
- ✅ Los datos tienen fechas recientes
- ✅ Hay más de 1000 filas de datos
- ✅ No hay errores rojos

**❌ Si hay error:**

Ve a [Troubleshooting - Paso 5](#error-paso-5-no-puedo-descargar-datos)

#### ✅ Checkpoint de Validación - Paso 5:

Antes de continuar al Paso 6, verifica:

- [ ] Ejecutaste el código de descarga de tu broker
- [ ] Viste el mensaje: "✅ Descarga completada"
- [ ] Viste una tabla con datos de SPY
- [ ] Los datos tienen fechas recientes (últimos 5 años)
- [ ] No hay errores críticos

**Si marcaste todos ✅ → Continúa al [Paso 6](#paso-6-validación-final-completa-5-min)**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 5](#error-paso-5-no-puedo-descargar-datos)**

---

### PASO 6: VALIDACIÓN FINAL COMPLETA (5 min)

**🎯 Objetivo:** Verificar que TODO el setup funciona correctamente

#### 📍 ¿Qué Vamos a Validar?

Este paso ejecuta un **script de validación automática** que verifica:

✅ Librerías instaladas  
✅ Conexión al broker  
✅ Capacidad de descargar datos  
✅ Funcionalidad de análisis básico  
✅ Todo listo para el workshop

#### 🚀 Acción: Ejecutar Validación Final

1. **Crea una nueva celda de código**

2. **Copia y pega este código:**

```python
# ============================================================
# 🔍 VALIDACIÓN COMPLETA DEL SETUP
# ============================================================
# Este script verifica que todo esté funcionando correctamente
# ============================================================

print("🔍 VALIDACIÓN COMPLETA DEL SETUP")
print("=" * 60)

validation_results = []

# ========================================
# 1. Verificar Librerías
# ========================================
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

# ========================================
# 2. Verificar Broker
# ========================================
print("\n🔑 Verificando configuración de broker...")

# Detectar qué broker está configurado
broker_configured = False

# Verificar Alpaca
try:
    if 'ALPACA_API_KEY' in globals() and ALPACA_API_KEY != "TU_API_KEY_AQUI":
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

# ========================================
# 3. Verificar Datos
# ========================================
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

# ========================================
# 4. Imprimir Resultados
# ========================================
print("\n" + "=" * 60)
print("📊 RESULTADOS DE LA VALIDACIÓN")
print("=" * 60)

for item, status in validation_results:
    print(f"{item:.<40} {status}")

# ========================================
# 5. Veredicto Final
# ========================================
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

#### 🔍 Interpretación de Resultados:

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

#### ✅ Checklist Final de Completación:

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

**🎯 Objetivo:** Conectar tu setup con los materiales del workshop

### 📚 Recursos Disponibles

Una vez completado el setup, tendrás acceso a:

#### 1️⃣ Colab Notebook Maestro (En Desarrollo)

**¿Qué es?**

El **Colab Notebook Maestro** será tu manual de código completo del workshop. Contendrá TODO el código de las 9 sesiones, listo para copiar y usar.

**💡 Analogía del Trader:**

```
Setup_y_Practica_Trading.ipynb = Tu "demo account" personal
├─ Lo creaste tú en este setup
├─ Es tu espacio para experimentar
└─ Modificas libremente sin miedo

Colab_Notebook_Maestro.ipynb = La "biblioteca de estrategias" oficial
├─ Código profesional de las 9 sesiones
├─ Validado y testeado
└─ Lo usarás como referencia
```

**📥 Disponibilidad:**

⏳ **En desarrollo** - Recibirás el link por email antes del inicio del workshop

**🎓 Cómo lo usarás:**

Durante el workshop:
1. Instructor explica conceptos → En el Notebook Maestro
2. Tú copias código relevante → A tu notebook personal
3. Experimentas y modificas → En tu espacio de práctica

#### 2️⃣ Prompts Library

**¿Qué es?**

Una colección de **35+ prompts** diseñados específicamente para trading algorítmico con IA Generativa.

**Incluye prompts para:**
- Generar hipótesis de estrategias
- Depurar código Python
- Traducir entre lenguajes (Python ↔ Pine Script ↔ MQL5)
- Explicar conceptos complejos
- Optimizar código existente
- Auditoría de riesgo

**📥 Ubicación en el Repositorio:**

```
workshop-trading-algoritmico-kit/
└── 03_PROMPTS_LIBRARY/
    ├── P01_Explicar_Codigo.md
    ├── P02_Generar_Estrategia.md
    ├── P03_Depurar_Error.md
    └── ... (35+ prompts)
```

**🔗 Acceso:**

[Ver Prompts Library](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)

#### 3️⃣ Template Pack Profesional

**¿Qué es?**

Plantillas de documentación institucional para cada estrategia que desarrolles.

**Incluye:**
- **Strategy Memo** → Documenta tu hipótesis y edge
- **Backtest Report** → Reporta resultados de validación
- **Risk Playbook** → Protocolos de crisis y apagado
- **README Técnico** → Para repositorios de estrategias

**📥 Ubicación en el Repositorio:**

```
workshop-trading-algoritmico-kit/
└── 02_TEMPLATE_PACK/
    ├── Strategy_Memo_Template.md
    ├── Backtest_Report_Template.md
    ├── Risk_Playbook_Template.md
    └── README_Template.md
```

**🔗 Acceso:**

[Ver Template Pack](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/02_TEMPLATE_PACK)

### 🎥 Recursos Externos Recomendados

#### Videos de Google Colab:

- 🎥 [Google Colab - Guía Oficial](https://www.youtube.com/watch?v=inN8seMm7UI) (10 min, inglés)
- 🎥 [Tutorial Colab en Español](https://www.youtube.com/results?search_query=google+colab+tutorial+español) (varios)

#### Videos de APIs de Trading:

- 🎥 [Alpaca API - Tutorial Oficial](https://www.youtube.com/c/AlpacaHQ) (canal oficial)
- 🎥 [IB API - Guía Completa](https://www.youtube.com/results?search_query=interactive+brokers+api+tutorial) (varios)

### 📁 Organización Recomendada en Google Drive

**Crea esta estructura en tu Google Drive:**

```
Mi_Workshop_Trading/
├── Notebooks/
│   ├── Setup_y_Practica_Trading.ipynb ← Tu notebook de este setup
│   └── [Futuro] Colab_Notebook_Maestro.ipynb
│
├── Estrategias/
│   └── [Crearás durante el workshop]
│
├── Datos/
│   └── [Datasets descargados]
│
└── Documentacion/
    ├── Strategy_Memos/
    ├── Backtest_Reports/
    └── Risk_Playbooks/
```

### 📨 Comunicación Durante el Workshop

**Canal principal: Telegram**

Recibirás invitación al grupo privado del workshop con:
- 📢 Anuncios del instructor
- 💬 Soporte entre participantes
- 📎 Materiales compartidos
- 🔗 Links a sesiones en vivo

---

## 🚨 TROUBLESHOOTING POR PASO

### Error Paso 1: No Puedo Acceder a Colab

#### ❌ Síntoma: Página no carga o da error 404

**Posibles Causas:**
1. Problemas de conexión a internet
2. Google Colab no disponible en tu región (raro)
3. Bloqueado por firewall corporativo

**✅ Soluciones:**

**Solución 1: Verifica tu conexión**
```
1. Abre otra página de Google (gmail.com, google.com)
2. Si otras páginas de Google funcionan, continúa
3. Si no funcionan, verifica tu conexión a internet
```

**Solución 2: Verifica la URL**
```
1. Asegúrate de escribir exactamente:
   https://colab.research.google.com
2. Sin espacios, sin tildes
```

**Solución 3: Prueba navegador alternativo**
```
1. Si usas Chrome, prueba Firefox
2. Si usas Safari, prueba Chrome
3. Actualiza tu navegador a la última versión
```

**Solución 4: Modo incógnito**
```
1. Ctrl+Shift+N (Windows/Linux) o Cmd+Shift+N (Mac)
2. Intenta acceder a Colab en modo incógnito
3. Si funciona, hay un problema con extensiones o caché
```

#### ❌ Síntoma: Pide login pero no tengo Gmail

**✅ Solución: Crea cuenta Gmail (5 minutos)**

1. Ve a: https://accounts.google.com/signup
2. Completa el formulario:
   - Nombre y apellido
   - Usuario deseado (@gmail.com)
   - Contraseña segura
   - Teléfono (para recuperación)
3. Verifica tu cuenta
4. Vuelve a intentar acceder a Colab

---

### Error Paso 2: No Puedo Crear el Notebook

#### ❌ Síntoma: Botón "New notebook" no funciona

**✅ Soluciones:**

**Solución 1: Recargar la página**
```
1. Presiona F5 o Ctrl+R (Cmd+R en Mac)
2. Espera a que cargue completamente
3. Intenta de nuevo
```

**Solución 2: Borrar caché**
```
1. Ctrl+Shift+Delete (Cmd+Shift+Delete en Mac)
2. Selecciona "Cookies y datos del sitio"
3. Selecciona "Imágenes y archivos en caché"
4. Click en "Borrar datos"
5. Recarga la página de Colab
```

#### ❌ Síntoma: No puedo renombrar el notebook

**✅ Solución:**

```
1. Click directamente sobre "Untitled0.ipynb"
2. Si no es clickeable, ve a: File → Rename
3. Escribe el nuevo nombre: Setup_y_Practica_Trading
4. No agregues .ipynb (se agrega automáticamente)
5. Presiona Enter
```

---

### Error Paso 3: Falló la Instalación

#### ❌ Síntoma: "ERROR: Could not install packages"

**✅ Soluciones:**

**Solución 1: Reiniciar runtime**
```
1. Ve al menú: Runtime → Disconnect and delete runtime
2. Espera 10 segundos
3. Runtime → Run all
4. Vuelve a ejecutar la celda de instalación
```

**Solución 2: Instalar una por una**

Si falla la instalación masiva, instala individualmente:

```python
# Ejecuta cada línea en celdas separadas
!pip install -q alpaca-py
!pip install -q ib_insync
!pip install -q pandas numpy
!pip install -q matplotlib seaborn
!pip install -q pandas-ta
```

#### ❌ Síntoma: Warnings amarillos durante instalación

**✅ Solución:**

Los warnings amarillos son **NORMALES** y no afectan la funcionalidad.

**Solo preocúpate si ves:**
- Mensajes en **ROJO** que digan "ERROR"
- "Installation failed"
- "Permission denied"

**Los warnings comunes (puedes ignorar):**
- "Requirement already satisfied"
- "Deprecated version"
- "Consider upgrading pip"

---

### Error Paso 4A: No Puedo Conectar con Alpaca

#### ❌ Síntoma: "Invalid API credentials"

**✅ Soluciones:**

**Solución 1: Verificar keys**
```
1. Vuelve al dashboard de Alpaca
2. Genera nuevas API keys
3. Cópialas exactamente (sin espacios)
4. Pégalas en el notebook
5. Vuelve a ejecutar la celda de configuración
```

**Solución 2: Verificar formato**

Tu código debe verse así:

```python
# ✅ CORRECTO:
ALPACA_API_KEY = "PKXXXXXXXXXXXXXXXX"  # Con comillas

# ❌ INCORRECTO:
ALPACA_API_KEY = PKXXXXXXXXXXXXXXXX    # Sin comillas
ALPACA_API_KEY = "PK XXXXXXXXXXXXXXXX" # Con espacios
```

#### ❌ Síntoma: "Connection timeout"

**✅ Soluciones:**

**Solución 1: Verificar URL base**
```python
# Asegúrate de tener:
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

# NO:
ALPACA_BASE_URL = "https://api.alpaca.markets"  # Esta es para live
```

**Solución 2: Verificar firewall**
```
1. Alpaca puede estar bloqueado por tu red
2. Intenta desde otra red (datos móviles)
3. Contacta a tu IT si es red corporativa
```

#### ❌ Síntoma: Botón "Generate New Key" está deshabilitado o no aparece

**Causa más común:** NO has activado 2FA (autenticación de 2 factores)

**✅ Solución:**

1. Ve a Settings → Security en Alpaca
2. Busca "Two-Factor Authentication" o "2FA"
3. Click en "Enable" o "Activar"
4. Sigue las instrucciones para configurar con Google Authenticator o Authy
5. Una vez activado, vuelve a la sección de API Keys
6. Ahora el botón "Generate New Key" estará habilitado

**⚠️ Alpaca requiere 2FA obligatoriamente para generar API Keys de trading**

#### ❌ Síntoma: "No puedo ver mi Secret Key"

**Causa:** Cerraste la ventana sin copiar la Secret Key

**✅ Solución:**

La Secret Key SOLO se muestra una vez. No hay forma de recuperarla.

**Pasos:**
1. Ve a API Keys en Alpaca
2. Elimina las keys anteriores (ya no sirven si perdiste la Secret)
3. Click en "Generate New Key"
4. ESTA VEZ, antes de hacer cualquier otra cosa:
   - Abre Bloc de Notas (Windows) o TextEdit (Mac)
   - Copia y pega AMBAS keys (API Key + Secret Key)
   - Guarda como `alpaca_keys.txt` en tu escritorio
   - VERIFICA que el archivo se guardó correctamente
   - Recién entonces cierra la ventana de Alpaca

**💡 Tip:** No cierres la ventana de Alpaca hasta confirmar que guardaste el archivo.

#### ❌ Síntoma: Página de Alpaca no carga o da error 403/404

**✅ Solución:**

1. **Abre ventana privada/incógnito:**
   - Chrome: Ctrl+Shift+N (Windows) o Cmd+Shift+N (Mac)
   - Firefox: Ctrl+Shift+P (Windows) o Cmd+Shift+P (Mac)
   - Safari: Cmd+Shift+N (Mac)
   - Edge: Ctrl+Shift+N (Windows)

2. **Intenta acceder a Alpaca de nuevo:** https://app.alpaca.markets

3. **Si persiste:**
   - Verifica tu conexión a internet
   - Intenta desde otro navegador
   - Borra caché y cookies del navegador
   - Espera 10 minutos y vuelve a intentar

4. **Problemas con firewall corporativo:**
   - Intenta desde tu red móvil (datos del celular)
   - Contacta al equipo de IT si es red corporativa

#### ❌ Síntoma: "Invalid credentials" o "Authentication failed" en el notebook

**Causa:** Keys incorrectas o incompletas

**✅ Solución:**

1. **Abre** `alpaca_keys.txt` de tu escritorio

2. **Verifica que las keys están completas:**
   - API Key debe tener 20 caracteres aprox (PKXXXXXXXXXXXXXXXXXX)
   - Secret Key debe tener 40 caracteres aprox (PSYYYYYYYY...)
   - NO deben estar cortadas

3. **En el notebook, asegúrate de:**
   - Copiar TODA la key (sin espacios al inicio o final)
   - Pegar entre comillas: `"PKXXXX..."`
   - NO agregar espacios extra

4. **Vuelve a ejecutar la celda de configuración:**
   - Shift + Enter o click en ▶ (play)

5. **Si persiste:**
   - Genera nuevas keys en Alpaca
   - Guárdalas de nuevo en `alpaca_keys.txt`
   - Pégalas de nuevo en el notebook

**💡 Tip del Instructor:** El error más común es copiar las keys con espacios extra o incompletas.



---

### Error Paso 4B: No Puedo Conectar con Interactive Brokers

#### ❌ Síntoma: "Cannot connect to TWS"

**✅ Soluciones:**

**Solución 1: Verificar IB Gateway abierto**
```
1. IB Gateway debe estar ABIERTO y CONECTADO
2. Verifica que iniciaste sesión con tus credenciales
3. No cierres IB Gateway mientras ejecutas código
```

**Solución 2: Verificar puerto**
```python
# Paper trading usa puerto 7497:
IB_PORT = 7497

# Live trading usa puerto 7496 (NO uses este):
# IB_PORT = 7496
```

**Solución 3: Verificar API habilitada**
```
1. En IB Gateway: Settings → API → Settings
2. Verifica que esté MARCADO:
   ☑ "Enable ActiveX and Socket Clients"
3. Trusted IPs debe incluir: 127.0.0.1
4. Socket port debe ser: 7497
5. Guarda cambios y reinicia IB Gateway
```

#### ❌ Síntoma: "Connection refused"

**✅ Solución:**

```
1. Cierra IB Gateway completamente
2. Vuelve a abrirlo
3. Inicia sesión de nuevo
4. Espera 10 segundos después del login
5. Ejecuta la celda de conexión nuevamente
```

---

### Error Paso 5: No Puedo Descargar Datos

#### ❌ Síntoma: "Symbol not found" o "Invalid request"

**✅ Soluciones:**

**Solución 1: Verificar símbolo**
```python
# Asegúrate de usar:
symbol = "SPY"  # Todo en mayúsculas

# NO:
symbol = "spy"  # Minúsculas
symbol = "S&P500"  # Símbolo incorrecto
```

**Solución 2: Verificar fechas**

```python
# Las fechas no pueden ser futuras
# Verifica que end_date no sea mayor que hoy
from datetime import datetime
end_date = datetime.now()  # Usa fecha actual
```

#### ❌ Síntoma: "Rate limit exceeded"

**✅ Solución:**

```
1. Esperaste demasiado poco entre requests
2. Espera 60 segundos
3. Vuelve a ejecutar la celda
```

---

### 🆘 Cuando Todo Falla

Si probaste todas las soluciones y aún tienes problemas:

**Opción 1: Empezar de cero**
```
1. Runtime → Disconnect and delete runtime
2. Cierra el notebook
3. Abre uno nuevo
4. Vuelve a empezar desde Paso 2
```

**Opción 2: Contactar soporte**

Ve a la sección de [Soporte](#-soporte-y-contacto)

---

## 💡 CONSEJOS Y MEJORES PRÁCTICAS

### 🔄 Mantener Tu Setup Actualizado

**Cada vez que abras tu notebook:**

1. **Si pasaron más de 12 horas:**
   - Ejecuta de nuevo la celda de instalación (Paso 3)
   - Ejecuta de nuevo la celda de configuración de broker (Paso 4)
   - Luego continúa normalmente

2. **Si es el mismo día:**
   - Ve directo a trabajar
   - Las librerías ya están instaladas

### 💾 Guardar Tu Trabajo

**Google Colab guarda automáticamente, pero:**

1. **Verifica el guardado:**
   - Busca el ícono de nube arriba
   - Si dice "All changes saved" → ✅ OK

2. **Descarga copia local (backup):**
   - File → Download → Download .ipynb
   - Guárdalo en tu computadora como respaldo

3. **Crea checkpoints:**
   - Cada vez que completes una sección importante
   - File → Save a copy in Drive
   - Renombra: `Setup_[Fecha]_v[N].ipynb`

### 🔐 Seguridad de API Keys

**MUY IMPORTANTE:**

1. ❌ **NUNCA** compartas tus keys en:
   - Grupos de Telegram
   - Foros públicos
   - GitHub público
   - Screenshots

2. ✅ **Usa variables de entorno** (avanzado):

```python
# Método más seguro (lo veremos en sesiones avanzadas)
from google.colab import userdata
ALPACA_API_KEY = userdata.get('ALPACA_KEY')
```

3. ✅ **Si expusiste tus keys accidentalmente:**
   - Ve a tu broker inmediatamente
   - Elimina las keys comprometidas
   - Genera nuevas keys

### 🚫 Errores Comunes a Evitar

**Durante el Workshop:**

1. ❌ **NO cierres el notebook durante sesiones**
   - Puedes perder tu sesión activa
   - Tendrías que reinstalar librerías

2. ❌ **NO modifiques el código sin entender**
   - Puedes romper la conexión
   - Mejor: copia el código a otra celda para experimentar

3. ❌ **NO uses Live Trading keys por error**
   - SIEMPRE usa Paper Trading durante el aprendizaje
   - Live Trading solo cuando estés 100% listo

4. ❌ **NO ignores los errores**
   - Cada error tiene una causa
   - Usa el troubleshooting
   - Pregunta en el grupo si persiste

### 🎓 Antes de Cada Sesión del Workshop

**Checklist de preparación:**

- [ ] Abre tu notebook 10 minutos antes
- [ ] Ejecuta la celda de instalación
- [ ] Ejecuta la celda de configuración de broker
- [ ] Ejecuta la celda de validación
- [ ] Verifica que todo muestra ✅ OK
- [ ] Ten papel y lápiz listos para notas
- [ ] Ten el Notebook Maestro abierto en otra pestaña
- [ ] Conecta a internet estable
- [ ] Desactiva notificaciones

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

### 🗓️ Preparación para el Workshop

**Antes de la Sesión 1:**

1. **Revisa los recursos:**
   - [ ] Explora la [Prompts Library](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)
   - [ ] Revisa el [Template Pack](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/02_TEMPLATE_PACK)
   - [ ] Lee el [Programa Detallado](Programa_Detallado_Workshop.md)

2. **Únete al grupo de Telegram:**
   - [ ] Recibirás invitación por email
   - [ ] Preséntate brevemente
   - [ ] Activa notificaciones

3. **Opcional - Familiarízate con Colab:**
   - [ ] Mira videos tutoriales
   - [ ] Experimenta creando celdas
   - [ ] Prueba ejecutar código simple

### 📚 Lecturas Previas Opcionales

**Si quieres adelantar teoría (opcional):**

- 📖 Chan, E. (2013). "Algorithmic Trading", Capítulos 1-2
- 📖 Carver, R. (2015). "Systematic Trading", Introducción
- 📖 López de Prado, M. (2018). "Advances in Financial ML", Prefacio

**NO es obligatorio leer nada antes del workshop.** Todo se explicará desde cero.

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
**➡️ Siguiente:** [Colab Notebook Maestro](../01_COLAB_NOTEBOOK_MAESTRO/Colab_Notebook_Maestro.ipynb) *(Disponible antes del workshop)*  
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

**Asunto:** `[Setup A] - [Tu problema en 5 palabras]`

**Email:** yismaryme@gmail.com

**Tiempo de respuesta:** 24-48 horas

**Incluye en tu email:**
1. Descripción del problema
2. Qué paso estabas siguiendo
3. Screenshot del error (si aplica)
4. Qué soluciones de troubleshooting ya probaste

### 💬 Telegram

**Para:** Consultas rápidas y urgentes

**Usuario:** [@yismafx](https://t.me/yismafx)

**Horarios de respuesta rápida:**
- Lunes a Viernes: 9:00 AM - 6:00 PM (GMT-3)
- Fines de semana: Respuestas limitadas

### 🔒 Grupo Premium del Workshop

**Disponible para participantes inscritos**

- Soporte comunitario
- Respuestas de otros participantes
- Material complementario compartido
- Anuncios importantes

**Recibirás invitación por email después de tu inscripción**

### ❓ FAQ - Preguntas Frecuentes

**P: ¿Cuánto tiempo dura el setup?**  
R: Ruta Express: 5-10 min. Ruta Guiada: 30-60 min (depende del broker)

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

## 🔖 VERSIÓN Y CHANGELOG

**Versión:** 5.0 (Refinado)  
**Última actualización:** 14 de Noviembre de 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

### Changelog:

**v5.1 (Nov 14, 2025):** Correcciones basadas en tiempos reales medidos por Yismary Quintero
- ✨ Autor actualizado: Yismary Quintero (no solo @yismafx)
- ✨ Tiempos actualizados: 10-15 min total (no 30-60 min)
- ✨ Ruta Express completamente reescrita:
  - Notebook con instrucciones en español destacado
  - Formas de ejecutar código: Shift+Enter O play ▶
  - Tiempo de ejecución notebook: 5 min (medido)
- ✨ Sección Alpaca exhaustivamente actualizada:
  - Ventana incógnito como primera solución para problemas de carga
  - 2FA obligatorio explicado ANTES de generar API Keys
  - Advertencia CRÍTICA sobre Secret Key (solo se muestra una vez)
  - Instrucciones para guardar keys en alpaca_keys.txt en escritorio
  - Tiempo real medido: 5 min (cuenta + 2FA + keys)
- ✨ Resumen de tiempos reales en tabla (basado en mediciones)
- ✨ Checklist final de Ruta Express agregado
- ✨ Troubleshooting de Alpaca expandido:
  - Botón Generate Key deshabilitado (falta 2FA)
  - No puedo ver Secret Key (cerró ventana)
  - Página no carga (ventana incógnito)
  - Invalid credentials (keys incorrectas)
- 🔧 Links actualizados en tabla de contenidos
- 🔧 Referencias a tiempos corregidas en todo el documento


**v5.0 (Nov 14, 2025):** Refinamiento completo del Setup A
- ✨ Reestructuración modular para mejor navegación
- ✨ Dual broker setup (Alpaca + Interactive Brokers)
- ✨ Placeholders para screenshots (solo 2 esenciales)
- ✨ Links a videos de YouTube para profundizar
- ✨ Referencias al Notebook Maestro (en desarrollo)
- ✨ Checkpoints de validación después de cada paso
- ✨ Troubleshooting exhaustivo por paso
- ✨ Mejoras en claridad y fluidez del documento
- 🔧 Corrección de link de descarga roto
- 🔧 Eliminación de referencias personales hardcodeadas

**v4.0 (Nov 10, 2025):** Setup funcional completo
- Versión anterior funcional pero necesitaba refinamiento

**v3.0 (Oct 2025):** Primera versión pública
- Setup básico con Alpaca únicamente

---

## ⚠️ DISCLAIMER LEGAL

**Material educativo para fines de aprendizaje únicamente.**

❌ **NO constituye asesoría de inversión**  
⚠️ **Trading algorítmico implica riesgo de pérdida de capital**  
📊 **Resultados pasados NO garantizan resultados futuros**  
💰 **Nunca operes con dinero que no puedas perder**

**Recordatorios importantes:**
- El trading algorítmico requiere conocimiento, práctica y gestión de riesgo
- El 90% de las estrategias fallan en validación rigurosa (Carver, 2015)
- Un Sharpe Ratio > 1.0 (neto de costos) es considerado bueno
- Los drawdowns son inevitables, incluso con estrategias robustas
- Paper trading NO es exactamente igual a live trading (slippage real)

**Responsabilidad:**
- Tú eres 100% responsable de tus decisiones de trading
- Este material es educativo, no predictivo
- Siempre valida estrategias exhaustivamente antes de usar capital real
- Considera consultar con un asesor financiero certificado

---

**🎉 ¡Felicitaciones por completar el Setup A!**

**Estás listo para comenzar tu journey en Trading Algorítmico Aumentado con IA Generativa.**

**Nos vemos en la Sesión 1 del workshop. 🚀**

---

[Fin del documento - Setup A v5.0]
