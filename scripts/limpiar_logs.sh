#!/bin/bash
LOG_FILE="/home/chalamandramagistral/microcosmos_elite/data/latido.log"
# Si el log supera los 10MB, lo recortamos a las últimas 1000 líneas
if [ $(stat -c%s "$LOG_FILE") -gt 10485760 ]; then
    tail -n 1000 "$LOG_FILE" > "${LOG_FILE}.tmp" && mv "${LOG_FILE}.tmp" "$LOG_FILE"
    echo "$(date) - Log purgado por exceso de tamaño."
fi
