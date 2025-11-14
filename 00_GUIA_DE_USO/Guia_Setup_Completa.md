# 🛠️ INSTRUCCIONES DE SETUP DEL AMBIENTE


🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 **Guía de Setup Completa**

---

**Workshop: Trading Algorítmico Aumentado con IA Generativa**  
**Versión:** 2.1 (Noviembre 2025)  
**Tiempo estimado:** 30 min a 3h (según opción elegida)

---

## 📑 Tabla de Contenidos

- [⚡ Quick Start - Elige Tu Camino](#-quick-start---elige-tu-camino)
- [📊 Tabla Comparativa Detallada](#-tabla-comparativa-detallada)
- [🚀 Guías de Setup por Opción](#-guías-de-setup-por-opción)
- [📚 Recursos Complementarios](#-recursos-complementarios)
- [✅ Validación Final](#-validación-final-después-del-setup)
- [🎯 Próximos Pasos](#-próximos-pasos)
- [📞 Soporte](#-soporte)

---

## ⚡ Quick Start - Elige Tu Camino

**🎯 Objetivo:** Encontrar tu setup ideal en menos de 2 minutos

Responde estas preguntas para ser dirigido al setup correcto:

---

### 🤔 Pregunta 1: ¿Tienes experiencia con Python?

```
                    ┌─────────────────────────────────────┐
                    │ ¿Tienes experiencia con Python?     │
                    └─────────────────────────────────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                      ❌ NO                 ✅ SÍ
                         │                     │
                         ↓                     ↓
              ┌──────────────────┐   ┌──────────────────┐
              │ Setup A: Colab   │   │ ¿Vas a deployar  │
              │ → 30 min         │   │ bots 24/7?       │
              └──────────────────┘   └──────────────────┘
                                              │
                                    ┌─────────┴─────────┐
                                    │                   │
                                 ❌ NO                ✅ SÍ
                                    │                   │
                                    ↓                   ↓
                         ┌──────────────────┐  ┌──────────────────┐
                         │ Setup A: Colab   │  │ Setup B: Python  │
                         │ → 30 min         │  │ Local → 2-3h     │
                         └──────────────────┘  └──────────────────┘
```

**Respuestas directas:**

- **❌ NO tengo experiencia con Python** → [Setup A: Colab Rápido](Setup_Colab_Rapido.md) ⭐ **Recomendado**
- **✅ SÍ tengo experiencia** → Continúa a Pregunta 2

---

### 🤔 Pregunta 2: ¿Planeas deployar bots 24/7?

**Solo si respondiste SÍ en Pregunta 1:**

- **❌ NO** → [Setup A: Colab Rápido](Setup_Colab_Rapido.md)
- **✅ SÍ** → [Setup B: Python Local](Setup_B_Python_Local.md)

---

### 🤔 Pregunta 3: ¿Usas principalmente Forex/CFDs con MetaTrader?

**Independiente de preguntas anteriores:**

- **✅ SÍ** → [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md)
- **❌ NO** → Continúa

---

### 🤔 Pregunta 4: ¿Necesitas acceso a mercados globales profesional?

**Solo si no elegiste MT5:**

- **✅ SÍ** → [Setup D: Interactive Brokers](Setup_D_Interactive_Brokers.md)
- **❌ NO** → [Setup A: Colab Rápido](Setup_Colab_Rapido.md)

---

## 📊 Tabla Comparativa Detallada

**Compara todas las opciones lado a lado:**

| Característica | [Setup A: Colab](Setup_Colab_Rapido.md) | [Setup B: Python Local](Setup_B_Python_Local.md) | [Setup C: MT5](Setup_C_MetaTrader5.md) | [Setup D: IB](Setup_D_Interactive_Brokers.md) |
|----------------|-------------------|---------------------|-----------------|----------------------|
| **⏱️ Tiempo setup** | 30-45 min | 2-3h | 1-2h | 2-3h |
| **💻 Experiencia Python** | No necesaria | Intermedia | Básica | Avanzada |
| **🚀 Deployment 24/7** | ❌ No | ✅ Sí (con VPS) | ✅ Sí | ✅ Sí |
| **💰 Costo** | Gratis | Gratis | Gratis | Gratis (paper) |
| **🌎 Mercados** | Multi-asset global | Multi-asset global | Forex/CFDs | Multi-asset global |
| **📈 Dificultad** | ⭐ Fácil | ⭐⭐⭐ Media | ⭐⭐ Media-fácil | ⭐⭐⭐⭐ Alta |
| **👥 Ideal para** | 👨‍🎓 Principiantes | 👨‍💻 Desarrolladores | 📈 Traders Forex | 🏦 Profesionales |
| **🛠️ Instalación local** | No requiere | Python + librerías | MT5 + Python | IB Gateway + Python |
| **📦 Gestión de dependencias** | Automática | Manual | Semi-automática | Manual |
| **🔧 Mantenimiento** | Bajo | Alto | Medio | Alto |

---

## 🚀 Guías de Setup por Opción

**Elige la guía que corresponde a tu setup:**

### ⭐ Opción A: Setup Rápido (Google Colab) - 30-45 min

**✅ Ideal para:** 80% de los participantes - No requiere instalar nada localmente

**Lo que incluye:**
- ✅ Creación de cuenta Google (si no tienes)
- ✅ Registro en Alpaca Paper Trading (gratis)
- ✅ Configuración de Google Colab
- ✅ Instalación automática de librerías
- ✅ Validación completa del ambiente
- ✅ Guía de uso del Colab Notebook Maestro

**Requisitos:**
- Cuenta Google (Gmail)
- Navegador web moderno
- Conexión a internet

**🔵 [IR A SETUP A: COLAB RÁPIDO →](Setup_Colab_Rapido.md)**

---

### 💻 Opción B: Setup Avanzado (Python Local) - 2-3h

**✅ Ideal para:** Desarrollo serio, deployment 24/7, control total

**Lo que incluye:**
- ✅ Instalación de Python 3.11+ (Anaconda o directo)
- ✅ Creación de ambiente virtual
- ✅ Instalación completa de librerías 2025
- ✅ Configuración de Jupyter Lab
- ✅ Setup de brokers (Alpaca, MT5, IB)
- ✅ Scripts de validación

**Requisitos:**
- Windows/macOS/Linux
- 5 GB espacio en disco
- Conocimientos básicos de terminal

**🔵 [IR A SETUP B: PYTHON LOCAL →](Setup_B_Python_Local.md)**

---

### 📊 Opción C: MetaTrader 5 Setup - 1-2h

**✅ Ideal para:** Traders de Forex/CFDs que usan o quieren usar MetaTrader

**Lo que incluye:**
- ✅ Instalación de MetaTrader 5
- ✅ Creación de cuenta demo
- ✅ Instalación de Python MT5 API
- ✅ Conexión Python ↔ MT5
- ✅ Scripts de ejemplo y validación

**Requisitos:**
- Windows (nativo) o macOS/Linux (Wine)
- Python 3.11+ instalado
- Broker compatible con MT5

**🔵 [IR A SETUP C: METATRADER 5 →](Setup_C_MetaTrader5.md)**

---

### 🏦 Opción D: Interactive Brokers Setup - 2-3h

**✅ Ideal para:** Traders profesionales con necesidad de acceso multi-mercado global

**Lo que incluye:**
- ✅ Registro en Interactive Brokers Paper Trading
- ✅ Instalación de IB Gateway
- ✅ Instalación de ib_insync
- ✅ Conexión Python ↔ IB
- ✅ Scripts de ejemplo y validación

**Requisitos:**
- Registro en IB (aprobación 24-48h)
- Python 3.11+ instalado
- Windows/macOS/Linux

**🔵 [IR A SETUP D: INTERACTIVE BROKERS →](Setup_D_Interactive_Brokers.md)**

---

## 📚 Recursos Complementarios

**Estos documentos complementan tu setup principal:**

### 📦 Librerías y Dependencias 2025

**Referencia completa de todas las librerías del workshop:**
- Core: pandas, numpy, scipy
- Datos: yfinance, alpaca-py, ib-insync, MetaTrader5
- Backtesting: vectorbt, backtrader, zipline-reloaded
- Análisis técnico: ta, pandas-ta, TA-Lib
- Y más...

**📖 [Ver Librerías y Dependencias 2025](Librerias_Dependencias_2025.md)**

---

### 📚 Guía de Uso del Colab Notebook Maestro

**Guía completa para usar el notebook del workshop:**
- Cómo navegar por las Sesiones 1-9
- Ejecutar celdas correctamente
- Troubleshooting de Colab
- Atajos de teclado

**📖 [Ver Guía de Uso de Colab](Guia_Uso_Colab_Notebook.md)**

**⚠️ Nota:** Obligatorio leer si elegiste Setup A (Colab)

---

### 🚨 Troubleshooting Común

**Errores comunes cross-platform y sus soluciones:**
- "No module named 'yfinance'"
- "Alpaca API authentication failed"
- "IndexError: list index out of range"
- "Session crashed" / "Out of Memory"
- Y más...

**📖 [Ver Troubleshooting Común](Troubleshooting_Comun.md)**

---

## ✅ Validación Final (Después del Setup)

**Independientemente de la opción que elegiste, verifica estos puntos antes de continuar:**

### 🎯 Ambiente de Desarrollo

☐ Puedo ejecutar código Python (Colab, Jupyter, o terminal)  
☐ Librerías core instaladas: pandas, numpy, yfinance  
☐ No hay errores de importación al ejecutar `import pandas as pd`

### 🔌 Conexión con Broker

☐ Tengo API keys configuradas (Alpaca, MT5, o IB)  
☐ Conexión con broker exitosa  
☐ Puedo obtener información de mi cuenta (balance, etc.)

### 📊 Descarga de Datos

☐ Puedo descargar datos históricos (ej: SPY últimos 5 días)  
☐ Datos tienen formato correcto (OHLCV)  
☐ No hay gaps o valores nulos inesperados

### ✅ Validación Automatizada

☐ Ejecuté el script de validación de mi setup  
☐ Todas las verificaciones pasaron (✅ verde)  
☐ Vi el mensaje: **"✅ Setup completado exitosamente"**

---

**Si algún punto NO está marcado:**

1. Revisa la sección de troubleshooting de tu setup específico
2. Consulta [Troubleshooting Común](Troubleshooting_Comun.md)
3. Contacta soporte (ver abajo)

---

## 🎯 Próximos Pasos

**¡Felicidades! Has completado el setup. 🎉**

**Tu journey continúa:**

### 1️⃣ Volver al Documento Principal

📖 [Volver a GUIA_INICIO.md](GUIA_INICIO.md)

Lee el roadmap completo del workshop (9 sesiones, 27 horas)

---

### 2️⃣ Completar el Checklist "Tu Primer Día"

📋 [Ver Checklist "Tu Primer Día"](GUIA_INICIO.md#-checklist-tu-primer-día)

Valida que tienes todo listo para empezar

---

### 3️⃣ Revisar el Programa Detallado

📚 [Ver Programa Detallado (Programa_Detallado_Workshop.md)](Programa_Detallado_Workshop.md)

Entiende qué aprenderás en cada sesión

---

### 4️⃣ ¡Empezar la Sesión 1!

**Si usas Colab:**
- Abre el [Colab Notebook Maestro](Guia_Uso_Colab_Notebook.md)
- Navega a "🟦 SESIÓN 1: FUNDAMENTOS"
- Ejecuta las celdas una por una

**Si usas Python Local:**
- Abre Jupyter Lab: `jupyter lab`
- Carga el notebook del workshop
- Navega a Sesión 1

**🚀 ¡Estás listo para comenzar!**

---

## 📞 Soporte

**Si algo no funciona después de seguir tu guía de setup:**

### 📧 Email
**yismaryme@gmail.com**  
Tiempo de respuesta: 24-48h

**Incluye en tu email:**
- Sistema operativo (Windows/macOS/Linux)
- Setup que elegiste (A/B/C/D)
- Paso exacto donde falló
- Error completo (screenshot o texto)
- Qué ya intentaste

---

### 💬 Telegram
**[@yismary](https://t.me/yismary)**  
Para consultas rápidas pre-workshop

---

### 🔒 Grupo Premium
**Solo participantes pagos**  
Soporte comunitario + sesiones de troubleshooting en vivo

---

### 🚨 Troubleshooting Primero

Antes de contactar, revisa:
1. Troubleshooting de tu setup específico
2. [Troubleshooting Común](Troubleshooting_Comun.md)
3. FAQ en [GUIA_INICIO.md](GUIA_INICIO.md#-faq---preguntas-frecuentes)

En 80% de los casos, la solución ya está documentada.

---

## 🔖 Versión y Actualizaciones

**Versión:** 2.1 (Noviembre 2025)  
**Última actualización:** 13 de noviembre de 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- v2.1 (Nov 2025): Arquitectura modular - 8 archivos separados
- v2.0 (Nov 2025): Guía de uso de Colab agregada
- v1.0 (Nov 2025): Versión inicial con 4 opciones de setup

---

## ⚠️ Disclaimer

**Este es material educativo.**

- ✅ Todas las herramientas son gratuitas para paper trading
- ⚠️ Nunca uses credenciales de live trading en el workshop
- 📊 Practica con cuentas demo/paper antes de arriesgar capital real
- 💰 Trading algorítmico tiene riesgo de pérdida de capital

---

**¿Listo para empezar?** 🚀

Recuerda: **GenAI = Copiloto, NO Piloto Automático.**  
El setup es el primer paso de un viaje de 3-6 meses.

**Elige tu setup arriba y comienza tu journey.** 🎓
