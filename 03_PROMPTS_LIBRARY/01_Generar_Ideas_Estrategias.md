# 🧠 PROMPT 01: Generar Ideas de Estrategias de Trading

> **Categoría:** Ideación  
> **Sesión del Workshop:** S3 - Ideación de Estrategias con GenAI  
> **Dificultad:** ⭐⭐ (Básico-Intermedio)  
> **Plataformas:** Claude, ChatGPT, Gemini

---

## 🎯 Propósito del Prompt

Usar IA Generativa para **brainstorming de estrategias de trading algorítmico** basadas en:
- Tu experiencia como trader manual
- Patrones que has observado
- Activos que conoces bien

**NO esperes:** Estrategias listas para producción  
**SÍ esperes:** 5-10 hipótesis iniciales para investigar y validar

---

## 📋 Template del Prompt

```markdown
CONTEXTO:
Soy un trader [manual/con experiencia en X mercados] interesado en desarrollar 
mi primera estrategia de trading algorítmico. Mi experiencia principal es en 
[describe: acciones/forex/crypto/futuros] y he notado que [describe patrón 
que has observado manualmente].

ROL:
Actúa como un Quant Trader Senior especializado en estrategias cuantitativas 
sistemáticas. Has trabajado en hedge funds desarrollando estrategias en los 
estilos: mean reversion, momentum, statistical arbitrage, y breakout.

TAREA:
Genera 5 ideas de estrategias de trading algorítmico que:
1. Se alineen con el patrón que he observado
2. Sean implementables con datos gratuitos (yfinance, Alpaca)
3. Tengan lógica económica clara (no data mining)
4. Estén en el rango de complejidad para un principiante (evita ML complejo)

Para cada estrategia incluye:
- Nombre descriptivo
- Hipótesis (¿qué patrón explota?)
- Reglas de entrada (simple)
- Reglas de salida (simple)
- Activos sugeridos
- Timeframe recomendado
- Riesgos principales

FORMATO:
Presenta cada estrategia en formato de bullet points, máximo 150 palabras por estrategia.

RESTRICCIONES:
- NO sugieras estrategias que requieran datos pagos
- NO incluyas machine learning complejo (solo si el usuario tiene experiencia)
- NO prometas retornos específicos
- SÍ incluye advertencias de overfitting donde aplique
- SÍ menciona autores/papers si la estrategia es conocida

EJEMPLO DE OUTPUT ESPERADO:
"Estrategia 1: Mean Reversion en ETFs de Sectores
Hipótesis: Los ETFs sectoriales tienden a revertir a su media cuando se alejan 
>2 desviaciones estándar de su promedio móvil de 20 días..."
```

---

## 💡 Ejemplo de Uso Real

### Input del Usuario:

```markdown
CONTEXTO:
Soy trader manual con 3 años de experiencia en acciones tecnológicas (FAANG). 
He notado que después de earnings beats sorpresivos, las acciones suelen 
consolidar por 2-3 días antes de continuar subiendo.

ROL:
[Copiar del template arriba]

TAREA:
[Copiar del template arriba, personalizado:]
Genera 5 ideas de estrategias que exploten este patrón post-earnings en 
acciones tech de alta capitalización.

[... resto del prompt]
```

### Output Esperado de la IA:

```markdown
**Estrategia 1: Post-Earnings Momentum Continuation**
Hipótesis: Earnings beats >5% generan momentum que continúa 3-5 días después 
del anuncio, tras una consolidación inicial.
Entrada: Comprar al cierre del día 3 post-earnings si precio está +2% vs. pre-earnings
Salida: Vender después de 5 días o si precio cae -2%
Activos: AAPL, MSFT, GOOGL, META, NVDA
Timeframe: Diario
Riesgo: Earnings traps (beat seguido de corrección por guidance negativo)

**Estrategia 2: Mean Reversion Post-Earnings Overreaction**
[...]

[Total: 5 estrategias]
```

---

## ⚠️ Advertencias Críticas

### 1. Las Ideas NO Son Estrategias Validadas
```
IA genera HIPÓTESIS, no estrategias probadas
→ Debes hacer backtest riguroso
→ Validar con walk-forward
→ Paper trading antes de live
```

### 2. Riesgo de "Soundsgoodism"
```
Ideas que suenan bien ≠ Ideas que funcionan
→ IA no tiene acceso a datos reales
→ No sabe qué patrones realmente persisten
→ Puede sugerir estrategias "obvias" que ya no funcionan
```

### 3. Sesgo de Confirmación
```
Si le dices a la IA "creo que X funciona"
→ IA tenderá a confirmar tu creencia
→ Genera estrategias alineadas con tu sesgo
→ Solución: Pide también estrategias CONTRARIAS
```

---

## 🔧 Variaciones del Prompt

### Variación A: Pedir Estrategias Contrarias
```markdown
[Después de recibir las 5 estrategias]

"Ahora genera 3 estrategias que exploten el PATRÓN CONTRARIO. 
Por ejemplo, si sugeriste mean reversion, ahora sugiere momentum. 
Quiero probar ambos lados de la hipótesis."
```

### Variación B: Enfoque en Asset Class Específico
```markdown
TAREA:
Genera 5 estrategias EXCLUSIVAMENTE para:
- Activo: SPY (S&P 500 ETF)
- Restricción: Solo usar precio y volumen (no indicadores técnicos complejos)
- Holding period: 1-3 días máximo
```

### Variación C: Con Restricciones de Capital
```markdown
CONTEXTO ADICIONAL:
Tengo un capital de $10,000 y solo puedo hacer ~20 trades/año debido a 
restricciones de mi broker (comisiones altas).

TAREA:
Genera estrategias de baja frecuencia (swing trading) que requieran menos 
de 2 trades por mes en promedio.
```

---

## 📊 Siguiente Paso Después del Prompt

### 1. Filtrar las Ideas (Tu Criterio)
```
De las 5-10 ideas que recibes:
✅ Selecciona las 3 que MÁS sentido económico tienen
✅ Que puedas explicar a otra persona el "por qué"
✅ Que tengas acceso a datos para backtest

❌ Descarta las que suenan "mágicas"
❌ Las que requieren datos que no tienes
❌ Las que no entiendes completamente
```

### 2. Investigar Precedentes
```bash
# Busca en Google Scholar:
"[nombre del patrón] trading strategy" + "backtest"

# Busca en papers:
- SSRN.com
- ArXiv.org (sección q-fin)

Pregunta: ¿Alguien ya investigó esto? ¿Qué encontraron?
```

### 3. Especificación Técnica (Usa Prompt 02)
```
Toma la idea seleccionada
→ Usa "PROMPT 02: Convertir Idea en Especificación"
→ Genera pseudocódigo detallado
→ Identifica edge específico
```

---

## 🎓 Fundamento Teórico

### ¿Por Qué Usar IA para Ideación?

**Ventajas:**
- ✅ Genera combinaciones que no consideraste
- ✅ Expone a estrategias de otros estilos (mean rev, momentum, arbitrage)
- ✅ Acelera brainstorming (10 ideas en 2 minutos vs. 2 horas)

**Desventajas:**
- ❌ IA no sabe qué funciona REALMENTE (no tiene datos)
- ❌ Puede sugerir estrategias "clásicas" que ya no funcionan
- ❌ No entiende contexto de mercado actual (2024-2025)

**Principio clave:** (López de Prado, 2018)
> "La mayoría de las estrategias descubiertas son falsas. 
> La ideación debe ser abundante, la validación debe ser rigurosa."

---

## 📚 Recursos Complementarios

### Para Profundizar:
- **Chan, E. (2013)** - Cap. 3: "Mean Reversion Strategies"
- **Carver, R. (2015)** - Cap. 4: "Developing a Trading System"
- **Workshop S3** - Ideación de Estrategias con GenAI (video completo)

### Otros Prompts Relacionados:
- [PROMPT 02: Convertir Idea en Especificación](02_Convertir_Idea_a_Especificacion.md)
- [PROMPT 04: Adaptar Código Existente](04_Adaptar_Codigo_Existente.md)
- [PROMPT 10: Detectar Overfitting](10_Detectar_Overfitting.md)

---

## ✅ Checklist de Uso

Antes de usar este prompt:
- [ ] Tengo clara mi experiencia de trading manual
- [ ] Puedo describir UN patrón que he observado
- [ ] Sé qué activos/mercados me interesan

Después de usar este prompt:
- [ ] Recibí 5-10 ideas de estrategias
- [ ] Seleccioné 2-3 que tienen sentido económico
- [ ] Investigué si existen papers sobre estos patrones
- [ ] Estoy listo para hacer especificación técnica (Prompt 02)

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Autor:** Workshop Trading Algorítmico Aumentado con IA Generativa  
**Licencia:** Uso educativo libre

---

## 💬 Feedback

¿Te funcionó este prompt? ¿Generaste alguna idea prometedora?  
Comparte tu experiencia: yismaryme@gmail.com

¿Encontraste formas de mejorarlo?  
Pull requests bienvenidos: [GitHub repo](https://github.com/yismafx/workshop-trading-algoritmico-kit)
