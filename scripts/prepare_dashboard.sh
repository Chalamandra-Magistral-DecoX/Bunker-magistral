#!/bin/bash
ROOT="/home/chalamandramagistral/microcosmos_elite"
DATA_FILE="$ROOT/data/informe_cuantico.csv"
JSON_OUT="$ROOT/frontend/public/data/history.json"

if [ -s "$DATA_FILE" ]; then
    # Usamos awk para añadir un pequeño ruido aleatorio al POAS para la visualización
    grep -v '^$' "$DATA_FILE" | tail -n 15 | awk -F',' 'BEGIN {OFS=","} {
        srand(); 
        noise=(rand()*0.4)-0.2; # Ruido entre -0.2 y +0.2
        $5=$5+noise; 
        print $0
    }' | jq -R -s '
      split("\n") | map(select(length > 0) | split(",")) | map({
        timestamp: .[0],
        ejecucion: .[1] | tonumber,
        ram: .[2] | tonumber,
        cpu: .[3] | tonumber,
        poas: .[4] | tonumber,
        fidelidad: .[5] | tonumber,
        campana: .[6] | tonumber
      })' > "$JSON_OUT"
    echo "💎 Visualización Sintonizada en $JSON_OUT"
else
    echo "⚠️ Esperando datos..."
fi
