# 🤔 FAQ COMPLETO - Workshop Trading Algorítmico Aumentado con IA Generativa

> ⚠️ **Base de Conocimiento Centralizada**  
> Este documento contiene TODAS las preguntas frecuentes del workshop.  
> Usa `Ctrl+F` para buscar palabras clave.

🏠 [Inicio](../README.md) > 📄 **FAQ Completo**

---

![Version](https://img.shields.io/badge/version-3.0-blue) ![Status](https://img.shields.io/badge/status-active-success) ![Questions](https://img.shields.io/badge/preguntas-35-green)

---

## 📋 ÍNDICE POR CATEGORÍAS

- [🔧 Preguntas Técnicas (P1-P10)](#-preguntas-técnicas)
- [💡 Preguntas Conceptuales (P11-P20)](#-preguntas-conceptuales)
- [💼 Preguntas Operativas (P21-P30)](#-preguntas-operativas)
- [💰 Preguntas Financieras (P31-P35)](#-preguntas-financieras)

---

## 🔧 PREGUNTAS TÉCNICAS

### P1: ¿Necesito saber programar en Python?

**R:** **NO**. Este workshop asume CERO conocimiento de programación. Te daremos el código completo y te enseñaremos a adaptarlo con ayuda de GenAI.

---

### P2: ¿Qué pasa si tengo un Mac / Linux?

**R:** El workshop funciona en **cualquier sistema operativo** porque usamos Google Colab (navegador). Si prefieres Python local, funciona en Mac, Linux y Windows.

---

### P3: ¿Puedo usar Interactive Brokers en vez de Alpaca?

**R:** **SÍ**, pero es más complejo. Alpaca es más amigable para principiantes. Si ya tienes cuenta IB, podemos adaptar el código en S7.

---

### P4: ¿Funciona para criptomonedas?

**R:** **SÍ**, con adaptaciones. El código base es para acciones/ETFs, pero en S7 enseñamos cómo adaptar a Binance/Crypto APIs.

---

### P5: ¿Necesito pagar por ChatGPT Plus?

**R:** **NO**. ChatGPT gratis es suficiente. Claude gratis también funciona. GitHub Copilot ($10/mes) es opcional y útil, pero no obligatorio.

---

### P6: ¿Qué versión de Python necesito?

**R:** **Python 3.8+** (Colab usa 3.10). Si instalas local, usa Anaconda que ya incluye todo.

---

### P7: ¿El código funciona en MetaTrader?

**R:** El código base es Python. En S7 enseñamos a **traducir tu lógica** a MQL5 (MetaTrader) con ayuda de GenAI.

---

### P8: ¿Puedo usar TradingView para ejecutar?

**R:** **SÍ**. TradingView (Pine Script) es una opción. En S7 cubrimos Pine Script + webhooks para conectar con brokers.

---

### P9: ¿Necesito VPS desde el inicio?

**R:** **NO**. VPS es solo necesario en S8 si decides deployment 24/7. Durante S1-S7 usas Colab o tu computadora.

---

### P10: ¿Los scripts auxiliares son open source?

**R:** **SÍ**. Todo el código en `04_SCRIPTS_AUXILIARES/` es público y open source (MIT License). Puedes usarlo libremente.

**🔗 Ver también:**
- [Stack Tecnológico en GUIA_INICIO](GUIA_INICIO.md#️-stack-tecnológico-del-workshop)
- [Troubleshooting Maestro](Troubleshooting_Maestro.md)

---

## 💡 PREGUNTAS CONCEPTUALES

### P11: ¿Qué diferencia hay entre trading algorítmico y trading con IA?

**R:** 
- **Trading algorítmico tradicional:** Reglas fijas programadas (ej: "compra cuando RSI < 30")
- **Trading con IA pura:** ML decide TODO (muy complejo, no recomendado para retail)
- **Trading algorítmico AUMENTADO con IA (este workshop):** Usas GenAI como copiloto para escribir/adaptar código, pero TÚ defines la lógica

---

### P12: ¿Por qué insisten tanto en "expectativas realistas"?

**R:** **Porque el 90% de los traders algorítmicos fallan por expectativas irreales.** 

Si crees que harás 100% anual sin drawdowns, te frustrarás y abandonarás. Nosotros te preparamos para la realidad: 20-30% anual con 20-30% DD es EXCELENTE.

**🔗 Ver también:** [Expectativas Realistas en GUIA_INICIO](GUIA_INICIO.md#️-expectativas-realistas-el-anti-hype)

---

### P13: ¿Qué es walk-forward optimization y por qué es crítico?

**R:** **WFO es validación rigurosa.** 

Optimizas en un periodo (training) y pruebas en otro periodo (testing) que la estrategia NUNCA vio. Si falla aquí, fallaría en live trading.

---

### P14: ¿Qué es overfitting y cómo lo evito?

**R:** **Overfitting = ajustar la estrategia al ruido histórico, no a patrones reales.** 

**Se evita con:**
1. WFO riguroso
2. Menos parámetros optimizables
3. Análisis Monte Carlo
4. Periodo de validación out-of-sample > 30% de los datos

---

### P15: ¿Por qué empezamos con paper trading y no directo en real?

**R:** **Porque el mercado real tiene fricciones que el backtest NO captura:**
- Slippage real vs estimado
- Latencia de ejecución
- Psicología al ver dinero real en juego
- Errores en el código que pasan en backtest

---

### P16: ¿Qué es el Sharpe Ratio y por qué importa?

**R:** **Sharpe mide retorno ajustado por riesgo.** 

**Interpretación:**
- **Sharpe < 1:** Malo
- **Sharpe 1-1.5:** Muy bueno para retail ⭐
- **Sharpe 1.5-2:** Excelente
- **Sharpe > 2:** Sospechoso de overfitting

---

### P17: ¿Puedo combinar múltiples estrategias?

**R:** **SÍ, y es altamente recomendado.** Carver (2015) sugiere 5-10 estrategias independientes para diversificación.

---

### P18: ¿Qué significa "GenAI = Copiloto, NO Piloto Automático"?

**R:** GenAI NO decide qué es rentable ni valida overfitting. GenAI SÍ escribe código 10x más rápido y debuggea errores.

---

### P19: ¿Por qué no usan machine learning avanzado en el workshop?

**R:** **Porque ML añade complejidad sin mejorar resultados para retail.** ML requiere muchos datos, es propenso a overfitting extremo, y no es necesario para estrategias rentables.

---

### P20: ¿Cuál es el "edge" en trading algorítmico?

**R:** El workshop NO te da un edge mágico. Te enseña a **sistematizar el edge que YA TIENES** de tu trading manual.

---

## 💼 PREGUNTAS OPERATIVAS

### P21: ¿Puedo tomar el workshop si vivo fuera de Argentina?

**R:** **SÍ**. El workshop es 100% online y las herramientas funcionan globalmente.

---

### P22: ¿Las sesiones son en vivo o grabadas?

**R:** **Ambas**: Sesiones en vivo (3h) con Q&A + Grabaciones 24/7 para repaso.

---

### P23: ¿Qué pasa si me pierdo una sesión?

**R:** Puedes verla grabada y completar el entregable. No es obligatorio estar en vivo.

---

### P24: ¿Hay examen final?

**R:** **NO hay examen.** Hay un Proyecto Final (S9) con código, Strategy Memo y Backtest Report.

---

### P25: ¿Puedo trabajar en equipo?

**R:** **SÍ**, equipos de 2-3 personas.

---

### P26: ¿El material queda disponible después del workshop?

**R:** **SÍ, acceso de por vida** a código, videos, prompts y actualizaciones (1 año gratis).

---

### P27: ¿Hay certificado al completar?

**R:** **NO hay certificado formal.** Tendrás un portfolio en GitHub.

---

### P28: ¿Ofrecen mentoría post-workshop?

**R:** **SÍ**: Grupo Telegram lifetime + 2 sesiones Q&A grupales.

---

### P29: ¿Puedo usar el material para enseñar?

**R:** Código público es open source. Contenido premium es solo uso personal.

---

### P30: ¿Qué pasa si tengo problemas técnicos durante el workshop?

**R:** Soporte multi-canal: Troubleshooting Maestro → Telegram → Email (24-48h).

---

## 💰 PREGUNTAS FINANCIERAS

### P31: ¿Cuánto capital necesito para empezar a operar?

**R:** 
- **Durante workshop:** $0 (paper trading)
- **Live trading:** Mínimo $1,000-$2,000 USD

---

### P32: ¿Cuáles son los costos ocultos del trading algorítmico?

**R:** 
- Comisiones: $0.001-$0.005 por acción
- Slippage: 1-5% del P&L
- VPS: $5-20/mes (opcional)
- Datos premium: $10-50/mes (opcional)

---

### P33: ¿Hay descuentos para grupos o empresas?

**R:** **SÍ**. Grupos 5+: 15% descuento. Contacto: yismaryme@gmail.com

---

### P34: ¿Qué retorno puedo esperar de mi estrategia?

**R:** **Expectativas realistas:**
- Sharpe 1.0-1.5
- 20-30% drawdown
- Retorno anual: 10-30% (NO 100%+)

---

### P35: ¿Qué pasa si pierdo dinero en live trading después del workshop?

**R:** **El riesgo es tuyo**. Por eso: paper trading 8-12 semanas + empezar con 1-5% capital + nunca operar con dinero que no puedas perder.

---

## 🔍 ¿NO ENCONTRASTE TU PREGUNTA?

- [📖 Guía de Inicio](GUIA_INICIO.md)
- [🚨 Troubleshooting Maestro](Troubleshooting_Maestro.md)
- [📧 Email](mailto:yismaryme@gmail.com)
- [💬 Telegram](https://t.me/yismary)

---

## 🔗 NAVEGACIÓN

**🏠 Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**📖 Ver también:**
- [Troubleshooting Maestro](Troubleshooting_Maestro.md)
- [Programa Detallado](Programa_Detallado_Workshop.md)
- [Setup Completo](Guia_Setup_Completa.md)
- [SITEMAP](SITEMAP.md)

---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
