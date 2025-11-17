# ⚡ SETUP A: COLAB EXPRESS

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 Setup A Express**

---

**⏱️ Tiempo:** 10-15 min | **Dificultad:** ⭐ Fácil | **Audiencia:** Usuarios experimentados con notebooks  
**📅 Última actualización:** Noviembre 2025 | **Versión:** 3.1

---

## 💡 ¿OTRAS RUTAS DE SETUP?

> 📚 **¿Prefieres explicaciones detalladas?**  
> Esta es la guía ultra-rápida. Si quieres más contexto:  
> → [Setup A: Colab Completo →](Setup_A_Colab_Rapido.md) (30-45 min)

> 📖 **¿Quieres máximo detalle exhaustivo?**  
> → [Setup A: Guiado →](Setup_A_Guiado.md) (60-90 min)

---

## 📑 TABLA DE CONTENIDOS

- [¿Para Quién Es Esta Guía?](#-para-quién-es-esta-guía)
- [Pre-Requisitos Rápidos](#-pre-requisitos-rápidos)
- [Paso 1: Descargar Notebook](#paso-1-descargar-notebook-pre-configurado-2-min)
- [Paso 2: Subir a Google Colab](#paso-2-subir-a-google-colab-3-min)
- [Paso 3: Seguir el Notebook](#paso-3-seguir-el-notebook-paso-a-paso-5-10-min)
- [Validación Rápida](#-validación-rápida)
- [Troubleshooting Express](#-troubleshooting-express)
- [Próximos Pasos](#-próximos-pasos)

---

## 🎯 ¿PARA QUIÉN ES ESTA GUÍA?

**✅ Úsala si:**
- ⏱️ Tienes poco tiempo (menos de 30 minutos)
- ✅ Ya usaste Google Colab o Jupyter notebooks antes
- 🎯 Solo quieres validar que todo funcione rápido
- 🚀 Prefieres instrucciones directas sin explicaciones largas

**❌ NO uses esta guía si:**
- 🆕 Es tu primera vez con notebooks
- 📚 Quieres entender cada paso en detalle
- ❓ Necesitas ayuda con conceptos básicos

**→ En ese caso, usa la [Guía Paso a Paso Completa](Setup_A_Guiado.md)**

---

## ✅ PRE-REQUISITOS RÁPIDOS

**Antes de empezar, asegúrate de tener:**

- [ ] Navegador web (Chrome recomendado)
- [ ] Cuenta Gmail activa
- [ ] Conexión a internet (3+ Mbps)
- [ ] 15 minutos sin interrupciones

**Si falta algo, ve a [Requisitos Mínimos Completos](Setup_A_Colab_Rapido.md#-requisitos-mínimos)**

---

## PASO 1: DESCARGAR NOTEBOOK PRE-CONFIGURADO (2 min)

### 📥 Opción A - Descarga Directa (Recomendada)

**1. Haz click derecho en este enlace:**

[**Setup_y_Practica_Trading.ipynb**](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb)

**2. Selecciona "Guardar enlace como..." o "Save link as..."**

**3. Guarda el archivo en una carpeta que recuerdes (ej: Descargas, Escritorio)**

**✅ Verificación:** El archivo debe terminar en `.ipynb` (no `.txt` o `.html`)

---

### 📥 Opción B - Desde GitHub

**Si la Opción A no funcionó:**

1. **Ve a:** https://github.com/yismafx/workshop-trading-algoritmico-kit  

2. **Navega a:** `00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb`

3. **Click en "Raw"** (botón arriba derecha del archivo)

4. **Guardar:** 
   - Windows: `Ctrl + S`
   - Mac: `Cmd + S`
   - O click derecho → "Guardar como..."

5. **Asegúrate:** Guardar como tipo "All files" o con extensión `.ipynb`

---

### 🚨 Troubleshooting Descarga

**Problema: Archivo se descarga como `.txt` o `.html`**

**Solución:**
1. Borra el archivo descargado
2. Intenta Opción B (GitHub Raw)
3. Al guardar, cambia manualmente la extensión a `.ipynb`

**Problema: No encuentro el archivo descargado**

**Solución:**
- Windows: Verifica carpeta `C:\Users\[TuNombre]\Downloads`
- Mac: Verifica carpeta `/Users/[TuNombre]/Downloads`
- O busca en tu navegador: `Ctrl+J` (Chrome) para ver descargas

---

## PASO 2: SUBIR A GOOGLE COLAB (3 min)

### 🚀 Abrir Google Colab

**1. Abre tu navegador**

**2. Ve a:** [**colab.research.google.com**](https://colab.research.google.com)

**3. Inicia sesión con tu cuenta Gmail**
   - Si ya estás logueado, saltará directamente al Colab

---

### 📤 Subir el Notebook

**Verás esta pantalla de bienvenida:**

![Interfaz de Google Colab - Open Notebook](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/screenshots/Colab_Screen1.png)

*La interfaz te permite abrir notebooks desde diferentes fuentes: Recent, Google Drive, GitHub o Upload*

---

**4. Click en la pestaña "Upload"**

**5. Click en "Choose File" o arrastra el archivo .ipynb**

**6. Selecciona el archivo `Setup_y_Practica_Trading.ipynb` que descargaste**

**7. Espera 5-10 segundos** mientras Colab carga el notebook

**✅ Verificación:** Verás el notebook abierto con celdas de código y texto

---

### 🚨 Troubleshooting Upload

**Problema: Botón "Upload" no aparece**

**Solución:**
1. Verifica que estés logueado con Gmail
2. Cierra y vuelve a abrir [colab.research.google.com](https://colab.research.google.com)
3. Intenta en modo incógnito del navegador

**Problema: Upload tarda más de 30 segundos**

**Solución:**
- Verifica tu conexión a internet
- Intenta cargar desde Google Drive:
  1. Sube el `.ipynb` a tu Google Drive
  2. En Colab: pestaña "Google Drive" → busca el archivo

**Problema: Error "Failed to load notebook"**

**Solución:**
- El archivo puede estar corrupto
- Re-descarga desde GitHub (Opción B del Paso 1)

---

## PASO 3: SEGUIR EL NOTEBOOK PASO A PASO (5-10 min)

### 💡 El Notebook es Tu Guía

**El archivo `Setup_y_Practica_Trading.ipynb` contiene:**

✅ Instrucciones en español en cada sección  
✅ Código pre-escrito listo para ejecutar  
✅ Orden lógico de pasos numerados  
✅ Validación automática al final

---

### ▶️ Cómo Ejecutar Celdas

**Método 1 - Atajo de Teclado (Más Rápido):**
- Click en la celda de código
- Presiona `Shift + Enter`
- La celda se ejecuta y avanza a la siguiente

**Método 2 - Botón de Play:**
- Click en el ícono ▶️ a la izquierda de la celda
- Espera a que termine (verás un ✅ cuando complete)

**Método 3 - Menu:**
- `Runtime` → `Run all` (ejecuta TODAS las celdas de una vez)
- ⚠️ Solo usa esto si ya revisaste todo el notebook

---

### 📋 Secciones del Notebook

**El notebook tiene estas secciones (síguelas en orden):**

#### 1️⃣ Bienvenida y Verificación de Versiones
- **Qué hace:** Verifica que Colab funcione correctamente
- **Acción:** Ejecuta la celda
- **Output esperado:** Versiones de Python, pandas, numpy

---

#### 2️⃣ Instalación de Librerías
- **Qué hace:** Instala todas las herramientas necesarias
- **Acción:** Ejecuta la celda (tomará 2-3 minutos)
- **Output esperado:** Múltiples líneas de instalación, sin errores rojos al final

⚠️ **Advertencia:** Esta celda puede tardar. Es normal.

---

#### 3️⃣ Configuración de Broker (Alpaca)
- **Qué hace:** Conecta tu cuenta de paper trading
- **Acción:** 
  2. Copia tus API Keys
  3. Pega en la celda de código (reemplaza los placeholders)
  4. Ejecuta

**Output esperado:** `✅ Conexión exitosa con Alpaca Paper Trading`

---

#### 4️⃣ Descarga de Datos Históricos
- **Qué hace:** Descarga datos del S&P 500 (SPY) para practicar
- **Acción:** Ejecuta la celda
- **Output esperado:** Tabla con datos OHLCV de SPY

---

#### 5️⃣ Validación Final
- **Qué hace:** Verifica que todo esté configurado correctamente
- **Acción:** Ejecuta la celda
- **Output esperado:** 
```
✅ Python: OK
✅ Librerías: OK
✅ Broker: OK
✅ Datos: OK

🎉 Setup completado exitosamente
```

---

### 🚨 Troubleshooting Durante el Notebook

**Error: "ModuleNotFoundError"**
→ La celda de instalación no completó. Re-ejecuta la celda 2️⃣

**Error: "401 Unauthorized" (Alpaca)**
→ API Keys incorrectas. Verifica que copiaste bien y que sean de Paper Trading.

**Error: "Session crashed"**
→ Colab se quedó sin memoria. `Runtime → Restart runtime` y vuelve a empezar.

**Otros errores:**
→ Consulta [Troubleshooting Maestro](Troubleshooting_Maestro.md) - Hub central de soluciones

---

## ✅ VALIDACIÓN RÁPIDA

**Al terminar, verifica estos puntos:**

### Checklist Post-Setup

- [ ] **Colab funciona:** Puedo ejecutar celdas sin errores
- [ ] **Librerías instaladas:** Import de pandas, numpy, yfinance funciona
- [ ] **Broker conectado:** Validación muestra ✅ para Alpaca
- [ ] **Datos descargados:** Veo tabla con datos de SPY
- [ ] **Validación final:** Última celda muestra "Setup completado exitosamente"

**Si algún punto NO está marcado:**

1. Revisa el [Troubleshooting Express](#-troubleshooting-express) de esta misma guía
2. Consulta [Troubleshooting Maestro](Troubleshooting_Maestro.md) - Hub central
3. Contacta soporte: yismaryme@gmail.com

---

## 🚨 TROUBLESHOOTING EXPRESS

### Top 5 Errores Más Comunes

**1. "Runtime not connected"**
- **Causa:** Colab no está conectado a un servidor
- **Solución:** Click en "Connect" (arriba derecha)

---

**2. "ModuleNotFoundError: No module named 'yfinance'"**
- **Causa:** Instalación incompleta
- **Solución:** Re-ejecuta celda de instalación completa

---

**3. "401 Unauthorized" (Alpaca)**
- **Causa:** API Keys incorrectas o modo incorrecto (Live vs Paper)
- **Solución:** 
  1. Ve a Alpaca Dashboard
  2. Confirma estás en "Paper Trading" (no Live)
  3. Regenera API Keys
  4. Copia de nuevo (sin espacios extra)

---

**4. "Session crashed"**
- **Causa:** Sin memoria o timeout
- **Solución:** 
  1. `Runtime → Disconnect and delete runtime`
  2. `Runtime → Run all`

---

**5. "File not found" o "404 Error" al descargar datos**
- **Causa:** Ticker incorrecto o API temporalmente caída
- **Solución:** 
  1. Verifica ticker (debe ser "SPY" no "spy" ni "S&P500")
  2. Espera 5 minutos y re-intenta
  3. Prueba con otro ticker: "AAPL"

---

**Para más errores:** [Troubleshooting Maestro](Troubleshooting_Maestro.md) - Soluciones completas

---

## 🎯 PRÓXIMOS PASOS

### ✅ Setup Completado

**¡Felicitaciones! Terminaste el setup en tiempo récord.**

**Ahora tienes:**
- ✅ Google Colab funcionando
- ✅ Librerías instaladas
- ✅ Broker conectado
- ✅ Datos históricos descargados

---

### 🗓️ Antes de la Sesión 1

**Lee esto para prepararte:**

1. **Revisa los recursos:**
   - 📘 [Mapa de Recursos del Workshop](Mapa_Recursos_Workshop.md)
   - 📋 [Programa Detallado](Programa_Detallado_Workshop.md)

2. **Únete al grupo:**
   - 💬 Telegram: Recibirás invitación por email
   - 🔒 Grupo Premium: Para participantes pagos

3. **Opcional - Profundiza:**
   - 📚 [Mejores Prácticas del Setup A](Mejores_Practicas_Setup_A.md)
   - 🔍 [¿Necesitas más detalles? Guía Completa](Setup_A_Colab_Rapido.md)

---

### 🚀 ¡Listo Para Empezar!

**Próxima parada:** [Sesión 1 del Workshop](Programa_Detallado_Workshop.md)

---

## 🔗 VER TAMBIÉN

**Otras rutas de Setup A:**
- [Setup A: Colab Completo](Setup_A_Colab_Rapido.md) - Con explicaciones detalladas (30-45 min)
- [Setup A: Guiado](Setup_A_Guiado.md) - Exhaustivo paso a paso (60-90 min)

**Siguiente paso:**
- [Guía Setup Completa](Guia_Setup_Completa.md) - Hub de todos los setups

---

## 🧭 NAVEGACIÓN

**🏠 Inicio:** [README Principal](../README.md)  
**⬅️ Anterior:** [Setup A: Colab Completo](Setup_A_Colab_Rapido.md)  
**➡️ Siguiente:** [Programa Detallado](Programa_Detallado_Workshop.md)  
**⬆️ Categoría:** [Guía de Uso](GUIA_INICIO.md)

---

## 📞 SOPORTE

**Si algo no funcionó:**

📧 **Email:** yismaryme@gmail.com (Asunto: `[Setup A Express] - [Tu error]`)  
💬 **Telegram:** [@yismafx](https://t.me/yismafx)  
📚 **Troubleshooting:** [Troubleshooting Maestro](Troubleshooting_Maestro.md) - Hub central de soluciones

---

## 📌 VERSIÓN

**v3.1 (Noviembre 2025)** - Hotfix: Paths corregidos  
**Última actualización:** 16 de Noviembre de 2025

**Changelog:**
- v3.1: Hotfix paths Troubleshooting_Maestro (estaba apuntando a carpeta inexistente)
- v3.0: Simplificación de referencias troubleshooting (solo interno + Maestro)
- v2.1: Fix enlaces rotos (404)
- v2.0: Navegación cruzada Setup A
- v1.0: Versión inicial

---

**🎉 ¡Felicitaciones por completar el Setup Express!**

**Tiempo récord: 10-15 minutos. Ahora estás listo para el workshop. 🚀**
