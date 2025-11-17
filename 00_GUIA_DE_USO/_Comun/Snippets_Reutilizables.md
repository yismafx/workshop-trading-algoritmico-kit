# 📦 SNIPPETS REUTILIZABLES DEL KIT
## Documentación Interna - Uso Exclusivo Product Owner

**Propósito:** Centralizar bloques de contenido reutilizables para mantener consistencia.  
**Uso:** Copiar snippet exacto en archivos del kit (no usar enlaces, copiar contenido).  
**Mantenimiento:** Actualizar aquí primero, luego propagar a todos los archivos.

---

## 📋 ÍNDICE DE SNIPPETS

1. [DISCLAIMER_ESTANDAR](#snippet-1-disclaimer_estandar)
2. [SOPORTE](#snippet-2-soporte)
3. [NAVEGACION_FOOTER](#snippet-3-navegacion_footer)
4. [BREADCRUMB_TEMPLATE](#snippet-4-breadcrumb_template)
5. [SEPARADOR_SECCION](#snippet-5-separador_seccion)
6. [VERSION_FOOTER](#snippet-6-version_footer)

---

## SNIPPET 1: DISCLAIMER_ESTANDAR

**📍 Ubicación:** Inicio de archivos principales (después del título, antes del breadcrumb)

**🎯 Uso en:**
- Setup_A_Colab_Rapido.md
- Setup_A_Express.md
- Setup_A_Guiado.md
- Setup_B_Python_Local.md
- Setup_C_MetaTrader5.md
- GUIA_INICIO.md

**📄 Contenido:**

```markdown
> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.
```

---

## SNIPPET 2: SOPORTE

**📍 Ubicación:** Antes del footer de versión (última sección del archivo)

**🎯 Uso en:** TODOS los archivos .md principales

**📄 Contenido:**

```markdown
## 📞 SOPORTE

**¿Necesitas ayuda?**

- 📧 **Email:** yismaryme@gmail.com
- 💬 **Telegram:** [@yismafx](https://t.me/yismafx)

**Horario de soporte:**
- Lun-Vie: 9:00 AM - 6:00 PM (GMT-5)
- Respuesta promedio: 24-48 horas

**Nota:** Soporte técnico solo para participantes registrados del workshop.
```

---

## SNIPPET 3: NAVEGACION_FOOTER

**📍 Ubicación:** Antes de la sección de SOPORTE

**🎯 Uso en:** Archivos técnicos y guías principales

**📄 Template (adaptar según archivo):**

```markdown
## 🔗 NAVEGACIÓN

**← Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

**Ver también:**
- [Troubleshooting Maestro](Troubleshooting_Maestro.md)
- [FAQ Completo](FAQ_COMPLETO.md)
- [SITEMAP](SITEMAP.md)
```

**Nota:** Adaptar los links según el contexto del archivo.

---

## SNIPPET 4: BREADCRUMB_TEMPLATE

**📍 Ubicación:** Segunda línea del archivo (después del disclaimer)

**🎯 Uso en:** TODOS los archivos principales

**📄 Template:**

```markdown
**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 {TITULO_ARCHIVO}**
```

**Ejemplos:**

```markdown
# Para Setup A: Colab Rápido
**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 Setup A: Colab Rápido**

# Para Setup B: Python Local
**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 Setup B: Python Local**

# Para GUIA_INICIO
**🏠 [Inicio](../README.md) > 📄 Guía de Inicio**

# Para FAQ
**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 FAQ Completo**
```

---

## SNIPPET 5: SEPARADOR_SECCION

**📍 Ubicación:** Entre secciones principales

**🎯 Uso en:** TODOS los archivos

**📄 Contenido:**

```markdown
---
```

**⚠️ IMPORTANTE:**
- Usar SOLO `---` (3 guiones simples)
- NO usar separadores decorativos ASCII `═══`
- Dejar línea en blanco antes y después del separador

**Ejemplo de uso correcto:**

```markdown
## Sección 1

Contenido de la sección 1.

---

## Sección 2

Contenido de la sección 2.
```

---

## SNIPPET 6: VERSION_FOOTER

**📍 Ubicación:** Última línea del archivo (después de SOPORTE)

**🎯 Uso en:** TODOS los archivos .md

**📄 Contenido:**

```markdown
---

**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
```

**⚠️ IMPORTANTE:**
- NO incluir changelog
- NO incluir historial de versiones
- Mantener formato simple y limpio

---

## 📄 PROCESO DE ACTUALIZACIÓN

**Cuando necesites actualizar un snippet:**

1. Actualiza el contenido aquí en `Snippets_Reutilizables.md`
2. Identifica todos los archivos que usan ese snippet (ver "Uso en:")
3. Busca y reemplaza el snippet en todos esos archivos
4. Valida que el cambio se aplicó correctamente

**Ejemplo de búsqueda:**
```bash
grep -l "📞 SOPORTE" 00_GUIA_DE_USO/*.md
```

---

## 📊 ESTADÍSTICAS DE USO

| Snippet | Archivos Afectados | Frecuencia |
|---------|-------------------|------------|
| DISCLAIMER_ESTANDAR | 6 archivos | Alta |
| SOPORTE | 21 archivos | Muy Alta |
| NAVEGACION_FOOTER | 15 archivos | Alta |
| BREADCRUMB | 21 archivos | Muy Alta |
| SEPARADOR | 21 archivos | Muy Alta |
| VERSION_FOOTER | 21 archivos | Muy Alta |

---

## ⚠️ ADVERTENCIAS

1. **NO usar includes o referencias automáticas** - Copiar contenido directamente
2. **Mantener comentarios HTML** - Marcar origen del snippet con `<!-- Snippet: X -->`
3. **Actualizar en batch** - No dejar snippets desincronizados
4. **Validar después de cambios** - Verificar que todos los archivos tienen la versión correcta

---

## 📝 EJEMPLO DE USO EN ARCHIVO

**Cómo usar snippets en un archivo .md:**

```markdown
# Título del Archivo

<!-- Snippet: DISCLAIMER_ESTANDAR (ver _Comun/Snippets_Reutilizables.md) -->
> ⚠️ **DISCLAIMER IMPORTANTE**  
> Este material es parte del Workshop "Trading Algorítmico Aumentado con IA Generativa".  
> El contenido es exclusivamente educativo. NO constituye asesoría financiera.  
> El trading implica riesgo de pérdida de capital. Opera solo con capital que puedas perder.

<!-- Snippet: BREADCRUMB_TEMPLATE -->
**🏠 [Inicio](../README.md) > 📂 [Guía de Uso](GUIA_INICIO.md) > 📄 Nombre del Archivo**

---

[CONTENIDO DEL ARCHIVO]

---

<!-- Snippet: NAVEGACION_FOOTER -->
## 🔗 NAVEGACIÓN

**← Volver a:**
- [Guía de Inicio](GUIA_INICIO.md)
- [README Principal](../README.md)

---

<!-- Snippet: SOPORTE -->
## 📞 SOPORTE

**¿Necesitas ayuda?**

- 📧 **Email:** yismaryme@gmail.com
- 💬 **Telegram:** [@yismafx](https://t.me/yismafx)

---

<!-- Snippet: VERSION_FOOTER -->
**Versión:** 3.0 | **Última actualización:** 17 de noviembre de 2025  
**Estado:** ✅ Validado y listo para uso
```

---

**FIN DE SNIPPETS_REUTILIZABLES.MD**

**Mantenido por:** Mary (Product Owner)  
**Última actualización:** 17 de noviembre de 2025  
**Versión:** 1.0
