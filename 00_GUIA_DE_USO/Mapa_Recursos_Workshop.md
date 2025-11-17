# 🗺️ MAPA DE RECURSOS DEL WORKSHOP

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

**Hub Central: Trading Algorítmico Aumentado con IA Generativa**

**🏠 [Inicio](../README.md) > 📄 Mapa de Recursos**

---

**🎯 Propósito:** Directorio completo de todos los recursos del workshop  
**👥 Para:** Participantes del workshop (público + premium)  
**📅 Última actualización:** Noviembre 2025 | **Versión:** 1.0

---

## 📑 TABLA DE CONTENIDOS

### 📦 Recursos Principales
- [Colab Notebook Maestro](#-colab-notebook-maestro)
- [Template Pack](#-template-pack)
- [Prompts Library](#-prompts-library)
- [Scripts Auxiliares](#-scripts-auxiliares)

### 📚 Documentación
- [Guías de Setup](#-guías-de-setup)
- [Programa del Workshop](#-programa-del-workshop)
- [Troubleshooting](#-troubleshooting)
- [Glosario y FAQ](#-glosario-y-faq)

### 🔗 Enlaces Externos
- [Librerías y Herramientas](#-librerías-y-herramientas)
- [Literatura Recomendada](#-literatura-recomendada)
- [Comunidad y Soporte](#-comunidad-y-soporte)

---

## 📓 COLAB NOTEBOOK MAESTRO

### 🎯 ¿Qué Es?

**El corazón del workshop:** Notebook de Google Colab con TODO el código de las 9 sesiones.

**Características:**
- ✅ Código ejecutable listo para usar
- ✅ Instrucciones en español en cada sección
- ✅ Comentarios exhaustivos línea por línea
- ✅ Ejercicios prácticos integrados
- ✅ Validación automática al final de cada sesión

---

### 📂 Ubicación

**Estructura:**
```
01_COLAB_NOTEBOOK_MAESTRO/
└── Colab_Notebook_Maestro.ipynb
```

**Acceso:**
- 🔒 **Premium:** Solo participantes del workshop
- 📧 **Cómo obtener:** Recibes link por email después de inscripción

---

### 📖 Cómo Usar el Notebook

**1. Descargar:**
- Link enviado por email
- O descarga desde Drive compartido (participantes premium)

**2. Subir a Colab:**
- [colab.research.google.com](https://colab.research.google.com)
- `File → Upload notebook`
- Selecciona el archivo `.ipynb`

**3. Navegar por sesiones:**
```
📓 Colab_Notebook_Maestro.ipynb
│
├── 🟦 SESIÓN 1: Fundamentos y Mapa del Trading Algorítmico
│   ├── 1.1 Conceptos Core
│   ├── 1.2 Arquitectura de Sistemas
│   ├── 1.3 Ejercicio Práctico
│   └── 1.4 Validación
│
├── 🟦 SESIÓN 2: Datos - La Base de Todo Sistema
│   ├── 2.1 Fuentes de Datos
│   ├── 2.2 Descarga y Limpieza
│   ├── 2.3 Validación de Calidad
│   └── 2.4 Ejercicio Práctico
│
├── 🟦 SESIÓN 3: Ideación de Estrategias con GenAI
│   ├── 3.1 Prompts para Ideación
│   ├── 3.2 Validación de Ideas
│   ├── 3.3 Pseudocódigo → Código
│   └── 3.4 Ejercicio Práctico
│
├── 🟨 SESIÓN 4: Implementación Práctica Guiada
│   ├── 4.1 Estrategia Mean Reversion
│   ├── 4.2 Estrategia Momentum
│   ├── 4.3 Gestión de Órdenes
│   └── 4.4 Ejercicio Práctico
│
├── 🟨 SESIÓN 5: Validación Rigurosa - Backtesting Profesional
│   ├── 5.1 Vectorbt Básico
│   ├── 5.2 Walk-Forward Optimization
│   ├── 5.3 Monte Carlo Simulation
│   └── 5.4 Métricas de Performance
│
├── 🟨 SESIÓN 6: Gestión Avanzada de Riesgo
│   ├── 6.1 Position Sizing (Kelly, Fixed Fractional)
│   ├── 6.2 Stop Loss Dinámico
│   ├── 6.3 Diversificación de Portafolio
│   └── 6.4 Ejercicio Práctico
│
├── 🟩 SESIÓN 7: Multi-Plataforma - Del Código a la Ejecución
│   ├── 7.1 Python → Pine Script (TradingView)
│   ├── 7.2 Python → MQL5 (MetaTrader)
│   ├── 7.3 Webhooks y APIs
│   └── 7.4 Ejercicio Práctico
│
├── 🟩 SESIÓN 8: Deployment Real - Paper Trading y Monitoreo
│   ├── 8.1 Paper Trading Setup
│   ├── 8.2 Logging y Monitoreo
│   ├── 8.3 Alertas Automáticas
│   └── 8.4 Ejercicio Práctico
│
└── 🟩 SESIÓN 9: Proyecto Final y Documentación Profesional
    ├── 9.1 Strategy Memo Template
    ├── 9.2 Backtesting Report Template
    ├── 9.3 README Técnico
    └── 9.4 Presentación Final
```

**4. Ejecutar celdas:**
- Sigue las instrucciones en cada sección
- Ejecuta celda por celda (`Shift + Enter`)
- Completa los ejercicios prácticos

---

## 📦 TEMPLATE PACK

### 🎯 ¿Qué Es?

**Plantillas profesionales** para documentar tus sistemas de trading a nivel institucional.

---

### 📂 Ubicación

```
02_TEMPLATE_PACK/
├── Strategy_Memo_Template.md
├── Backtesting_Report_Template.md
├── README_Tecnico_Template.md
├── Risk_Management_Plan_Template.md
└── Trade_Journal_Template.xlsx
```

---

### 📄 Templates Disponibles

#### 1. Strategy Memo Template

**Para qué:** Documentar la lógica de tu estrategia como lo haría un hedge fund.

**Contiene:**
- Executive Summary
- Hypothesis y Edge
- Entrada y Salida (reglas precisas)
- Risk Management
- Backtesting Results
- Limitaciones y Risks

**Formato:** Markdown (.md)

**📘 Template** *(Disponible próximamente en v3.0)*

---

#### 2. Backtesting Report Template

**Para qué:** Reportar resultados de backtesting de forma transparente y reproducible.

**Contiene:**
- Resumen ejecutivo de métricas
- Período de testing y datos
- Resultados Walk-Forward
- Monte Carlo Analysis
- Equity Curve
- Drawdown Analysis
- Limitaciones del backtest

**Formato:** Markdown (.md) + Jupyter Notebook (.ipynb)

**📘 Template** *(Disponible próximamente en v3.0)*

---

#### 3. README Técnico Template

**Para qué:** Documentar tu repositorio de trading como un proyecto open-source.

**Contiene:**
- Descripción del sistema
- Instalación y setup
- Uso y configuración
- Estructura del código
- Testing y validación
- Deployment
- Licencia y disclaimers

**Formato:** Markdown (.md)

**📘 Template** *(Disponible próximamente en v3.0)*

---

#### 4. Risk Management Plan Template

**Para qué:** Definir reglas de gestión de riesgo antes de operar en vivo.

**Contiene:**
- Maximum Drawdown Limits
- Position Sizing Rules
- Stop Loss Strategy
- Portfolio Diversification
- Circuit Breakers
- Emergency Procedures

**Formato:** Markdown (.md)

**📘 Template** *(Disponible próximamente en v3.0)*

---

#### 5. Trade Journal Template

**Para qué:** Registrar cada operación y análisis post-trade.

**Contiene:**
- Fecha y hora de entrada/salida
- Activo y dirección (Long/Short)
- Razón de entrada (setup)
- Precio entrada/salida
- P&L realizado
- Notas post-trade

**Formato:** Excel (.xlsx) o Google Sheets

**📘 [Descargar Template](https://github.com/yismafx/workshop-trading-algoritmico-kit/blob/main/02_TEMPLATE_PACK/Trade_Journal_Template.xlsx)**

---

### ✅ Cómo Usar los Templates

**Paso 1:** Descarga el template que necesites

**Paso 2:** Copia y pega en tu proyecto

**Paso 3:** Llena las secciones con TU información

**Paso 4:** Usa GenAI para ayudarte:
```
Prompt ejemplo:
"Tengo esta estrategia de mean reversion en SPY. 
Ayúdame a llenar el Strategy Memo Template con esta información: [pega tu lógica]"
```

**Paso 5:** Itera y mejora

---

## 🤖 PROMPTS LIBRARY

### 🎯 ¿Qué Es?

**35+ prompts probados** para usar con Claude, ChatGPT, o cualquier IA Generativa en tu flujo de trading algorítmico.

---

### 📂 Ubicación

```
03_PROMPTS_LIBRARY/
├── 01_Ideacion_Estrategias/
│   ├── P01_Generar_Ideas_Estrategia.md
│   ├── P02_Validar_Hipotesis.md
│   └── P03_Pseudocodigo_a_Codigo.md
│
├── 02_Implementacion_Codigo/
│   ├── P04_Adaptar_Codigo_Existente.md
│   ├── P05_Explicar_Codigo_Complejo.md
│   ├── P06_Depurar_Errores.md
│   └── P07_Optimizar_Performance.md
│
├── 03_Backtesting/
│   ├── P08_Disenar_Backtest_Riguroso.md
│   ├── P09_Interpretar_Metricas.md
│   └── P10_Detectar_Overfitting.md
│
├── 04_Risk_Management/
│   ├── P11_Calcular_Position_Size.md
│   ├── P12_Disenar_Stop_Loss.md
│   └── P13_Diversificar_Portfolio.md
│
├── 05_Multi_Plataforma/
│   ├── P14_Python_to_Pine_Script.md
│   ├── P15_Python_to_MQL5.md
│   └── P16_Configurar_Webhooks.md
│
└── 06_Documentacion/
    ├── P17_Escribir_Strategy_Memo.md
    ├── P18_Generar_Backtesting_Report.md
    └── P19_Crear_README_Tecnico.md
```

---

### 🏆 Top 10 Prompts Más Usados

**1. P01 - Generar Ideas de Estrategia**
```markdown
Prompt: "Actúa como un quant trader profesional..."
Caso de uso: Brainstorming de nuevas estrategias
Sessión: 3
```

**2. P04 - Adaptar Código Existente**
```markdown
Prompt: "Tengo este código de mean reversion en SPY. Adáptalo para..."
Caso de uso: Modificar estrategias existentes
Sesión: 4
```

**3. P06 - Depurar Errores**
```markdown
Prompt: "Este código me da el siguiente error: [pegar error]. Ayúdame a..."
Caso de uso: Resolver bugs
Sesión: Todas
```

**4. P08 - Diseñar Backtest Riguroso**
```markdown
Prompt: "Diseña un backtest walk-forward para esta estrategia..."
Caso de uso: Validación profesional
Sesión: 5
```

**5. P09 - Interpretar Métricas**
```markdown
Prompt: "Estos son mis resultados de backtest: Sharpe 0.8, Max DD 25%..."
Caso de uso: Entender si los resultados son buenos
Sesión: 5
```

**6. P11 - Calcular Position Size**
```markdown
Prompt: "Tengo $10,000 de capital. Mi estrategia tiene win rate de 55%..."
Caso de uso: Sizing correcto de posiciones
Sesión: 6
```

**7. P14 - Python to Pine Script**
```markdown
Prompt: "Convierte esta estrategia Python a Pine Script de TradingView..."
Caso de uso: Ejecutar en TradingView
Sesión: 7
```

**8. P17 - Escribir Strategy Memo**
```markdown
Prompt: "Ayúdame a documentar mi estrategia usando el Strategy Memo Template..."
Caso de uso: Documentación profesional
Sesión: 9
```

**9. P05 - Explicar Código Complejo**
```markdown
Prompt: "Explícame este código línea por línea como si fuera un trader sin experiencia..."
Caso de uso: Entender código de otros
Sesión: Todas
```

**10. P10 - Detectar Overfitting**
```markdown
Prompt: "Mi estrategia tiene Sharpe 3.5 en backtest. ¿Es overfitting?..."
Caso de uso: Validar realismo de resultados
Sesión: 5
```

---

### 📚 Guía de Uso de Prompts

**Paso 1:** Identifica tu necesidad (ej: "necesito adaptar código")

**Paso 2:** Encuentra el prompt correspondiente en la carpeta

**Paso 3:** Lee el prompt completo y las instrucciones

**Paso 4:** Personaliza con TU contexto específico

**Paso 5:** Copia y pega en Claude/ChatGPT

**Paso 6:** Itera basado en los resultados

---

### 🔓 Acceso

- ✅ **Público:** Prompts básicos (15 prompts)
- 🔒 **Premium:** Prompts avanzados completos (35+ prompts)

**📘 [Ver Prompts Públicos](https://github.com/yismafx/workshop-trading-algoritmico-kit/tree/main/03_PROMPTS_LIBRARY)**

---

## 🐍 SCRIPTS AUXILIARES

### 🎯 ¿Qué Son?

**Utilidades Python reutilizables** para tareas comunes en trading algorítmico.

---

### 📂 Ubicación

```
04_SCRIPTS_AUXILIARES/
├── data_pipeline.py
├── risk_calculator.py
├── backtest_analyzer.py
├── order_manager.py
├── performance_metrics.py
└── webhook_handler.py
```

---

### 📄 Scripts Disponibles

#### 1. data_pipeline.py

**Para qué:** Descargar, limpiar y validar datos históricos.

**Funciones principales:**
```python
def download_historical_data(ticker, start_date, end_date, source='yfinance')
def clean_ohlcv_data(df)
def validate_data_quality(df)
def resample_timeframe(df, timeframe='1D')
```

**Uso:**
```python
from data_pipeline import download_historical_data, clean_ohlcv_data

# Descargar y limpiar
data = download_historical_data('SPY', '2020-01-01', '2024-01-01')
data_clean = clean_ohlcv_data(data)
```

---

#### 2. risk_calculator.py

**Para qué:** Calcular position sizing y gestión de riesgo.

**Funciones principales:**
```python
def kelly_criterion(win_rate, avg_win, avg_loss)
def fixed_fractional_position_size(capital, risk_pct, stop_loss_pct)
def calculate_max_positions(capital, risk_per_trade, correlation_matrix)
```

**Uso:**
```python
from risk_calculator import fixed_fractional_position_size

# Calcular tamaño de posición
capital = 10000
risk_pct = 0.02  # 2% de riesgo
stop_loss_pct = 0.05  # 5% stop loss

position_size = fixed_fractional_position_size(capital, risk_pct, stop_loss_pct)
print(f"Tamaño de posición: {position_size} acciones")
```

---

#### 3. backtest_analyzer.py

**Para qué:** Analizar resultados de backtesting.

**Funciones principales:**
```python
def calculate_sharpe_ratio(returns, risk_free_rate=0.02)
def calculate_max_drawdown(equity_curve)
def calculate_win_rate(trades_df)
def plot_equity_curve(equity_curve)
```

**Uso:**
```python
from backtest_analyzer import calculate_sharpe_ratio, calculate_max_drawdown

# Analizar resultados
sharpe = calculate_sharpe_ratio(returns)
max_dd = calculate_max_drawdown(equity_curve)

print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {max_dd:.2%}")
```

---

#### 4. order_manager.py

**Para qué:** Gestionar envío de órdenes a brokers (Alpaca, IB).

**Funciones principales:**
```python
def send_market_order(api, ticker, qty, side='buy')
def send_limit_order(api, ticker, qty, limit_price, side='buy')
def cancel_order(api, order_id)
def get_open_positions(api)
```

**Uso:**
```python
from order_manager import send_market_order
import alpaca_trade_api as tradeapi

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=PAPER_URL)

# Enviar orden de compra
order = send_market_order(api, 'SPY', qty=10, side='buy')
print(f"Orden enviada: {order.id}")
```

---

#### 5. performance_metrics.py

**Para qué:** Calcular métricas avanzadas de performance.

**Funciones principales:**
```python
def calculate_sortino_ratio(returns, target_return=0)
def calculate_calmar_ratio(returns, max_drawdown)
def calculate_omega_ratio(returns, threshold=0)
def calculate_tail_ratio(returns)
```

---

#### 6. webhook_handler.py

**Para qué:** Recibir y procesar webhooks desde TradingView u otras plataformas.

**Funciones principales:**
```python
def setup_flask_server(port=5000)
def validate_webhook_signature(payload, secret)
def parse_tradingview_webhook(payload)
def execute_trade_from_webhook(payload, api)
```

---

### ✅ Cómo Usar los Scripts

**Paso 1:** Descarga el script que necesites

**Paso 2:** Importa en tu notebook de Colab:
```python
# Si subes el script a Colab
!wget https://raw.githubusercontent.com/yismafx/workshop-trading-algoritmico-kit/main/04_SCRIPTS_AUXILIARES/data_pipeline.py

# Importa
from data_pipeline import download_historical_data
```

**Paso 3:** Usa las funciones según necesites

---

## 📚 GUÍAS DE SETUP

### Opciones de Setup Disponibles

**4 setups para diferentes necesidades:**

#### Setup A: Colab Rápido (⭐ Recomendado)
- **Tiempo:** 10-15 min
- **Dificultad:** ⭐ Fácil
- **Para:** 80% de participantes

**📘 [Ir a Setup A](Setup_A_Colab_Rapido.md)**

---

#### Setup B: Python Local
- **Tiempo:** 2-3h
- **Dificultad:** ⭐⭐⭐ Media
- **Para:** Deployment 24/7

**📘 [Ir a Setup B](Setup_B_Python_Local.md)**

---

#### Setup C: MetaTrader 5
- **Tiempo:** 1-2h
- **Dificultad:** ⭐⭐ Media-Fácil
- **Para:** Traders de Forex/CFDs

**📘 [Ir a Setup C](Setup_C_MetaTrader5.md)**

---

#### Setup D: Interactive Brokers
- **Tiempo:** 2-3h
- **Dificultad:** ⭐⭐⭐⭐ Alta
- **Para:** Profesionales con IB


---

### Guías Complementarias

**Setup A (Colab) - Guías Especializadas:**
- 📘 [Setup Express (10 min)](Setup_A_Express.md)
- 📚 [Setup Guiado (30-60 min)](Setup_A_Guiado.md)
- ✅ [Mejores Prácticas](Mejores_Practicas_Setup_A.md)
- 🚨 [Troubleshooting Completo](Troubleshooting_Maestro.md)

---

## 📖 PROGRAMA DEL WORKSHOP

### Estructura Completa

**27 horas | 9 sesiones | 3 semanas**

📘 **[Ver Programa Detallado](Programa_Detallado_Workshop.md)**

**Incluye:**
- Objetivos de cada sesión
- Temario detallado
- Ejercicios prácticos
- Entregables
- Recursos complementarios

---

## 🚨 TROUBLESHOOTING

### Guías de Resolución de Errores

**Por Setup:**
- 🚨 [Troubleshooting Setup A (Colab)](Troubleshooting_Maestro.md) - 50+ errores
- 🚨 [Troubleshooting Común](Troubleshooting_Comun.md) - Cross-platform

**Por Herramienta:**
- Errores de instalación
- Errores de conexión a broker
- Errores de descarga de datos
- Errores de Colab/Runtime
- Errores de código Python

---

## 📖 GLOSARIO Y FAQ

### Glosario

**Términos técnicos explicados:**

📘 **[Ver Glosario Completo](GLOSARIO_NAVEGACION.md)**

**Incluye:**
- Edge, Sharpe Ratio, Drawdown
- Backtesting, Walk-Forward, Monte Carlo
- Position Sizing, Kelly Criterion
- API, Webhook, Slippage
- Y más...

---

### FAQ - Preguntas Frecuentes

**Respuestas a preguntas comunes:**

📘 **[Ver FAQ Completo](GUIA_INICIO.md#-faq---preguntas-frecuentes)**

**Categorías:**
- Setup y configuración
- Brokers y cuentas
- Colab y Notebooks
- Estrategias y backtesting
- IA Generativa y prompts

---

## 📚 LIBRERÍAS Y HERRAMIENTAS

### Librerías Python 2025

**Librerías principales usadas en el workshop:**

**Categorías:**
- **Core:** pandas, numpy, scipy
- **Datos:** yfinance, alpaca-py, ib-insync
- **Backtesting:** vectorbt, backtrader, zipline
- **Análisis Técnico:** ta, pandas-ta, TA-Lib
- **Visualización:** matplotlib, seaborn, plotly
- **Machine Learning:** scikit-learn, tensorflow (opcional)

---

### Herramientas Externas

**Plataformas y servicios:**

**Brokers:**
- [Alpaca](https://alpaca.markets) - Paper Trading gratis
- [Interactive Brokers](https://www.interactivebrokers.com) - Mercados globales

**Plataformas de Ejecución:**
- [TradingView](https://www.tradingview.com) - Gráficos y alertas
- [MetaTrader 5](https://www.metatrader5.com) - Forex/CFDs

**IA Generativa:**
- [Claude](https://claude.ai) - Recomendado para código
- [ChatGPT](https://chat.openai.com) - Alternativa
- [GitHub Copilot](https://github.com/features/copilot) - IDE integration

---

## 📖 LITERATURA RECOMENDADA

### Libros Core del Workshop

**1. Chan, E. (2013) - Algorithmic Trading**
- Estrategias mean reversion y momentum
- Testing y validación
- Risk management

**2. Carver, R. (2015) - Systematic Trading**
- Diversificación
- Position sizing
- Gestión de portafolio

**3. López de Prado, M. (2018) - Advances in Financial ML**
- Anti-overfitting
- Cross-validation especializada
- Features engineering

**4. Strimpe, J. (2024) - Python for Algorithmic Trading Cookbook**
- APIs modernas (Alpaca, IB)
- Best practices 2024-2025
- Integración con GenAI

---

### Lecturas Complementarias

**Backtesting y Validación:**
- Pardo, R. (2008) - "The Evaluation and Optimization of Trading Strategies"
- Bailey & López de Prado (2014) - "The Deflated Sharpe Ratio"

**Risk Management:**
- Tharp, V. (2008) - "Trade Your Way to Financial Freedom"
- Taleb, N. (2007) - "The Black Swan"

**Python para Finanzas:**
- Hilpisch, Y. (2018) - "Python for Finance" (2nd Edition)
- VanderPlas, J. (2016) - "Python Data Science Handbook"

---

## 👥 COMUNIDAD Y SOPORTE

### Grupo Premium del Workshop

**Para participantes inscritos:**

- 💬 **Telegram:** Soporte comunitario
- 📧 **Email:** yismaryme@gmail.com
- 🎥 **Sesiones en vivo:** Google Meet (link en calendario)

**Recibirás invitación por email después de inscripción**

---

### Canales de Soporte

**📧 Email:**
- **Para:** Consultas técnicas, issues, feedback
- **Tiempo respuesta:** 24-48h
- **Asunto formato:** `[Categoría] - [Tu consulta]`

**💬 Telegram:**
- **Para:** Consultas rápidas, networking
- **Usuario:** [@yismafx](https://t.me/yismafx)
- **Horarios:** Lun-Vie 9AM-6PM (GMT-3)

**🔒 Grupo Premium:**
- **Para:** Participantes pagos
- **Beneficios:** Soporte prioritario, material exclusivo, Q&A sessions

---

### Comunidad Fractals Market

**Canal principal:**

📱 **[Fractals Market](https://t.me/fractals_market)**

**Actividades:**
- Noticias de trading algorítmico
- Nuevas herramientas y librerías
- Casos de estudio de la comunidad
- Anuncios de próximas cohortes

---

## 🗺️ SITEMAP DEL REPOSITORIO

**Mapa completo de la estructura:**

📘 **[Ver SITEMAP.md](SITEMAP.md)**

**Navega fácilmente por:**
```
workshop-trading-algoritmico-kit/
├── 00_GUIA_DE_USO/           ← Documentación y setups
├── 01_COLAB_NOTEBOOK_MAESTRO/ ← Código de las 9 sesiones (premium)
├── 02_TEMPLATE_PACK/          ← Templates profesionales
├── 03_PROMPTS_LIBRARY/        ← 35+ prompts para GenAI
└── 04_SCRIPTS_AUXILIARES/     ← Utilidades Python reutilizables
```

---

## 🎯 CÓMO NAVEGAR ESTE MAPA

**Para Principiantes:**
1. Empieza con [Setup A (Colab)](Setup_A_Colab_Rapido.md)
2. Explora el [Colab Notebook Maestro](#-colab-notebook-maestro)
3. Usa [Prompts Library](#-prompts-library) cuando necesites ayuda

**Para Avanzados:**
1. Revisa [Scripts Auxiliares](#-scripts-auxiliares)
2. Personaliza [Templates](#-template-pack)
3. Contribuye con tus propias herramientas

**Para Instructores:**
1. Revisa [Programa Detallado](#-programa-del-workshop)
2. Usa [Troubleshooting](#-troubleshooting) para anticipar problemas
3. Comparte [Literatura Recomendada](#-literatura-recomendada)

---

## 🧭 NAVEGACIÓN

**🏠 Inicio:** [README Principal](../README.md)  
**⬅️ Anterior:** [Guía de Inicio](GUIA_INICIO.md)  
**➡️ Siguiente:** [Programa Detallado](Programa_Detallado_Workshop.md)  
**⬆️ Categoría:** [Guía de Uso](GUIA_INICIO.md)

---

## 📞 SOPORTE

**¿No encuentras algo?**

📧 **Email:** yismaryme@gmail.com (Asunto: `[Mapa Recursos] - No encuentro [X]`)  
💬 **Telegram:** [@yismafx](https://t.me/yismafx)

---

## 📌 VERSIÓN

**v1.0 (Noviembre 2025)** - Mapa de Recursos centralizado  
**Última actualización:** 15 de Noviembre de 2025

**Changelog:**
- **v1.0 (Nov 15, 2025):** Creación del Mapa de Recursos
  - Hub central de todos los materiales
  - Links a todos los recursos
  - Guías de uso integradas

---

**🗺️ ¡Con este mapa, nunca te perderás en el workshop!**

**Marca esta página como favorita para referencia rápida. 🎯**
