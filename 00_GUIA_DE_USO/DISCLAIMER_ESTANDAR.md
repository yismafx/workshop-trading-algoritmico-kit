# 📋 DISCLAIMER ESTÁNDAR OFICIAL
**Workshop Trading Algorítmico Aumentado con IA Generativa**

---

## ✅ VERSIÓN APROBADA

Usar esta versión EXACTA en todos los archivos del workshop:

```markdown
> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.
```

---

## 📍 UBICACIÓN EN CADA ARCHIVO

### Archivos principales (GUIA_INICIO, README, etc.):
**Posición:** Después del título principal, antes del índice

**Ejemplo:**
```markdown
# Guía de Inicio

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

## 📑 Índice
...
```

### Archivos de Setup (Setup_A_Express, Setup_Colab_Rapido, etc.):
**Posición:** Después del título, antes de "¿Para quién es esta guía?"

**Ejemplo:**
```markdown
# Setup A: Colab Rápido

> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

## ¿Para quién es esta guía?
...
```

### Archivos de recursos (Mapa_Recursos, Troubleshooting, etc.):
**Posición:** Después del título, antes del primer contenido

---

## 🚫 LO QUE NO DEBE VARIAR

### ❌ NO cambiar:
- El emoji ⚠️
- El texto "DISCLAIMER IMPORTANTE" en bold
- La frase exacta sobre asesoría financiera
- La advertencia sobre riesgo de capital

### ❌ NO agregar:
- Texto adicional
- Líneas extra
- Explicaciones adicionales
- Variaciones del disclaimer

### ❌ NO eliminar:
- Ninguna línea
- Ninguna palabra
- El formato de quote (>)

---

## ✅ ARCHIVOS QUE DEBEN TENER ESTE DISCLAIMER

1. `README.md`
2. `GUIA_INICIO.md`
3. `Setup_A_Colab_Rapido.md`
4. `Setup_A_Express.md`
5. `Troubleshooting_Maestro.md`
6. `Mejores_Practicas_Setup_A.md`
7. `Mapa_Recursos_Workshop.md`
8. `GLOSARIO_NAVEGACION.md`
9. Todos los archivos de Setups B, C, D (cuando se creen)
10. Cualquier documento público del workshop

---

## 📝 VALIDACIÓN

Para verificar que el disclaimer está correcto:

```bash
# Buscar disclaimers en todos los archivos .md
grep -r "DISCLAIMER IMPORTANTE" *.md

# Verificar que todos tengan el mismo texto exacto
grep -A 4 "DISCLAIMER IMPORTANTE" *.md | sort | uniq -c
```

El comando debe mostrar EXACTAMENTE 4 líneas idénticas por cada archivo.

---

## 🔄 PROCESO DE ACTUALIZACIÓN

Si en el futuro necesitas cambiar el disclaimer:

1. ✅ Actualizar ESTE archivo primero
2. ✅ Aplicar cambio a TODOS los archivos simultáneamente
3. ✅ Verificar con grep que todos coincidan
4. ✅ Commit con mensaje: "chore: Actualizar disclaimer estándar en todos los archivos"

---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso  
**Mantenedor:** Mary López (@yismary)
