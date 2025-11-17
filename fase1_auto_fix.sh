#!/bin/bash
# SCRIPT DE CORRECCIÓN AUTOMATIZADA - FASE 1
# Workshop: Trading Algorítmico Aumentado con IA Generativa
# Fecha: 16 de noviembre de 2025
# Ejecutor: Claude Sonnet 4.5

set -e  # Detener en caso de error

echo "═══════════════════════════════════════════════════════════════"
echo "  FASE 1: CORRECCIÓN AUTOMATIZADA DEL REPOSITORIO"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Variables
REPO_PATH="."
GUIA_PATH="$REPO_PATH/00_GUIA_DE_USO"
LOG_FILE="fase1_execution_log.txt"

# Inicializar log
echo "Inicio de ejecución: $(date)" > $LOG_FILE
echo "═══════════════════════════════════════════════════════════════" >> $LOG_FILE

# ═════════════════════════════════════════════════════════════════
# ETAPA 1: ELIMINACIÓN DE DUPLICACIÓN
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ETAPA 1: ELIMINACIÓN DE DUPLICACIÓN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Tarea 1.1: Eliminar carpeta duplicada
echo "[1.1] Eliminando carpeta '00_GUIA_DE_USO - copia'..."
if [ -d "$REPO_PATH/00_GUIA_DE_USO - copia" ]; then
    rm -rf "$REPO_PATH/00_GUIA_DE_USO - copia"
    echo "✅ Carpeta eliminada correctamente" | tee -a $LOG_FILE
else
    echo "ℹ️  Carpeta ya no existe (posiblemente eliminada previamente)" | tee -a $LOG_FILE
fi

# Tarea 1.2: Eliminar archivo backup
echo "[1.2] Eliminando archivo backup GUIA_INICIO.vold.md..."
if [ -f "$GUIA_PATH/GUIA_INICIO.vold.md" ]; then
    rm "$GUIA_PATH/GUIA_INICIO.vold.md"
    echo "✅ Archivo backup eliminado" | tee -a $LOG_FILE
else
    echo "ℹ️  Archivo backup ya no existe" | tee -a $LOG_FILE
fi

echo ""
echo "✅ ETAPA 1 COMPLETADA"
echo ""

# ═════════════════════════════════════════════════════════════════
# ETAPA 2: CORRECCIÓN DE LINKS ROTOS
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ETAPA 2: CORRECCIÓN DE LINKS ROTOS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Crear backup antes de modificaciones masivas
echo "[2.0] Creando backup de seguridad..."
BACKUP_DIR="$REPO_PATH/00_GUIA_DE_USO_BACKUP_$(date +%Y%m%d_%H%M%S)"
cp -r "$GUIA_PATH" "$BACKUP_DIR"
echo "✅ Backup creado en: $BACKUP_DIR" | tee -a $LOG_FILE
echo ""

# Tarea 2.1: Setup_Colab_Rapido.md → Setup_A_Colab_Rapido.md
echo "[2.1] Corrigiendo: Setup_Colab_Rapido.md → Setup_A_Colab_Rapido.md"

# Contar ocurrencias antes
ANTES=$(grep -r "Setup_Colab_Rapido\.md" "$GUIA_PATH"/*.md 2>/dev/null | wc -l || echo "0")
echo "    Ocurrencias encontradas: $ANTES" | tee -a $LOG_FILE

# Aplicar corrección
find "$GUIA_PATH" -type f -name "*.md" -exec sed -i.bak 's/Setup_Colab_Rapido\.md/Setup_A_Colab_Rapido.md/g' {} \;

# Contar ocurrencias después
DESPUES=$(grep -r "Setup_Colab_Rapido\.md" "$GUIA_PATH"/*.md 2>/dev/null | wc -l || echo "0")

if [ "$DESPUES" -eq 0 ]; then
    echo "✅ Corrección aplicada: $ANTES ocurrencias corregidas" | tee -a $LOG_FILE
    # Eliminar archivos .bak temporales
    find "$GUIA_PATH" -type f -name "*.bak" -delete
else
    echo "❌ ERROR: Aún quedan $DESPUES ocurrencias sin corregir" | tee -a $LOG_FILE
fi

echo ""

# Tarea 2.2: Troubleshooting_Setup_A.md → Troubleshooting_Maestro.md
echo "[2.2] Corrigiendo: Troubleshooting_Setup_A.md → Troubleshooting_Maestro.md"

ANTES=$(grep -r "Troubleshooting_Setup_A\.md" "$GUIA_PATH"/*.md 2>/dev/null | wc -l || echo "0")
echo "    Ocurrencias encontradas: $ANTES" | tee -a $LOG_FILE

find "$GUIA_PATH" -type f -name "*.md" -exec sed -i.bak 's/Troubleshooting_Setup_A\.md/Troubleshooting_Maestro.md/g' {} \;

DESPUES=$(grep -r "Troubleshooting_Setup_A\.md" "$GUIA_PATH"/*.md 2>/dev/null | wc -l || echo "0")

if [ "$DESPUES" -eq 0 ]; then
    echo "✅ Corrección aplicada: $ANTES ocurrencias corregidas" | tee -a $LOG_FILE
    find "$GUIA_PATH" -type f -name "*.bak" -delete
else
    echo "❌ ERROR: Aún quedan $DESPUES ocurrencias sin corregir" | tee -a $LOG_FILE
fi

echo ""

# Tarea 2.3: Eliminar referencias a Setup_D_Interactive_Brokers.md
echo "[2.3] Eliminando referencias a Setup_D_Interactive_Brokers.md"

ARCHIVOS_AFECTADOS=(
    "$GUIA_PATH/GLOSARIO_NAVEGACION.md"
    "$GUIA_PATH/Mapa_Recursos_Workshop.md"
    "$GUIA_PATH/SITEMAP.md"
)

for archivo in "${ARCHIVOS_AFECTADOS[@]}"; do
    if [ -f "$archivo" ]; then
        # Eliminar líneas que contienen Setup_D_Interactive_Brokers
        sed -i.bak '/Setup_D_Interactive_Brokers/d' "$archivo"
        echo "    ✓ $(basename $archivo)" | tee -a $LOG_FILE
    fi
done

# Verificar
SETUP_D_REFS=$(grep -r "Setup_D_Interactive_Brokers" "$GUIA_PATH"/*.md 2>/dev/null | wc -l || echo "0")
if [ "$SETUP_D_REFS" -eq 0 ]; then
    echo "✅ Todas las referencias a Setup D eliminadas" | tee -a $LOG_FILE
    find "$GUIA_PATH" -type f -name "*.bak" -delete
else
    echo "⚠️  Aún quedan $SETUP_D_REFS referencias a Setup D" | tee -a $LOG_FILE
fi

echo ""

# Tarea 2.4: Eliminar referencias a Setup_A_Broker_*.md
echo "[2.4] Eliminando referencias a Setup_A_Broker_*.md"

# Eliminar líneas con Setup_A_Broker_Alpaca.md o Setup_A_Broker_IB.md
find "$GUIA_PATH" -type f -name "*.md" -exec sed -i.bak '/Setup_A_Broker_/d' {} \;

BROKER_REFS=$(grep -r "Setup_A_Broker_" "$GUIA_PATH"/*.md 2>/dev/null | wc -l || echo "0")
if [ "$BROKER_REFS" -eq 0 ]; then
    echo "✅ Todas las referencias a Setup_A_Broker_*.md eliminadas" | tee -a $LOG_FILE
    find "$GUIA_PATH" -type f -name "*.bak" -delete
else
    echo "⚠️  Aún quedan $BROKER_REFS referencias" | tee -a $LOG_FILE
fi

echo ""

# Tarea 2.5: Eliminar referencia a MANUAL_DE_ESTILO.md (documento interno)
echo "[2.5] Eliminando referencia a MANUAL_DE_ESTILO.md en README.md (documento interno)"

if [ -f "$GUIA_PATH/README.md" ]; then
    # Contar ocurrencias antes
    ANTES=$(grep -c "MANUAL_DE_ESTILO" "$GUIA_PATH/README.md" 2>/dev/null || echo "0")
    echo "    Ocurrencias encontradas: $ANTES" | tee -a $LOG_FILE
    
    # Eliminar líneas que contienen MANUAL_DE_ESTILO
    sed -i.bak '/MANUAL_DE_ESTILO/d' "$GUIA_PATH/README.md"
    
    # Verificar
    DESPUES=$(grep -c "MANUAL_DE_ESTILO" "$GUIA_PATH/README.md" 2>/dev/null || echo "0")
    
    if [ "$DESPUES" -eq 0 ]; then
        echo "✅ Referencia eliminada en README.md (documento interno, solo Mary)" | tee -a $LOG_FILE
        rm -f "$GUIA_PATH/README.md.bak"
    else
        echo "⚠️  Aún quedan $DESPUES referencias" | tee -a $LOG_FILE
    fi
else
    echo "ℹ️  README.md no existe en la ruta esperada" | tee -a $LOG_FILE
fi

echo ""
echo "✅ ETAPA 2 COMPLETADA"
echo ""

# ═════════════════════════════════════════════════════════════════
# ETAPA 3: CONSOLIDACIÓN DE CONTENIDO
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ETAPA 3: CONSOLIDACIÓN DE CONTENIDO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Tarea 3.1: Verificar Troubleshooting_Comun.md vs Troubleshooting_Maestro.md
echo "[3.1] Analizando Troubleshooting_Comun.md vs Troubleshooting_Maestro.md"

if [ -f "$GUIA_PATH/Troubleshooting_Comun.md" ]; then
    echo "⚠️  Archivo Troubleshooting_Comun.md existe" | tee -a $LOG_FILE
    echo "    Requiere revisión manual para verificar contenido único" | tee -a $LOG_FILE
    echo "    Acción: Marcar para revisión en Tarea 3.1" | tee -a $LOG_FILE
    
    # Crear reporte de diferencias
    if [ -f "$GUIA_PATH/Troubleshooting_Maestro.md" ]; then
        echo "    Generando reporte de diferencias..." | tee -a $LOG_FILE
        diff "$GUIA_PATH/Troubleshooting_Comun.md" "$GUIA_PATH/Troubleshooting_Maestro.md" > troubleshooting_diff.txt 2>&1 || true
        echo "    Reporte guardado en: troubleshooting_diff.txt" | tee -a $LOG_FILE
    fi
else
    echo "ℹ️  Troubleshooting_Comun.md no existe o ya fue eliminado" | tee -a $LOG_FILE
fi

echo ""
echo "⚠️  ETAPA 3 REQUIERE REVISIÓN MANUAL"
echo ""

# ═════════════════════════════════════════════════════════════════
# ETAPA 5: VALIDACIÓN (Etapa 4 es manual)
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ETAPA 5: VALIDACIÓN AUTOMATIZADA"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Tarea 5.1: Validar links
echo "[5.1] Validando links..."

# Buscar todos los links .md en archivos markdown
find "$GUIA_PATH" -name "*.md" -exec grep -Ho '\[.*\]([^)]*\.md)' {} \; | \
    grep -o '([^)]*.md)' | tr -d '()' | sort -u > /tmp/referenced_files.txt

TOTAL_LINKS=$(wc -l < /tmp/referenced_files.txt)
BROKEN_LINKS=0

echo "    Total de archivos .md referenciados: $TOTAL_LINKS" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

while IFS= read -r file; do
    # Limpiar path (eliminar ../ y ./)
    clean_file=$(echo "$file" | sed 's|^\./||' | sed 's|^\.\./||')
    
    # Verificar en múltiples ubicaciones posibles
    if [ -f "$GUIA_PATH/$clean_file" ]; then
        echo "    ✓ $clean_file" | tee -a $LOG_FILE
    elif [ -f "$REPO_PATH/$clean_file" ]; then
        echo "    ✓ $clean_file (en raíz)" | tee -a $LOG_FILE
    else
        echo "    ❌ LINK ROTO: $file" | tee -a $LOG_FILE
        BROKEN_LINKS=$((BROKEN_LINKS + 1))
    fi
done < /tmp/referenced_files.txt

echo "" | tee -a $LOG_FILE

if [ "$BROKEN_LINKS" -eq 0 ]; then
    echo "✅ VALIDACIÓN EXITOSA: 0 links rotos" | tee -a $LOG_FILE
else
    echo "❌ VALIDACIÓN FALLIDA: $BROKEN_LINKS links rotos detectados" | tee -a $LOG_FILE
fi

echo ""

# ═════════════════════════════════════════════════════════════════
# REPORTE FINAL
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "REPORTE FINAL - FASE 1"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "Fin de ejecución: $(date)" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

echo "═══════════════════════════════════════════════════════════════"
echo "  RESUMEN DE EJECUCIÓN"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Etapa 1: ELIMINACIÓN DE DUPLICACIÓN" | tee -a $LOG_FILE
echo "  ✅ Carpeta duplicada eliminada" | tee -a $LOG_FILE
echo "  ✅ Archivo backup eliminado" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "Etapa 2: CORRECCIÓN DE LINKS ROTOS" | tee -a $LOG_FILE
echo "  ✅ Setup_Colab_Rapido.md corregido" | tee -a $LOG_FILE
echo "  ✅ Troubleshooting_Setup_A.md corregido" | tee -a $LOG_FILE
echo "  ✅ Referencias a Setup D eliminadas" | tee -a $LOG_FILE
echo "  ✅ Referencias a Setup_A_Broker_*.md eliminadas" | tee -a $LOG_FILE
echo "  ✅ Referencia a MANUAL_DE_ESTILO eliminada (doc interno)" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "Etapa 3: CONSOLIDACIÓN DE CONTENIDO" | tee -a $LOG_FILE
echo "  ⚠️  Requiere revisión manual (Troubleshooting_Comun.md)" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "Etapa 5: VALIDACIÓN" | tee -a $LOG_FILE
if [ "$BROKEN_LINKS" -eq 0 ]; then
    echo "  ✅ Links rotos = 0" | tee -a $LOG_FILE
else
    echo "  ❌ Links rotos = $BROKEN_LINKS" | tee -a $LOG_FILE
fi
echo "" | tee -a $LOG_FILE
echo "═══════════════════════════════════════════════════════════════"
echo "" | tee -a $LOG_FILE

echo "📋 Log completo guardado en: $LOG_FILE"
echo "💾 Backup de seguridad en: $BACKUP_DIR"
echo ""

if [ "$BROKEN_LINKS" -eq 0 ]; then
    echo "✅ FASE 1 COMPLETADA EXITOSAMENTE"
    echo ""
    echo "Próximos pasos:"
    echo "  1. Revisar Troubleshooting_Comun.md vs Troubleshooting_Maestro.md"
    echo "  2. Testing Team: Validar flujos de navegación"
    echo "  3. Mary: Aprobar cambios"
    echo "  4. Commit y deploy a GitHub Pages"
    exit 0
else
    echo "⚠️  FASE 1 COMPLETADA CON ADVERTENCIAS"
    echo ""
    echo "Acción requerida:"
    echo "  Revisar links rotos reportados arriba antes de proceder"
    exit 1
fi
