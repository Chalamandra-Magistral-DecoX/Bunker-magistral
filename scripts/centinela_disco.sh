#!/bin/bash
UMBRAL=90
USO=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ "$USO" -gt "$UMBRAL" ]; then
    echo "⚠️ DISCO CRÍTICO: ${USO}% - Iniciando purga de emergencia..."
    rm -rf ~/.cache/pip
    find ~/microcosmos_elite -type d -name "__pycache__" -exec rm -rf {} +
    # Vaciar logs pesados
    truncate -s 0 ~/microcosmos_elite/data/latido.log
    echo "✅ Purga completada."
fi
