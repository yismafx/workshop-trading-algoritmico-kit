# 📋 STRATEGY MEMO TEMPLATE

> **Versión:** 1.0 (Básico - Público)  
> **Fecha creación:** [FECHA]  
> **Autor:** [TU NOMBRE]  
> **Status:** [Draft | Review | Active | Archived]

---

## ⚠️ DISCLAIMER

Este template es parte del **Workshop Trading Algorítmico Aumentado con IA Generativa**.
- El contenido es exclusivamente educativo
- NO constituye asesoría financiera
- El trading implica riesgo de pérdida de capital

---

## 🎯 EXECUTIVE SUMMARY

**Estrategia en 1 línea:**  
[Ej: "Mean reversion en SPY basada en desviación estándar de 20 días"]

**Edge hipotético:**  
[Ej: "Comprar cuando SPY cae -2σ de su media móvil, mantener 3 días"]

**Retorno esperado:**  
[Ej: "12-18% anual con Sharpe 1.2-1.5"]

**Capital requerido:**  
[Ej: "$10,000 mínimo para diversificación"]

---

## 1. HIPÓTESIS DE TRADING

### 1.1 Tesis Central

**¿Por qué esta estrategia debería funcionar?**

[Explica la lógica fundamental. Ejemplo:
"Los mercados tienden a sobrereaccionar en el corto plazo y revertir a la media. 
Estudios académicos (Chan, 2013) muestran que caídas extremas en índices seguidas 
de recuperación ocurren en ~60% de casos históricos."]

**Referencias:**
- [ ] Paper académico o libro: [Cita]
- [ ] Evento de mercado que valida: [Descripción]
- [ ] Backtest exploratorio: [Link o adjunto]

### 1.2 Condiciones de Mercado

**¿En qué entorno funciona mejor esta estrategia?**

- **Volatilidad:** [ ] Baja | [ ] Media | [X] Alta
- **Tendencia:** [ ] Alcista | [X] Neutral | [ ] Bajista
- **Régimen:** [Ej: "Funciona en mercados laterales con picos de volatilidad"]

---

## 2. ESPECIFICACIÓN TÉCNICA

### 2.1 Universo de Activos

**Activos a tradear:**
- [ ] Acciones (tickers): [SPY, QQQ, IWM]
- [ ] Forex: [EUR/USD]
- [ ] Cripto: [BTC/USD]
- [ ] Otros: [Especificar]

**Criterios de selección:**
[Ej: "ETFs líquidos con volumen >1M diario, spread <0.05%"]

### 2.2 Señales de Entrada

**Condición 1:**  
```python
# Ejemplo de pseudocódigo
if close < (sma_20 - 2 * std_20):
    signal = "BUY"
```

**Condición 2:**  
[Si aplica, agregar más condiciones]

**Filtros adicionales:**
- [ ] Volumen mínimo: [Especificar]
- [ ] Horario: [Ej: "Solo primeros 30 min de sesión"]
- [ ] Confirmación: [Ej: "Esperar 1 vela de confirmación"]

### 2.3 Señales de Salida

**Exit por objetivo:**  
[Ej: "Vender a los 3 días O cuando retorno >2%"]

**Stop-loss:**  
[Ej: "Salir si pérdida >-4% desde entrada"]

**Trailing stop:**  
[Si aplica: "Activar trailing stop de 50% cuando ganancia >3%"]

### 2.4 Gestión de Riesgo

**Tamaño de posición:**  
[Ej: "2% de capital por trade (Kelly Criterion ajustado)"]

**Máximo de posiciones simultáneas:**  
[Ej: "3 activos máximo"]

**Capital de reserva:**  
[Ej: "Mantener 20% en cash para oportunidades"]

---

## 3. BACKTEST INICIAL (Exploratorio)

### 3.1 Parámetros de Prueba

| Parámetro | Valor |
|-----------|-------|
| Periodo | [2018-01-01 a 2024-12-31] |
| Activos | [SPY] |
| Capital inicial | [$10,000] |
| Comisiones | [0.1% por trade] |
| Slippage | [0.05%] |

### 3.2 Resultados Preliminares

| Métrica | Valor | Benchmark (SPY) |
|---------|-------|-----------------|
| **Retorno anual** | [14.5%] | [12.0%] |
| **Sharpe Ratio** | [1.3] | [0.9] |
| **Max Drawdown** | [-22%] | [-34%] |
| **Win Rate** | [58%] | N/A |
| **Profit Factor** | [1.4] | N/A |
| **Nº Trades** | [45/año] | N/A |

### 3.3 ⚠️ Advertencias y Limitaciones

**Posibles sesgos detectados:**
- [ ] Lookahead bias: [¿Usaste información futura?]
- [ ] Survivorship bias: [¿Solo probaste con activos que sobrevivieron?]
- [ ] Data snooping: [¿Optimizaste parámetros hasta que "funcionó"?]

**Riesgos identificados:**
1. [Ej: "Sharpe 1.3 es bueno pero no excepcional. Puede ser ruido."]
2. [Ej: "Solo 6 años de datos. Necesita walk-forward validation."]
3. [Ej: "Drawdown -22% requiere estómago fuerte. ¿Puedo soportarlo?"]

---

## 4. VALIDACIÓN RIGUROSA (Por Hacer)

### 4.1 Walk-Forward Analysis

- [ ] Dividir datos en ventanas de entrenamiento/prueba
- [ ] Re-optimizar parámetros cada ventana
- [ ] Validar out-of-sample performance

**Status:** [ ] No iniciado | [ ] En progreso | [ ] Completado

### 4.2 Monte Carlo Simulation

- [ ] Simular 10,000 escenarios con orden aleatorio de trades
- [ ] Calcular percentiles de Max DD y retorno
- [ ] Validar que resultados no son "lucky path"

**Status:** [ ] No iniciado | [ ] En progreso | [ ] Completado

### 4.3 Paper Trading

- [ ] Ejecutar estrategia en cuenta demo 3-6 meses
- [ ] Monitorear slippage real vs. supuesto
- [ ] Documentar emociones y decisiones manuales

**Status:** [ ] No iniciado | [ ] En progreso | [ ] Completado

---

## 5. PLAN DE IMPLEMENTACIÓN

### 5.1 Tecnología

**Plataforma:**  
[ ] Python + Alpaca | [ ] TradingView (Pine Script) | [ ] MetaTrader 5

**Notebook principal:**  
[Link a notebook: `estrategia_mean_reversion_v1.ipynb`]

**Dependencias:**
```bash
# Librerías requeridas
yfinance==0.2.43
pandas==2.1.4
pandas-ta==0.3.14b0
alpaca-py==0.28.3
```

### 5.2 Checklist Pre-Lanzamiento

**Código:**
- [ ] Código revisado y comentado
- [ ] Tests unitarios para lógica crítica
- [ ] Manejo de errores (API caída, datos faltantes)
- [ ] Logging implementado

**Risk Management:**
- [ ] Stop-loss automático configurado
- [ ] Circuit breaker si pérdida >X% diaria
- [ ] Alertas por email/Telegram

**Monitoreo:**
- [ ] Dashboard de performance en tiempo real
- [ ] Registro de trades en Google Sheets / DB
- [ ] Revisión semanal programada

### 5.3 Cronograma

| Fase | Fecha Inicio | Fecha Fin | Status |
|------|--------------|-----------|--------|
| **Paper Trading** | [2025-01-15] | [2025-04-15] | Pendiente |
| **Análisis resultados** | [2025-04-16] | [2025-04-30] | Pendiente |
| **Live con capital mínimo** | [2025-05-01] | [2025-08-01] | Pendiente |
| **Scale-up** | [2025-08-01] | TBD | Pendiente |

---

## 6. GESTIÓN DE VERSIONES

### Version History

| Versión | Fecha | Cambios | Autor |
|---------|-------|---------|-------|
| 1.0 | [2025-01-10] | Memo inicial creado | [Nombre] |
| 1.1 | [Futuro] | Agregado walk-forward results | [Nombre] |

### Parámetros Actuales

| Parámetro | Valor Actual | Última Optimización |
|-----------|--------------|---------------------|
| `sma_period` | 20 | 2025-01-10 |
| `std_threshold` | 2.0 | 2025-01-10 |
| `hold_days` | 3 | 2025-01-10 |
| `stop_loss_pct` | -4% | 2025-01-10 |

**⚠️ Regla de oro:** NO cambiar parámetros impulsivamente por 1-2 trades malos.

---

## 7. POST-MORTEM DE TRADES

### Trade Log (Últimos 3)

**Trade #1:**
- **Fecha:** [2025-01-05]
- **Ticker:** SPY
- **Entrada:** $485.20 | **Salida:** $492.10
- **Retorno:** +1.42% ✅
- **Aprendizaje:** [Funcionó según plan. Sin cambios.]

**Trade #2:**
- **Fecha:** [2025-01-08]
- **Ticker:** SPY
- **Entrada:** $490.50 | **Salida:** $485.20
- **Retorno:** -1.08% ❌
- **Aprendizaje:** [Stop-loss activado correctamente. Noticias macro afectaron.]

**Trade #3:**
- **Fecha:** [Pendiente]

---

## 8. RECURSOS Y CONTACTO

### Documentos Relacionados

- 📊 [Backtest Report Completo](./Backtest_Report_v1.md)
- 💻 [Notebook de Implementación](./notebook_estrategia.ipynb)
- 📚 [Risk Management Plan](./Risk_Management_Plan.md)

### Referencias Bibliográficas

1. **Chan, E. (2013)**. *Algorithmic Trading: Winning Strategies and Their Rationale*. Wiley.
2. **López de Prado, M. (2018)**. *Advances in Financial Machine Learning*. Wiley.
3. **Carver, R. (2015)**. *Systematic Trading*. Harriman House.

### Soporte Workshop

- 📧 Email: yismaryme@gmail.com
- 💬 Telegram: [@yismafx](https://t.me/yismafx)
- 🔒 Grupo Premium: [Link para participantes]

---

## ✅ CHECKLIST DE COMPLETACIÓN

**Antes de considerar este memo "completo":**

- [ ] Todas las secciones 1-7 están llenas (no placeholders)
- [ ] Backtest exploratorio ejecutado
- [ ] Walk-forward O Monte Carlo completado
- [ ] Paper trading iniciado (mínimo 1 mes)
- [ ] Risk management definido con números específicos
- [ ] Código documentado y con tests básicos
- [ ] Al menos 3 trades documentados en post-mortem

**Status actual:** [ ] Draft | [ ] Ready for Paper Trading | [ ] Live

---

## 🎓 NOTAS DEL INSTRUCTOR

**¿Primera vez usando este template?**

Este es un template **básico** para empezar. En el contenido premium del workshop tendrás acceso a:
- ✅ Template avanzado con 15 secciones adicionales
- ✅ Checklist de 50 puntos de validación (López de Prado)
- ✅ Plantillas de análisis estadístico
- ✅ Integración con Notion/Obsidian
- ✅ 5+ ejemplos de Strategy Memos de estrategias reales

**Recuerda:**
> "Un Strategy Memo bien documentado es la diferencia entre un trader sistemático y un gambler con código."  
> — Adaptado de Carver (2015)

---

**Versión Template:** 1.0 (Público)  
**Última actualización:** 20 de noviembre de 2025  
**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa  
**Licencia:** Uso libre para participantes del workshop. No redistribuir sin permiso.
