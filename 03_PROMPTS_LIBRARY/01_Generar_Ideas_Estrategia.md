# 🤖 PROMPT 01: Generar Ideas de Estrategia con GenAI

> **Categoría:** Ideación y Brainstorming  
> **Nivel:** Básico  
> **Sesión del Workshop:** S3 - Ideación de Estrategias  
> **Compatible con:** Claude, ChatGPT, Gemini

---

## 🎯 PROPÓSITO

Usar IA Generativa para generar hipótesis de estrategias de trading basadas en:
- Tus observaciones del mercado
- Conceptos que has escuchado pero no sabes cómo implementar
- Indicadores técnicos que quieres combinar de forma novedosa

**⚠️ Importante:** La IA genera *hipótesis*, NO estrategias validadas. Siempre requiere backtesting riguroso.

---

## 📋 ESTRUCTURA DEL PROMPT

Este prompt sigue el framework **ROL - CONTEXTO - TAREA - FORMATO - RESTRICCIONES**.

### Template Básico

```markdown
🎭 ROL:
Actúa como un quant trader profesional con 10+ años de experiencia en 
trading algorítmico. Tu especialidad es generar hipótesis de estrategias 
basadas en análisis técnico y anomalías de mercado.

📊 CONTEXTO:
Estoy desarrollando estrategias para [TIPO DE ACTIVO: acciones/forex/cripto].
Mi horizonte temporal es [TIMEFRAME: intraday/swing/posicional].
Tengo experiencia en [NIVEL: principiante/intermedio/avanzado].

Observación del mercado que quiero explorar:
[TU OBSERVACIÓN: Ej. "He notado que SPY tiende a recuperarse después de caídas 
súbitas de -2% o más en un solo día"]

🎯 TAREA:
Genera 3 hipótesis de estrategias cuantitativas basadas en mi observación. 
Para cada estrategia, especifica:

1. **Nombre descriptivo** (Ej: "Mean Reversion Post-Shock")
2. **Tesis fundamental** (¿Por qué debería funcionar?)
3. **Condiciones de entrada** (Señal específica)
4. **Condiciones de salida** (Stop-loss y take-profit)
5. **Indicadores técnicos requeridos** (Ej: SMA, RSI, Bollinger Bands)
6. **Riesgos principales** (¿Qué podría hacer que falle?)
7. **Referencias** (Papers académicos o traders conocidos que hayan explorado esto)

📤 FORMATO:
Presenta cada estrategia en una tabla estructurada.

⛔ RESTRICCIONES:
- NO uses estrategias que requieran machine learning complejo (por ahora)
- NO asumas que tengo acceso a datos de nivel 2 (order book)
- NO recomiendes estrategias con más de 5 parámetros a optimizar (riesgo de overfitting)
- SIEMPRE incluye advertencias sobre limitaciones conocidas
```

---

## 🔥 EJEMPLO DE USO REAL

### Input (Tu prompt al AI):

```markdown
🎭 ROL:
Actúa como un quant trader profesional con 10+ años de experiencia en 
trading algorítmico. Tu especialidad es generar hipótesis de estrategias 
basadas en análisis técnico y anomalías de mercado.

📊 CONTEXTO:
Estoy desarrollando estrategias para acciones de gran capitalización (S&P 500).
Mi horizonte temporal es swing trading (mantener 2-10 días).
Tengo experiencia intermedia en Python y trading manual.

Observación del mercado que quiero explorar:
"He notado que cuando el VIX sube bruscamente (+20% en un día), el SPY suele 
caer ese día pero recuperarse en los siguientes 3-5 días."

🎯 TAREA:
Genera 3 hipótesis de estrategias cuantitativas basadas en mi observación. 
Para cada estrategia, especifica:

1. Nombre descriptivo
2. Tesis fundamental
3. Condiciones de entrada
4. Condiciones de salida
5. Indicadores técnicos requeridos
6. Riesgos principales
7. Referencias

📤 FORMATO:
Presenta cada estrategia en una tabla estructurada.

⛔ RESTRICCIONES:
- NO uses estrategias que requieran machine learning complejo
- NO asumas que tengo acceso a datos de nivel 2
- NO recomiendes estrategias con más de 5 parámetros a optimizar
- SIEMPRE incluye advertencias sobre limitaciones conocidas
```

### Output Esperado (Lo que el AI responderá):

```markdown
Aquí están 3 hipótesis de estrategias basadas en tu observación VIX-SPY:

---

**ESTRATEGIA 1: VIX Spike Reversion**

| Componente | Detalle |
|------------|---------|
| **Nombre** | VIX Spike Mean Reversion |
| **Tesis** | Los picos de miedo (VIX) son sobrereacciones temporales. Cuando VIX sube +20% en un día, el mercado entra en pánico y sobrevendido, creando oportunidad de compra en SPY con alta probabilidad de rebote. Basado en fenómeno de "volatility clustering" (Mandelbrot, 1963). |
| **Entrada** | COMPRAR SPY cuando: <br>1. VIX sube ≥20% en el día <br>2. SPY cierra en rojo (-0.5% o más) <br>3. RSI(14) < 35 (confirmación de sobreventa) |
| **Salida** | VENDER cuando: <br>- Take-profit: SPY sube +2% desde entrada <br>- Stop-loss: SPY cae -3% desde entrada <br>- Tiempo máximo: 5 días (salir incluso si no hit TP/SL) |
| **Indicadores** | - VIX (diario) <br>- RSI(14) en SPY <br>- Precio de cierre SPY |
| **Riesgos** | 1. VIX puede seguir subiendo (crisis prolongada) <br>2. Correlación VIX-SPY puede romperse <br>3. Solo funciona en mercados líquidos normales |
| **Referencias** | - Whaley (1993): "Derivatives on Market Volatility" <br>- Chan (2013), Cap. 3: Mean Reversion Strategies |

---

**ESTRATEGIA 2: VIX Spike + Volume Confirmation**

[Similar estructura para Estrategia 2...]

---

**ESTRATEGIA 3: Multi-Timeframe VIX Divergence**

[Similar estructura para Estrategia 3...]

---

⚠️ **ADVERTENCIAS CRÍTICAS:**

1. Estas son HIPÓTESIS, no estrategias probadas
2. Debes hacer backtesting riguroso en al menos 5 años de datos
3. VIX spike strategies funcionan ~60-70% del tiempo históricamente, 
   pero los 30% de fallas pueden ser grandes drawdowns
4. NO ejecutes con dinero real sin validación walk-forward
```

---

## 💡 VARIACIONES DEL PROMPT

### Variación A: Partir de un Indicador Específico

```markdown
Observación del mercado que quiero explorar:
"Quiero combinar Bollinger Bands con el indicador MACD. He oído que 
'comprar cuando precio toca banda inferior Y MACD cruza al alza' funciona."

[Resto del prompt igual...]
```

### Variación B: Partir de Paper Académico

```markdown
Observación del mercado que quiero explorar:
"Leí el paper de Jegadeesh & Titman (1993) sobre momentum. 
Quiero adaptar su estrategia 'comprar ganadores, vender perdedores' 
al universo de ETFs en lugar de acciones individuales."

[Resto del prompt igual...]
```

### Variación C: Invertir Estrategia Conocida

```markdown
Observación del mercado que quiero explorar:
"Las estrategias de momentum funcionan en tendencias alcistas, 
pero ¿funcionaría INVERTIR las señales en mercados bajistas?"

[Resto del prompt igual...]
```

---

## ✅ CHECKLIST POST-GENERACIÓN

Después de recibir ideas del AI, valida:

- [ ] ¿La tesis fundamental tiene sentido lógico?
- [ ] ¿Puedo obtener los datos necesarios gratis/barato?
- [ ] ¿Los indicadores son estándar (disponibles en pandas-ta)?
- [ ] ¿La estrategia tiene ≤5 parámetros a optimizar?
- [ ] ¿El AI citó alguna referencia académica/profesional?
- [ ] ¿El AI mencionó riesgos específicos?

**Si 4+ checks = ✅:** Vale la pena hacer backtest exploratorio  
**Si <4 checks = ✅:** Refina el prompt o pide otra iteración

---

## 🎓 TIPS DE EXPERTO

### 1. Sé Específico en Tu Observación

❌ **Malo:** "Quiero una estrategia de trading"  
✅ **Bueno:** "He notado que AAPL tiende a subir los viernes antes de earnings"

### 2. Menciona Tu Nivel de Experiencia

Esto ayuda al AI a calibrar complejidad:
- Principiante → Estrategias simples (1-2 indicadores)
- Intermedio → Estrategias con filtros (3-4 condiciones)
- Avanzado → Estrategias con multi-timeframe

### 3. Itera con Follow-ups

```markdown
Prompt inicial: [Genera 3 estrategias...]

Follow-up 1: "La Estrategia 2 me interesa. Profundiza en cómo 
             manejar el sizing cuando hay múltiples señales simultáneas."

Follow-up 2: "¿Qué ajustes necesitaría para aplicar esto a criptomonedas 
             en lugar de acciones?"
```

### 4. Usa Este Prompt ANTES de Codificar

```
Flujo correcto:
1. Usar este prompt → Generar hipótesis
2. Seleccionar 1-2 hipótesis interesantes
3. Hacer backtest exploratorio manual
4. Solo SI pasa backtest → Codificar completo
```

---

## 🔗 PRÓXIMOS PASOS

**Después de tener tus 3 hipótesis:**

1. **Documenta** en tu [Strategy Memo Template](../../02_TEMPLATE_PACK/Strategy_Memo_Template.md)
2. **Pseudocódigo** → Usa Prompt 03: "Convertir Idea a Pseudocódigo"
3. **Backtest** → Aprende en Sesión 5 del workshop
4. **Validación** → Walk-forward (Sesión 5)

---

## 📚 RECURSOS ADICIONALES

### En el Workshop Premium:

- 🔒 **Prompt 01B:** Generar Estrategias Adaptativas (Machine Learning)
- 🔒 **Prompt 01C:** Estrategias Multi-Asset con Correlaciones
- 🔒 **Prompt 01D:** Estrategias de Crisis (Black Swan Events)
- 🔒 **Biblioteca de 100+ Observaciones de Mercado** para usar como seeds

### Lecturas Recomendadas:

- **Chan, E. (2013)** - Algorithmic Trading, Cap. 3
- **Jegadeesh & Titman (1993)** - "Returns to Buying Winners and Selling Losers"
- **López de Prado (2018)** - Advances in Financial ML, Cap. 2

---

## 💬 SOPORTE

**¿Tienes dudas sobre este prompt?**

📧 Email: yismaryme@gmail.com  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Solo participantes del workshop]

---

**Versión:** 1.0 (Público)  
**Última actualización:** 20 de noviembre de 2025  
**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa
