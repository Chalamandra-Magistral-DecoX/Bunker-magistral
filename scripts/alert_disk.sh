#!/bin/bash
AVAIL=$(df -h . | tail -1 | awk '{print $4}' | sed 's/G//')
if (( $(echo "$AVAIL < 1" | bc -l) )); then
  echo "⚠️ DISCO CRÍTICO: Solo $AVAIL GB libres!" | tee -a ~/microcosmos_elite/data/alerts.log
  # Opcional: notificar Telegram
  ~/microcosmos_elite/scripts/notificar.sh "ALERTA DISCO: $AVAIL GB libres en Nodo Xalapa"
fi
