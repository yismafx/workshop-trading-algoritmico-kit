# Librerías: Mínimas vs Completas

🏠 [Inicio](../README.md) > 📄 **Librerías Mínimas vs Completas**

---

## ⚠️ DOCUMENTO EN DESARROLLO

Esta comparación detallada estará disponible en la **próxima versión del kit (v2.2)**.

---

## 🎯 ¿Qué es Librerías Mínimas vs Completas?

Este documento será tu guía para entender **cuántas librerías realmente necesitas** según tu nivel y objetivos:

- ✅ **Setup Mínimo** - Para empezar rápido
- ✅ **Setup Completo** - Para trading profesional
- ✅ **Setup Avanzado** - Para desarrollo custom
- ✅ Comparación de tamaños y tiempos de instalación
- ✅ Cuándo usar cada setup

---

## ✅ INFORMACIÓN DISPONIBLE AHORA

**Mientras tanto:**

### 🚀 Setup Recomendado para Empezar
**Usa Google Colab** → [Setup_A_Colab_Rapido.md](Setup_A_Colab_Rapido.md)

**Ventajas:**
- ✅ Todas las librerías preinstaladas
- ✅ Sin decisiones complicadas
- ✅ Funciona "out of the box"
- ✅ Sin fricción de instalación

---

## 📊 RESUMEN RÁPIDO (Mientras esperas v2.2)

### 🟢 Librerías MÍNIMAS (Setup Básico)
**Para:** Aprender y experimentar
```bash
pip install yfinance pandas numpy matplotlib backtrader
```
**Tamaño:** ~200 MB  
**Tiempo:** 2-3 minutos

---

### 🟡 Librerías COMPLETAS (Setup Recomendado)
**Para:** Workshop completo y trading serio
```bash
pip install yfinance pandas numpy matplotlib seaborn backtrader vectorbt \
            alpaca-trade-api scipy statsmodels jupyter
```
**Tamaño:** ~500 MB  
**Tiempo:** 5-7 minutos

---

### 🔴 Librerías AVANZADAS (Setup Pro)
**Para:** Desarrollo custom y ML
```bash
# Setup completo + librerías de ML/AI
pip install [setup completo] + scikit-learn tensorflow lightgbm
```
**Tamaño:** ~2 GB  
**Tiempo:** 15-20 minutos

---

## 📅 CONTENIDO PLANEADO PARA v2.2

Cuando esté listo, **Librerías Mínimas vs Completas** incluirá:

### 📋 Comparación Detallada
| Librería | Mínimo | Completo | Avanzado | Propósito |
|----------|--------|----------|----------|-----------|
| pandas | ✅ | ✅ | ✅ | Datos |
| numpy | ✅ | ✅ | ✅ | Cálculos |
| yfinance | ✅ | ✅ | ✅ | Descarga datos |
| matplotlib | ✅ | ✅ | ✅ | Gráficos básicos |
| backtrader | ✅ | ✅ | ✅ | Backtesting |
| seaborn | ❌ | ✅ | ✅ | Gráficos avanzados |
| vectorbt | ❌ | ✅ | ✅ | Backtesting rápido |
| scikit-learn | ❌ | ❌ | ✅ | Machine Learning |
| ... | ... | ... | ... | ... |

### 🎯 Guía de Decisión
```
¿Qué setup necesito?

→ Soy nuevo, solo quiero aprender
  └→ Setup MÍNIMO

→ Voy a hacer el workshop completo
  └→ Setup COMPLETO

→ Quiero integrar ML/AI avanzado
  └→ Setup AVANZADO

→ No quiero decidir, dame lo más simple
  └→ Usa Google Colab (todo preinstalado)
```

### ⚖️ Pros y Contras

**Setup Mínimo:**
- ✅ Rápido de instalar
- ✅ Ocupa poco espacio
- ❌ Limitaciones en funcionalidad
- ❌ Necesitarás instalar más después

**Setup Completo:**
- ✅ Todo lo necesario para el workshop
- ✅ No necesitas instalar más
- ✅ Balance ideal
- ❌ Tarda más en instalar

**Setup Avanzado:**
- ✅ Máxima flexibilidad
- ✅ Para desarrollo profesional
- ❌ Instalación lenta
- ❌ Usa mucho espacio
- ❌ Complejidad innecesaria si eres nuevo

### 💾 Requisitos de Sistema
- **Espacio en disco:** 200 MB - 2 GB
- **RAM:** 4 GB mínimo, 8 GB recomendado
- **Python:** 3.8+ (3.10+ recomendado)
- **Conexión:** Para descargar paquetes

---

## 💡 RECOMENDACIÓN PROFESIONAL

**Para el 95% de los participantes:**

👉 **Usa Google Colab** ([Setup_A_Colab_Rapido.md](Setup_A_Colab_Rapido.md))

**Por qué:**
- ✅ Sin decisiones de qué instalar
- ✅ Sin problemas de compatibilidad
- ✅ Sin consumir espacio local
- ✅ Funciona en cualquier dispositivo
- ✅ GPU gratis incluida

**Instala Python local solo si:**
- ⚠️ Necesitas trabajar offline frecuentemente
- ⚠️ Tienes limitaciones de conectividad
- ⚠️ Quieres integrar con tools locales específicos
- ⚠️ Desarrollo avanzado y customización profunda

---

## 🆘 ¿NECESITAS AYUDA PARA DECIDIR?

**Si no sabes qué setup elegir:**

1. **Empieza con Colab:** [Setup_A_Colab_Rapido.md](Setup_A_Colab_Rapido.md)
2. **Si necesitas local:** [Setup_B_Python_Local.md](Setup_B_Python_Local.md)
3. **Contacta:** yismaryme@gmail.com

---

## 🔗 NAVEGACIÓN

**← Volver a:**
- [Guía de Setup Completa](Guia_Setup_Completa.md)
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**Ver también:**
- [Librerias_Dependencias_2025.md](Librerias_Dependencias_2025.md) - Lista completa
- [SITEMAP.md](SITEMAP.md) - Mapa del repositorio

---

**Última actualización:** Noviembre 2025 • **Versión:** Placeholder v2.1  
**Estado:** 🟡 En Desarrollo
