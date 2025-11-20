# 🚨 PROMPT 10: Detectar Overfitting en Resultados de Backtest

> **Categoría:** Validación  
> **Sesión del Workshop:** S5 - Validación Rigurosa (Backtesting Profesional)  
> **Dificultad:** ⭐⭐⭐ (Intermedio-Avanzado)  
> **Plataformas:** Claude (recomendado), ChatGPT

---

## 🎯 Propósito del Prompt

Identificar si tus resultados de backtest son **demasiado buenos para ser verdad** y probablemente fruto de overfitting (ajuste excesivo a datos históricos).

**Principio clave:** (López de Prado, 2018)
> "El overfitting es el enemigo número uno del trading algorítmico.  
> Una estrategia sobreajustada funciona perfectamente en backtest y falla en live."

**Señales de alarma:**
- Sharpe Ratio > 3
- Win Rate > 80%
- Max Drawdown < 5%
- Curva de equity "demasiado suave"

---

## 📋 Template del Prompt

```markdown
CONTEXTO:
Acabo de hacer backtest de mi estrategia [describe brevemente] y los resultados 
parecen muy buenos. Quiero saber si es overfitting antes de arriesgar capital real.

ROL:
Actúa como un Quant Analyst especializado en validación de estrategias.  
Has visto cientos de backtests y sabes identificar overfitting sutil.  
Eres escéptico por naturaleza (como López de Prado).

MIS RESULTADOS DE BACKTEST:
```
Periodo: [Ej: 2015-2024, 10 años]
Total Trades: [Ej: 234]
Win Rate: [Ej: 67%]
Sharpe Ratio: [Ej: 2.8]
Max Drawdown: [Ej: -12%]
CAGR: [Ej: 24%]
Profit Factor: [Ej: 2.1]
Avg Win: [Ej: +2.3%]
Avg Loss: [Ej: -1.1%]
```

MI PROCESO DE DESARROLLO:
- Datos usados: [Ej: SPY 2015-2024 daily]
- ¿Optimicé parámetros? [Sí/No] [Si sí, cuáles y cómo]
- ¿Hice walk-forward? [Sí/No]
- ¿Out-of-sample testing? [Sí/No]
- Cambios que hice: [Ej: "Probé 5 variantes de la estrategia, esta dio mejores resultados"]

TAREA:
1. **ANÁLISIS DE RIESGO DE OVERFITTING:**
   Evalúa cada métrica e identifica red flags (0-10 puntos cada una)

2. **DIAGNÓSTICO:**
   - Probabilidad de overfitting: Baja / Media / Alta / Muy Alta
   - Justificación detallada (referencias a López de Prado)

3. **SEÑALES ESPECÍFICAS:**
   Lista las 3-5 señales más preocupantes en MIS resultados

4. **RECOMENDACIONES:**
   - Pruebas adicionales que debería hacer
   - Cómo reducir riesgo de overfitting
   - ¿Es seguro ir a paper trading?

FORMATO:
Usa tabla de scoring, colores 🟢🟡🔴, secciones claras.

RESTRICCIONES:
- NO seas complaciente (mejor falso positivo que falso negativo)
- SÍ usa criterios cuantitativos específicos (no "parece bien")
- SÍ referencia papers/libros cuando aplique
- NO ignores ninguna señal de alarma, por pequeña que sea
```

---

## 💡 Ejemplo de Uso Real

### Resultados Sospechosos:

```markdown
MIS RESULTADOS:
Periodo: 2010-2024 (14 años)
Total Trades: 487
Win Rate: 78%
Sharpe Ratio: 4.2
Max Drawdown: -6.5%
CAGR: 38%
Profit Factor: 3.8

MI PROCESO:
- Datos: SPY daily
- Optimicé: Sí, probé 20 combinaciones de parámetros (RSI thresholds 20-40)
- Walk-forward: No
- Out-of-sample: No
- Cambios: Probé esta estrategia después de descartar 3 que no funcionaron
```

### Output Esperado de la IA:

```markdown
## 🚨 ANÁLISIS DE RIESGO DE OVERFITTING

### Tabla de Scoring (0-10, donde 10 = máximo riesgo)

| Métrica | Valor | Benchmark | Score | Flag |
|---------|-------|-----------|-------|------|
| **Sharpe Ratio** | 4.2 | <2.5 aceptable | 9/10 | 🔴 |
| **Win Rate** | 78% | 50-65% típico | 8/10 | 🔴 |
| **Max Drawdown** | -6.5% | -15% a -25% realista | 8/10 | 🔴 |
| **Profit Factor** | 3.8 | 1.5-2.5 realista | 7/10 | 🟡 |
| **Total Trades** | 487 | >100 aceptable | 2/10 | 🟢 |
| **Optimización** | 20 combos | <5 combos seguro | 9/10 | 🔴 |
| **Walk-Forward** | No | Crítico | 10/10 | 🔴 |
| **Out-of-Sample** | No | Crítico | 10/10 | 🔴 |
| **Estrategias probadas** | 4 total | Data snooping | 7/10 | 🟡 |

**SCORE TOTAL: 70/90 = 78% de riesgo de overfitting**

---

## 🚨 DIAGNÓSTICO

### Probabilidad de Overfitting: **MUY ALTA (95%)**

### Justificación Detallada:

#### 1. Sharpe Ratio 4.2 (CRÍTICO 🔴)
**Por qué es problemático:**
> "Un Sharpe Ratio superior a 3 es extraordinariamente raro en estrategias reales.  
> Incluso fondos de hedge funds top tier (Renaissance, Citadel) tienen Sharpe ~2-2.5" 
> (López de Prado, 2018, p. 134)

**Contexto histórico:**
- Warren Buffett (1965-2023): Sharpe ~0.7
- Renaissance Medallion Fund: Sharpe ~2.8 (mejor del mundo)
- Tu estrategia: Sharpe 4.2 → **Más que los mejores traders profesionales**

**Probabilidad:** 99% de que este Sharpe NO se replicará en live trading.

---

#### 2. Win Rate 78% (CRÍTICO 🔴)
**Por qué es problemático:**
Mean reversion típicamente tiene win rate 55-65%.  
Win rate >75% sugiere:
- Selección de trades favorables (cherry-picking)
- Stop loss demasiado generoso (deja correr pérdidas)
- Parámetros optimizados para maximizar win rate

**Pregunta clave:**  
¿Tus pérdidas son pequeñas (-1%) o grandes (-10%)?  
Si son grandes, el win rate alto es ilusorio (Profit Factor revela la verdad).

---

#### 3. Max Drawdown -6.5% (CRÍTICO 🔴)
**Por qué es problemático:**
> "Un max drawdown <10% en 14 años es casi imposible sin apalancamiento extremo  
> o selección sesgada de parámetros" (Chan, 2013)

**Comparación realista:**
- SPY (2010-2024) Max DD: ~-34% (COVID-19)
- Estrategia conservadora: ~-15% a -20%
- Tu estrategia: -6.5% → **Evitó TODAS las crisis**

**Implicación:**  
La estrategia probablemente está calibrada para evitar drawdowns históricos conocidos  
(overfitting a eventos específicos: 2015-2016 corrección, COVID-19, etc.)

---

#### 4. Optimización Sin Walk-Forward (CRÍTICO 🔴)
**Proceso que seguiste:**
1. Probaste 20 combinaciones de parámetros RSI (ej: 20-25, 25-30, ..., 35-40)
2. Seleccionaste la que dio mejor Sharpe (digamos RSI 30-35)
3. NO validaste en periodo out-of-sample

**El problema:** (Bailey & López de Prado, 2014)
> "Probar múltiples configuraciones sin cross-validation garantiza overfitting.  
> Con 20 pruebas, estadísticamente 1 dará resultados excelentes por azar."

**Analogía:**
Es como lanzar 20 monedas y decir "esta moneda da cara el 90% del tiempo"  
porque en 10 lanzamientos dio 9 caras. Pura suerte.

---

#### 5. Data Snooping (MODERADO 🟡)
Probaste 4 estrategias en total:
- Estrategia A: Desechada (mala)
- Estrategia B: Desechada (mala)
- Estrategia C: Desechada (mala)
- Estrategia D: ¡Excelente! ← Esta

**El problema:**  
Los mismos datos vieron 4 estrategias.  
La probabilidad de que 1 de 4 funcione por azar es 25%.

**Solución recomendada:**  
Validar Estrategia D en datos completamente nuevos  
(ej: período 2024-actualidad si backtest fue 2010-2023).

---

## 🔴 SEÑALES ESPECÍFICAS MÁS PREOCUPANTES

### 1. Sharpe 4.2 sin walk-forward
**Riesgo:** 95% de colapso en live  
**Referencia:** López de Prado (2018), Cap. 11

### 2. Win Rate 78% + Max DD 6.5%
**Riesgo:** Estrategia "evita" pérdidas grandes artificialmente  
**Probable causa:** Stop loss optimizado para datos históricos

### 3. Optimización de 20 parámetros sin validación
**Riesgo:** Garantía matemática de overfitting  
**Referencia:** Bailey & López de Prado (2014), "The Deflated Sharpe Ratio"

### 4. Ausencia de periodo out-of-sample
**Riesgo:** No tienes NINGUNA evidencia de que funcione en datos no vistos  
**Estándar mínimo:** 30% de datos fuera de muestra

### 5. CAGR 38% constante por 14 años
**Riesgo:** Implica rendimiento superior a 99.9% de fondos profesionales  
**Realidad esperada:** CAGR colapsará a 5-12% en live (o negativo)

---

## 📋 RECOMENDACIONES CRÍTICAS

### ❌ NO vayas a paper trading aún
**Razón:** Riesgo 95% de que resultados sean falsos  
Perderás tiempo y capital (aunque sea simulado)

### ✅ SÍ haz estas validaciones ANTES:

#### 1. Walk-Forward Analysis (CRÍTICO)
```
Divide datos en 5 ventanas:
- Window 1: Train 2010-2012 | Test 2013
- Window 2: Train 2011-2013 | Test 2014
- Window 3: Train 2012-2014 | Test 2015
- Window 4: Train 2013-2015 | Test 2016
- Window 5: Train 2014-2016 | Test 2017

¿El Sharpe se mantiene >2 en TODAS las ventanas de test?
Si cae a <1 en alguna → Overfitting confirmado
```

**Tutorial:** Workshop S5, sección Walk-Forward

---

#### 2. Out-of-Sample Testing (CRÍTICO)
```
Reserva 2023-2024 (nunca vistos) para validación final.
¿Sharpe en out-of-sample >1.5?
Si Sharpe cae de 4.2 → 0.8 → Overfitting confirmado
```

---

#### 3. Prueba de Robustez de Parámetros
```python
# En lugar de RSI 30-35 fijo, prueba:
for oversold in [25, 30, 35, 40]:
    for overbought in [65, 70, 75, 80]:
        backtest_strategy(oversold, overbought)

# ¿Sharpe >2 con MÚLTIPLES combinaciones?
# O solo con 30-35 específico?
```

**Si solo funciona con 1 combinación:** Overfitting  
**Si funciona con 5+ combinaciones:** Robusto

---

#### 4. Monte Carlo Simulation
```python
# Mezcla aleatoriamente trades
# Genera 1000 curvas de equity alternativas
# ¿Tu Sharpe 4.2 está en top 5%?

# Si sí → Puede ser suerte
# Si no → Estrategia tiene edge real
```

**Tutorial:** Workshop S5, sección Monte Carlo

---

#### 5. Deflated Sharpe Ratio (Avanzado)
```python
from scipy import stats

def deflated_sharpe(sharpe, n_trials, n_obs):
    """
    Bailey & López de Prado (2014)
    """
    variance = ((1 + (sharpe ** 2) / 2) / (n_obs - 1)) * n_trials
    deflated_sr = sharpe - (sharpe * variance)
    return deflated_sr

# Tu caso:
deflated = deflated_sharpe(
    sharpe=4.2,
    n_trials=20,  # Probaste 20 combos
    n_obs=487     # Trades
)
print(f"Deflated Sharpe: {deflated:.2f}")
# Si <1.5 → Overfitting
```

---

## 🎯 CRITERIO DE DECISIÓN

### Puedes proceder a paper trading SI Y SOLO SI:
- [ ] Walk-forward Sharpe >1.5 en TODAS las ventanas
- [ ] Out-of-sample Sharpe >1.2
- [ ] Robustez: Funciona con ≥5 combinaciones de parámetros
- [ ] Max DD realista: -15% a -25%
- [ ] Win rate realista: 50-65%
- [ ] Lógica económica clara (no es "magia")

**Si falla alguno:** Rediseña la estrategia

---

## 📚 PARA PROFUNDIZAR

### Papers Obligatorios:
- **Bailey & López de Prado (2014):** "The Deflated Sharpe Ratio"
- **López de Prado (2018):** Cap. 11 "Backtesting"
- **Pardo (2008):** "The Evaluation and Optimization of Trading Strategies"

### Workshop:
- **S5:** Validación Rigurosa - Backtesting Profesional
- **S6:** Gestión Avanzada de Riesgo

---

## ✅ AUTOEVALUACIÓN

¿Entendiste las señales de overfitting? Responde:

1. ¿Por qué Sharpe >3 es sospechoso?
2. ¿Qué es walk-forward analysis?
3. ¿Cuál es el riesgo de optimizar 20 parámetros?
4. ¿Qué harías diferente en tu próximo backtest?
```

---

## ⚠️ Advertencia Final

### La IA Puede Ser Muy Optimista

Algunos LLMs tienden a:
- Subestimar riesgo de overfitting
- Dar false reassurance ("tus resultados son prometedores")
- No aplicar criterios estrictos de López de Prado

**Solución:**  
Si la IA dice "probabilidad de overfitting media", asume "alta".  
Siempre aplica validaciones adicionales.

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Autor:** Workshop Trading Algorítmico Aumentado con IA Generativa
