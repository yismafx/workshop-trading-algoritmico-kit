# ✅ MEJORES PRÁCTICAS: SETUP A (GOOGLE COLAB)

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Setup_A_Colab_Rapido.md) > 📄 Mejores Prácticas**

---

**🎯 Objetivo:** Maximizar tu experiencia con Google Colab  
**👥 Para:** Participantes usando Setup A durante y después del workshop  
**📅 Última actualización:** 17 de noviembre de 2025  
**📌 Versión:** 3.0

---

## 📑 TABLA DE CONTENIDOS

- [Rutina Diaria/Semanal](#-rutina-diariasemanal)
- [Guardar Tu Trabajo](#-guardar-tu-trabajo)
- [Seguridad de API Keys](#-seguridad-de-api-keys)
- [Errores Comunes a Evitar](#-errores-comunes-a-evitar)
- [Checklist Pre-Sesión](#-checklist-antes-de-cada-sesión-del-workshop)
- [Tips Avanzados de Colab](#-tips-avanzados-de-google-colab)
- [Optimización de Rendimiento](#-optimización-de-rendimiento)
- [Gestión de Sesiones](#-gestión-de-sesiones-de-colab)

---

## 🔄 RUTINA DIARIA/SEMANAL

### Si Vuelves el Mismo Día

**Escenario:** Cerraste la pestaña de Colab, pero fue el mismo día (menos de 12 horas)

**✅ Qué hacer:**

1. **Abre tu notebook:**
   - Ve a [colab.research.google.com](https://colab.research.google.com)
   - Pestaña "Recent" → selecciona tu notebook
   
2. **Verifica la conexión:**
   - Arriba derecha: ¿Dice "Connected" o "Connect"?
   - Si dice "Connect" → click para reconectar
   
3. **NO necesitas reinstalar:**
   - Las librerías siguen instaladas
   - El ambiente persiste si fue menos de 12h
   
4. **Reconecta broker (opcional):**
   - Si vas a operar, ejecuta la celda de configuración del broker
   - Si solo vas a leer código, no es necesario

**⏱️ Tiempo:** 30 segundos

---

### Si Pasó Más de un Día (o >12 horas)

**Escenario:** Vuelves después de 24 horas o más

**✅ Qué hacer:**

1. **Abre el notebook** (igual que arriba)

2. **Reconecta al runtime:**
   - `Runtime → Reconnect` (si está desconectado)
   
3. **Re-ejecuta celda de instalación:**
   ```python
   # Celda de instalación de librerías
   !pip install yfinance pandas numpy...
   ```
   - **Por qué:** El ambiente se resetea cada 12 horas de inactividad
   - **Tiempo:** 2-3 minutos
   
4. **Re-ejecuta configuración de broker:**
   ```python
   # Celda con tus API Keys
   ALPACA_API_KEY = "..."
   ALPACA_SECRET_KEY = "..."
   ```
   
5. **Continúa normalmente**

**⏱️ Tiempo:** 3-5 minutos

---

### Si Pasó Más de una Semana

**Escenario:** Vuelves después de vacaciones o pausa larga

**✅ Qué hacer:**

1. **Verifica actualizaciones:**
   - Revisa si hay nueva versión del notebook en GitHub
   - Busca anuncios en el grupo de Telegram
   
2. **Considera descargar copia fresh:**
   - Baja el notebook actualizado del repo
   - Sube el nuevo a Colab
   - Transfiere tu código personal si lo hay
   
3. **Re-ejecuta TODO desde cero:**
   - `Runtime → Run all`
   - Valida que todo funcione con las últimas versiones de librerías

**⏱️ Tiempo:** 10-15 minutos

---

## 💾 GUARDAR TU TRABAJO

### Auto-Guardado de Colab

**✅ Buenas noticias:**
- Google Colab guarda automáticamente cada pocos segundos
- No necesitas hacer "Ctrl+S" constantemente

**Cómo verificar:**
1. Mira arriba del notebook
2. Busca el ícono de nube ☁️
3. Si dice "All changes saved" → ✅ Todo guardado
4. Si dice "Saving..." → ⏳ Espera unos segundos

---

### Descarga de Respaldo (Backup Local)

**⚠️ Importante:** Aunque Colab auto-guarda, SIEMPRE ten un backup local

**Cómo hacer backup:**

**Opción 1 - Download .ipynb (Recomendada):**
1. `File → Download → Download .ipynb`
2. Guárdalo en tu computadora
3. Renombra con fecha: `Setup_2025-11-15_v1.ipynb`

**Opción 2 - Save to GitHub:**
1. `File → Save a copy in GitHub`
2. Requiere: Conectar tu cuenta GitHub
3. Ventaja: Control de versiones automático

**Opción 3 - Save to Google Drive:**
1. `File → Save a copy in Drive`
2. Se guarda en tu Drive
3. Accesible desde cualquier dispositivo

---

### Crear Checkpoints (Versiones)

**¿Cuándo crear checkpoints?**
- Después de completar una sección importante
- Antes de hacer cambios grandes al código
- Al final de cada sesión del workshop

**Cómo:**
1. `File → Save a copy in Drive`
2. Renombra con convención clara:
   - `Setup_S1_Completado.ipynb`
   - `Setup_S5_ConMiEstrategia.ipynb`
   - `Setup_2025-11-15_Backup.ipynb`

**Beneficio:** Si algo se rompe, vuelves a una versión anterior

---

## 🔐 SEGURIDAD DE API KEYS

### ❌ NUNCA Hagas Esto

**1. Compartir notebook con keys visibles:**
```python
# ❌ MAL - API Keys en texto plano
ALPACA_API_KEY = "PKX3ABC123..."  # VISIBLE para quien vea el notebook
ALPACA_SECRET_KEY = "DEF456..."
```

**Riesgo:** Si compartes este notebook, expones tus keys

---

**2. Subir a GitHub público con keys:**
```python
# ❌ MAL - GitHub indexa esto
api_key = "mi_key_secreta_123"
```

**Riesgo:** Los bots de GitHub escanean keys y las roban en minutos

---

**3. Screenshots con keys visibles:**
```python
# ❌ MAL - Visible en pantalla compartida
print(f"Mi API Key: {ALPACA_API_KEY}")
```

**Riesgo:** Keys en Telegram, Discord, o captura de pantalla

---

### ✅ Mejores Prácticas de Seguridad

**1. Usa variables de entorno (Método Avanzado):**

```python
# ✅ BUENO - Keys almacenadas en Colab Secrets
from google.colab import userdata

ALPACA_API_KEY = userdata.get('ALPACA_KEY')
ALPACA_SECRET_KEY = userdata.get('ALPACA_SECRET')
```

**Cómo configurar:**
1. En Colab, click en el ícono de llave 🔑 (panel izquierdo)
2. `+ Add new secret`
3. Name: `ALPACA_KEY`, Value: [tu key]
4. Repite para `ALPACA_SECRET`

**Ventaja:** Keys no aparecen en el código

---

**2. Borra keys antes de compartir:**

```python
# ✅ BUENO - Placeholders antes de compartir
ALPACA_API_KEY = "TU_API_KEY_AQUI"
ALPACA_SECRET_KEY = "TU_SECRET_KEY_AQUI"
```

**Proceso:**
1. Antes de compartir notebook: Reemplaza keys con placeholders
2. Guarda
3. Comparte
4. Después: Vuelve a poner tus keys reales

---

**3. Si expusiste keys accidentalmente:**

**⚠️ ACCIÓN INMEDIATA:**

1. **Ve a tu broker AHORA:**
   - Alpaca: [app.alpaca.markets/paper/dashboard/overview](https://app.alpaca.markets/paper/dashboard/overview)
   - IB: TWS/Gateway → Account Settings

2. **Elimina las keys comprometidas:**
   - Alpaca: `Account → API Keys → Delete`
   - IB: Revoke API access

3. **Genera nuevas keys:**
   - Alpaca: `Generate new key`
   - Copia las nuevas
   
4. **Actualiza tu notebook** con las nuevas keys

5. **Verifica transacciones:**
   - Revisa si hubo operaciones no autorizadas
   - Contacta soporte del broker si hay actividad sospechosa

**Tiempo crítico:** Hazlo en menos de 5 minutos

---

## 🚫 ERRORES COMUNES A EVITAR

### Error #1: Cerrar Notebook Durante Sesiones

**❌ Lo que NO debes hacer:**
- Cerrar la pestaña de Colab mientras el instructor explica
- Apagar tu computadora con Colab abierto

**⚠️ Consecuencia:**
- Pierdes la sesión activa
- Tienes que reinstalar librerías
- Te retrasas vs. el resto de la clase

**✅ Lo que SÍ debes hacer:**
- Mantén Colab abierto en una pestaña durante TODA la sesión
- Si necesitas cerrar: Guarda todo primero (`File → Save`)
- Avisa al instructor que vas a desconectarte

---

### Error #2: Modificar Código Sin Entender

**❌ Lo que NO debes hacer:**
```python
# Código del instructor
data = yf.download("SPY", start="2020-01-01")

# Tú modificas sin entender:
data = yf.download("SPY123RANDOM", start="1990-99-99")  # ❌ Rompe todo
```

**⚠️ Consecuencia:**
- El código falla con errores crípticos
- No sabes cómo arreglarlo
- Pierdes tiempo

**✅ Lo que SÍ debes hacer:**
- Si quieres experimentar: **Crea una celda nueva** abajo
- Copia el código del instructor
- Modifica en la celda nueva
- Si falla, simplemente borra esa celda
- El código original queda intacto

---

### Error #3: Usar Live Trading Keys Por Error

**❌ Lo que NO debes hacer:**
```python
# ⚠️ PELIGRO - Keys de cuenta REAL (Live)
ALPACA_API_KEY = "PK_LIVE_ABC..."  # ← Esto es DINERO REAL
```

**⚠️ Consecuencia:**
- Puedes ejecutar operaciones con dinero real sin querer
- Pérdidas reales de capital

**✅ Lo que SÍ debes hacer:**
- SIEMPRE usa Paper Trading durante el workshop
- Verifica que tus keys digan "PAPER" no "LIVE"
- En Alpaca Dashboard: Asegúrate estar en modo "Paper" (arriba derecha)
- Live Trading: SOLO cuando termines el workshop Y valides todo

---

### Error #4: Ignorar los Errores

**❌ Lo que NO debes hacer:**
```python
# Sale un error rojo...
# "Meh, lo ignoro y sigo"
# [Ejecuta siguiente celda]
# [Todo falla en cascada]
```

**⚠️ Consecuencia:**
- Los errores se acumulan
- Terminas con ambiente roto
- Tienes que empezar de cero

**✅ Lo que SÍ debes hacer:**
1. **PARA cuando veas un error**
2. **Lee el mensaje de error** (última línea es la más importante)
3. **Consulta troubleshooting:** [Guía completa](Troubleshooting_Maestro.md)
4. **Pregunta en el grupo** si no encuentras solución
5. **Arregla el error** antes de continuar

---

### Error #5: No Hacer Backups

**❌ Lo que NO debes hacer:**
- Confiar 100% en el auto-guardado de Colab
- No descargar copias locales
- Trabajar semanas sin backup

**⚠️ Consecuencia:**
- Si Google tiene problemas: Pierdes todo
- Si borras algo por error: No hay manera de recuperar

**✅ Lo que SÍ debes hacer:**
- **Al final de cada sesión:** Descarga el notebook
- **Después de logros importantes:** Save a copy in Drive
- **Mensualmente:** Backup completo a tu computadora

---

## 🎓 CHECKLIST ANTES DE CADA SESIÓN DEL WORKSHOP

### Preparación 10 Minutos Antes

**Imprime esta checklist y úsala antes de CADA sesión:**

---

**🔌 AMBIENTE TÉCNICO**

- [ ] **Computadora cargada** (o conectada a corriente)
- [ ] **Internet estable** verificado ([fast.com](https://fast.com) > 3 Mbps)
- [ ] **Navegador actualizado** (Chrome preferiblemente)
- [ ] **Otras pestañas cerradas** (especialmente YouTube, Netflix)
- [ ] **Notificaciones desactivadas** (Focus mode en Windows/Mac)

---

**📓 COLAB Y NOTEBOOK**

- [ ] **Colab abierto** ([colab.research.google.com](https://colab.research.google.com))
- [ ] **Notebook cargado** (el del workshop, no uno viejo)
- [ ] **Runtime conectado** (dice "Connected" arriba derecha)
- [ ] **Celda de instalación ejecutada:**
  ```python
  !pip install yfinance pandas numpy...
  # Ejecutaste esto y terminó sin errores
  ```
- [ ] **Celda de configuración de broker ejecutada:**
  ```python
  # Tus API Keys configuradas
  ALPACA_API_KEY = "..."
  ```

---

**✅ VALIDACIÓN**

- [ ] **Celda de validación ejecutada** (muestra ✅ para todo)
  ```
  ✅ Python: OK
  ✅ Librerías: OK
  ✅ Broker: OK
  ✅ Datos: OK
  ```
- [ ] **Test de descarga de datos:**
  ```python
  import yfinance as yf
  data = yf.download("SPY", start="2024-01-01", end="2024-01-10")
  print(data.head())  # ✅ Muestra tabla sin errores
  ```

---

**📚 MATERIALES**

- [ ] **Papel y lápiz listos** (para tomar notas)
- [ ] **Notebook Maestro abierto** en otra pestaña (para referencia)
- [ ] **Prompts Library accesible** ([GitHub link](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY))
- [ ] **Grupo de Telegram abierto** (para consultas rápidas)

---

**🧘 MENTALIDAD**

- [ ] **15 minutos de buffer** (llegaste temprano, no apurado)
- [ ] **Café/agua al lado** (hidratación)
- [ ] **Postura cómoda** (vas a estar 3 horas)
- [ ] **Actitud de aprendizaje** (las preguntas son bienvenidas)

---

**⏱️ Tiempo total:** 10 minutos de prep = 3 horas sin interrupciones

**🎯 Objetivo:** Empezar la sesión 100% listo, sin perder tiempo en setup

---

## 💡 TIPS AVANZADOS DE GOOGLE COLAB

### Atajos de Teclado Útiles

**Navegación:**
- `Ctrl + M, H` → Mostrar todos los atajos
- `Ctrl + M, A` → Insertar celda arriba
- `Ctrl + M, B` → Insertar celda abajo
- `Ctrl + M, D` → Eliminar celda actual
- `Ctrl + M, Y` → Convertir celda a código
- `Ctrl + M, M` → Convertir celda a markdown (texto)

**Ejecución:**
- `Shift + Enter` → Ejecutar celda y avanzar
- `Ctrl + Enter` → Ejecutar celda sin avanzar
- `Alt + Enter` → Ejecutar celda e insertar nueva abajo

**Edición:**
- `Ctrl + /` → Comentar/descomentar línea
- `Ctrl + ]` → Indentar
- `Ctrl + [` → Des-indentar
- `Ctrl + F` → Buscar en el notebook

---

### Modo Oscuro (Dark Mode)

**Cómo activar:**
1. `Tools → Settings`
2. `Site → Theme`
3. Selecciona "Dark"

**Beneficio:** Menos cansancio visual en sesiones largas

---

### Conectar a Google Drive

**¿Para qué?**
- Guardar/cargar archivos grandes
- Trabajar con datasets propios
- Persistencia de datos entre sesiones

**Cómo:**
```python
from google.colab import drive
drive.mount('/content/drive')

# Ahora puedes acceder a tus archivos:
# /content/drive/MyDrive/[tus carpetas]
```

**Verás:** Popup pidiendo permiso para acceder a Drive → Click "Allow"

---

### Usar GPU/TPU (Opcional - Avanzado)

**¿Cuándo usar?**
- Machine Learning pesado
- Backtesting de miles de estrategias simultáneas
- Optimización de parámetros con fuerza bruta

**Cómo activar:**
1. `Runtime → Change runtime type`
2. `Hardware accelerator → GPU` o `TPU`
3. Click "Save"

**⚠️ Advertencia:** 
- GPU/TPU tienen límite de uso mensual
- No necesario para el workshop básico
- Usa solo si sabes lo que haces

---

### Snippets de Código Pre-Guardados

**Cómo usar:**
1. Click en el ícono `<>` (panel izquierdo)
2. Busca snippets útiles:
   - "Load data from Drive"
   - "Download file from web"
   - "Display DataFrame as table"
3. Click para insertar en el notebook

**Beneficio:** Código probado, listo para usar

---

## ⚡ OPTIMIZACIÓN DE RENDIMIENTO

### Si Colab Va Lento

**Problema:** Celdas tardan mucho en ejecutar

**Soluciones:**

**1. Limpia la RAM:**
```python
# Libera memoria no usada
import gc
gc.collect()
```

**2. Cierra variables grandes no necesarias:**
```python
# Si ya no necesitas un DataFrame enorme:
del dataframe_gigante
gc.collect()
```

**3. Verifica uso de RAM:**
```python
# Ve cuánta RAM estás usando
!free -h
```

**4. Reinicia el runtime:**
- `Runtime → Restart runtime`
- Re-ejecuta solo lo necesario

---

### Evita Cargar Datos Repetitivamente

**❌ Ineficiente:**
```python
# Cada vez que ejecutas esta celda, re-descarga
data = yf.download("SPY", start="2000-01-01", end="2024-01-01")  # ← 24 años!
```

**✅ Eficiente:**
```python
# Descarga una vez, guarda en variable
if 'data' not in locals():
    data = yf.download("SPY", start="2000-01-01", end="2024-01-01")
    print("Datos descargados")
else:
    print("Usando datos existentes")
```

**Beneficio:** Ahorra tiempo y ancho de banda

---

## 🕐 GESTIÓN DE SESIONES DE COLAB

### Límites de Colab (Gratis)

**Debes saber:**
- **12 horas máximo** de runtime continuo
- **12 horas de inactividad** = desconexión automática
- **Límite de RAM:** ~12 GB (puede variar)
- **Límite de uso:** ~100 GPU hours/mes (si usas GPU)

**Después del límite:** "You have been using Colab for a while..."

---

### Cómo Extender Tu Sesión

**1. Mantén actividad:**
- Ejecuta celdas periódicamente
- Abre/cierra celdas
- Mueve el mouse en el notebook

**2. Evita operaciones largas sin supervisión:**
- No dejes corriendo backtests de 6 horas
- Mejor: Divide en chunks de 1 hora

**3. Colab Pro (Pago - Opcional):**
- $10/mes
- Runtimes más largos (24h)
- Más RAM (hasta 52 GB)
- Prioridad en GPUs
- **Evalúa:** Solo si usas Colab intensivamente

---

### Cuando Se Acabe Tu Sesión

**Escenario:** Llegas al límite de 12 horas

**Qué hacer:**
1. **Guarda todo:** `File → Save`
2. **Descarga backup:** `File → Download .ipynb`
3. **Espera 5-10 minutos**
4. **Reconecta:** `Runtime → Disconnect → Connect`
5. **Re-ejecuta:** Celda de instalación → Configuración → Continúa

**No pierdes:** 
- ✅ El código (guardado en Drive)
- ✅ Tus notas (en celdas markdown)

**Sí pierdes:**
- ❌ Variables en memoria
- ❌ Datos cargados
- ❌ Librerías instaladas

**Por eso:** Siempre guarda datasets importantes en Drive o descarga local

---

## 🎯 RESUMEN: Top 10 Reglas de Oro

**Memoriza estas 10 reglas:**

1. **📝 Guarda frecuentemente** (aunque sea auto, descarga backups)
2. **🔐 Nunca compartas API Keys** (usa variables de entorno)
3. **⏸️ Para cuando veas errores** (no los ignores)
4. **📋 Usa el checklist pre-sesión** (10 min antes de cada clase)
5. **📓 Mantén Colab abierto** durante sesiones del workshop
6. **🧪 Experimenta en celdas nuevas** (no modifiques el código del instructor)
7. **💾 Backups, backups, backups** (local + Drive + GitHub)
8. **🕐 Conoce los límites de Colab** (12h runtime, 12h inactividad)
9. **📚 Lee troubleshooting primero** antes de preguntar
10. **🚀 Paper Trading SIEMPRE** durante el aprendizaje

---

## 🔗 NAVEGACIÓN

**◀️ Anterior:** [Setup A: Colab Rápido](Setup_A_Colab_Rapido.md)  
**▶️ Siguiente:** [Troubleshooting Maestro](Troubleshooting_Maestro.md)

**🏠 Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**📖 Ver también:**
- [Setup A: Express](Setup_A_Express.md)
- [Setup A: Guiado](Setup_A_Guiado.md)
- [Checklist Implementación](Checklist_Implementacion_Setup_A.md)
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
