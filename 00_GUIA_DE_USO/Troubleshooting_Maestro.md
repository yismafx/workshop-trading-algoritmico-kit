# 🚨 TROUBLESHOOTING MAESTRO

🏠 [Inicio](../README.md) > 📄 **Troubleshooting Maestro**

---

## 📋 ÍNDICE RÁPIDO

**Navegación por categoría:**

1. [🚀 Quick Fixes (Soluciones Rápidas)](#-quick-fixes-soluciones-rápidas)
2. [⚙️ Setup y Configuración](#%EF%B8%8F-setup-y-configuración)
3. [📊 Datos y APIs](#-datos-y-apis)
4. [💻 Código y Notebooks](#-código-y-notebooks)
5. [📈 Backtesting](#-backtesting)
6. [🔗 Integración con Brokers](#-integración-con-brokers)
7. [🤖 IA Generativa](#-ia-generativa)
8. [📞 Contacto para Soporte](#-contacto-para-soporte)

---

## 🎯 ¿QUÉ ES TROUBLESHOOTING MAESTRO?

**Troubleshooting Maestro** es tu centro de comando para resolver CUALQUIER problema técnico del workshop.

**Estructura modular:**
```
Troubleshooting_Maestro.md (ESTE ARCHIVO)
    ├─ Hub central de navegación
    ├─ Quick Fixes para problemas comunes
    └─ Referencias a troubleshooting específico:
         ├─ Troubleshooting_Comun.md (errores cross-platform)
         ├─ Setup_A_Colab_Rapido.md (problemas de Colab)
         ├─ Setup_B_Python_Local.md (problemas de instalación local)
         ├─ Setup_C_MetaTrader5.md (problemas de MT5)
         └─ Cada sesión S1-S9 tiene su propia sección
```

---

## 🚀 QUICK FIXES (Soluciones Rápidas)

### 🔴 ERROR #1: "ModuleNotFoundError"

**Problema:** Python no encuentra una librería

**Solución rápida:**
```python
# En Google Colab:
!pip install nombre-de-la-libreria --break-system-packages

# Si el error persiste:
!pip install --upgrade nombre-de-la-libreria
```

**Prevención:**
- Ejecuta las celdas de instalación ANTES que las de código
- No saltees el bloque de instalación inicial

---

### 🔴 ERROR #2: "Runtime disconnected" (Colab)

**Problema:** Colab se desconectó

**Soluciones:**
1. Reconectar: `Runtime > Connect`
2. Si persiste: `Runtime > Factory reset runtime`
3. Ejecutar todas las celdas desde el inicio

**Prevención:**
- No dejes Colab inactivo más de 90 minutos
- Guarda tu notebook frecuentemente (Ctrl+S)

---

### 🔴 ERROR #3: "KeyError" en datos históricos

**Problema:** Falta una columna esperada (ej. 'Close', 'Volume')

**Causas comunes:**
- Ticker incorrecto (ej. `AAPL` vs `aapl`)
- Fechas fuera de rango de datos disponibles
- API key vencida o incorrecta

**Soluciones:**
```python
# Verificar qué columnas tienes:
print(df.columns)

# Verificar fechas disponibles:
print(f"Datos desde: {df.index.min()}")
print(f"Datos hasta: {df.index.max()}")

# Verificar ticker:
print(f"Símbolo: {df.attrs.get('symbol', 'N/A')}")
```

**Referencias:**
- [Troubleshooting Común - Sección Datos](Troubleshooting_Comun.md#-datos-y-apis)
- [Setup Colab Rápido - Paso 5 Validación](Setup_A_Colab_Rapido.md#paso-5-validación-completa)

---

### 🔴 ERROR #4: "Rate limit exceeded" (APIs)

**Problema:** Hiciste demasiadas peticiones a la API

**Soluciones:**
1. Espera 1 minuto antes de reintentar
2. Reduce la frecuencia de peticiones
3. Usa datos en cache si están disponibles

**Prevención:**
- No ejecutes el mismo código de descarga múltiples veces seguidas
- Guarda datos descargados en CSV para reutilizar

```python
# Guardar datos:
df.to_csv('datos_AAPL_2024.csv')

# Cargar datos guardados:
df = pd.read_csv('datos_AAPL_2024.csv', index_col=0, parse_dates=True)
```

---

### 🔴 ERROR #5: Código se cuelga / No termina

**Problema:** Loop infinito o proceso muy lento

**Soluciones:**
1. Interrumpir: `Runtime > Interrupt execution`
2. Verificar loops (¿tienen condición de salida?)
3. Reducir datos (prueba con menos años)

**Debugging:**
```python
# Agregar prints para tracking:
for i in range(len(data)):
    if i % 100 == 0:  # Print cada 100 iteraciones
        print(f"Procesando fila {i}/{len(data)}")
    # Tu código aquí
```

---

### 🔴 ERROR #6: "Out of Memory" (Colab)

**Problema:** Colab se quedó sin RAM

**Soluciones:**
1. `Runtime > Factory reset runtime`
2. Reduce el tamaño de datos
3. Usa sampling o chunking
4. Upgrade a Colab Pro si necesitas más RAM

**Optimización:**
```python
# Antes (carga todo):
df = pd.read_csv('datos_grandes.csv')

# Después (sampling):
df = pd.read_csv('datos_grandes.csv', nrows=10000)

# O chunking:
for chunk in pd.read_csv('datos_grandes.csv', chunksize=1000):
    procesar(chunk)
```

---

## ⚙️ SETUP Y CONFIGURACIÓN

### 📦 Problemas de Instalación

**Si estás usando:**

- **Google Colab:** Ver [Setup Colab Rápido - Troubleshooting](Setup_A_Colab_Rapido.md#-troubleshooting)
- **Python Local:** Ver [Setup B Python Local - Troubleshooting](#) *(Fase 1B)*
- **MetaTrader 5:** Ver [Setup C MetaTrader5 - Troubleshooting](#) *(Fase 1B)*

### 🔧 Errores de Dependencias

**"Conflict detected for package X"**

**Solución:**
```bash
# Opción 1: Forzar instalación
!pip install nombre-paquete --force-reinstall

# Opción 2: Crear ambiente limpio
!pip install nombre-paquete --ignore-installed
```

---

## 📊 DATOS Y APIS

### 🔌 Problemas con Alpaca API

**Ver guía completa:** [Troubleshooting Común - APIs](Troubleshooting_Comun.md#-rate-limit-exceeded-apis)

**Errores comunes:**
- ❌ "Forbidden" → API keys incorrectas
- ❌ "Subscription does not permit" → Plan básico no tiene acceso a esos datos
- ❌ "Rate limit" → Demasiadas peticiones

**Solución para "Subscription does not permit":**
```python
# Alpaca Basic Plan tiene restricción de 15 minutos
# Usa datos HASTA AYER:
from datetime import datetime, timedelta

end_date = datetime.now() - timedelta(days=1)
```

---

### 📈 Datos Históricos Incompletos

**Síntomas:**
- Gaps en los datos
- Fechas faltantes
- Volumen = 0

**Verificación:**
```python
# Detectar gaps:
import pandas as pd
df['gap'] = df.index.to_series().diff()
gaps = df[df['gap'] > pd.Timedelta('1 day')]
print(f"Gaps encontrados: {len(gaps)}")

# Detectar volumen = 0:
low_volume = df[df['Volume'] == 0]
print(f"Días sin volumen: {len(low_volume)}")
```

**Soluciones:**
- Cambiar de fuente de datos (yfinance → Alpaca)
- Usar forward-fill para gaps pequeños
- Eliminar períodos sin volumen

---

## 💻 CÓDIGO Y NOTEBOOKS

### 🐍 Errores de Sintaxis Python

**Ver guía completa:** [Troubleshooting Común - Código](Troubleshooting_Comun.md#-código-se-cuelga--no-termina)

**Errores comunes para traders sin experiencia en código:**

```python
# ❌ ERROR: Indentación incorrecta
def mi_funcion():
print("Hola")  # Falta indentación

# ✅ CORRECTO:
def mi_funcion():
    print("Hola")  # 4 espacios de indentación
```

```python
# ❌ ERROR: Variable no definida
resultado = calcular_rsi()  # ¿calcular_rsi existe?

# ✅ CORRECTO: Verificar que función existe
if 'calcular_rsi' in dir():
    resultado = calcular_rsi()
else:
    print("ERROR: calcular_rsi no está definido")
```

---

### 📓 Notebooks que no Ejecutan

**Problema:** Celdas no corren o se saltan

**Checklist:**
- [ ] ¿Ejecutaste las celdas en orden?
- [ ] ¿La celda de instalación corrió exitosamente?
- [ ] ¿Hay errores en celdas anteriores?

**Solución:**
1. `Runtime > Restart runtime`
2. `Runtime > Run all` (ejecutar todo desde inicio)
3. Revisar cada celda por errores

---

## 📈 BACKTESTING

### ⚠️ Resultados Demasiado Buenos

**Si tu estrategia tiene Sharpe > 3.0 o Win Rate > 80%:**

**🚨 ALERTA: Probablemente hay OVERFITTING o LOOK-AHEAD BIAS**

**Verificaciones obligatorias:**

```python
# 1. ¿Usas información del futuro?
# ❌ MAL: Calcula promedio con datos de hoy hacia adelante
df['SMA'] = df['Close'].rolling(20).mean()
signals = df['Close'] > df['SMA']  # Esto usa datos futuros!

# ✅ BIEN: Shift de 1 día
df['SMA'] = df['Close'].shift(1).rolling(20).mean()
signals = df['Close'] > df['SMA']
```

```python
# 2. ¿Optimizaste parámetros con TODO el dataset?
# ❌ MAL:
best_params = optimize(data_completa)  # Overfitting garantizado

# ✅ BIEN: Walk-Forward Optimization
train_data = data[:int(len(data)*0.7)]
test_data = data[int(len(data)*0.7):]
best_params = optimize(train_data)
results = backtest(test_data, best_params)
```

**Referencia:** López de Prado (2018, cap. 11): "Backtesting is not a research tool, it's a verification tool"

---

### 📉 Estrategia que Funciona en Backtest pero Falla en Live

**Causas comunes:**

1. **Slippage no modelado:** Backtest asume ejecución perfecta
2. **Comisiones ignoradas:** Broker cobra $5 por trade → Rentabilidad desaparece
3. **Liquidez asumida:** Backtest compra 1000 acciones, pero en realidad solo hay 100
4. **Datos de sobreviviente:** Solo testeas con empresas que aún existen

**Solución:**
```python
# Agregar costos realistas:
commission = 0.001  # 0.1% por operación
slippage = 0.0005   # 0.05% de slippage
```

---

## 🔗 INTEGRACIÓN CON BROKERS

### 🔌 Conexión Fallida

**Ver troubleshooting específico:**
- **Alpaca:** [Setup Colab Rápido - Paso 4](Setup_A_Colab_Rapido.md#paso-4-conectar-con-alpaca-api)
- **Interactive Brokers:** *(Fase 1B)*
- **MetaTrader 5:** *(Fase 1B)*

---

### 🚫 Órdenes Rechazadas

**Causas comunes:**
- Fondos insuficientes
- Mercado cerrado
- Tamaño de orden no permitido
- Symbol incorrecto

**Verificación:**
```python
# Antes de enviar orden:
account = api.get_account()
print(f"Buying Power: ${account.buying_power}")
print(f"Market Open: {market.is_open}")
```

---

## 🤖 IA GENERATIVA

### 💬 Claude/ChatGPT da Código Erróneo

**Problema:** La IA genera código que no funciona

**Estrategia de Validación:**

```
1. ❌ NO copies código de IA ciegamente
2. ✅ Lee línea por línea
3. ✅ Ejecuta en bloques pequeños
4. ✅ Verifica outputs intermedios
5. ✅ Compara con código del workshop
```

**Prompt mejorado para evitar errores:**
```
Genera código Python para [TAREA].

REQUISITOS CRÍTICOS:
- Solo usa librerías: pandas, numpy, yfinance
- Comenta CADA línea explicando qué hace
- Incluye manejo de errores (try-except)
- Incluye validación de inputs
- NO uses funciones que no existan en pandas 2.0

FORMATO DE OUTPUT:
1. Código completo
2. Ejemplo de uso
3. Output esperado
```

---

### 🤯 Alucinaciones de la IA

**Ejemplos comunes:**

```python
# ❌ La IA inventa funciones que NO existen:
import yfinance as yf
data = yf.download_with_sentiment('AAPL')  # ¡Esto NO existe!

# ✅ VERIFICAR: ¿La función existe?
import yfinance as yf
print(dir(yf))  # Lista todas las funciones disponibles
```

**Regla de oro:** Si la IA sugiere algo que parece "demasiado fácil", VERIFICA en la documentación oficial.

---

## 📞 CONTACTO PARA SOPORTE

### 🆘 ¿Cuándo Contactar?

**Contacta si:**
- ✅ Leíste esta guía completa
- ✅ Probaste las soluciones sugeridas
- ✅ El problema persiste después de 30+ minutos

**NO contactes para:**
- ❌ Errores que están en esta guía
- ❌ Preguntas respondidas en FAQ
- ❌ Solicitudes de "hacer el trabajo por ti"

---

### 📧 Formato de Consulta Recomendado

```
Asunto: [ERROR] Descripción breve (max 10 palabras)

1. ¿Qué estabas intentando hacer?
   [Describe la tarea específica]

2. ¿Qué error obtuviste? (copia el mensaje COMPLETO)
   [Pega el error con traceback completo]

3. ¿Qué pasos ya intentaste?
   - Intento 1: [Describe]
   - Intento 2: [Describe]

4. Screenshots (si es posible)
   [Adjunta imagen del error]

5. Contexto adicional:
   - Sesión: S[X]
   - Archivo: [nombre.ipynb]
   - Línea de código: [número]
```

---

### 📱 Canales de Soporte

**Opción 1: Email**
- 📧 yismaryme@gmail.com
- ⏱️ Tiempo de respuesta: 24-48h
- 🎯 Para: Errores complejos, dudas conceptuales

**Opción 2: Telegram**
- 💬 [@yismary](https://t.me/yismary)
- ⏱️ Tiempo de respuesta: Variable (consultas rápidas)
- 🎯 Para: Preguntas urgentes, clarificaciones

**Opción 3: Grupo Premium**
- 🔒 [Enlace en email de bienvenida]
- ⏱️ Tiempo de respuesta: Comunitario (otros participantes ayudan)
- 🎯 Para: Soporte peer-to-peer, networking

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

## 🔗 NAVEGACIÓN

**← Volver a:**
- [README Principal](../README.md)
- [Guía de Inicio](GUIA_INICIO.md)
- [Setup Colab Rápido](Setup_A_Colab_Rapido.md)

**Ver también:**
- [Troubleshooting Común](Troubleshooting_Comun.md) - Soluciones cross-platform
- [SITEMAP.md](SITEMAP.md) - Mapa completo del repositorio
- [GLOSARIO_NAVEGACION.md](GLOSARIO_NAVEGACION.md) - Índice de archivos

---

## 📊 ROADMAP DE TROUBLESHOOTING

```
✅ v2.1 (Actual) - Troubleshooting Maestro básico
    ├─ Quick Fixes centralizados
    ├─ Referencias a docs específicos
    └─ Estructura modular
🟡 v2.2 (Próxima) - Expansión de contenido
    ├─ 50+ errores documentados
    ├─ Videos de soluciones
    └─ Base de conocimiento searchable
🟡 v3.0 (Futura) - Troubleshooting Interactivo
    ├─ Diagnóstico automático
    ├─ Chatbot con soluciones
    └─ FAQ dinámico
```

---

## 📖 VERSIÓN Y CHANGELOG

**Versión:** 2.1  
**Última actualización:** 16 de Noviembre de 2025  
**Mantenido por:** [@yismafx](https://github.com/yismafx)

**Changelog:**
- **v2.1 (Nov 16, 2025):** Troubleshooting Maestro inicial
  - Hub centralizado de troubleshooting
  - Quick Fixes para top 6 errores
  - Referencias a troubleshooting específico
  - Estructura modular para expansión futura
  - Guías de validación y debugging
  - Mejores prácticas documentadas

---

## ⚠️ DISCLAIMER

**Material para fines educativos únicamente.**

❌ NO constituye asesoría de inversión  
⚠️ Trading algorítmico implica riesgo de pérdida de capital  
📊 Resultados pasados NO garantizan resultados futuros  
💰 Nunca operes con dinero que no puedas perder

**Troubleshooting no garantiza:**
- Que tu estrategia sea rentable
- Que todos los problemas tengan solución inmediata
- Que el workshop sea plug-and-play sin esfuerzo

**Troubleshooting SÍ te ayuda a:**
- Resolver problemas técnicos comunes
- Aprender a debuggear de forma sistemática
- Evitar errores costosos en producción

---

**¿No encontraste tu problema?**  
💬 [Contacta soporte](#-contacto-para-soporte) con el formato recomendado

**¿Resolviste un problema no documentado?**  
🙏 [Compártelo](https://github.com/yismafx/workshop-trading-algoritmico-kit/issues) para ayudar a otros

---

**Última actualización:** Noviembre 16, 2025 • **Versión:** 2.1  
**Estado:** ✅ Operativo (Placeholder mejorado, expansión continua)
