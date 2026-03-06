#!/bin/bash
ROOT="$HOME/microcosmos_elite"
while true; do
    echo "💓 Latido: $(date)"
    python3 "$ROOT/scripts/shor_15.py"
    bash "$ROOT/scripts/sync_metrics.sh"
    # Sincronización con GitHub cada 5 ciclos
    COUNT=$((COUNT+1))
    if [ $COUNT -ge 5 ]; then
    bash ~/microcosmos_elite/scripts/prepare_dashboard.sh
        bash ~/microcosmos_elite/scripts/auto_push.sh
        COUNT=0
    fi
    sleep 10
done
