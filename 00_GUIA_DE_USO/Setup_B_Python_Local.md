# 📖 SETUP B: PYTHON LOCAL - GUÍA PASO A PASO

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 💻 Setup Python Local**

---

**⏱️ Tiempo estimado:** 45-90 minutos  
**🎯 Nivel de detalle:** Paso a paso para Windows  
**📅 Última actualización:** Noviembre 2025  
**🎓 Dificultad:** ⭐⭐⭐ (3/5 estrellas)

---

## 🎯 ¿PARA QUIÉN ES ESTA GUÍA?

### ✅ Esta Guía es PERFECTA si:

- ✅ **Ya completaste** el [Setup A (Google Colab)](Setup_A_Guiado.md)
- 🚀 Quieres **pasar de prototipos a producción** (estrategias 24/7)
- 💻 Tienes una **PC con Windows** disponible
- ⚡ Necesitas que tus estrategias **corran sin depender de internet**
- 📊 Quieres **mayor control** sobre tu ambiente de desarrollo
- 🔄 Planeas **automatizar estrategias** que ejecuten continuamente

### ❌ Esta Guía NO es Ideal si:

- 🆕 **No has hecho el Setup A** (Google Colab)  
  → Ve primero a [Setup A Guiado](Setup_A_Guiado.md) - Aprende lo básico
  
- 🍎 Tienes **Mac o Linux**  
  → Esta guía cubre solo Windows. Contacta soporte para otras plataformas
  
- ⏱️ Solo quieres **prototipar rápido** sin deployment  
  → Sigue usando [Colab](Setup_A_Guiado.md) - Es más simple

- 📱 Quieres trabajar desde **celular o tablet**  
  → Usa [Colab](Setup_A_Guiado.md) - No necesitas instalar nada

---

## 📑 TABLA DE CONTENIDOS

### 🚀 Quick Links
- [⚡ Mapa de Progreso](#-mapa-de-progreso)
- [🔄 ¿Por Qué Migrar de Colab?](#-por-qué-migrar-de-colab-a-python-local)
- [🚨 ¿Problemas?](#-troubleshooting-por-paso)
- [📞 Soporte](#-soporte-y-contacto)

### 📖 Pasos Detallados
1. [Paso 1: Instalar Python en Windows](#paso-1-instalar-python-en-windows-10-min)
2. [Paso 2: Instalar Jupyter Notebook](#paso-2-instalar-jupyter-notebook-10-min)
3. [Paso 3: Configurar Virtual Environment](#paso-3-configurar-virtual-environment-15-min)
4. [Paso 4: Migrar Notebooks de Colab](#paso-4-migrar-notebooks-de-colab-a-jupyter-10-min)
5. [Paso 5: Instalar Librerías de Trading](#paso-5-instalar-librerías-de-trading-15-min)
6. [Paso 6: Validación Final y Primer Notebook Local](#paso-6-validación-final-y-primer-notebook-local-10-min)

### 🔗 Navegación
- [Diferencias Colab vs. Jupyter Local](#-diferencias-clave-colab-vs-jupyter-local)
- [Tips de Migración](#-tips-profesionales-de-migración)
- [Troubleshooting por Paso](#-troubleshooting-por-paso)
- [Próximos Pasos](#-próximos-pasos)

---

## 🗺️ MAPA DE PROGRESO

**Sigue este camino durante el setup:**

```
RUTA PYTHON LOCAL (WINDOWS):

├─ ✅ Paso 1: Instalar Python en Windows (10 min)
├─ ⏳ Paso 2: Instalar Jupyter Notebook (10 min)
├─ ⬜ Paso 3: Configurar Virtual Environment (15 min)
├─ ⬜ Paso 4: Migrar Notebooks de Colab (10 min)
├─ ⬜ Paso 5: Instalar Librerías de Trading (15 min)
└─ ⬜ Paso 6: Validación Final (10 min)

TOTAL: 45-90 minutos
```

---

## 🔄 ¿POR QUÉ MIGRAR DE COLAB A PYTHON LOCAL?

### 📍 Entendiendo la Diferencia

**💡 Analogía del Trader:**

> **Google Colab** es como **operar desde la plataforma web de tu broker**:
> - ✅ Rápido de acceder
> - ✅ No instalas nada
> - ❌ Dependes de internet
> - ❌ Sesión se cierra sola (12h)
>
> **Python Local** es como **tener tu propia sala de operaciones**:
> - ✅ Control total 24/7
> - ✅ Sin límites de tiempo
> - ✅ Funciona sin internet (después del setup)
> - ❌ Requiere configuración inicial

---

### 🆚 Comparación Directa

| Característica | Google Colab | Python Local |
|---------------|--------------|--------------|
| **Instalación** | ✅ Cero (navegador) | ⚠️ ~1 hora (una vez) |
| **Ejecución 24/7** | ❌ Máximo 12h | ✅ Ilimitado |
| **Dependencia internet** | ❌ Siempre | ✅ Solo para datos |
| **Velocidad** | ⚠️ Compartida | ✅ Tu CPU dedicada |
| **Almacenamiento** | ⚠️ Temporal | ✅ Permanente |
| **Automatización** | ❌ Limitada | ✅ Total (cron, scheduler) |
| **Producción** | ❌ No recomendado | ✅ Ideal |
| **Costo** | ✅ Gratis | ✅ Gratis (PC propia) |

---

### 🎯 Casos de Uso Ideales

**Usa Colab cuando:**
- 🧪 Estás prototipando estrategias nuevas
- 📚 Estás aprendiendo y experimentando
- ⚡ Necesitas resultados rápidos sin setup
- 🌐 Trabajas desde múltiples dispositivos

**Usa Python Local cuando:**
- 🚀 Vas a deployar una estrategia a producción
- 🔄 Necesitas ejecutar código 24/7
- 📊 Manejas datasets muy grandes (>5GB)
- 🔒 Requieres máxima privacidad de datos
- ⚙️ Quieres automatizar tareas con schedulers

**💡 Mejor Práctica:**

> Usa **Colab para desarrollar** y **Python Local para deployar**.
> 
> 1. Desarrolla y testea en Colab (rápido, sin fricción)
> 2. Cuando la estrategia funcione, migra a Python Local
> 3. Automatiza y déjala corriendo 24/7

---

## PASO 1: INSTALAR PYTHON EN WINDOWS (10 min)

### 🎯 Objetivo del Paso
Instalar Python 3.11+ en tu PC con Windows y verificar que funciona correctamente.

---

### 📍 ¿Qué es Python?

**💡 Analogía del Trader:**

> Python es el "motor" que ejecuta tu código de trading:
>
> - **Sin Python** → Tienes el "blueprint" de la estrategia (código)
> - **Con Python** → Puedes ejecutar la estrategia y ver resultados
>
> Es como tener el manual de un carro vs. tener el motor que lo hace andar.

---

### 🚀 Acción: Instalar Python

**Paso 1.1 - Descargar Python:**

1. **Abre tu navegador** (Chrome recomendado)
2. **Ve a:** https://www.python.org/downloads/
3. **Verás un botón grande:** "Download Python 3.11.X" o superior
4. **Click en el botón** para descargar

**🔍 Verificación:**
- El archivo descargado debe llamarse: `python-3.11.X-amd64.exe`
- Tamaño aproximado: 25-30 MB

⚠️ **IMPORTANTE:** Descarga la versión **3.11 o superior**. NO uses versiones viejas como 3.7 o 3.8.

---

**Paso 1.2 - Ejecutar el Instalador:**

1. **Doble click** en el archivo descargado (`python-3.11.X-amd64.exe`)
2. **⚠️ CRÍTICO:** En la primera pantalla, marca la casilla:
   ```
   ☑ Add python.exe to PATH
   ```
   **Esto es MUY importante** - si no lo marcas, tendrás problemas después.

3. **Click en:** "Install Now" (instalación recomendada)
4. **Espera** 2-3 minutos mientras se instala
5. **Verás:** "Setup was successful"
6. **Click:** "Close"

---

**Paso 1.3 - Verificar la Instalación:**

1. **Abre el Command Prompt (CMD):**
   - Presiona `Windows + R`
   - Escribe: `cmd`
   - Presiona Enter

2. **En la ventana negra que se abre, escribe:**
   ```bash
   python --version
   ```

3. **Presiona Enter**

**✅ Deberías ver:**
```
Python 3.11.X
```

**Si ves esto, ¡perfecto! Python está instalado.**

---

**❌ Si ves un error:**

```
'python' is not recognized as an internal or external command
```

**Causa:** No marcaste "Add python.exe to PATH" en el Paso 1.2

**Solución:**
1. Desinstala Python (Panel de Control → Programas → Desinstalar)
2. Vuelve a instalar siguiendo el Paso 1.2
3. **Esta vez marca** la casilla "Add python.exe to PATH"

---

### ✅ Checkpoint de Validación - Paso 1

Antes de continuar, verifica:

- [ ] Descargaste Python 3.11 o superior
- [ ] Marcaste "Add python.exe to PATH" durante instalación
- [ ] Ejecutaste `python --version` en CMD
- [ ] Viste la versión de Python (ej: Python 3.11.5)

**Si marcaste todos ✅ → Continúa al Paso 2**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 1](#error-paso-1-python-no-se-reconoce)**

---

## PASO 2: INSTALAR JUPYTER NOTEBOOK (10 min)

### 🎯 Objetivo del Paso
Instalar Jupyter Notebook, la herramienta que te permitirá trabajar con notebooks igual que en Colab, pero localmente.

---

### 📍 ¿Qué es Jupyter Notebook?

**💡 Analogía del Trader:**

> Jupyter es como **TradingView local en tu PC**:
>
> - **Google Colab** → TradingView en la nube (accedes por navegador)
> - **Jupyter local** → TradingView instalado en tu PC
>
> Ambos hacen lo mismo, pero Jupyter corre en tu máquina.

**La ventaja:** Los notebooks que hiciste en Colab funcionan en Jupyter sin cambios.

---

### 🚀 Acción: Instalar Jupyter

**Paso 2.1 - Instalar Jupyter vía pip:**

1. **Abre Command Prompt (CMD):**
   - Windows + R
   - Escribe: `cmd`
   - Enter

2. **Escribe este comando y presiona Enter:**
   ```bash
   pip install jupyter notebook
   ```

3. **Espera 2-3 minutos** mientras se instala

**Verás muchas líneas de texto. Es normal.**

4. **Al final deberías ver:**
   ```
   Successfully installed jupyter-...
   ```

---

**Paso 2.2 - Verificar la Instalación:**

1. **En el mismo CMD, escribe:**
   ```bash
   jupyter --version
   ```

2. **Presiona Enter**

**✅ Deberías ver algo como:**
```
jupyter core     : 5.X.X
jupyter-notebook : 7.X.X
```

**Si ves versiones, ¡perfecto! Jupyter está instalado.**

---

**Paso 2.3 - Iniciar Jupyter por Primera Vez:**

1. **En CMD, escribe:**
   ```bash
   jupyter notebook
   ```

2. **Presiona Enter**

3. **Verás:**
   - Varias líneas de texto en el CMD
   - Se abrirá **automáticamente** tu navegador
   - Verás una pantalla similar a esto:

```
http://localhost:8888/tree

Jupyter Notebook

Files    Running    Clusters

[Lista de carpetas de tu PC]
```

**🎉 ¡Felicidades! Jupyter está corriendo en tu PC.**

---

**Paso 2.4 - Entender la Interfaz:**

**La interfaz de Jupyter tiene 3 partes:**

```
┌────────────────────────────────────────┐
│ 🔝 BARRA SUPERIOR                      │
│    [New ▼] [Upload]  [Refresh]        │
├────────────────────────────────────────┤
│ 📂 NAVEGADOR DE ARCHIVOS               │
│                                        │
│    📁 Desktop                          │
│    📁 Documents                        │
│    📁 Downloads                        │
│    📄 mi_notebook.ipynb                │
│                                        │
└────────────────────────────────────────┘
```

**Componentes:**
- **Barra superior:** Crear notebooks, subir archivos
- **Navegador:** Explorar carpetas de tu PC
- **New:** Crear nuevo notebook

---

**Paso 2.5 - Crear Tu Primer Notebook Local:**

1. **Click en:** `New` (arriba derecha)
2. **Selecciona:** `Python 3` (o `Python 3.11`)
3. **Se abrirá un notebook nuevo**

**Verás:**
```
Untitled

[Celda de código vacía]
```

4. **En la celda, escribe:**
   ```python
   print("¡Mi primer notebook local!")
   ```

5. **Ejecuta:** Shift + Enter

**✅ Deberías ver:**
```
¡Mi primer notebook local!
```

**🎉 ¡Perfecto! Jupyter funciona correctamente.**

---

**Paso 2.6 - Cerrar Jupyter (Importante):**

**Para cerrar Jupyter correctamente:**

1. **En el navegador:** Cierra todas las pestañas de Jupyter
2. **En el CMD:** Presiona `Ctrl + C` (dos veces)
3. **Confirma:** Escribe `y` y Enter cuando pregunte

**💡 Recuerda:** Jupyter corre en el CMD. Si cierras el CMD, Jupyter se cierra.

---

### ✅ Checkpoint de Validación - Paso 2

Antes de continuar, verifica:

- [ ] Instalaste Jupyter con `pip install jupyter notebook`
- [ ] Ejecutaste `jupyter --version` y viste versiones
- [ ] Iniciaste Jupyter con `jupyter notebook`
- [ ] Se abrió el navegador en `localhost:8888`
- [ ] Creaste un notebook y ejecutaste código
- [ ] Sabes cómo cerrar Jupyter (Ctrl+C en CMD)

**Si marcaste todos ✅ → Continúa al Paso 3**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 2](#error-paso-2-jupyter-no-inicia)**

---

## PASO 3: CONFIGURAR VIRTUAL ENVIRONMENT (15 min)

### 🎯 Objetivo del Paso
Crear un ambiente virtual aislado para tus proyectos de trading, evitando conflictos entre librerías.

---

### 📍 ¿Qué es un Virtual Environment?

**💡 Analogía del Trader:**

> Un virtual environment es como tener **cuentas separadas en tu broker**:
>
> - **Sin virtual env** → Todas las estrategias comparten las mismas librerías (riesgo de conflictos)
> - **Con virtual env** → Cada proyecto tiene su propio set de librerías (aislado y seguro)
>
> Ejemplo: 
> - Proyecto A usa pandas versión 1.5
> - Proyecto B usa pandas versión 2.0
> - Sin virtual env → CONFLICTO
> - Con virtual env → Cada uno usa su versión

---

### 🚀 Acción: Crear Virtual Environment

**Paso 3.1 - Crear Carpeta para Proyectos:**

1. **Abre el Explorador de Archivos** (Windows + E)
2. **Ve a:** `C:\`
3. **Crea una carpeta nueva llamada:** `TradingAlgo`
   - Click derecho → Nuevo → Carpeta
   - Nombra: `TradingAlgo`

**Ahora tienes:** `C:\TradingAlgo\`

**💡 ¿Por qué C:\TradingAlgo?**
- Ruta corta y fácil de recordar
- No tiene espacios (evita problemas)
- Está en la raíz de C:\ (fácil de acceder)

---

**Paso 3.2 - Abrir CMD en la Carpeta:**

1. **Navega a:** `C:\TradingAlgo\` en el Explorador
2. **Click en la barra de direcciones** (donde dice C:\TradingAlgo)
3. **Escribe:** `cmd` y presiona Enter

**Se abrirá CMD ya ubicado en esa carpeta:**
```
C:\TradingAlgo>
```

---

**Paso 3.3 - Crear el Virtual Environment:**

1. **En CMD, escribe:**
   ```bash
   python -m venv venv_trading
   ```

2. **Presiona Enter**

3. **Espera 30-60 segundos** (se está creando el ambiente)

**Explicación del comando:**
- `python` → Ejecuta Python
- `-m venv` → Usa el módulo venv (virtual environment)
- `venv_trading` → Nombre de tu ambiente virtual

**Verás que se creó una carpeta:** `C:\TradingAlgo\venv_trading\`

---

**Paso 3.4 - Activar el Virtual Environment:**

1. **En CMD, escribe:**
   ```bash
   venv_trading\Scripts\activate
   ```

2. **Presiona Enter**

**✅ Si funcionó, verás:**
```
(venv_trading) C:\TradingAlgo>
```

**Nota el `(venv_trading)` al inicio** - eso significa que el ambiente virtual está activo.

---

**Paso 3.5 - Verificar el Ambiente Activo:**

1. **Con el ambiente activo, escribe:**
   ```bash
   python --version
   ```

2. **Y también:**
   ```bash
   pip --version
   ```

**✅ Deberías ver:**
```
Python 3.11.X
pip 23.X.X from C:\TradingAlgo\venv_trading\...
```

**Nota:** El path de pip debe mostrar `venv_trading` - esto confirma que estás usando el ambiente virtual.

---

**Paso 3.6 - Actualizar pip en el Virtual Environment:**

**⚠️ IMPORTANTE:** Siempre actualiza pip primero.

1. **Con el ambiente activo, ejecuta:**
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Espera 30 segundos**

**✅ Deberías ver:**
```
Successfully installed pip-23.X.X
```

---

### 🔑 Comandos Clave de Virtual Environment

**Para recordar:**

| Acción | Comando |
|--------|---------|
| **Crear** venv | `python -m venv venv_trading` |
| **Activar** venv | `venv_trading\Scripts\activate` |
| **Desactivar** venv | `deactivate` |
| **Verificar** activo | Buscar `(venv_trading)` en CMD |

**💡 Regla de Oro:**

> **Siempre activa el virtual environment** antes de instalar librerías o ejecutar notebooks.
>
> Si ves `(venv_trading)` al inicio del CMD → ✅ Todo bien
> Si NO ves `(venv_trading)` → ⚠️ Activa el ambiente primero

---

### ✅ Checkpoint de Validación - Paso 3

Antes de continuar, verifica:

- [ ] Creaste la carpeta `C:\TradingAlgo\`
- [ ] Ejecutaste `python -m venv venv_trading`
- [ ] Activaste el ambiente con `venv_trading\Scripts\activate`
- [ ] Ves `(venv_trading)` al inicio del CMD
- [ ] Actualizaste pip con `python -m pip install --upgrade pip`

**Si marcaste todos ✅ → Continúa al Paso 4**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 3](#error-paso-3-virtual-environment-no-se-activa)**

---

## PASO 4: MIGRAR NOTEBOOKS DE COLAB A JUPYTER (10 min)

### 🎯 Objetivo del Paso
Aprender a descargar tus notebooks de Colab y abrirlos en Jupyter local sin perder nada.

---

### 📍 ¿Cómo Funciona la Migración?

**💡 Analogía del Trader:**

> Migrar notebooks es como **exportar tu historial de operaciones** de un broker a otro:
>
> - Tus operaciones (código) se mantienen igual
> - Solo cambias la plataforma donde las ves
> - El formato es estándar (.ipynb) → Funciona en ambos lados

**La buena noticia:** Los notebooks de Colab y Jupyter usan el mismo formato (`.ipynb`).

---

### 🚀 Acción: Migrar un Notebook

**Paso 4.1 - Descargar Notebook desde Colab:**

1. **Abre Google Colab:** https://colab.research.google.com
2. **Abre el notebook que quieres migrar** (ej: `Setup_y_Practica_Trading`)
3. **Click en:** `File` (menú superior)
4. **Selecciona:** `Download` → `Download .ipynb`

**Se descargará un archivo:**
```
Setup_y_Practica_Trading.ipynb
```

**Por defecto, está en:** `C:\Users\TuUsuario\Downloads\`

---

**Paso 4.2 - Mover el Notebook a tu Carpeta de Proyectos:**

1. **Abre el Explorador de Archivos**
2. **Ve a:** `Downloads`
3. **Encuentra:** `Setup_y_Practica_Trading.ipynb`
4. **Copia el archivo** (Ctrl+C)
5. **Navega a:** `C:\TradingAlgo\`
6. **Pega el archivo** (Ctrl+V)

**Ahora tienes:**
```
C:\TradingAlgo\
├── venv_trading\
└── Setup_y_Practica_Trading.ipynb
```

---

**Paso 4.3 - Abrir el Notebook en Jupyter:**

1. **Abre CMD en:** `C:\TradingAlgo\`
   - Explorador → C:\TradingAlgo
   - Click en barra de direcciones → Escribe `cmd` → Enter

2. **Activa el virtual environment:**
   ```bash
   venv_trading\Scripts\activate
   ```

3. **Inicia Jupyter:**
   ```bash
   jupyter notebook
   ```

4. **En el navegador (que se abrió), verás:**
   ```
   Files
   
   📁 venv_trading
   📄 Setup_y_Practica_Trading.ipynb
   ```

5. **Click en:** `Setup_y_Practica_Trading.ipynb`

**🎉 ¡El notebook se abrió en Jupyter!**

---

**Paso 4.4 - Verificar que Todo Funciona:**

1. **En el notebook abierto, busca una celda con código**
2. **Ejecuta la celda:** Shift + Enter
3. **Verifica que se ejecuta sin errores**

**⚠️ NOTA:** Si la celda usa librerías (pandas, numpy, etc.), puede dar error porque aún no las instalamos en el virtual environment. **Esto es normal** - lo arreglaremos en el Paso 5.

---

### 🔄 Tips Profesionales de Migración

**💡 Tip #1: Rutas de Archivos**

**Problema común:** En Colab, los archivos se guardan en `/content/`. En Jupyter local, esa ruta no existe.

**Solución:**

❌ **En Colab (no funciona local):**
```python
df.to_csv("/content/datos.csv")
```

✅ **En Jupyter Local (funciona):**
```python
df.to_csv("datos.csv")  # Se guarda en C:\TradingAlgo\
```

O mejor aún, usa rutas absolutas:
```python
import os
ruta = os.path.join(os.getcwd(), "datos.csv")
df.to_csv(ruta)
```

---

**💡 Tip #2: Google Drive**

**Problema:** Colab se conecta fácil a Google Drive. Jupyter local no.

**❌ Este código NO funciona en Jupyter:**
```python
from google.colab import drive
drive.mount('/content/drive')
```

**✅ Alternativas:**
1. **Descarga archivos de Drive manualmente** a `C:\TradingAlgo\`
2. **Usa Google Drive Desktop** (sincroniza Drive con tu PC)
3. **Usa librerías:** `pydrive` o `gdown` para descargar archivos

---

**💡 Tip #3: Magic Commands de Colab**

Algunos "magic commands" de Colab no funcionan en Jupyter:

**❌ No funciona en Jupyter:**
```python
!pip install yfinance  # Funciona, pero NO respeta virtual env
```

**✅ Funciona correctamente:**
```python
import sys
!{sys.executable} -m pip install yfinance
```

Pero es mejor instalar librerías antes, en CMD (Paso 5).

---

**💡 Tip #4: Reiniciar Kernel**

**En Colab:**
- Runtime → Restart runtime

**En Jupyter:**
- Kernel → Restart

**Es lo mismo, solo cambia el nombre del menú.**

---

### 📋 Checklist de Compatibilidad Colab → Jupyter

Antes de migrar un notebook, revisa:

- [ ] No usa `/content/` en rutas de archivos
- [ ] No usa `from google.colab import drive`
- [ ] No depende de archivos en Google Drive (o ya los descargaste)
- [ ] Las librerías usadas están disponibles (las instalaremos en Paso 5)
- [ ] No usa comandos `!` que dependan de Colab (ej: `!wget`)

**Si hay incompatibilidades, ajusta el código siguiendo los tips de arriba.**

---

### ✅ Checkpoint de Validación - Paso 4

Antes de continuar, verifica:

- [ ] Descargaste un notebook de Colab (.ipynb)
- [ ] Copiaste el archivo a `C:\TradingAlgo\`
- [ ] Abriste Jupyter con el virtual environment activo
- [ ] Viste el notebook en la lista de archivos
- [ ] Abriste el notebook y verificaste que se ve igual que en Colab
- [ ] Entiendes las diferencias clave (rutas, Drive, etc.)

**Si marcaste todos ✅ → Continúa al Paso 5**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 4](#error-paso-4-notebook-no-se-abre-en-jupyter)**

---

## PASO 5: INSTALAR LIBRERÍAS DE TRADING (15 min)

### 🎯 Objetivo del Paso
Instalar todas las librerías de trading en tu virtual environment local, igual que teníamos en Colab.

---

### 📍 ¿Por Qué Reinstalar Librerías?

**💡 Analogía del Trader:**

> Cada virtual environment es como una **cuenta nueva en el broker**:
>
> - En Colab → Ya tenía pandas, numpy, etc. preinstalados
> - En tu virtual environment → Empieza vacío, debes instalar todo
>
> Es como configurar una nueva plataforma de trading desde cero.

---

### 🚀 Acción: Instalar Librerías

**Paso 5.1 - Verificar Virtual Environment Activo:**

1. **Abre CMD** en `C:\TradingAlgo\`
2. **Verifica que veas:** `(venv_trading) C:\TradingAlgo>`
3. **Si NO ves `(venv_trading)`, activa el ambiente:**
   ```bash
   venv_trading\Scripts\activate
   ```

---

**Paso 5.2 - Instalar Librerías Básicas:**

**Copia y pega estos comandos UNO POR UNO:**

```bash
pip install pandas
```
Espera que termine (30 seg)

```bash
pip install numpy
```
Espera que termine (30 seg)

```bash
pip install matplotlib
```
Espera que termine (30 seg)

```bash
pip install yfinance
```
Espera que termine (20 seg)

---

**Paso 5.3 - Instalar Librerías de Brokers:**

```bash
pip install alpaca-py
```

```bash
pip install ib_insync
```

---

**Paso 5.4 - Instalar Librerías de Análisis Técnico:**

```bash
pip install pandas-ta
```

```bash
pip install ta-lib
```

**⚠️ NOTA sobre ta-lib:**

Si `ta-lib` da error en Windows, es normal. Requiere compilador C++.

**Alternativa si falla:**
```bash
pip install TA-Lib-Precompiled
```

O salta ta-lib por ahora - `pandas-ta` es suficiente.

---

**Paso 5.5 - Instalar Librerías de Backtesting:**

```bash
pip install vectorbt
```

```bash
pip install backtrader
```

---

**Paso 5.6 - Crear archivo requirements.txt:**

**Este paso es OPCIONAL pero muy recomendado.**

Un archivo `requirements.txt` lista todas las librerías instaladas. Te permite reinstalar todo con un solo comando.

1. **Con el virtual environment activo, ejecuta:**
   ```bash
   pip freeze > requirements.txt
   ```

2. **Verifica que se creó:**
   ```bash
   dir requirements.txt
   ```

**Ahora tienes:** `C:\TradingAlgo\requirements.txt`

**💡 ¿Para qué sirve?**

Si en el futuro creas otro virtual environment, puedes instalar todo con:
```bash
pip install -r requirements.txt
```

---

**Paso 5.7 - Verificar Instalación:**

1. **Inicia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Crea un notebook nuevo** (New → Python 3)

3. **En una celda, escribe:**
   ```python
   # Verificación de librerías
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import yfinance as yf
   import pandas_ta as ta
   
   print("✅ pandas:", pd.__version__)
   print("✅ numpy:", np.__version__)
   print("✅ matplotlib:", plt.matplotlib.__version__)
   print("✅ yfinance:", yf.__version__)
   print("✅ pandas_ta:", ta.version)
   
   print("\n🎉 ¡Todas las librerías funcionan!")
   ```

4. **Ejecuta la celda** (Shift + Enter)

**✅ Deberías ver:**
```
✅ pandas: 2.X.X
✅ numpy: 1.X.X
✅ matplotlib: 3.X.X
✅ yfinance: 0.X.X
✅ pandas_ta: 0.X.X

🎉 ¡Todas las librerías funcionan!
```

---

### 📋 Lista Completa de Librerías Instaladas

| Librería | Versión | Para Qué Sirve |
|----------|---------|----------------|
| pandas | 2.X | Análisis de datos |
| numpy | 1.X | Cálculos numéricos |
| matplotlib | 3.X | Gráficos |
| yfinance | 0.X | Descargar datos |
| alpaca-py | Latest | Broker Alpaca |
| ib_insync | Latest | Interactive Brokers |
| pandas-ta | Latest | Indicadores técnicos |
| vectorbt | Latest | Backtesting vectorizado |
| backtrader | Latest | Backtesting tradicional |

---

### ✅ Checkpoint de Validación - Paso 5

Antes de continuar, verifica:

- [ ] Virtual environment activo (`(venv_trading)`)
- [ ] Instalaste pandas, numpy, matplotlib
- [ ] Instalaste yfinance
- [ ] Instalaste alpaca-py y/o ib_insync
- [ ] Instalaste pandas-ta
- [ ] Instalaste vectorbt
- [ ] Creaste requirements.txt (opcional)
- [ ] Verificaste que todas las librerías importan sin error

**Si marcaste todos ✅ → Continúa al Paso 6**  
**Si hay algún ❌ → Ve a [Troubleshooting - Paso 5](#error-paso-5-librería-no-se-instala)**

---

## PASO 6: VALIDACIÓN FINAL Y PRIMER NOTEBOOK LOCAL (10 min)

### 🎯 Objetivo del Paso
Verificar que todo el setup funciona correctamente ejecutando un notebook completo de trading.

---

### 🚀 Acción: Test Completo

**Paso 6.1 - Crear Notebook de Validación:**

1. **Asegúrate que Jupyter esté corriendo**
   - Si no: `jupyter notebook` en CMD (con venv activo)

2. **Crea un notebook nuevo:**
   - Click en `New` → `Python 3`

3. **Renombra el notebook:**
   - Click en "Untitled"
   - Cambia a: `Validacion_Setup_Local`

---

**Paso 6.2 - Script de Validación Completo:**

**Copia este código en la primera celda:**

```python
# ═══════════════════════════════════════════════════════════
# 🔍 VALIDACIÓN SETUP PYTHON LOCAL
# ═══════════════════════════════════════════════════════════

print("🔍 VALIDANDO SETUP PYTHON LOCAL")
print("=" * 60)

# Test 1: Verificar librerías
print("\n📦 1. Verificando librerías...")
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import yfinance as yf
    import pandas_ta as ta
    print("✅ Todas las librerías importadas correctamente")
except ImportError as e:
    print(f"❌ Error importando librerías: {e}")

# Test 2: Descargar datos
print("\n📊 2. Descargando datos de prueba...")
try:
    df = yf.download("SPY", start="2023-01-01", end="2024-01-01", progress=False)
    print(f"✅ Datos descargados: {len(df)} filas")
    print(f"   Fecha inicio: {df.index[0].date()}")
    print(f"   Fecha fin: {df.index[-1].date()}")
except Exception as e:
    print(f"❌ Error descargando datos: {e}")

# Test 3: Calcular indicador técnico
print("\n📈 3. Calculando indicadores técnicos...")
try:
    df['SMA_20'] = ta.sma(df['Close'], length=20)
    df['RSI'] = ta.rsi(df['Close'], length=14)
    print("✅ Indicadores calculados (SMA_20, RSI)")
    print(f"   SMA_20 actual: {df['SMA_20'].iloc[-1]:.2f}")
    print(f"   RSI actual: {df['RSI'].iloc[-1]:.2f}")
except Exception as e:
    print(f"❌ Error calculando indicadores: {e}")

# Test 4: Crear gráfico
print("\n📊 4. Generando gráfico...")
try:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='SPY Close', linewidth=2)
    plt.plot(df.index, df['SMA_20'], label='SMA 20', linestyle='--')
    plt.title('SPY - Precio y SMA 20')
    plt.xlabel('Fecha')
    plt.ylabel('Precio ($)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("✅ Gráfico generado correctamente")
except Exception as e:
    print(f"❌ Error generando gráfico: {e}")

# Test 5: Guardar datos localmente
print("\n💾 5. Guardando datos localmente...")
try:
    df.to_csv("test_data_SPY.csv")
    print("✅ Datos guardados en: test_data_SPY.csv")
    print(f"   Ubicación: C:\\TradingAlgo\\test_data_SPY.csv")
except Exception as e:
    print(f"❌ Error guardando datos: {e}")

# Resultado Final
print("\n" + "=" * 60)
print("🎉 VALIDACIÓN COMPLETADA")
print("=" * 60)
print("\n✅ Setup Python Local funcionando al 100%")
print("✅ Puedes empezar a desarrollar estrategias localmente")
print("\n🎓 Próximo paso: Migra tus notebooks de Colab y empieza a automatizar")
print("=" * 60)
```

---

**Paso 6.3 - Ejecutar Validación:**

1. **Ejecuta la celda** (Shift + Enter)
2. **Espera 20-30 segundos**

**✅ Deberías ver:**
```
🔍 VALIDANDO SETUP PYTHON LOCAL
============================================================

📦 1. Verificando librerías...
✅ Todas las librerías importadas correctamente

📊 2. Descargando datos de prueba...
✅ Datos descargados: 252 filas
   Fecha inicio: 2023-01-03
   Fecha fin: 2023-12-29

📈 3. Calculando indicadores técnicos...
✅ Indicadores calculados (SMA_20, RSI)
   SMA_20 actual: 452.15
   RSI actual: 67.23

📊 4. Generando gráfico...
[GRÁFICO DE SPY CON SMA 20]
✅ Gráfico generado correctamente

💾 5. Guardando datos localmente...
✅ Datos guardados en: test_data_SPY.csv
   Ubicación: C:\TradingAlgo\test_data_SPY.csv

============================================================
🎉 VALIDACIÓN COMPLETADA
============================================================

✅ Setup Python Local funcionando al 100%
✅ Puedes empezar a desarrollar estrategias localmente

🎓 Próximo paso: Migra tus notebooks de Colab y empieza a automatizar
============================================================
```

**Y deberías ver un gráfico de SPY.**

---

**Paso 6.4 - Verificar Archivo CSV Creado:**

1. **Abre el Explorador de Archivos**
2. **Ve a:** `C:\TradingAlgo\`
3. **Deberías ver:** `test_data_SPY.csv`

**Esto confirma que puedes guardar datos localmente.**

---

### ✅ Checklist Final de Completación

**Marca todos los items que completaste:**

- [ ] Instalaste Python 3.11+ en Windows (Paso 1)
- [ ] Instalaste Jupyter Notebook (Paso 2)
- [ ] Creaste virtual environment `venv_trading` (Paso 3)
- [ ] Migraste un notebook de Colab a Jupyter (Paso 4)
- [ ] Instalaste todas las librerías de trading (Paso 5)
- [ ] Ejecutaste la validación final (Paso 6)
- [ ] Todos los tests muestran ✅
- [ ] Viste el gráfico de SPY
- [ ] Se creó el archivo `test_data_SPY.csv`

**Si marcaste TODOS ✅:**

🎉 **¡FELICIDADES! Has completado el Setup B al 100%**

**Ahora tienes:**
- ✅ Python instalado localmente
- ✅ Jupyter funcionando en tu PC
- ✅ Virtual environment configurado
- ✅ Todas las librerías de trading
- ✅ Capacidad de migrar notebooks de Colab
- ✅ Ambiente listo para producción 24/7

→ Continúa a [Próximos Pasos](#-próximos-pasos)

**Si hay algún ❌:**

→ Ve a [Troubleshooting](#-troubleshooting-por-paso)

---

## 📊 DIFERENCIAS CLAVE: COLAB VS. JUPYTER LOCAL

### Comparativa Detallada

| Aspecto | Google Colab | Jupyter Local |
|---------|--------------|---------------|
| **Inicio** | Abres navegador | `jupyter notebook` en CMD |
| **Cierre** | Cierras pestaña | Ctrl+C en CMD |
| **Archivos** | Drive o temporal | `C:\TradingAlgo\` |
| **Librerías** | Preinstaladas | Instalas tú |
| **Virtual env** | No aplica | Recomendado |
| **Tiempo ejecución** | 12h máximo | Ilimitado |
| **Internet** | Siempre necesario | Solo para descargar datos |
| **Velocidad** | Variable (compartida) | Tu CPU (dedicada) |
| **Costo** | Gratis | Gratis (tu PC) |

---

### Flujo de Trabajo Recomendado

**🔄 Workflow Profesional:**

```
1. DESARROLLAR EN COLAB
   ├─ Prototipar estrategia rápido
   ├─ Testear con datos pequeños
   └─ Iterar y ajustar

2. MIGRAR A JUPYTER LOCAL
   ├─ Descargar notebook (.ipynb)
   ├─ Copiar a C:\TradingAlgo\
   └─ Ajustar rutas si es necesario

3. PRODUCCIÓN EN LOCAL
   ├─ Ejecutar con datos completos
   ├─ Automatizar (Paso 7 - siguiente guía)
   └─ Monitorear 24/7
```

---

## 🔧 TROUBLESHOOTING POR PASO

### Error Paso 1: Python No Se Reconoce

**Síntoma:** Al ejecutar `python --version` ves:
```
'python' is not recognized...
```

**Causa:** No se agregó Python al PATH

**Solución:**

**Opción 1 - Reinstalar (recomendado):**
1. Panel de Control → Desinstalar programas
2. Busca "Python 3.11"
3. Desinstala
4. Vuelve al Paso 1.2
5. **Esta vez marca:** ☑ Add python.exe to PATH

**Opción 2 - Agregar manualmente al PATH:**
1. Busca dónde se instaló Python: `C:\Users\TuUsuario\AppData\Local\Programs\Python\Python311\`
2. Windows + R → `sysdm.cpl` → Enter
3. Pestaña "Avanzado" → "Variables de entorno"
4. Busca "Path" → Editar
5. Agregar: `C:\Users\TuUsuario\AppData\Local\Programs\Python\Python311\`
6. Reinicia CMD

---

### Error Paso 2: Jupyter No Inicia

**Síntoma:** Al ejecutar `jupyter notebook` ves error

**Causa:** pip no instaló Jupyter correctamente

**Solución:**

**Solución 1 - Reinstalar Jupyter:**
```bash
pip uninstall jupyter notebook
pip install jupyter notebook
```

**Solución 2 - Usar pip con Python explícito:**
```bash
python -m pip install jupyter notebook
```

**Solución 3 - Verificar PATH:**
```bash
python -m jupyter notebook
```

Si este funciona, crea un alias o úsalo siempre así.

---

### Error Paso 3: Virtual Environment No Se Activa

**Síntoma:** No ves `(venv_trading)` después de activar

**Causa:** Problemas con Scripts de ejecución

**Solución:**

**Solución 1 - Usar ruta completa:**
```bash
C:\TradingAlgo\venv_trading\Scripts\activate
```

**Solución 2 - Cambiar política de ejecución (PowerShell):**
Si estás en PowerShell en vez de CMD:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Luego:
```powershell
venv_trading\Scripts\Activate.ps1
```

**Solución 3 - Usar CMD en vez de PowerShell:**
1. Abre CMD (no PowerShell)
2. Navega a `C:\TradingAlgo\`
3. `venv_trading\Scripts\activate`

---

### Error Paso 4: Notebook No Se Abre en Jupyter

**Síntoma:** Click en .ipynb pero no abre o da error

**Causa:** Notebook corrupto o incompatibilidad

**Solución:**

**Solución 1 - Volver a descargar desde Colab:**
1. En Colab: File → Download → Download .ipynb
2. Reemplaza el archivo en `C:\TradingAlgo\`

**Solución 2 - Verificar extensión:**
1. Verifica que el archivo sea `.ipynb` (no `.ipynb.txt`)
2. Windows + R → `control folders`
3. Pestaña "Vista" → Desmarcar "Ocultar extensiones..."

**Solución 3 - Abrir manualmente:**
1. Jupyter → Upload
2. Selecciona el .ipynb descargado
3. Click en "Upload"

---

### Error Paso 5: Librería No Se Instala

**Síntoma:** `pip install X` da error

**Causas comunes:**

**Error: "No matching distribution found"**

**Solución:**
```bash
python -m pip install --upgrade pip
pip install NOMBRE_LIBRERIA
```

**Error: "Microsoft Visual C++ required"**

**Solución (para ta-lib):**
```bash
pip install TA-Lib-Precompiled
```

O descarga desde: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib

**Error: "Permission denied"**

**Solución:**
```bash
pip install --user NOMBRE_LIBRERIA
```

---

## 🎯 PRÓXIMOS PASOS

### ✅ Has Completado el Setup B

**¡Felicitaciones! Ahora tienes:**

✅ Python 3.11+ instalado localmente  
✅ Jupyter Notebook funcionando  
✅ Virtual environment configurado  
✅ Todas las librerías de trading instaladas  
✅ Capacidad de migrar de Colab a local  
✅ Ambiente listo para desarrollo y producción

---

### 🚀 Siguientes Pasos Recomendados

**1. Migra tus notebooks de Colab:**
- [ ] Descarga todos tus notebooks importantes
- [ ] Cópialos a `C:\TradingAlgo\`
- [ ] Ajusta rutas y dependencias si es necesario
- [ ] Verifica que ejecutan correctamente

**2. Organiza tu carpeta de proyectos:**
```
C:\TradingAlgo\
├── venv_trading\           (virtual environment)
├── notebooks\              (tus notebooks)
│   ├── estrategias\
│   ├── backtests\
│   └── analisis\
├── data\                   (datos descargados)
│   ├── historicos\
│   └── live\
├── logs\                   (logs de ejecución)
└── requirements.txt        (librerías)
```

**3. Aprende comandos esenciales:**
- [ ] Iniciar Jupyter: `jupyter notebook`
- [ ] Activar venv: `venv_trading\Scripts\activate`
- [ ] Instalar librería: `pip install NOMBRE`
- [ ] Listar instaladas: `pip list`
- [ ] Guardar requirements: `pip freeze > requirements.txt`

**4. Próxima guía - Automatización (Avanzado):**
- Programar ejecución automática (Task Scheduler)
- Logging profesional
- Monitoreo de estrategias
- Alertas por email/Telegram
- Backup automático

---

### 📚 Recursos Complementarios

**Documentación oficial:**
- Python: https://docs.python.org/3/
- Jupyter: https://jupyter.org/documentation
- pandas: https://pandas.pydata.org/docs/
- yfinance: https://pypi.org/project/yfinance/

**Videos recomendados (español):**
- [Python para Trading - Curso Completo](https://www.youtube.com/watch?v=Hj8TI_V0kMc) (4h)
- [Jupyter Notebook - Tutorial Práctico](https://www.youtube.com/watch?v=6Vr9ZUntCyE) (45min)

---

## 🧭 NAVEGACIÓN

**🏠 Inicio:** [README Principal](../README.md)  
**⬅️ Anterior:** [Setup A - Google Colab](Setup_A_Guiado.md)  
**➡️ Siguiente:** [Setup C - MetaTrader 5](Setup_C_MetaTrader5.md)  
**⬆️ Categoría:** [Guía de Uso](GUIA_INICIO.md)

---

## 📞 SOPORTE Y CONTACTO

### 🆘 Si Necesitas Ayuda

**Antes de contactar, intenta:**

1. ✅ Revisar el [Troubleshooting](#-troubleshooting-por-paso) de este documento
2. ✅ Buscar en el grupo de Telegram
3. ✅ Reiniciar CMD y Jupyter
4. ✅ Desactivar y reactivar virtual environment

**Si el problema persiste:**

### 📧 Email

**Asunto:** `[Setup B - Python Local] - [Tu problema]`

**Email:** yismaryme@gmail.com

**Tiempo de respuesta:** 24-48 horas

**Incluye:**
1. Descripción del problema
2. Qué paso estabas siguiendo
3. Screenshot del error
4. Versión de Python (`python --version`)
5. Qué soluciones ya probaste

---

### 💬 Telegram

**Para:** Consultas rápidas

**Usuario:** [@yismafx](https://t.me/yismafx)

**Horarios:**
- Lunes a Viernes: 9:00 AM - 6:00 PM (GMT-3)
- Fines de semana: Respuestas limitadas

---

## ❓ FAQ - Preguntas Frecuentes

**P: ¿Puedo tener Colab Y Python Local al mismo tiempo?**  
R: Sí, absolutamente. Usa Colab para desarrollo rápido y Local para producción.

**P: ¿Cuánto espacio en disco necesito?**  
R: ~2-3 GB (Python + librerías + virtual env). Más espacio para datos.

**P: ¿Mi PC debe estar prendida 24/7?**  
R: Solo si quieres estrategias corriendo 24/7. Para desarrollo, no.

**P: ¿Puedo usar VSCode en vez de Jupyter?**  
R: Sí, VSCode soporta notebooks .ipynb. Pero esta guía cubre Jupyter.

**P: ¿Qué pasa si actualizo Python?**  
R: Deberás recrear el virtual environment con la nueva versión.

**P: ¿Puedo compartir mi virtual environment?**  
R: No directamente. Comparte `requirements.txt` para que otros instalen las mismas librerías.

**P: ¿Cómo desinstalo todo si quiero empezar de cero?**  
R: 
1. Elimina `C:\TradingAlgo\`
2. Desinstala Python (Panel de Control)
3. Vuelve a empezar desde Paso 1

---

## 📌 VERSIÓN

**v1.0 (Noviembre 2025)** - Setup Python Local para Windows  
**Última actualización:** Noviembre 15, 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- **v1.0 (Nov 15, 2025):** Guía inicial Setup B
  - Instalación Python 3.11+ en Windows
  - Configuración Jupyter Notebook
  - Virtual environments
  - Migración desde Colab
  - Instalación librerías de trading
  - Validación completa
  - Troubleshooting exhaustivo

---

## ⚠️ DISCLAIMER LEGAL

**Material educativo para fines de aprendizaje únicamente.**

❌ **NO constituye asesoría de inversión**  
⚠️ **Trading algorítmico implica riesgo de pérdida de capital**  
📊 **Resultados pasados NO garantizan resultados futuros**  
💰 **Nunca operes con dinero que no puedas perder**

**Recordatorios importantes:**
- Este setup es para desarrollo de estrategias educativas
- El trading algorítmico en producción requiere conocimientos avanzados
- Siempre usa paper trading antes de capital real
- Python local no garantiza uptime - considera servidores para producción seria

**Responsabilidad:**
- Tú eres 100% responsable de tu setup y estrategias
- Este material es educativo, no profesional
- Considera consultar con un asesor financiero certificado
- No nos hacemos responsables por pérdidas o problemas técnicos

---

**🎉 ¡Felicitaciones por completar el Setup B!**

**Ahora tienes el poder de desarrollar y deployar estrategias localmente.**

**Próximo paso: Setup C (MetaTrader 5) si quieres operar en MT5. 🚀**

---

[Fin del documento - Setup B Python Local v1.0]
