# ⚡ SETUP A: COLAB RÁPIDO (EXPRESS)

**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > ⚙️ [Setup](Guia_Setup_Completa.md) > 📄 Setup Colab Rápido**

---

**⏱️ Tiempo:** 10-15 min | **Dificultad:** ⭐ Fácil | **Requiere:** Navegador + Gmail  
**📊 Satisfacción:** ⭐⭐⭐⭐⭐ 4.7/5 | **Uso:** 8 de cada 10 participantes  
**📅 Última actualización:** Noviembre 2025 | **Versión:** 6.0

---

## 📑 TABLA DE CONTENIDOS

### ⚡ Atajos Inteligentes
- [🚀 **Empezar YA** - Ruta Express 10 min](#-ruta-express-10-15-minutos)
- [🔑 **Obtener API Keys** de Alpaca](#-configurar-broker)
- [❌ **Tengo un error AHORA**](#-troubleshooting-crítico)
- [📖 **Necesito más explicación**](#-necesitas-más-explicación-guía-paso-a-paso)

### 📖 Contenido Principal
1. [¿Qué Vas a Lograr?](#-qué-vas-a-lograr-en-este-setup)
2. [¿Es Este Setup Para Ti?](#-es-este-setup-para-ti)
3. [Requisitos Mínimos](#-requisitos-mínimos)
4. [⚡ Ruta Express (10-15 min)](#-ruta-express-10-15-minutos)
5. [🔗 Configurar Broker](#-configurar-broker)
6. [🗺️ Recursos del Workshop](#️-recursos-del-workshop)
7. [🚨 Troubleshooting Crítico](#-troubleshooting-crítico)
8. [✅ Mejores Prácticas](#-mejores-prácticas-críticas)
9. [🎯 Próximos Pasos](#-próximos-pasos)

### 🔗 Guías Complementarias
- [📘 Setup Express Completo](Setup_A_Express.md) - Versión detallada 10-15 min
- [📚 Setup Guiado Paso a Paso](Setup_A_Guiado.md) - Versión exhaustiva 30-60 min
- [🔑 Configurar Alpaca](Setup_A_Broker_Alpaca.md) - Guía especializada broker
- [🏦 Configurar Interactive Brokers](Setup_A_Broker_IB.md) - Guía especializada broker
- [✅ Mejores Prácticas Completas](Mejores_Practicas_Setup_A.md) - Tips de uso continuo
- [🚨 Troubleshooting Completo](Troubleshooting_Setup_A.md) - 50+ errores resueltos
- [🗺️ Mapa de Recursos](Mapa_Recursos_Workshop.md) - Hub central del workshop

---

## 🧭 NOTA: ¿Por Qué Python Primero?

> **TL;DR:** Python es el "lenguaje universal" del trading algorítmico.  
> Lo aprendes UNA VEZ, lo usas en TODAS las plataformas.  
> En Sesión 7, IA Generativa traduce tu código Python → TradingView/MetaTrader.

**📖 Explicación completa:** [Filosofía Python Primero (README)](../README.md#-filosofía-python-primero)

---

## ⚠️ MEJORES PRÁCTICAS CRÍTICAS

**Antes de continuar, lee esto (2 minutos):**

📘 **[Mejores Prácticas del Setup A →](Mejores_Practicas_Setup_A.md)**

**Top 3 errores que debes evitar:**
1. ❌ Cerrar el notebook durante las sesiones del workshop
2. ❌ Usar Live Trading keys en lugar de Paper Trading
3. ❌ Ignorar los errores sin consultar troubleshooting

**✅ Checklist pre-sesión (úsala antes de cada workshop):**
- [ ] Abrir notebook 10 min antes
- [ ] Ejecutar celda de instalación
- [ ] Ejecutar celda de configuración broker
- [ ] Validar que todo muestre ✅ OK

---

## 🎯 ¿QUÉ VAS A LOGRAR EN ESTE SETUP?

Al completar esta guía, tendrás:

✅ **Google Colab configurado** y funcionando  
✅ **Notebook personal de práctica** creado  
✅ **Librerías de trading** instaladas y validadas  
✅ **Conexión a broker** (Alpaca o Interactive Brokers) configurada  
✅ **Primer dataset histórico** descargado (SPY 2020-2024)  
✅ **Entorno 100% funcional** para el workshop

---

## 🎯 ¿ES ESTE SETUP PARA TI?

### ✅ Este Setup es PERFECTO si:

- 📊 Eres **trader profesional** con años de experiencia en mercados
  
- ❌ **NO tienes** experiencia programando
  - **¿Qué significa?** Nunca has escrito código en ningún lenguaje
  - **¿Es normal?** ✅ Sí, 7 de cada 10 participantes están en esta situación
  - **¿Puedo hacer el workshop igual?** ✅ Absolutamente, está diseñado para ti

- ✅ Prefieres **aprender primero, automatizar después**

- ❌ **NO quieres** instalar programas en tu computadora
  - **Ventaja:** Todo funciona en el navegador
  - **Sin instalaciones** complejas de Python, librerías, o IDEs

- ✅ Quieres empezar a **practicar HOY** (en menos de 1 hora)

- ✅ Tienes conexión a **internet estable**
  - **¿Cuánto necesito?** Mínimo 3 Mbps
  - **¿Cómo verifico?** Visita [fast.com](https://fast.com)

- ✅ Tienes o puedes crear una **cuenta Gmail**
  - **¿Por qué Gmail?** Google Colab requiere cuenta Google
  - **¿Cómo creo una?** [Crear cuenta Gmail](https://accounts.google.com/signup)

### ❌ Este Setup NO es Ideal si:

- 🚀 Ya necesitas sistemas funcionando **24/7 en producción**  
  → Ve a [Setup B: Python Local ⚠️ v2.2](Setup_B_Python_Local.md)
  - **Estado:** 🟡 En desarrollo (disponible en v2.2 - Diciembre 2025)
  - **Mientras tanto:** Usa Setup A, migrarás después
  
- 📊 Usas principalmente **MetaTrader** y quieres empezar ahí  
  → Ve a [Setup C: MetaTrader 5 ⚠️ v2.3](Setup_C_MetaTrader5.md)
  - **Estado:** 🟡 En desarrollo (disponible en v2.3 - Enero 2026)
  - **Mientras tanto:** Usa Setup A y aprende a traducir código (Sesión 7)
  
- 💼 Ya tienes cuenta en **Interactive Brokers** y quieres máxima integración  
  → Ve a [Setup D: Interactive Brokers ⚠️ v2.4](Setup_D_Interactive_Brokers.md)
  - **Estado:** 🟡 En desarrollo (disponible en v2.4 - Febrero 2026)
  - **Mientras tanto:** Usa Setup A + [Guía IB](Setup_A_Broker_IB.md)

### 📊 Estadística del Workshop:

> 🎯 **8 de cada 10 participantes** usan este setup exitosamente  
> ⭐ **Satisfacción:** 4.7/5.0 según feedback de cohortes anteriores  
> ⏱️ **Tiempo promedio real:** 12 minutos (no los 30-60 que toma la guiada)

---

## ✅ REQUISITOS MÍNIMOS

### 💻 Hardware (Tu Equipo)

**Necesitas:**

- ✅ **Cualquier computadora** con internet (Mac, Windows, o Linux)
  - **¿Mi laptop vieja funciona?** Probablemente sí, si tiene 5 años o menos
  - **¿Funciona en tablet?** No recomendado, mejor usar computadora
  
- ✅ **Conexión a internet estable**
  - **¿Cuánto necesito?** Mínimo 3 Mbps (para streaming de video del workshop)
  - **¿Cómo verifico mi velocidad?** Visita [fast.com](https://fast.com) en tu navegador
  - **¿Qué pasa si es más lenta?** Puedes seguir, pero videos pueden pausarse
  - **Tip:** Cierra otras pestañas que usen internet (Netflix, YouTube, etc.)
  
- ✅ **RAM: 4 GB recomendado** (2 GB funciona, pero más lento)
  - **¿Cómo verifico mi RAM?**
    - **Windows:** Click derecho en "Este equipo" → Propiedades
    - **Mac:** Apple menu → About This Mac
    - **Linux:** Comando `free -h` en terminal

**NO necesitas:**
- ❌ Computadora potente o cara
- ❌ Instalar programas complejos
- ❌ Configurar entornos virtuales

### 🌐 Software (Programas)

**Necesitas:**

- ✅ **Navegador web moderno:**
  
  - ✅ **Google Chrome 90+** ⭐ *Recomendado*
    - **¿Por qué Chrome?** Google Colab funciona mejor en Chrome (son de Google)
    - **¿Tengo Chrome?** Abre Chrome y ve a `chrome://version`
    - **¿No tengo Chrome?** Descarga gratis desde [google.com/chrome](https://www.google.com/chrome)
    - **¿Qué versión necesito?** 90 o superior (cualquier Chrome de 2021-2025 funciona)
  
  - ✅ **Firefox 88+** (alternativa)
    - Funciona bien, pero algunos atajos de teclado pueden diferir
    - Verifica versión: Menu → Help → About Firefox
  
  - ✅ **Safari 14+** (solo Mac)
    - Funciona aceptablemente, Chrome es mejor
  
  - ✅ **Edge 90+** (Windows)
    - Basado en Chromium, funciona similar a Chrome

- ✅ **Cuenta Gmail:**
  - **¿Ya tengo Gmail?** → ✅ Listo, continúa
  - **¿No tengo Gmail?** → Crearemos en 5 minutos
    - Ve a [accounts.google.com/signup](https://accounts.google.com/signup)
    - Sigue los pasos (nombre, contraseña, verificación)
  - **¿Puedo usar cuenta de trabajo/universidad?** Sí, si es cuenta Google

**NO necesitas:**
- ❌ Python instalado en tu computadora
- ❌ IDEs o editores de código (VSCode, PyCharm, etc.)
- ❌ Terminal o línea de comandos
- ❌ Git o control de versiones

### 🧠 Conocimientos

**Lo que SÍ necesitas saber:**
- ✅ Usar un navegador web
  - Abrir pestañas
  - Hacer click en enlaces
  - Descargar archivos
  
- ✅ Enviar y recibir emails
  
- ✅ Fundamentos de trading (esto ya lo dominas)
  - Stop-loss, take-profit
  - Gestión de riesgo
  - Mercados y activos

**Lo que NO necesitas saber:**
- ❌ Programación (cero código antes del workshop es OK)
- ❌ Python o ningún otro lenguaje
- ❌ Git, GitHub, o control de versiones
- ❌ Terminal, línea de comandos, o bash
- ❌ Matemáticas avanzadas o estadística

---

## ⚡ RUTA EXPRESS (10-15 minutos)

**🎯 Para traders con prisa o experiencia en notebooks**

### 📥 Resumen de 3 Pasos

**1. Descargar Notebook**
- Click derecho → Guardar enlace como
- [Setup_y_Practica_Trading.ipynb](https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/00_GUIA_DE_USO/Setup_y_Practica_Trading.ipynb)

**2. Subir a Google Colab**
- Abre [colab.research.google.com](https://colab.research.google.com)
- File → Upload notebook
- Selecciona el archivo .ipynb

**3. Ejecutar celdas**
- Sigue instrucciones en el notebook
- Ejecuta celda por celda (Shift+Enter)
- Valida al final

---

### 📖 ¿Necesitas Más Detalles?

**Guía Express Completa con screenshots y troubleshooting:**

📘 **[Setup Express Completo (15-20 min) →](Setup_A_Express.md)**

**Incluye:**
- ✅ Troubleshooting de descarga del notebook
- ✅ Screenshots de cada paso en Colab
- ✅ Qué hacer si el upload falla
- ✅ Cómo navegar por el notebook
- ✅ Validación paso a paso

---

## 📖 ¿NECESITAS MÁS EXPLICACIÓN? GUÍA PASO A PASO

**¿La Ruta Express fue muy rápida?**

Tenemos una guía detallada que explica CADA paso con screenshots, nivel de detalle extremo, y troubleshooting integrado.

**📚 [Ir a Guía Paso a Paso Completa (30-60 min) →](Setup_A_Guiado.md)**

**Incluye:**
- ✅ **Paso 1:** Acceder a Google Colab (crear cuenta Gmail, abrir Colab)
- ✅ **Paso 2:** Crear tu notebook personal (subir archivo, verificar)
- ✅ **Paso 3:** Instalar librerías (qué es cada una, por qué la necesitas)
- ✅ **Paso 4:** Configurar broker → **[Ver guías especializadas ↓](#-configurar-broker)**
- ✅ **Paso 5:** Descargar primer dataset (SPY histórico, validación)
- ✅ **Paso 6:** Validación final completa (checklist automatizado)

**⏱️ Tiempo:** 30-60 min | **Nivel detalle:** Extremo (para no-programadores)

---

## 🔗 CONFIGURAR BROKER

**Elige tu broker para paper trading (cuentas de práctica gratis):**

### Opción A: Alpaca (⭐ Recomendada para principiantes)

**Ventajas:** 
- Setup en 10 min
- API simple y bien documentada
- Multi-asset (stocks, crypto)
- Sin mínimo de depósito

**📘 [Guía Completa: Setup Broker Alpaca →](Setup_A_Broker_Alpaca.md)**

**Incluye:**
- Crear cuenta Alpaca Paper Trading
- Obtener API Keys (paso a paso con screenshots)
- Configurar en Python/Colab
- Validar conexión
- Troubleshooting errores comunes de Alpaca

**⏱️ Tiempo:** 10-15 min | **Dificultad:** ⭐ Fácil

---

### Opción B: Interactive Brokers (Avanzado)

**Ventajas:** 
- Acceso a mercados globales
- Datos profesionales de calidad
- Comisiones muy bajas
- Plataforma institucional

**⚠️ Requiere:** 
- Más tiempo (30-60 min)
- Aprobación de cuenta (24-48h)
- Conocimientos técnicos intermedios

**📘 [Guía Completa: Setup Broker Interactive Brokers →](Setup_A_Broker_IB.md)**

**Incluye:**
- Registro en IB Paper Trading
- Instalar IB Gateway o TWS
- Configurar ib_insync
- Validar conexión
- Troubleshooting errores comunes de IB

**⏱️ Tiempo:** 30-60 min | **Dificultad:** ⭐⭐⭐ Alta

---

**💡 Recomendación del Instructor:**  
Usa **Alpaca durante el workshop**. Es más rápido y simple.  
Puedes migrar a Interactive Brokers después si necesitas mercados globales.

---

## 🗺️ RECURSOS DEL WORKSHOP

**Ahora que tienes el setup listo, explora los recursos del workshop:**

📚 **[Mapa Completo de Recursos →](Mapa_Recursos_Workshop.md)**

**Recursos disponibles:**
- 📓 **Colab Notebook Maestro** - Código de las 9 sesiones
- 📦 **Template Pack** - Strategy Memo, Backtesting Report, README técnico
- 🤖 **Prompts Library** - 35+ prompts probados para GenAI
- 🐍 **Scripts Auxiliares** - Utilidades Python reutilizables
- 📖 **Documentación** - Glosario, FAQ, Troubleshooting

**🎯 Próximo paso:** [Revisar el Programa Detallado](Programa_Detallado_Workshop.md)

---

## 🚨 TROUBLESHOOTING CRÍTICO

**Si tienes un error AHORA, aquí están los 3 más comunes:**

### Error 1: "ModuleNotFoundError: No module named 'yfinance'"

**Síntoma:** Al ejecutar `import yfinance` aparece este error.

**Causa:** Las librerías no se instalaron correctamente.

**Solución rápida:**
```python
!pip install --upgrade yfinance pandas numpy
```
Luego reinicia el runtime: `Runtime → Restart runtime`

**📘 [Solución completa →](Troubleshooting_Setup_A.md#1-modulenotfounderror-no-module-named-yfinance)**

---

### Error 2: "alpaca_trade_api.rest.APIError: 401 Unauthorized"

**Síntoma:** Al conectar con Alpaca sale error 401.

**Causa:** API Keys incorrectas, expiradas, o usando keys de Live en lugar de Paper.

**Solución rápida:**
1. Ve a [Alpaca Dashboard](https://app.alpaca.markets/paper/dashboard/overview)
2. **Verifica que estés en modo "Paper Trading"** (arriba derecha)
3. Regenera tus API Keys: `Account → API Keys → Regenerate`
4. Copia y pega de nuevo en el notebook (asegúrate copiar TODA la key)

**📘 [Solución completa →](Troubleshooting_Setup_A.md#2-alpaca_trade_apirestapierror-401-unauthorized)**

---

### Error 3: "Session crashed" / "Your session crashed for an unknown reason"

**Síntoma:** Pantalla blanca en Colab con mensaje de sesión caída.

**Causa:** Colab se quedó sin memoria (RAM) o timeout por inactividad.

**Solución rápida:**
1. `Runtime → Disconnect and delete runtime`
2. `Runtime → Run all` (volver a ejecutar todo desde el inicio)
3. **Importante:** Ejecuta las celdas más despacio, una por una

**📘 [Solución completa →](Troubleshooting_Setup_A.md#3-session-crashed--your-session-crashed-for-an-unknown-reason)**

---

**¿Otro error?** → **[Troubleshooting Completo (50+ errores resueltos) →](Troubleshooting_Setup_A.md)**

---

## 🎯 PRÓXIMOS PASOS

### ✅ Has Completado el Setup A

**¡Felicitaciones! Ahora tienes:**

✅ Google Colab configurado y funcionando  
✅ Notebook personal de práctica creado  
✅ Librerías de trading instaladas y validadas  
✅ Conexión a broker establecida (Alpaca o IB)  
✅ Capacidad de descargar datos históricos  
✅ Entorno 100% listo para el workshop

---

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
   - [ ] Mira [video tutorial de Colab](https://www.youtube.com/watch?v=inN8seMm7UI)
   - [ ] Experimenta creando celdas nuevas
   - [ ] Prueba ejecutar código simple (ej: `print("Hola")`)

---

### 📚 Lecturas Previas Opcionales

**Si quieres adelantar teoría (NO obligatorio):**

- 📖 Chan, E. (2013). "Algorithmic Trading", Capítulos 1-2
- 📖 Carver, R. (2015). "Systematic Trading", Introducción
- 📖 López de Prado, M. (2018). "Advances in Financial ML", Prefacio

**NO es obligatorio leer nada antes del workshop.** Todo se explicará desde cero.

---

### 🔗 Explora Otros Setups (Opcional)

**Si quieres ver alternativas para después:**

- 📄 [Setup B: Python Local ⚠️ v2.2](Setup_B_Python_Local.md) - Para deployment 24/7
- 📄 [Setup C: MetaTrader 5 ⚠️ v2.3](Setup_C_MetaTrader5.md) - Para usuarios de MT5
- 📄 [Setup D: Interactive Brokers ⚠️ v2.4](Setup_D_Interactive_Brokers.md) - Para máxima integración

**Recomendación:** Mantén este Setup A como principal durante el workshop.  
Los otros setups son para después, cuando ya domines los fundamentos.

---

## 🧭 NAVEGACIÓN

**🏠 Inicio:** [README Principal](../README.md)  
**⬅️ Anterior:** [Guía de Setup Completa](Guia_Setup_Completa.md)  
**➡️ Siguiente:** [Programa Detallado Workshop](Programa_Detallado_Workshop.md)  
**⬆️ Categoría:** [Guía de Uso](GUIA_INICIO.md)

---

## 📞 SOPORTE Y CONTACTO

### 🆘 Si Necesitas Ayuda

**Antes de contactar, intenta:**

1. ✅ Revisar el [Troubleshooting Crítico](#-troubleshooting-crítico) de este documento
2. ✅ Consultar el [Troubleshooting Completo](Troubleshooting_Setup_A.md)
3. ✅ Buscar en el grupo de Telegram (probablemente alguien tuvo el mismo problema)
4. ✅ Reiniciar el runtime de Colab (`Runtime → Disconnect and delete runtime`)

**Si el problema persiste:**

### 📧 Email

**Asunto:** `[Setup A] - [Tu problema en 5 palabras]`  
**Email:** yismaryme@gmail.com  
**Tiempo de respuesta:** 24-48 horas

**Incluye en tu email:**
1. Descripción del problema (¿qué intentabas hacer?)
2. Qué paso estabas siguiendo (número de paso o sección)
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

### ❓ FAQ - Preguntas Frecuentes

**P: ¿Cuánto tiempo dura el setup?**  
R: Ruta Express: 10-15 min. Ruta Guiada: 30-60 min (depende del broker)

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

**v6.0 (Noviembre 2025)** - Arquitectura modular refactorizada  
**Última actualización:** 15 de Noviembre de 2025

**Changelog:**
- **v6.0 (Nov 15, 2025):** Refactorización modular completa
  - Separado en 8 archivos especializados
  - Troubleshooting movido a archivo dedicado
  - Brokers en guías separadas
  - Quick Links agregados
  - Nivel de detalle extremo implementado
  - Reducción 81% en tamaño del archivo (de 2,675 a 585 líneas)
- **v5.3 (Nov 2025):** Versión limpia y enfocada
- **v5.0 (Nov 2025):** Integración con recursos del workshop

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

[Fin del documento - Setup A v6.0 Modular]
