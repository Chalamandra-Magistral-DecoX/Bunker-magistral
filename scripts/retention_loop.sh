#!/bin/bash
# Simula el envío de valor a los correos en money.log
LEADS=$(cut -d',' -f2 ~/microcosmos_elite/data/money.log)
for lead in $LEADS; do
    echo "[$(date)] Enviando 'Blueprint Cuántico' a $lead" >> ~/microcosmos_elite/data/retention.log
done
