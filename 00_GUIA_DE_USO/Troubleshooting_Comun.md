# Troubleshooting Común

🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 **Troubleshooting**

---

## ⚠️ DOCUMENTO EN DESARROLLO

Esta guía de resolución de problemas estará disponible en la **próxima versión del kit (v2.2)**.

---

## 🎯 ¿Qué es Troubleshooting Común?

**Troubleshooting Común** será tu guía de referencia rápida para resolver los errores más frecuentes en trading algorítmico:

- ✅ Errores de instalación y setup
- ✅ Problemas con datos históricos
- ✅ Errores de código (Python, APIs)
- ✅ Issues con notebooks de Colab
- ✅ Problemas de conectividad con brokers
- ✅ Errores de backtesting
- ✅ Soluciones paso a paso

---

## ✅ RECURSOS DISPONIBLES AHORA

**Mientras tanto, puedes consultar:**

### 📖 Documentación Existente
1. **[Setup Colab Rápido](Setup_Colab_Rapido.md)**
   - Sección de troubleshooting básico
   - Errores comunes de Colab
   - Soluciones rápidas

2. **[Guía de Setup Completa](Guia_Setup_Completa.md)**
   - Problemas de instalación
   - Configuración de ambientes
   - Validación de setup

3. **[GUIA_INICIO.md](GUIA_INICIO.md)**
   - FAQ general
   - Preguntas frecuentes
   - Contacto para soporte

---

## 🆘 SOLUCIONES RÁPIDAS (Mientras esperas v2.2)

### 🔴 ERROR: "ModuleNotFoundError"

**Problema:** Python no encuentra una librería

**Solución rápida:**
```python
# En Colab:
!pip install nombre-de-la-libreria
```

---

### 🔴 ERROR: "Runtime disconnected"

**Problema:** Colab se desconectó

**Soluciones:**
1. Reconectar: `Runtime > Connect`
2. Si persiste: `Runtime > Factory reset runtime`
3. Ejecutar celdas desde el inicio

---

### 🔴 ERROR: "KeyError" en datos históricos

**Problema:** Falta una columna esperada

**Soluciones:**
1. Verificar que descargaste datos correctamente
2. Revisar el ticker/símbolo (puede estar mal escrito)
3. Verificar fechas (algunos activos tienen datos limitados)

---

### 🔴 ERROR: "Rate limit exceeded" (APIs)

**Problema:** Hiciste demasiadas peticiones a la API

**Soluciones:**
1. Espera 1 minuto antes de reintentar
2. Reduce la frecuencia de peticiones
3. Usa datos en cache si están disponibles

---

### 🔴 ERROR: Código se cuelga / No termina

**Problema:** Loop infinito o proceso muy lento

**Soluciones:**
1. Interrumpir: `Runtime > Interrupt execution`
2. Verificar loops (¿tienen condición de salida?)
3. Reducir datos (prueba con menos años)

---

### 🔴 ERROR: "Out of Memory"

**Problema:** Colab se quedó sin RAM

**Soluciones:**
1. `Runtime > Factory reset runtime`
2. Reduce el tamaño de datos
3. Usa sampling o chunking
4. Upgrade a Colab Pro si necesitas más RAM

---

## 📅 CONTENIDO PLANEADO PARA v2.2

Cuando esté listo, **Troubleshooting Común** incluirá:

### 🔧 Setup y Instalación
- Problemas con Python/Anaconda
- Errores de dependencias
- Conflictos de versiones
- Ambientes virtuales

### 📊 Datos y APIs
- Errores al descargar datos
- Datos corruptos o incompletos
- APIs que no responden
- Autenticación fallida
- Rate limits y throttling

### 💻 Código y Notebooks
- Errores de sintaxis comunes
- Import errors
- Runtime crashes
- Memory leaks
- Performance issues

### 📈 Backtesting
- Resultados inconsistentes
- Errores de fechas
- Look-ahead bias no detectado
- Problemas con walk-forward
- Métricas incorrectas

### 🔗 Integración con Brokers
- Conexión fallida
- Órdenes rechazadas
- Problemas de autenticación
- Diferencias real vs demo
- Paper trading issues

### 🤖 IA Generativa
- Claude/ChatGPT da código erróneo
- Alucinaciones de la IA
- Cómo validar código generado
- Prompts que no funcionan
- Debugging con IA

---

## 🆘 ¿NECESITAS AYUDA URGENTE?

**Si tienes un error que no puedes resolver:**

### Opción 1: Busca en la Documentación
1. [Setup_Colab_Rapido.md](Setup_Colab_Rapido.md) - Errores de Colab
2. [Guia_Setup_Completa.md](Guia_Setup_Completa.md) - Errores de instalación
3. [GUIA_INICIO.md](GUIA_INICIO.md) - FAQ general

### Opción 2: Usa IA Generativa
```
PROMPT PARA DEBUGGING:
"Tengo este error en Python: [PEGA ERROR COMPLETO]
El código que estaba ejecutando es: [PEGA CÓDIGO]
¿Cuál es la causa y cómo lo soluciono?"
```

### Opción 3: Contacto Directo
- 📧 Email: yismaryme@gmail.com
- 💬 Telegram: [@yismary](https://t.me/yismary)
- 📱 Canal: Fractals Market

**Formato de consulta recomendado:**
```
Asunto: [ERROR] Descripción breve

1. ¿Qué estabas intentando hacer?
2. ¿Qué error obtuviste? (copia el mensaje completo)
3. ¿Qué pasos ya intentaste?
4. Screenshot del error (si es posible)
```

---

## 💡 MEJORES PRÁCTICAS PARA EVITAR ERRORES

### ✅ Antes de Empezar
- [ ] Lee la documentación del setup
- [ ] Valida tu ambiente (corre tests)
- [ ] Haz backup de notebooks antes de modificar
- [ ] Usa versiones estables de librerías

### ✅ Durante el Desarrollo
- [ ] Ejecuta código en pequeños bloques
- [ ] Valida outputs después de cada paso
- [ ] Comenta tu código para recordar qué hace
- [ ] Usa try-except para manejar errores

### ✅ Si Algo Falla
- [ ] Lee el error completo (no solo la última línea)
- [ ] Busca el error en Google (probablemente alguien ya lo tuvo)
- [ ] Intenta la solución más simple primero
- [ ] Si nada funciona: pide ayuda con contexto completo

---

## 📊 ROADMAP

```
✅ v2.1 (Actual) - Troubleshooting básico en docs
🟡 v2.2 (Próxima) - Troubleshooting_Comun.md completo
🟡 v2.3 (Futura) - Videos de solución de errores
🟡 v3.0 (Futura) - FAQ interactivo con búsqueda
```

---

## 🔗 NAVEGACIÓN

**← Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [Setup Colab Rápido](Setup_Colab_Rapido.md)
- [Guía de Setup Completa](Guia_Setup_Completa.md)
- [README Principal](../README.md)

**Ver también:**
- [SITEMAP.md](SITEMAP.md) - Mapa del repositorio
- [GLOSARIO_NAVEGACION.md](GLOSARIO_NAVEGACION.md) - Índice de archivos

---

**Última actualización:** Noviembre 2025 • **Versión:** Placeholder v2.1  
**Estado:** 🟡 En Desarrollo
