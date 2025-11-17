# 🚨 TROUBLESHOOTING MAESTRO

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

🏠 [Inicio](../README.md) > 📄 **Troubleshooting Maestro**

---

**📅 Última actualización:** 17 de noviembre de 2025  
**📌 Versión:** 3.0

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
8. [📞 Soporte](#-soporte)
9. [💡 Mejores Prácticas](#-mejores-prácticas-para-evitar-errores)
10. [📊 Roadmap](#-roadmap-de-troubleshooting)

---

## 🎯 ¿QUÉ ES TROUBLESHOOTING MAESTRO?

**Troubleshooting Maestro** es tu centro de comando para resolver CUALQUIER problema técnico del workshop.

**Estructura modular:**
```
Troubleshooting_Maestro.md (ESTE ARCHIVO)
    ├─ Hub central de navegación
    ├─ Quick Fixes para problemas comunes (6 errores más frecuentes)
    ├─ Troubleshooting por categoría (Setup, Datos, Código, etc.)
    └─ Referencias a guías específicas:
         ├─ Setup_A_Colab_Rapido.md (problemas de Colab)
         ├─ Setup_B_Python_Local.md (instalación local)
         └─ Setup_C_MetaTrader5.md (integración MT5)
```

**⚠️ Nota sobre contenido del workshop:**

Este documento contiene troubleshooting **público y general** para el kit de trading algorítmico.

El troubleshooting específico de:
- Ejercicios de sesiones S1-S9
- Estrategias privadas del workshop
- Código de casos de estudio avanzados

...está disponible dentro del **material privado del workshop** para participantes registrados.

Si eres participante y tienes problemas con contenido específico de una sesión, contacta soporte directamente.

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
- Ver sección [📊 Datos y APIs](#-datos-y-apis) más abajo en este documento
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
- **Python Local:** Ver [Setup B: Python Local](Setup_B_Python_Local.md) - Sección Troubleshooting
- **MetaTrader 5:** Ver [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md) - Sección Troubleshooting

**Nota:** Los Setups B y C incluyen troubleshooting específico en sus respectivas guías.

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

📚 **Más información:**
- Ver sección [🔴 ERROR #4: Rate limit exceeded](#-error-4-rate-limit-exceeded-apis) más arriba
- Consulta [FAQ - Problemas con APIs](FAQ_COMPLETO.md#-preguntas-técnicas)

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

📚 **Más información:**
- Ver sección [🔴 ERROR #5: Código se cuelga / No termina](#-error-5-código-se-cuelga--no-termina) más arriba
- Consulta [FAQ Completo](FAQ_COMPLETO.md) para dudas generales

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

**Ver troubleshooting específico por broker:**
- **Alpaca:** [Setup A - Conexión Alpaca](Setup_A_Colab_Rapido.md#paso-4-conectar-con-alpaca-api)
- **Interactive Brokers:** Contacta soporte para integración personalizada
- **MetaTrader 5:** Ver [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md)

**Nota:** IB requiere configuración avanzada. Consulta con soporte antes de intentar integración.

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

## 📞 SOPORTE

**¿Necesitas ayuda?**

- 📧 **Email:** yismaryme@gmail.com
- 💬 **Telegram:** [@yismary](https://t.me/yismary)

**Horario de soporte:**
- Lun-Vie: 9:00 AM - 6:00 PM (GMT-5)
- Respuesta promedio: 24-48 horas

**Nota:** Soporte técnico solo para participantes registrados del workshop.

**Antes de contactar:**
1. ✅ Leíste esta guía completa
2. ✅ Probaste las soluciones sugeridas
3. ✅ El problema persiste después de 30+ minutos

**Formato recomendado para tu consulta:**
- Asunto: [ERROR] Descripción breve
- Qué intentabas hacer
- Mensaje de error completo
- Qué pasos ya intentaste
- Screenshots (si aplica)

---

## 🔗 NAVEGACIÓN

**🏠 Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**📖 Ver también:**
- [FAQ Completo](FAQ_COMPLETO.md)
- [Setup A: Guiado](Setup_A_Guiado.md)
- [Setup B: Python Local](Setup_B_Python_Local.md)
- [Setup C: MetaTrader 5](Setup_C_MetaTrader5.md)
- [SITEMAP](SITEMAP.md)

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

## 📊 ROADMAP DE TROUBLESHOOTING

```
✅ v3.0 (Actual) - Troubleshooting Maestro estandarizado
    ├─ Quick Fixes para 6 errores más comunes
    ├─ Troubleshooting por categorías (8 secciones)
    ├─ Referencias actualizadas a Setup A, B, C
    ├─ Mejores prácticas documentadas
    └─ Navegación completa
🟡 v3.1 (Próxima) - Expansión de casos
    ├─ 20+ errores adicionales documentados
    ├─ Sección de debugging avanzado
    └─ Troubleshooting para APIs adicionales
🟡 v4.0 (Futura) - Troubleshooting Interactivo
    ├─ Diagnóstico automático de errores
    ├─ Base de conocimiento searchable
    └─ Integración con FAQ dinámico
```

---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
