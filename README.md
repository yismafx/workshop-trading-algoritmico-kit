# Workshop: Trading Algorítmico Aumentado con IA Generativa

**Transforma tu trading manual en sistemas algorítmicos potenciados por IA**

---

## ¿A Quién Está Dirigido?

Este workshop **no es para principiantes** en el mercado. Está diseñado exclusivamente para **traders con experiencia** que buscan sistematizar su "edge" (ventaja) y dar el salto profesional de la operación discrecional a la algorítmica.

### Perfil Ideal

**Traders Manuales/Discrecionales**  
Profesionales que ya operan y tienen estrategias e intuición de mercado, pero están limitados por el tiempo de pantalla, la psicología o la incapacidad de probar rigurosamente sus ideas.

**Analistas Financieros (Buy/Sell Side)**  
Analistas que desean construir y probar modelos sistemáticos en lugar de depender únicamente de reportes estáticos.

---

## Pre-Requisitos

### ✅ Conocimiento Obligatorio

**Experiencia Operativa Real**  
Entender profundamente la estructura del mercado, la ejecución de órdenes, el slippage y la gestión de riesgo. Debes saber qué es un stop-loss, un take-profit y un ratio Sharpe por experiencia propia.

**Dominio de Plataformas (Nivel Usuario)**  
Haber operado activamente con plataformas como TradingView, MetaTrader (MT4/MT5) o un bróker con API (ej. Interactive Brokers). No enseñaremos a usar estas plataformas, sino a automatizarlas.

**Mentalidad Cuantitativa**  
Una disposición para adoptar un enfoque 100% sistemático, basado en reglas y validación estadística.

### ❌ Lo Que NO Se Requiere (Enseñamos Desde Cero)

**NO se requiere experiencia en Programación**  
Enseñaremos los fundamentos de Python, Pine Script (TradingView) y MQL5 (MetaTrader) desde cero, usando la IA Generativa como acelerador.

**NO se requiere experiencia en IA Generativa**  
Enseñaremos las técnicas de Prompt Engineering específicas para trading, ideación de estrategias y revisión de código.

---

## El Kit Completo

Todos los participantes recibirán un kit de herramientas profesionales:

### 📓 Colab Notebook Maestro

Un solo Google Colab Notebook con **todo el código del workshop**, desde la descarga de datos, la limpieza, el backtesting, la optimización WFO y la gestión de riesgo. Es un sistema end-to-end listo para adaptar.

### 📦 Template Pack Profesional

Un conjunto de plantillas de documentación de **nivel institucional**, listas para usar:
- Strategy Memo
- Reporte de Backtesting
- README técnico para repositorios

### 🤖 Prompts Library (Biblioteca de Prompts)

Una colección curada de prompts de IA Generativa probados y estructurados, diseñados para:
- Generar hipótesis de estrategias
- Generar y depurar código en Python, Pine y MQL5
- Explicar y refactorizar código legacy

---

## Estructura del Workshop

### 📅 Información General

**Duración Total:** 27 horas cronológicas  
**Formato:** 9 sesiones de 3 horas cada una  
**Ritmo:** 3 sesiones por semana (completo en 3 semanas)

---

### 🟦 Semana 1: Fundamentos (9 horas)

**Sesión 1: Fundamentos y Mapa del Trading Algorítmico**  
Dominar el "mapa" completo del trading algorítmico, establecer expectativas realistas y configurar el entorno de desarrollo profesional.

- Expectativas Realistas (El "Anti-Hype")
- Las Fases del Trading Algorítmico
- Prompt Engineering Fundamental (Framework)
- Ecosistema de Herramientas
- **Entregable:** Mapa Mental + Ambiente configurado + Dataset SPY descargado

**Sesión 2: Datos - La Base de Todo Sistema**  
Dominar la descarga, limpieza, validación y almacenamiento de datos históricos con calidad institucional.

- El Mantra: "Garbage In, Garbage Out" (Chan, 2013)
- Fuentes de Datos y APIs (yfinance, Alpaca)
- Validación y Limpieza (Data Sins)
- **Entregable:** Script data_pipeline.py funcional + Dataset limpio validado

**Sesión 3: Ideación de Estrategias con GenAI**  
Desarrollar un framework sistemático para generar, validar y documentar hipótesis de trading usando IA Generativa.

- El Framework de 5 Pasos (Observación → Hipótesis → Traducción → Validación → Viabilidad)
- Fuentes de "Alpha": Reversión a la Media vs. Momentum
- GenAI como Copiloto de Investigación
- **Entregable:** "Idea Log" con 3 hipótesis + Especificación Técnica completa

---

### 🟨 Semana 2: Implementación (9 horas)

**Sesión 4: Implementación Práctica Guiada**  
Implementar la estrategia completa desde cero usando GenAI como copiloto de desarrollo.

- Arquitectura del Código (Separación de Responsabilidades)
- GenAI como Acelerador de Código
- Pruebas Unitarias (pytest)
- **Entregable:** Código Modular Completo + 3 Pruebas Unitarias + Visualización de señales

**Sesión 5: Validación Rigurosa - Backtesting Profesional**  
Implementar backtesting riguroso, entendiendo y evitando las trampas de overfitting.

- Trampas Comunes (Look-ahead bias, Survivorship bias, Data snooping)
- Técnicas Anti-Overfitting (WFO, Deflated Sharpe Ratio)
- Simulación Monte Carlo
- **Entregable:** Reporte Walk-Forward + Análisis Monte Carlo + Veredicto de robustez

**Sesión 6: Gestión Avanzada de Riesgo**  
Implementar dimensionamiento de posición y protocolos de riesgo a nivel de portafolio.

- Métodos de Position Sizing (Fijo, Volatilidad, Kelly Criterion)
- El "Interruptor de Circuito" (Circuit Breaker)
- Playbook de Crisis
- **Entregable:** Función get_position_size + Backtest comparativo + Playbook de Crisis

---

### 🟩 Semana 3: Producción (9 horas)

**Sesión 7: Multi-Plataforma - Del Código a la Ejecución**  
Implementar la estrategia en TradingView y conectarla a un broker usando Webhooks y APIs.

- Python vs. Pine Script
- Conversión con GenAI (Python → Pine Script)
- Arquitectura de Ejecución (Webhooks)
- **Entregable:** Estrategia en Pine Script + Servidor Webhook + Conector Alpaca API

**Sesión 8: Deployment Real - Paper Trading y Monitoreo**  
Desplegar el sistema en un servidor (VPS), implementar monitoreo 24/7 y gestionar la transición paper → live.

- Infraestructura de Producción (VPS, Docker)
- Monitoreo y Health Checks
- El Checklist Pre-Live
- **Entregable:** Sistema desplegado en VPS + Health Checks + Reporte Paper Trading

**Sesión 9: Proyecto Final y Documentación Profesional**  
Consolidar todo en un proyecto final con documentación de nivel institucional.

- Creación del "Portfolio Piece"
- Estructura del Strategy Document
- Framework de Mejora Continua
- **Entregable:** Documento de Estrategia Profesional + Repositorio completo + Presentación

---

## Expectativas Realistas

> Este workshop NO te hará millonario. Te dará un PROCESO robusto y repetible.

**Métricas Realistas:**

📊 **Sharpe Ratio:** 1.0 - 1.5 (neto de costos)  
📉 **Max Drawdown:** 20% - 30% (soportable psicológicamente)  
🎯 **Tasa de Fracaso:** 90% de las estrategias fallan (nuestro objetivo es ser el 10%)  
⏰ **Tiempo de Desarrollo:** 3-6 meses hasta primera estrategia rentable

---

## Stack Tecnológico

### Lenguajes
- Python 3.10+
- Pine Script (TradingView)
- MQL5 (MetaTrader)

### Librerías Principales
- `pandas`, `numpy` - Manipulación de datos
- `yfinance`, `alpaca-trade-api` - Descarga de datos
- `backtrader`, `vectorbt` - Backtesting
- `matplotlib`, `seaborn` - Visualización

### Plataformas
- **Google Colab** - Notebooks sin instalación local
- **TradingView** - Desarrollo visual y ejecución
- **Alpaca** - Paper trading y live trading
- **Interactive Broker** - Paper trading

### IA Generativa
- **Claude (Anthropic)** - Recomendado para código
- **ChatGPT (OpenAI)** - Alternativa válida
- **GitHub Copilot** - Opcional pero útil

---

## Inscripciones

### 💰 Inversión

**Precio:** Solicitar Información  
**Incluye:** 27 horas de formación + Colab Notebook Maestro + Template Pack + Prompts Library

**Métodos de Pago:** Solicitar información

### 📅 Próxima Cohorte

**Inicio:** A Confirmar
**Formato:** Virtual (Google Meet)  
**Cupo:** Limitados

### 📞 Contacto

📧 **Email:** [yismaryme@gmail.com](mailto:yismaryme@gmail.com)  
💬 **Telegram:** [@yismary](https://t.me/yismary)  
📱 **Canal:** Fractals Market

---

## Documentación Completa

### 🚀 Inicio Rápido

1. **[📖 LEEME_PRIMERO.md](00_GUIA_DE_USO/LEEME_PRIMERO.md)** - Guía completa
2. **[🗺️ Mapa Mental Interactivo](https://yismafx.github.io/workshop-trading-algoritmico-kit/00_GUIA_DE_USO/MAPA_MENTAL_SISTEMA_TRADING_PNG.html)** - Arquitectura del sistema
3. **[⚙️ Instrucciones de Setup](00_GUIA_DE_USO/Instrucciones_Setup_Ambiente.md)** - Configuración paso a paso

### 📂 Contenido Público (Este Repo)

```
📦 workshop-trading-algoritmico-kit/
│
├── 📂 00_GUIA_DE_USO/          → Documentación
├── 📂 02_TEMPLATE_PACK/        → Templates profesionales
├── 📂 03_PROMPTS_LIBRARY/      → Prompts para GenAI
└── 📂 04_SCRIPTS_AUXILIARES/   → Código reutilizable
```

---

## Arquitectura del Sistema

El sistema tiene **5 componentes principales** aumentados por IA:

**🗄️ DATA PIPELINE** - Descarga y limpia datos históricos  
**🧠 ESTRATEGIA** - Genera señales de trading  
**🛡️ RISK MANAGEMENT** - Protección de capital  
**🔬 BACKTESTING** - Validación histórica (WFO, Monte Carlo)  
**⚙️ EXECUTION** - Trading en vivo (Webhooks, APIs)

**🤖 IA Generativa (Capa Transversal)**  
Aumenta cada componente en 4 dimensiones: Ideación, Debugging, Traducción, Documentación

**[Ver Diagrama Completo →](https://yismafx.github.io/workshop-trading-algoritmico-kit/00_GUIA_DE_USO/MAPA_MENTAL_SISTEMA_TRADING_PNG.html)**

---

## Contenido Premium vs Público

### ✅ Contenido Público (Este Repo)

- Documentación del workshop
- Templates profesionales (Strategy Memo, Backtest Report)
- Scripts auxiliares (open source)
- Biblioteca de prompts básicos
- Mapa mental interactivo del sistema

### 🔒 Contenido Premium (Participantes del Workshop)

- **Colab Notebook Maestro** (código completo de 9 sesiones)
- **Videos grabados** de todas las sesiones
- **Estrategias backtestadas** (código + resultados WFO)
- **Biblioteca de 35+ prompts avanzados**
- **Soporte directo** (Telegram privado)
- **Casos de estudio reales**
- **Playbook de Crisis Management**

---

## Referencias Bibliográficas

Este workshop se basa en los fundamentos establecidos por:

1. **Chan, E. (2013)** - *Algorithmic Trading: Winning Strategies and Their Rationale*
2. **Carver, R. (2015)** - *Systematic Trading: A Unique New Method for Designing Trading and Investing Systems*
3. **López de Prado, M. (2018)** - *Advances in Financial Machine Learning*
4. **Strimpe, J. (2024)** - *Python for Algorithmic Trading Cookbook*

---

## Contribuciones

Este repositorio es **parcialmente open-source**.

**Puedes:**
- Reportar bugs (Issues)
- Sugerir mejoras (Issues)
- Contribuir código a scripts auxiliares (Pull Requests)

**No puedes:**
- Vender o redistribuir el material premium
- Crear workshops derivados sin permiso
- Usar con fines comerciales sin autorización

---

## Disclaimer

⚠️ **Material para fines educativos únicamente**

❌ NO constituye asesoría de inversión  
⚠️ Trading algorítmico implica riesgo de pérdida de capital  
📊 Resultados pasados NO garantizan resultados futuros  
💰 Nunca operes con dinero que no puedas permitirte perder

**Estadísticas Realistas:**
- 90% de las estrategias fallarán en validación rigurosa
- Un Sharpe Ratio > 1.0 es bueno, > 1.5 es excelente
- Drawdowns del 20-30% son normales en estrategias robustas
- El desarrollo toma meses, no días

---

## ⭐ Apoya Este Proyecto

Si este repositorio te resulta útil:
- Dale una estrella al repo
- Compártelo con otros traders
- Únete a las discusiones (Issues)

---

**Última actualización:** Noviembre 2025 • **Versión:** 1.0 (S1-S2 completas)

**Mantenido por:** [@yismafx](https://github.com/yismafx) | **Comunidad:** Fractals Market