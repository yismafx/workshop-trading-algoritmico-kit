# 🤖 PROMPT 05: Interpretar Métricas de Backtesting

> **Categoría:** Análisis y Validación  
> **Nivel:** Intermedio  
> **Sesión del Workshop:** S5 - Backtesting Profesional  
> **Compatible con:** Claude, ChatGPT, Gemini

---

## 🎯 PROPÓSITO

Entender si los resultados de tu backtest son:
- **Buenos** (vale la pena llevar a paper trading)
- **Sospechosos** (posible overfitting o bugs)
- **Malos** (mejor descartarlos o ajustar)

Y más importante: **¿POR QUÉ?** Con explicaciones basadas en Chan, López de Prado, y Carver.

**⚠️ Importante:** Métricas buenas en backtest NO garantizan éxito en live trading. Este prompt te ayuda a identificar red flags.

---

## 📋 ESTRUCTURA DEL PROMPT

### Template Básico

```markdown
🎭 ROL:
Actúa como un analista quant senior evaluando resultados de backtest.
Tu misión es detectar overfitting, data snooping, y otros problemas que 
traders novatos suelen pasar por alto.

📊 CONTEXTO:
Hice backtest de mi estrategia [NOMBRE ESTRATEGIA] en [ACTIVO] desde [FECHA INICIO] 
hasta [FECHA FIN] (duración: [X AÑOS]).

Tipo de estrategia: [Momentum | Mean Reversion | Arbitrage | etc.]
Timeframe: [Intraday | Daily | Weekly]
Capital inicial: $[MONTO]

Resultados del backtest:
```
Total Return: [X%]
Annualized Return: [Y%]
Sharpe Ratio: [Z]
Max Drawdown: [W%]
Win Rate: [%]
Profit Factor: [Valor]
Total Trades: [N]
Avg Trade Duration: [X días/horas]
```

🎯 TAREA:
Analiza estos resultados y dame:

1. **Veredicto general** (Bueno/Sospechoso/Malo) con calificación 1-10
2. **Análisis métrica por métrica:**
   - ¿Cada métrica está en rango saludable?
   - ¿Hay inconsistencias entre métricas?
3. **Red flags detectados** (overfitting, pocos trades, etc.)
4. **Comparación con benchmark:** ¿Le gana a Buy & Hold del activo?
5. **Recomendación:** ¿Qué hacer a continuación?

📤 FORMATO:
Estructura tu respuesta en las 5 secciones claramente separadas.
Usa tabla para comparar con benchmarks.

⛔ RESTRICCIONES:
- NO me felicites si los resultados son sospechosos
- SIEMPRE señala si Sharpe >2.5 (posible overfitting)
- SIEMPRE valida si hay suficientes trades (mínimo 30)
- Cita a Chan/López de Prado/Carver cuando sea relevante
```

---

## 🔥 EJEMPLO DE USO REAL

### Input (Tu prompt al AI):

```markdown
🎭 ROL:
Actúa como analista quant senior evaluando backtest.
Detecta overfitting y problemas que novatos pasan por alto.

📊 CONTEXTO:
Hice backtest de mi estrategia "SMA Crossover 20/50" en SPY desde 
2015-01-01 hasta 2024-12-31 (duración: 10 años).

Tipo de estrategia: Momentum (cruce de medias móviles)
Timeframe: Daily
Capital inicial: $10,000

Resultados del backtest:
```
Total Return: 85.3%
Annualized Return: 6.4%
Sharpe Ratio: 1.15
Max Drawdown: -28.5%
Win Rate: 48%
Profit Factor: 1.32
Total Trades: 42
Avg Trade Duration: 87 días
Largest Win: +12.3%
Largest Loss: -8.7%
```

🎯 TAREA:
[Estructura completa del template...]
```

### Output Esperado (Lo que el AI responderá):

```markdown
# ═══════════════════════════════════════════════════════════════
# 1. VEREDICTO GENERAL
# ═══════════════════════════════════════════════════════════════

**Calificación: 6.5/10 - ACEPTABLE CON RESERVAS**

**Resumen:**
Esta estrategia muestra resultados *razonables pero no excepcionales*. 
Los números están en rangos realistas (no hay red flags de overfitting grosero), 
pero hay áreas de preocupación que requieren validación adicional.

**¿Vale la pena continuar?** 
✅ SÍ - Pero solo si pasa walk-forward validation.

# ═══════════════════════════════════════════════════════════════
# 2. ANÁLISIS MÉTRICA POR MÉTRICA
# ═══════════════════════════════════════════════════════════════

## 📈 Total Return: 85.3% (10 años)

**Interpretación:** Ganancia de 85.3% en una década.

**¿Es bueno?**
- 🟡 MODERADO
- SPY (Buy & Hold) en mismo periodo: ~200%+ (aprox)
- Tu estrategia UNDERPERFORM vs. simplemente comprar y mantener

**Comentario de experto (Chan, 2013):**
> "Una estrategia activa debe superar Buy & Hold después de costos, 
> o no justifica el esfuerzo y riesgo adicional."

**Acción:** Calcula retorno de SPY B&H en tu periodo exacto para comparar.

---

## 📊 Annualized Return: 6.4%

**Interpretación:** Promedio de ganancia anual.

**¿Es bueno?**
- 🟡 MODERADO
- S&P 500 promedio histórico: ~10% anual
- Bonos del tesoro USA: ~3-4% anual

**Benchmark:**
| Estrategia | Retorno Anual |
|-----------|---------------|
| Tu estrategia SMA | 6.4% |
| SPY Buy & Hold | ~7-10% (depende del periodo) |
| Cartera 60/40 (acciones/bonos) | ~7% |

**Veredicto:** Está en rango aceptable pero no es excepcional.

---

## 🎯 Sharpe Ratio: 1.15

**Interpretación:** Retorno ajustado por riesgo (volatilidad).

**¿Es bueno?**
- ✅ BUENO
- Sharpe < 0: Pierdes dinero
- Sharpe 0-1: Retorno no justifica riesgo
- **Sharpe 1-2: BUENO (mayoría de estrategias retail)** ← Tú estás aquí
- Sharpe > 2: Excelente (nivel profesional)
- Sharpe > 3: SOSPECHOSO (posible overfitting)

**Comentario de experto (López de Prado, 2018):**
> "Sharpe > 2.5 en backtest suele ser data snooping. 
> Sharpe 1.0-1.5 es lo que deberías esperar en estrategias simples."

**Veredicto:** ✅ Sharpe 1.15 es realista y saludable.

---

## 📉 Max Drawdown: -28.5%

**Interpretación:** Peor caída desde pico hasta valle.

**¿Es bueno?**
- ⚠️ PREOCUPANTE
- Drawdowns típicos:
  - < -15%: Excelente
  - -15% a -25%: Aceptable
  - **-25% a -35%: Alto (requiere estómago fuerte)** ← Tú estás aquí
  - > -35%: Muy alto (mayoría abandona)

**Pregunta crítica:**
¿Podrías VER -28.5% en tu cuenta y NO entrar en pánico?
Si la respuesta es NO, esta estrategia no es para ti.

**Comentario de experto (Carver, 2015):**
> "Max DD en backtest suele ser 1.5x menor que en live trading. 
> Si backtested DD = -28%, espera -42% en realidad."

**Veredicto:** ⚠️ Limite superior de tolerancia para retail trader.

---

## 🎲 Win Rate: 48%

**Interpretación:** Porcentaje de trades ganadores.

**¿Es bueno?**
- ✅ REALISTA
- Win Rate NO es métrica crítica por sí sola
- Más importante: Profit Factor (cuánto ganas vs. pierdes)

**Análisis:**
- 48% win rate con Profit Factor 1.32 = Ganas más cuando ganas que lo que pierdes
- Estrategia de "cortar pérdidas, dejar correr ganancias"

**Veredicto:** ✅ Win Rate <50% es NORMAL y aceptable.

---

## 💰 Profit Factor: 1.32

**Interpretación:** Ratio de ganancias totales / pérdidas totales.

**¿Es bueno?**
- 🟡 JUSTO EN EL LÍMITE
- PF < 1.0: Pierdes dinero
- **PF 1.0-1.5: Breakeven a marginal** ← Tú estás aquí
- PF 1.5-2.0: Bueno
- PF > 2.0: Muy bueno
- PF > 3.0: Sospechoso (posible overfitting)

**Cálculo implícito:**
- Si ganaste $13,200 y perdiste $10,000, PF = 1.32
- Significa: Por cada $1 que pierdes, ganas $1.32

**Veredicto:** ⚠️ Margen muy ajustado. Costos de transacción pueden eliminarlo.

---

## 📊 Total Trades: 42

**Interpretación:** Número de operaciones en 10 años.

**¿Es suficiente?**
- ⚠️ LÍMITE INFERIOR
- Regla de oro (López de Prado): Mínimo 30 trades para significancia estadística
- 42 trades / 10 años = ~4 trades/año (muy poco frecuente)

**Problema:**
Con solo 42 trades, es difícil confiar en las estadísticas.
Un par de trades "lucky" pueden inflar el Sharpe artificialmente.

**Veredicto:** ⚠️ Justo en el límite. Idealmente >100 trades.

---

## ⏱️ Avg Trade Duration: 87 días

**Interpretación:** Mantienes posiciones ~3 meses.

**¿Es coherente con la estrategia?**
- ✅ SÍ
- SMA 20/50 es estrategia de swing/posición (no intraday)
- 87 días = ~4 meses es razonable para este tipo

**Implicación:**
- Menos trades = Menos comisiones ✅
- Menos trades = Menor significancia estadística ⚠️

**Veredicto:** ✅ Coherente con tipo de estrategia.

---

## 🏆 Largest Win vs. Largest Loss

**Win:** +12.3%  
**Loss:** -8.7%

**¿Es bueno?**
- ✅ POSITIVO
- Ganancias grandes > Pérdidas grandes (asimetría favorable)
- Ratio: 12.3 / 8.7 = 1.41 (bueno)

**Pregunta crítica:**
¿Cómo manejaste la pérdida de -8.7%? ¿Fue por stop-loss o aguantar?
Si aguantaste esperando rebote, es riesgoso.

**Veredicto:** ✅ Asimetría favorable (característica de estrategia saludable).

# ═══════════════════════════════════════════════════════════════
# 3. RED FLAGS DETECTADOS
# ═══════════════════════════════════════════════════════════════

## 🚩 Red Flag #1: Underperformance vs. Buy & Hold

**Problema:**
Si SPY subió ~200% en 10 años y tu estrategia solo 85%, 
¿para qué complicarse con trading activo?

**Causa posible:**
- Saliste del mercado en tendencias alcistas largas
- Costos de transacción comen las ganancias
- Timing de entradas/salidas no es óptimo

**Solución:**
Compara DIRECTAMENTE con B&H en tu código:
```python
buy_hold_return = (df['Close'][-1] / df['Close'][0]) - 1
print(f"Buy & Hold: {buy_hold_return:.2%}")
```

---

## 🚩 Red Flag #2: Profit Factor Marginal (1.32)

**Problema:**
PF = 1.32 significa que tu edge es pequeño.
Con comisiones (0.1% por lado = 0.2% roundtrip), tu edge puede desaparecer.

**Cálculo:**
42 trades × 0.2% comisión = 8.4% de drag
85.3% return - 8.4% comisiones = 76.9% net (14% menos)

**Solución:**
1. Incluye costos de transacción en tu backtest
2. Si PF cae <1.2 después de costos, descarta estrategia

---

## 🚩 Red Flag #3: Pocos Trades (42)

**Problema:**
Con 42 trades, el p-value de tu Sharpe es débil.
Puede ser suerte estadística, no edge real.

**Test:**
Haz Monte Carlo simulation:
- Baraja orden de trades aleatoriamente 10,000 veces
- Calcula Sharpe en cada shuffle
- Si 30% de shuffles dan Sharpe >1.15, tu resultado es ruido

**Solución:**
Implementa walk-forward analysis para validar robustez.

---

## 🚩 Red Flag #4: Max DD Alto (-28.5%)

**Problema:**
En live trading, es probable que experimentes -35% a -40% drawdown.
¿Seguirías el sistema después de ver -40%?

**Test psicológico:**
Imagina que inviertes $50,000:
- Drawdown de -40% = Ver $20,000 evaporarse
- ¿Tendrías disciplina para NO cerrar posiciones en pánico?

**Solución:**
Si DD te asusta, reduce tamaño de posición (trade con menos capital).

# ═══════════════════════════════════════════════════════════════
# 4. COMPARACIÓN CON BENCHMARK
# ═══════════════════════════════════════════════════════════════

| Métrica | Tu Estrategia | SPY B&H* | Cartera 60/40* | Veredicto |
|---------|---------------|----------|----------------|-----------|
| **Total Return** | 85.3% | ~200% | ~100% | ❌ Pierde |
| **Ann. Return** | 6.4% | ~10% | ~7% | ⚠️ Igual a 60/40 |
| **Sharpe Ratio** | 1.15 | ~0.8 | ~0.9 | ✅ Gana |
| **Max DD** | -28.5% | -35% | -20% | 🟡 Intermedio |
| **Volatilidad** | Media | Alta | Baja | 🟡 Intermedio |

*Valores aproximados para periodo 2015-2024

**Conclusión:**
- Tu estrategia tiene MEJOR Sharpe (menos volatilidad para el retorno)
- Pero tiene PEOR retorno absoluto que B&H

**Ideal para:**
- Inversionistas adversos al riesgo
- Quienes prefieren crecimiento estable vs. explosivo

**No ideal para:**
- Quienes buscan maximizar retorno absoluto
- Horizonte largo plazo (>10 años) donde B&H suele ganar

# ═══════════════════════════════════════════════════════════════
# 5. RECOMENDACIÓN
# ═══════════════════════════════════════════════════════════════

## 🎯 VEREDICTO FINAL: PROCEDER CON VALIDACIÓN ADICIONAL

**NO ejecutes con dinero real todavía.** Sigue estos pasos:

### ✅ Paso 1: Walk-Forward Analysis (CRÍTICO)

```python
# Divide datos en ventanas de 2 años
# Entrena en ventana 1, testa en ventana 2
# Si Sharpe out-of-sample >0.8, es prometedor
```

**Meta:** Sharpe out-of-sample >1.0  
**Si falla:** Descarta estrategia (era overfitting)

---

### ✅ Paso 2: Incluir Costos de Transacción

```python
# Agregar comisiones + slippage
commission = 0.001  # 0.1% por lado
slippage = 0.0005   # 0.05% de slippage

# Recalcular todas las métricas
# Si Profit Factor cae <1.15, replantear
```

**Meta:** PF >1.3 después de costos  
**Si falla:** Reducir frecuencia de trading

---

### ✅ Paso 3: Paper Trading (3-6 Meses)

**Objetivo:** Validar que backtest se traduce a realidad

**Qué monitorear:**
- Slippage real vs. supuesto
- Ejecución de órdenes (¿se llenan?)
- Tu psicología (¿puedes seguir el sistema?)

**Meta:** Sharpe en paper >0.9  
**Si falla:** Hay diferencia backtest-realidad

---

### ✅ Paso 4: Mejoras Potenciales

**Antes de pasar a live, considera:**

1. **Agregar filtro de volatilidad:**
   - No tradear cuando VIX >30 (mercado caótico)
   
2. **Position sizing dinámico:**
   - Reducir tamaño en drawdown, aumentar en racha ganadora
   
3. **Stop-loss adaptativo:**
   - En lugar de fijo, usar ATR-based stop

4. **Combinar con otra estrategia:**
   - SMA + RSI para filtrar señales débiles

---

## 📚 LECTURAS RECOMENDADAS

**Para profundizar en interpretación de métricas:**

1. **López de Prado (2018)** - Cap. 11: "The Dangers of Backtesting"
2. **Chan (2013)** - Cap. 2: "Evaluating Strategy Performance"
3. **Carver (2015)** - Cap. 7: "Understanding Risk and Returns"
4. **Bailey & López de Prado (2014)** - "The Deflated Sharpe Ratio"

---

## ⚠️ ADVERTENCIA FINAL

```
Métricas buenas en backtest ≠ Garantía de éxito en live

Pasos obligatorios antes de dinero real:
1. Walk-forward validation ✅
2. Paper trading 3+ meses ✅
3. Empezar con capital pequeño (1-5% del total) ✅
4. Revisar performance cada mes ✅

NO saltarse estos pasos por impaciencia.
```
```

---

## 💡 VARIACIONES DEL PROMPT

### Variación A: Comparar Dos Estrategias

```markdown
📊 CONTEXTO:
Tengo backtest de DOS estrategias. No sé cuál es mejor.

Estrategia A (Mean Reversion):
[Métricas A]

Estrategia B (Momentum):
[Métricas B]

🎯 TAREA:
1. Compara ambas lado a lado
2. ¿Cuál tiene mejor risk-adjusted return?
3. ¿Cuál es más robusta (menos overfitting)?
4. ¿Puedo combinarlas para diversificar?
```

### Variación B: Detectar Overfitting Específico

```markdown
📊 CONTEXTO:
Mi estrategia tiene Sharpe 3.8 en backtest.
Creo que es demasiado bueno para ser verdad.

🎯 TAREA:
1. ¿Qué % de probabilidad es overfitting?
2. ¿Qué pruebas adicionales debo hacer?
3. ¿Cómo "deflate" el Sharpe (López de Prado)?
4. ¿Qué métricas alternativas revisar?
```

### Variación C: Análisis Post-Mortem (Estrategia que Falló)

```markdown
📊 CONTEXTO:
Backtest: Sharpe 1.5 → Paper trading: Sharpe 0.3

¿Qué salió mal?

🎯 TAREA:
1. Causas comunes de degradación backtest→live
2. ¿Cómo detectar esto ANTES de paper trading?
3. ¿Es recuperable o descarto la estrategia?
```

---

## ✅ CHECKLIST DE ANÁLISIS

Usa esta lista para evaluar TU backtest:

- [ ] Total return >10% anual
- [ ] Sharpe >1.0 (>1.5 ideal)
- [ ] Max DD <-30%
- [ ] Profit Factor >1.5
- [ ] Total trades >30 (>100 ideal)
- [ ] Win rate coherente con tipo de estrategia
- [ ] Le gana a Buy & Hold (o justifica por menor DD)
- [ ] Incluí costos de transacción
- [ ] Validé con walk-forward
- [ ] Paper trading ejecutado (3+ meses)

**Mínimo para avanzar:** 7/10 checks ✅

---

## 📚 RECURSOS ADICIONALES

### En el Workshop Premium:

- 🔒 **Prompt 05B:** Análisis de Equity Curve (visualización)
- 🔒 **Prompt 05C:** Deflated Sharpe Ratio Calculator
- 🔒 **Prompt 05D:** Monte Carlo Simulation Setup
- 🔒 **Dashboard Interactivo** de Métricas con Plotly

### Calculadoras Online:

- **Portfolio Visualizer:** portfoliovisualizer.com
- **QuantStats:** pypi.org/project/quantstats
- **PyFolio:** Librería de Quantopian (open source)

---

## 💬 SOPORTE

**¿Dudas sobre tus métricas?**

📧 Email: yismaryme@gmail.com (envía resumen de métricas)  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Code reviews + análisis de backtests]

**Recuerda:** Es mejor preguntar antes de perder dinero real.

---

**Versión:** 1.0 (Público)  
**Última actualización:** 20 de noviembre de 2025  
**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa
