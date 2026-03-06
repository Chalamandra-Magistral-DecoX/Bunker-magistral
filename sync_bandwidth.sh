#!/bin/bash
# Honeygain estimado (ajusta según veas en dashboard)
HONEY_GAIN=0.20
# PacketStream estimado
PACKET_GAIN=0.15
FECHA=$(date +%Y-%m-%d)
TOTAL=$(echo "$HONEY_GAIN + $PACKET_GAIN" | bc)
sqlite3 ~/microcosmos_elite/boveda.db "INSERT INTO pagos (monto, cliente) VALUES ($TOTAL, 'bandwidth_$FECHA');"
echo "✅ Bandwidth: +$TOTAL USD agregados"
