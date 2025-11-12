# Workshop: Trading Algorítmico Aumentado con IA Generativa

**Transforma tu trading manual en sistemas algorítmicos potenciados por IA**

---

## ¿A Quién Está Dirigido?

**Este workshop NO es para principiantes.** Está diseñado para:

**Traders Manuales/Discrecionales**
- Ya operan con estrategias propias
- Limitados por tiempo de pantalla y psicología
- Buscan sistematizar su edge

**Analistas Financieros (Buy/Sell Side)**
- Quieren construir modelos sistemáticos
- Buscan ir más allá de reportes estáticos

---

## Pre-Requisitos

### ✅ Lo Que SÍ Necesitas

**Experiencia Operativa Real**
- Conoces stop-loss, take-profit, ratio Sharpe por experiencia propia
- Entiendes slippage, ejecución de órdenes, gestión de riesgo

**Dominio de Plataformas (Nivel Usuario)**
- Has operado con TradingView, MetaTrader o broker con API
- No enseñamos a usarlas, sino a automatizarlas

**Mentalidad Cuantitativa**
- Disposición a adoptar enfoque 100% sistemático
- Basado en reglas y validación estadística

### ❌ Lo Que NO Necesitas (Enseñamos Desde Cero)

- ❌ Experiencia en Programación (Python, Pine Script, MQL5)
- ❌ Experiencia en IA Generativa (Prompt Engineering)
- ❌ Conocimientos de backtesting riguroso

---

## El Kit Completo

### 📓 Colab Notebook Maestro
- Todo el código del workshop en un solo notebook
- Sistema end-to-end: descarga → limpieza → backtesting → WFO → riesgo
- Listo para adaptar a tus estrategias

### 📦 Template Pack Profesional
- Strategy Memo (nivel institucional)
- Reporte de Backtesting
- README técnico para repositorios

### 🤖 Prompts Library (35+ Prompts)
- Generar hipótesis de estrategias
- Depurar código (Python, Pine, MQL5)
- Traducir entre lenguajes
- Refactorizar código legacy

---

## Estructura del Workshop

**Duración:** 27 horas • **Formato:** 9 sesiones de 3h • **Ritmo:** 3 sesiones/semana

---

### 🟦 Semana 1: Fundamentos (9h)

**S1: Fundamentos y Mapa del Trading Algorítmico**
- Expectativas realistas (El "Anti-Hype")
- Fases del trading algorítmico
- Prompt Engineering (Framework ROL-CONTEXTO-TAREA-FORMATO)
- Ecosistema de herramientas
- **Entregable:** Mapa Mental + Ambiente configurado + Dataset SPY

**S2: Datos - La Base de Todo Sistema**
- Mantra: "Garbage In, Garbage Out" (Chan, 2013)
- APIs: yfinance (gratis) vs Alpaca (pro)
- Validación y limpieza (Data Sins)
- **Entregable:** Script `data_pipeline.py` + Dataset limpio validado

**S3: Ideación de Estrategias con GenAI**
- Framework de 5 Pasos (Observación → Hipótesis → Traducción → Validación → Viabilidad)
- Fuentes de "Alpha": Reversión a la Media vs Momentum
- GenAI como copiloto de investigación
- **Entregable:** "Idea Log" con 3 hipótesis + Especificación Técnica

---

### 🟨 Semana 2: Implementación (9h)

**S4: Implementación Práctica Guiada**
- Arquitectura modular (main.py, data_handler.py, indicators.py, strategy.py)
- GenAI como acelerador de código
- Pruebas unitarias con pytest
- **Entregable:** Código completo + 3 tests + Visualización de señales

**S5: Validación Rigurosa - Backtesting Profesional**
- Trampas: Look-ahead bias, Survivorship bias, Data snooping
- Anti-Overfitting: Walk-Forward Optimization (WFO), Deflated Sharpe Ratio
- Simulación Monte Carlo
- **Entregable:** Reporte WFO + Análisis Monte Carlo + Veredicto robustez

**S6: Gestión Avanzada de Riesgo**
- Position Sizing: Fijo, Volatilidad, Kelly Criterion
- Circuit Breaker (Interruptor de Circuito)
- Playbook de Crisis
- **Entregable:** Función `get_position_size()` + Backtest comparativo + Playbook

---

### 🟩 Semana 3: Producción (9h)

**S7: Multi-Plataforma - Del Código a la Ejecución**
- Python (desarrollo) vs Pine Script (ejecución)
- Conversión con GenAI (Python → Pine Script)
- Arquitectura: TradingView → Webhook → FastAPI → Alpaca
- **Entregable:** Estrategia en Pine + Servidor Webhook + Conector API

**S8: Deployment Real - Paper Trading y Monitoreo**
- Infraestructura: VPS, Docker
- Health Checks (monitoreo 24/7)
- Checklist Pre-Live (8 semanas paper, P&L coincide, Playbook listo)
- **Entregable:** Sistema en VPS + Health Checks + Reporte Paper Trading

**S9: Proyecto Final y Documentación Profesional**
- Strategy Document (Hipótesis, Datos, Backtesting, Riesgo, Ejecución)
- Framework de Mejora Continua
- Peer Review
- **Entregable:** Documento profesional + Repositorio completo + Presentación

---

## Expectativas Realistas

> ⚠️ Este workshop NO te hará millonario. Te dará un PROCESO robusto y repetible.

| Métrica | Objetivo Realista | ❌ Expectativa Irreal |
|---------|------------------|----------------------|
| **Sharpe Ratio** | 1.0 - 1.5 | 3.0+ |
| **Max Drawdown** | 20% - 30% | < 5% |
| **Tasa de éxito** | 2 de cada 10 estrategias | Todas funcionan |
| **Tiempo** | 3-6 meses | 1 semana |

**Estadísticas Realistas:**
- 90% de estrategias fallan en validación rigurosa (nuestro objetivo: ser el 10%)
- Drawdowns del 20-30% son normales en estrategias robustas
- El desarrollo toma meses, no días

---

## Stack Tecnológico

**Lenguajes:** Python 3.10+, Pine Script, MQL5  
**Datos:** yfinance, alpaca-trade-api  
**Backtesting:** backtrader, vectorbt  
**Visualización:** matplotlib, seaborn  
**Plataformas:** Google Colab, TradingView, Alpaca, Interactive Brokers  
**IA Generativa:** Claude (recomendado), ChatGPT, GitHub Copilot

---

## Inscripciones

### 💰 Inversión
- **Precio:** Solicitar información
- **Incluye:** 27h formación + Colab Notebook + Templates + Prompts Library
- **Pago:** Consultar opciones disponibles

### 📅 Próxima Cohorte
- **Inicio:** A confirmar
- **Formato:** Virtual (Google Meet)
- **Cupo:** Limitado

### 📞 Contacto
📧 [yismaryme@gmail.com](mailto:yismaryme@gmail.com)  
💬 Telegram: [@yismary](https://t.me/yismary)  
📱 Canal: Fractals Market

---

## Documentación

### 🚀 Inicio Rápido
1. [📖 LEEME_PRIMERO.md](00_GUIA_DE_USO/LEEME_PRIMERO.md) - Guía completa
2. [🗺️ Mapa Mental Interactivo](https://yismafx.github.io/workshop-trading-algoritmico-kit/00_GUIA_DE_USO/MAPA_MENTAL_SISTEMA_TRADING_PNG.html) - Arquitectura del sistema
3. [⚙️ Instrucciones de Setup](00_GUIA_DE_USO/Instrucciones_Setup_Ambiente.md) - Configuración paso a paso

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

**5 componentes principales aumentados por IA:**

🗄️ **DATA PIPELINE** - Descarga y limpia datos históricos  
🧠 **ESTRATEGIA** - Genera señales de trading  
🛡️ **RISK MANAGEMENT** - Protección de capital  
🔬 **BACKTESTING** - Validación histórica (WFO, Monte Carlo)  
⚙️ **EXECUTION** - Trading en vivo (Webhooks, APIs)

🤖 **IA Generativa (Capa Transversal)**  
Aumenta cada componente en 4 dimensiones: Ideación, Debugging, Traducción, Documentación

**[Ver Diagrama Completo →](https://yismafx.github.io/workshop-trading-algoritmico-kit/00_GUIA_DE_USO/MAPA_MENTAL_SISTEMA_TRADING_PNG.html)**

---

## Contenido Premium vs Público

### ✅ Público (Este Repo)
- Documentación del workshop
- Templates profesionales
- Scripts auxiliares (open source)
- Prompts básicos
- Mapa mental interactivo

### 🔒 Premium (Participantes del Workshop)
- Colab Notebook Maestro (código completo 9 sesiones)
- Videos grabados de todas las sesiones
- Estrategias backtestadas (código + resultados WFO)
- Biblioteca 35+ prompts avanzados
- Soporte directo (Telegram privado)
- Casos de estudio reales
- Playbook de Crisis Management

---

## Referencias Bibliográficas

1. **Chan, E. (2013)** - *Algorithmic Trading: Winning Strategies and Their Rationale*
2. **Carver, R. (2015)** - *Systematic Trading: A Unique New Method for Designing Trading and Investing Systems*
3. **López de Prado, M. (2018)** - *Advances in Financial Machine Learning*
4. **Strimpe, J. (2024)** - *Python for Algorithmic Trading Cookbook*

---

## Contribuciones

**Puedes:**
- Reportar bugs (Issues)
- Sugerir mejoras (Issues)
- Contribuir código (Pull Requests)

**No puedes:**
- Vender o redistribuir material premium
- Crear workshops derivados sin permiso

---

## Disclaimer

⚠️ **Material para fines educativos únicamente**

❌ NO constituye asesoría de inversión  
⚠️ Trading algorítmico implica riesgo de pérdida de capital  
📊 Resultados pasados NO garantizan resultados futuros  
💰 Nunca operes con dinero que no puedas perder

---

## ⭐ Apoya Este Proyecto

- Dale una estrella al repo
- Compártelo con otros traders
- Únete a las discusiones (Issues)

---

**Última actualización:** Noviembre 2025 • **Versión:** 1.0 (S1-S2 completas)

**Mantenido por:** [@yismafx](https://github.com/yismafx) | **Comunidad:** Fractals Market