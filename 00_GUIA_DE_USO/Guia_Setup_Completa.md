# 🛠️ GUÍA DE SETUP COMPLETA

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 **Guía de Setup Completa**

---

**⏱️ Tiempo de lectura:** 5 minutos  
**📅 Última actualización:** 17 de noviembre de 2025  
**📌 Versión:** 3.0

---

## 🎯 Elige Tu Setup

**Tenemos 3 opciones de setup disponibles para el workshop:**

Cada setup está diseñado para un perfil específico de participante. La mayoría (80%) usará **Setup A: Google Colab + Alpaca** por su simplicidad y rapidez.

**¿No estás seguro cuál elegir?** Usa la tabla comparativa abajo para decidir en 2 minutos.

---

## 📊 Tabla Comparativa

| Setup | ⏱️ Tiempo | 💻 Python | 🚀 Deploy 24/7 | 🌎 Mercados | 👥 Ideal Para |
|-------|----------|----------|---------------|-------------|---------------|
| **🎯 A: Colab + Alpaca** | 30-45 min | ❌ No | ❌ No | Multi-asset | **80% participantes** ⭐ |
| **💻 B: Python Local** | 2-3h | ✅ Sí | ✅ Sí | Multi-asset | Bot 24/7 en Producción |
| **📊 C: MetaTrader 5** | 1-2h | ⚠️ Básico | ✅ Sí | Forex/CFDs | Traders Forex |

**💡 Regla simple:**  
Si no tienes Python instalado o no sabes si lo tienes → **Elige Setup A**

**📖 ¿Necesitas comparativa más detallada?**  
Ver: [GUIA_INICIO - Sección Stack Tecnológico](GUIA_INICIO.md#️-stack-tecnológico-del-workshop)

---

## 🚀 Setup A: Google Colab + Alpaca

### 🎯 Descripción

**Setup 100% en la nube - No instalas nada localmente**

Usa Google Colab (navegador) + broker Alpaca (paper trading gratuito) para ejecutar todo el contenido del workshop sin configurar Python en tu computadora.

### ✅ Ideal Si...

- ✅ No tienes experiencia con Python
- ✅ Quieres empezar rápido (30-45 min)
- ✅ Tu objetivo es aprender/backtest (no deploy inmediato)
- ✅ Trabajas desde múltiples dispositivos

### 📋 Características

- **Tiempo:** 30-45 min (versión estándar)
- **Costo:** $0 USD
- **Requisitos:** Solo cuenta Google + navegador
- **Mantenimiento:** Bajo (Google gestiona todo)

### 🔀 3 Variantes Disponibles

Elige según tu preferencia de detalle:

| Variante | Tiempo | Target |
|----------|--------|--------|
| **⚡ [Express](Setup_A_Express.md)** | 10-15 min | Usuarios con prisa |
| **📚 [Completo](Setup_A_Colab_Rapido.md)** | 30-45 min | **Recomendado** ⭐ |
| **📖 [Guiado](Setup_A_Guiado.md)** | 60-90 min | Principiantes absolutos |

### 🎯 Empezar Setup A

**👉 [IR A SETUP A: COLAB COMPLETO →](Setup_A_Colab_Rapido.md)** ⭐ RECOMENDADO

O elige tu variante favorita arriba ↑

---

## 💻 Setup B: Python Local

### 🎯 Descripción

**Setup con Python instalado localmente en tu computadora**

Instala Python, Jupyter Lab, y todas las librerías para desarrollo profesional y deployment 24/7 en VPS.

### ✅ Ideal Si...

- ✅ Ya sabes Python y manejas terminal
- ✅ Planeas deployar bots en producción 24/7
- ✅ Necesitas control total del ambiente
- ✅ Tienes tiempo para setup más complejo

### 📋 Características

- **Tiempo:** 2-3 horas
- **Costo:** $0 (software) + VPS opcional
- **Requisitos:** Conocimientos Python intermedio
- **Mantenimiento:** Alto (actualizaciones manuales)

### 🛠️ Lo Que Incluye

- ✅ Instalación Python 3.11+ (Anaconda o directo)
- ✅ Ambiente virtual configurado
- ✅ 20+ librerías instaladas (pandas, alpaca-py, etc.)
- ✅ Jupyter Lab configurado
- ✅ Scripts de validación

### 🎯 Empezar Setup B

**👉 [IR A SETUP B: PYTHON LOCAL →](Setup_B_Python_Local.md)**

---

## 📊 Setup C: MetaTrader 5

### 🎯 Descripción

**Setup enfocado en traders de Forex/CFDs con MetaTrader 5**

Integra Python con MetaTrader 5 para automatizar estrategias en mercados Forex/CFDs con brokers que soporten MT5.

### ✅ Ideal Si...

- ✅ Operas principalmente Forex o CFDs
- ✅ Ya usas (o quieres usar) MetaTrader 5
- ✅ Tu broker soporta MT5
- ✅ Quieres combinar análisis Python + ejecución MT5

### 📋 Características

- **Tiempo:** 1-2 horas
- **Costo:** $0 (MT5 es gratuito)
- **Requisitos:** Python básico + broker compatible
- **Mantenimiento:** Medio

### 🛠️ Lo Que Incluye

- ✅ Instalación MetaTrader 5 (Windows/Wine)
- ✅ Cuenta demo con broker MT5
- ✅ Librería `MetaTrader5` para Python
- ✅ Conexión Python ↔ MT5 validada
- ✅ Scripts de ejemplo y validación

### 🎯 Empezar Setup C

**👉 [IR A SETUP C: METATRADER 5 →](Setup_C_MetaTrader5.md)**

---

## ✅ Después del Setup

**Una vez completes tu setup, sigue estos pasos:**

### 1️⃣ Validar Setup Completo

**Checklist mínima:**

- ☐ Ambiente de desarrollo funciona
- ☐ Librerías core instaladas (pandas, numpy)
- ☐ Conexión con broker exitosa
- ☐ Puedes descargar datos históricos

**¿Algo falló?** → [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

### 2️⃣ Volver a la Guía de Inicio

📖 **[GUIA_INICIO](GUIA_INICIO.md)**

Lee el roadmap completo del workshop:
- 9 sesiones, 27 horas
- Checklist "Tu Primer Día"
- Expectativas realistas

---

### 3️⃣ Revisar el Programa Detallado

📚 **[Programa_Detallado_Workshop.md](Programa_Detallado_Workshop.md)**

Entiende qué aprenderás en cada sesión

---

### 4️⃣ ¡Empezar la Sesión 1!

**Si usas Setup A (Colab):**
- Abre el Colab Notebook Maestro (🔒 Premium)
- Navega a "🟦 SESIÓN 1: FUNDAMENTOS"
- Ejecuta celdas una por una

**Si usas Setup B/C (Local):**
- Abre Jupyter Lab: `jupyter lab`
- Carga el notebook del workshop
- Navega a Sesión 1

**🚀 ¡Estás listo para comenzar el workshop!**

---

## 🔗 Ver También

**Documentos relacionados:**

📖 **[GUIA_INICIO](GUIA_INICIO.md)**  
Tu punto de partida - Onboarding completo

📚 **[Programa Detallado del Workshop](Programa_Detallado_Workshop.md)**  
Contenido sesión por sesión

🛠️ **[Troubleshooting Maestro](Troubleshooting_Maestro.md)**  
Base de conocimiento de errores y soluciones

---

## 🔗 NAVEGACIÓN

**🏠 Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**📖 Ver también:**
- [Setup A: Express](Setup_A_Express.md) - 10-15 min
- [Setup A: Colab Completo](Setup_A_Colab_Rapido.md) - 30-45 min ⭐
- [Setup A: Guiado](Setup_A_Guiado.md) - 60-90 min
- [Setup B: Python Local](Setup_B_Python_Local.md) - 2-3h
- [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md) - 1-2h
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

**Antes de contactar:**
1. ✅ Revisa tabla comparativa
2. ✅ Lee descripción de cada setup
3. ✅ Consulta [FAQ en GUIA_INICIO](GUIA_INICIO.md)

---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
