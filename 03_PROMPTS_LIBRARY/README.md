# 🤖 PROMPTS LIBRARY - Versión Pública

> **Workshop:** Trading Algorítmico Aumentado con IA Generativa  
> **Versión:** 1.0 (Público)  
> **Última actualización:** Noviembre de 2025

**🏠 [← Volver al Inicio](../README.md)** | **📋 [Ver Templates](../02_TEMPLATE_PACK/)** | **🐍 [Ver Scripts](../04_SCRIPTS_AUXILIARES/)**

---

## 🎯 ¿Qué es esto?

Biblioteca de **prompts probados y optimizados** para usar IA Generativa (Claude, ChatGPT, Gemini) en cada etapa del desarrollo de estrategias de trading algorítmico.

**Concepto clave:** GenAI = Copiloto (no piloto automático)

---

## 📂 Contenido Disponible (5 Prompts Públicos)

| # | Prompt | Categoría | Sesión | Nivel | Archivo |
|---|--------|-----------|--------|-------|---------|
| 01 | **Generar Ideas de Estrategia** | Ideación | S3 | Básico | [Ver →](01_Generar_Ideas_Estrategias.md) |
| 04 | **Adaptar Código Existente** | Implementación | S4 | Intermedio | [Ver →](04_Adaptar_Codigo_Existente.md) |
| 05 | **Explicar Código Complejo** | Comprensión | Todas | Básico | [Ver →](05_Explicar_Codigo_Complejo.md) |
| 06 | **Depurar Errores** | Debugging | S4-S5 | Intermedio | [Ver →](06_Depurar_Errores.md) |
| 10 | **Detectar Overfitting** | Validación | S5 | Avanzado | [Ver →](10_Detectar_Overfitting.md) |

### 📋 Descripción de Cada Prompt

#### 01 - [Generar Ideas de Estrategia](01_Generar_Ideas_Estrategias.md)

**¿Para qué?**  
Generar hipótesis de estrategias cuantitativas basadas en tus observaciones del mercado.

**Input típico:** "He notado que SPY sube después de caídas fuertes"  
**Output:** 3 estrategias con tesis, condiciones de entrada/salida, riesgos

**Cuándo usar:**
- Sesión 3 del workshop (Ideación)
- Cuando tienes observación pero no sabes cómo cuantificarla
- Para generar variaciones de estrategia conocida

---

#### 04 - [Adaptar Código Existente](04_Adaptar_Codigo_Existente.md)

**¿Para qué?**  
Modificar código de estrategias encontradas en libros/GitHub a tus necesidades.

**Input típico:** Código que funciona para SPY diario → Quieres BTC 4h  
**Output:** Código adaptado con comentarios en líneas cambiadas

**Cuándo usar:**
- Sesión 4 (Implementación)
- Cuando encuentras estrategia interesante pero para otro activo/timeframe
- Para agregar funcionalidades (stop-loss, logging, etc.)

---

#### 05 - [Explicar Código Complejo](05_Explicar_Codigo_Complejo.md)

**¿Para qué?**  
Entender código de trading que te parece confuso línea por línea.

**Input típico:** Código con z-score, rolling(), .shift()  
**Output:** Explicación pedagógica con analogías del trading manual

**Cuándo usar:**
- Siempre que no entiendas código ajeno
- Antes de adaptar código (necesitas entenderlo primero)
- Para aprender conceptos nuevos (vectorización, pandas avanzado)

---

#### 06 - [Depurar Errores](06_Depurar_Errores.md)

**¿Para qué?**  
Resolver errores de código de forma sistemática con ayuda de IA.

**Input típico:** Código + traceback completo  
**Output:** Diagnóstico, solución, explicación, prevención, test case

**Cuándo usar:**
- Sesión 4-5 (Implementación y Backtesting)
- Cuando código da error y no sabes por qué
- Cuando resultados son sospechosos (posible bug lógico)

---

#### 10 - [Detectar Overfitting](10_Detectar_Overfitting.md)

**¿Para qué?**  
Identificar si resultados de backtest son overfitting o reales.

**Input típico:** Sharpe 4.2, Max DD -6%, Win Rate 78%, etc.  
**Output:** Análisis de riesgo, scoring, red flags, recomendaciones

**Cuándo usar:**
- Sesión 5 (Validación Rigurosa)
- Después de ejecutar backtest con resultados "muy buenos"
- Antes de decidir si continuar con paper trading

---

## 🔒 Contenido Premium (30+ Prompts Adicionales)

En el **workshop completo** recibes:

### Ideación Avanzada (S3):
- 🔒 P01B: Estrategias Adaptativas (Machine Learning)
- 🔒 P01C: Multi-Asset con Correlaciones
- 🔒 P01D: Estrategias de Crisis (Black Swan)
- 🔒 P01E: Generar desde Paper Académico
- 🔒 P01F: Invertir Estrategia Conocida

### Implementación Avanzada (S4):
- 🔒 P02B: Optimizar Performance (vectorización)
- 🔒 P02C: Python → Pine Script (TradingView)
- 🔒 P02D: Python → MQL5 (MetaTrader)
- 🔒 P02E: Agregar Risk Management Avanzado
- 🔒 P02F: Paralelizar Backtesting

### Backtesting Riguroso (S5):
- 🔒 P03A: Diseñar Walk-Forward Analysis
- 🔒 P03B: Monte Carlo Simulation
- 🔒 P03C: Detectar Lookahead Bias Automáticamente
- 🔒 P03D: Calcular Deflated Sharpe Ratio
- 🔒 P03E: Analizar Equity Curve (visual)

### Risk Management (S6):
- 🔒 P04A: Calcular Position Size (Kelly, Fixed Fractional)
- 🔒 P04B: Diseñar Stop-Loss Dinámico (ATR-based)
- 🔒 P04C: Portfolio Diversification
- 🔒 P04D: Circuit Breakers (cuándo detener bot)

### Multi-Plataforma (S7):
- 🔒 P05A: Configurar Webhooks (TradingView → Alpaca)
- 🔒 P05B: Integrar con Interactive Brokers API
- 🔒 P05C: Sincronizar Múltiples Cuentas
- 🔒 P05D: Testear Estrategia Cross-Exchange

### Deployment (S8):
- 🔒 P06A: Setup VPS para Bot 24/7
- 🔒 P06B: Implementar Logging Profesional
- 🔒 P06C: Configurar Alertas (Email/Telegram/SMS)
- 🔒 P06D: Crear Dashboard de Monitoreo

### Documentación (S9):
- 🔒 P07A: Escribir README Técnico
- 🔒 P07B: Generar Docstrings Automáticamente
- 🔒 P07C: Crear Tutorial de Instalación
- 🔒 P07D: Documentar API de Funciones

---

## 📖 Cómo Usar Los Prompts

### Estructura de Cada Prompt

Todos los prompts siguen formato **ROL - CONTEXTO - TAREA - FORMATO - RESTRICCIONES**:

```markdown
🎭 ROL: Define quién es el AI (ej: "Quant trader con 10 años exp")
📊 CONTEXTO: Tu situación específica
🎯 TAREA: Qué necesitas que haga (5 pasos detallados)
📤 FORMATO: Cómo quieres la respuesta
⛔ RESTRICCIONES: Qué NO hacer
```

### Paso a Paso

#### 1. Abre el archivo del prompt

```bash
cd 03_PROMPTS_LIBRARY
open 01_Generar_Ideas_Estrategia.md
```

#### 2. Copia el template

Busca la sección "Template Básico" y copia todo el bloque markdown.

#### 3. Personaliza tu contexto

Reemplaza los placeholders:
- `[TU OBSERVACIÓN]` → Tu observación real
- `[ACTIVO]` → Activo que tradeas
- `[TIMEFRAME]` → Tu horizonte temporal
- Etc.

#### 4. Pega en Claude/ChatGPT/Gemini

**Recomendación de modelo:**
- Claude Sonnet 4: Mejor para código y análisis profundo
- ChatGPT o1: Mejor para razonamiento matemático
- Gemini Pro: Alternativa gratuita

#### 5. Itera con follow-ups

No esperes respuesta perfecta en primer intento:

```markdown
Prompt inicial: [Genera 3 estrategias...]
↓
AI responde con 3 estrategias
↓
Follow-up 1: "La Estrategia 2 me interesa. Profundiza en..."
↓
Follow-up 2: "¿Qué ajustes para criptos en lugar de acciones?"
```

---

## 🎓 Mejores Prácticas

### ✅ DO (Haz esto):

1. **Lee el prompt completo antes de usar**
   - Cada prompt tiene secciones de "Tips", "Variaciones", "Ejemplos"
   - Aprender el patrón es más valioso que copiar-pegar

2. **Sé específico en tu contexto**
   - ❌ "Quiero una estrategia de trading"
   - ✅ "Estrategia mean reversion en SPY, timeframe diario, nivel intermedio"

3. **Usa ejemplos de uso real**
   - Cada prompt tiene sección "🔥 Ejemplo de Uso Real"
   - Compara tu input con el ejemplo para calibrar

4. **Valida el output del AI**
   - Cada prompt tiene "✅ Checklist Post-Generación"
   - NO uses output sin validar

5. **Itera, no esperes perfección**
   - Primera respuesta del AI: 70% útil
   - Con 2-3 follow-ups: 95% útil

### ❌ DON'T (Evita esto):

1. **No uses prompts sin personalizar**
   - Template dice `[TU NOMBRE]` → NO dejes eso
   - Llenar TODOS los campos es obligatorio

2. **No confíes ciegamente en el AI**
   - AI puede alucinar bugs sutiles
   - SIEMPRE testea código antes de usar

3. **No ignores las restricciones**
   - Prompt dice "⛔ NO uses ML complejo"
   - Si AI lo usa igual, recuérdale la restricción

4. **No uses un solo prompt para todo**
   - Cada prompt tiene propósito específico
   - Usar prompt correcto = mejor resultado

---

## 📊 Ejemplo de Flujo Completo

**Caso:** Desarrollar estrategia desde cero hasta paper trading

### Semana 1: Ideación
```
Día 1: Prompt 01 → Generar 3 ideas de estrategia
Día 2: Evaluar ideas, seleccionar 1
```

### Semana 2: Implementación
```
Día 3: Prompt 02 → Adaptar código base de GitHub
Día 4: Prompt 03 → Entender partes complejas del código
Día 5: Prompt 04 → Debuggear errores que surgen
```

### Semana 3: Validación
```
Día 6: Ejecutar backtest
Día 7: Prompt 05 → Interpretar métricas
Día 8: Decidir si continuar (basado en análisis)
```

**Resultado:**
- 8 días desde idea → backtest validado
- Sin prompts: 3-4 semanas típicamente
- Aceleración: 3-4x más rápido

---

## 🔗 Integración con Otros Recursos

### Usa prompts CON templates:

```
Paso 1: Prompt 01 → Generar ideas
        ↓
Paso 2: Copiar ideas a Strategy_Memo_Template.md
        ↓
Paso 3: Prompt 05 → Interpretar métricas backtest
        ↓
Paso 4: Copiar análisis a Strategy_Memo
```

### Usa prompts CON scripts:

```
Paso 1: Ejecutar data_pipeline_simple.py
        ↓
Paso 2: Si hay error → Prompt 04 (Debugging)
        ↓
Paso 3: Prompt 03 → Entender partes del script
        ↓
Paso 4: Prompt 02 → Adaptar script para tu caso
```

---

## 📚 Recursos Adicionales

### Lecturas Sobre Prompt Engineering:

- **OpenAI Prompt Engineering Guide** (free)
- **Anthropic Prompt Library** (ejemplos reales)
- **Learn Prompting** (learnprompting.org)

### En el Workshop:

- 📂 [02_TEMPLATE_PACK/](../02_TEMPLATE_PACK/) - Templates para documentar
- 📂 [04_SCRIPTS_AUXILIARES/](../04_SCRIPTS_AUXILIARES/) - Scripts complementarios
- 📂 [00_GUIA_DE_USO/](../00_GUIA_DE_USO/) - Guías del workshop

---

## 💬 Soporte

**¿Prompt no funciona como esperabas?**

📧 Email: yismaryme@gmail.com (adjunta tu prompt + respuesta del AI)  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Code reviews + optimización de prompts]

**Recuerda:** Compartir tu prompt ayuda a mejorar la biblioteca para todos.

---

## 📝 Changelog

### v1.0 (Nov 2025)
- ✅ 5 prompts públicos incluidos
- 🔒 30+ prompts adicionales en versión premium

---

## ⚠️ Disclaimer

Estos prompts son herramientas educativas. El uso de IA Generativa NO garantiza:
- Estrategias rentables
- Código libre de bugs
- Análisis correcto 100% del tiempo

**Pero SÍ te ayuda a:**
- Acelerar desarrollo 3-4x
- Aprender conceptos más rápido
- Validar tus ideas con otra "opinión"
- Evitar errores comunes (si usas checklistsprovidas)

**Regla de oro:**
> "Usa GenAI como copiloto experimentado que te sugiere ideas.  
> Tú eres el piloto final que decide."

---

**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa  
**Versión:** 1.0 (Público)  
**Licencia:** Uso libre para participantes. No redistribuir sin permiso.
