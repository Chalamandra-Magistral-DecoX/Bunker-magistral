#!/bin/bash
while true; do
    clear
    echo "--- MONITOR DE ESTRÉS CUÁNTICO (CELERON N4020) ---"
    tail -n 5 ~/microcosmos_elite/data/informe_rendimiento.csv | awk -F',' '{
        printf "TS: %s | CPU: %s%% | RAM Δ: %s MB | FID: %s%%\n", $1, $4, $3, $6
    }'
    echo "--------------------------------------------------"
    # Alerta de Swapping (Si RAM Delta > 500MB en este hardware)
    LAST_RAM=$(tail -n 1 ~/microcosmos_elite/data/informe_rendimiento.csv | cut -d',' -f3)
    if (( $(echo "$LAST_RAM > 500" | bc -l) )); then
        echo "⚠️ ALERTA: Consumo de RAM crítico. Riesgo de Swapping."
    fi
    sleep 3
done
