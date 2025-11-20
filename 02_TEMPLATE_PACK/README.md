# 📋 TEMPLATE PACK - Versión Pública

> **Workshop:** Trading Algorítmico Aumentado con IA Generativa  
> **Versión:** 1.0 (Público)  
> **Última actualización:** Noviembre de 2025

**🏠 [← Volver al Inicio](../README.md)** | **📂 [Ver Prompts](../03_PROMPTS_LIBRARY/)** | **🐍 [Ver Scripts](../04_SCRIPTS_AUXILIARES/)**

---

## 🎯 ¿Qué es esto?

Esta carpeta contiene **templates profesionales** en formato Markdown para documentar tus estrategias de trading algorítmico.

**Filosofía:** Documentación clara = Mejor decisiones = Menos pérdidas

---

## 📂 Contenido Disponible (Público)

### ✅ [Strategy_Memo_Template.md](Strategy_Memo_Template.md)

**¿Para qué?**  
Documentar estrategias de trading de forma profesional antes de implementarlas.

**👉 [Ver Template →](Strategy_Memo_Template.md)**

**Cuándo usar:**
- Cuando tienes una hipótesis de estrategia (ej: "Mean reversion en SPY")
- ANTES de escribir código (ayuda a clarificar lógica)
- Para comunicar estrategia a otros traders/inversionistas

**Secciones incluidas:**
1. Executive Summary (estrategia en 3 líneas)
2. Hipótesis de Trading (¿por qué debería funcionar?)
3. Especificación Técnica (señales de entrada/salida)
4. Backtest Inicial (resultados exploratorios)
5. Validación Rigurosa (walk-forward, Monte Carlo)
6. Plan de Implementación (tecnología, cronograma)
7. Gestión de Versiones (control de cambios)
8. Post-Mortem de Trades (registro de operaciones)

**Nivel:** Básico (18 secciones)

---

## 🔒 Contenido Premium (No Incluido Aquí)

En el **workshop completo** recibes:

### Templates Adicionales:

1. **Backtesting_Report_Template.md** (Avanzado)
   - 25+ secciones
   - Análisis estadístico profundo
   - Gráficos de equity curve, drawdown
   - Matriz de correlación entre trades
   - Análisis de régimen de mercado

2. **Risk_Management_Plan_Template.md**
   - Position sizing con Kelly Criterion
   - Stop-loss dinámico basado en ATR
   - Diversificación de portfolio
   - Circuit breakers (cuando detener el bot)
   - Plan de recuperación post-drawdown

3. **README_Technical_Template.md**
   - Documentación de código estilo GitHub
   - Instrucciones de instalación
   - Troubleshooting común
   - API de funciones principales

4. **Deployment_Checklist_Template.md**
   - 50+ checks antes de ir a live
   - Validación de ambiente de producción
   - Monitoreo y alertas
   - Rollback plan si algo falla

5. **Strategy_Comparison_Matrix_Template.xlsx**
   - Comparar 5+ estrategias lado a lado
   - Métricas normalizadas
   - Scoring automático
   - Recomendación basada en tu perfil de riesgo

---

## 📖 Cómo Usar Los Templates

### Paso 1: Copia el Template

```bash
cp Strategy_Memo_Template.md My_Strategy_MeanReversion_SPY.md
```

### Paso 2: Rellena Secciones

**NO dejes placeholders como `[TU NOMBRE]`**. Llena TODAS las secciones.

**Orden recomendado:**
1. Executive Summary (lo último, cuando ya sepas todo)
2. Hipótesis de Trading (empieza aquí)
3. Especificación Técnica (define reglas claras)
4. Backtest Inicial (ejecuta y documenta)
5. Validación (walk-forward, Monte Carlo)
6. Plan de Implementación (si pasa validación)

### Paso 3: Itera con GenAI

**Usa los prompts de 03_PROMPTS_LIBRARY/ para llenar secciones:**

```markdown
Ejemplo:
1. Usa Prompt 01 para generar hipótesis
2. Copia output del AI al Strategy Memo
3. Usa Prompt 05 para interpretar métricas de backtest
4. Copia análisis al Strategy Memo
5. Tienes documento profesional en 30 minutos
```

### Paso 4: Revisa Regularmente

**Actualiza tu memo cada:**
- ❌ Después de cada trade (exagerado)
- ✅ Mensualmente (revisión de performance)
- ✅ Después de eventos mayores (crashes, cambio de régimen)
- ✅ Al cambiar parámetros de la estrategia

---

## 🎓 Mejores Prácticas

### ✅ DO (Haz esto):

1. **Sé honesto con los números**
   - No maquilles resultados de backtest
   - Incluye costos de transacción
   - Documenta TODOS los drawdowns

2. **Incluye el "Por Qué"**
   - No solo digas "Sharpe = 1.5"
   - Explica: "Sharpe 1.5 es bueno porque..."

3. **Versiona tus estrategias**
   - Strategy_v1.0 (versión inicial)
   - Strategy_v1.1 (agregado stop-loss)
   - Strategy_v2.0 (cambio mayor de lógica)

4. **Usa control de versiones**
   ```bash
   git init
   git add Strategy_Memo_v1.0.md
   git commit -m "Versión inicial post-backtest"
   ```

### ❌ DON'T (Evita esto):

1. **No dejes secciones vacías**
   - Si no tienes datos para una sección, escribe "Pendiente: [razón]"
   - Ejemplo: "Walk-forward: Pendiente hasta tener 3 años de datos"

2. **No ignores advertencias**
   - Template dice "⚠️ Si Sharpe >3, revisar overfitting"
   - No lo borres porque tu Sharpe es 3.2

3. **No uses templates como checklist burocrático**
   - Template es herramienta para PENSAR, no para cumplir requisito

4. **No copies-pegues entre estrategias**
   - Cada estrategia es única
   - Rellena desde cero cada vez

---

## 📊 Ejemplo de Uso Real

**Caso:** Desarrollaste estrategia "SMA Crossover" para SPY

**Día 1:** Tienes idea → Llenas sección "Hipótesis"  
**Día 2:** Haces backtest → Llenas sección "Backtest Inicial"  
**Día 3:** Analizas métricas → Usas Prompt 05 → Llenas "Análisis"  
**Semana 1:** Walk-forward completo → Llenas "Validación"  
**Semana 2:** Empieza paper trading → Llenas "Plan Implementación"  
**Mes 3:** Revisión mensual → Actualizas "Post-Mortem de Trades"

**Resultado:**
- Documento vivo que evoluciona con tu estrategia
- Decisiones documentadas (sabes POR QUÉ hiciste X)
- Base para futuras estrategias (patrones que funcionan)

---

## 🔗 Recursos Relacionados

### En este Repositorio:

- 📂 [03_PROMPTS_LIBRARY/](../03_PROMPTS_LIBRARY/) - Usa GenAI para llenar templates
- 📂 [04_SCRIPTS_AUXILIARES/](../04_SCRIPTS_AUXILIARES/) - Scripts para generar datos del memo
- 📂 [00_GUIA_DE_USO/](../00_GUIA_DE_USO/) - Guías del workshop

### Lecturas Recomendadas:

- **Chan, E. (2013)** - Algorithmic Trading, Cap. 9 (Documentación)
- **Carver, R. (2015)** - Systematic Trading, Cap. 12 (Trading Diary)
- **López de Prado (2018)** - Advances in Financial ML, Cap. 11 (Backtesting)

---

## 💬 Soporte

**¿Dudas sobre cómo usar templates?**

📧 Email: yismaryme@gmail.com  
💬 Telegram: [@yismafx](https://t.me/yismafx)  
🔒 Grupo Premium: [Para participantes del workshop]

---

## 📝 Changelog

### v1.0 (Nov 2025)
- ✅ Template Strategy Memo (Básico) incluido
- 🔒 4 templates adicionales en versión premium

---

## ⚠️ Disclaimer

Estos templates son herramientas educativas. El uso de templates NO garantiza:
- Que tu estrategia sea rentable
- Que evitarás pérdidas
- Que pasarás todas las validaciones

**Pero SÍ te ayudan a:**
- Pensar críticamente sobre tu estrategia
- Documentar decisiones para aprender de errores
- Comunicar profesionalmente tus ideas

---

**Parte de:** Workshop Trading Algorítmico Aumentado con IA Generativa  
**Versión:** 1.0 (Público)  
**Licencia:** Uso libre para participantes. No redistribuir sin permiso.
