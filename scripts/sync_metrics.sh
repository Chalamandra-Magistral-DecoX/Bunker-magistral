#!/bin/bash
ROOT="/home/chalamandramagistral/microcosmos_elite"
REPORT_CSV="$ROOT/data/informe_rendimiento.csv"

# 1. Hardware (usa claves reales de metrics_engine.py)
HW_RAW=$(python3 "$ROOT/scripts/metrics_engine.py" 2>/dev/null || echo '{"timestamp":"'$(date +%s)'","poas":0,"true_cac":0,"ratio":0,"status":"ERROR"}')
TS=$(echo "$HW_RAW" | jq -r '.timestamp // "'$(date +%s)'"')
POAS_HW=$(echo "$HW_RAW" | jq -r '.poas // 0')
CAC=$(echo "$HW_RAW" | jq -r '.true_cac // 0')
RATIO=$(echo "$HW_RAW" | jq -r '.ratio // 0')

# 2. Negocio (Grover)
BIZ_RAW=$(python3 "$ROOT/scripts/grover_engine.py" 2>/dev/null || echo '{"poas":0,"fidelidad":0,"mejor_campaña":0}')
POAS=$(echo "$BIZ_RAW" | jq -r '.poas // 0')
FID=$(echo "$BIZ_RAW" | jq -r '.fidelidad // 0')
IDX=$(echo "$BIZ_RAW" | jq -r '.mejor_campaña // 0')

# 3. Registro (adaptado a claves reales)
echo "$TS,$POAS_HW,$CAC,$RATIO,$POAS,$FID,$IDX" >> "$REPORT_CSV"

# 4. JSON para frontend
JSON_DATA=$(jq -n \
  --arg ts "$TS" \
  --arg poas_hw "$POAS_HW" --arg cac "$CAC" --arg ratio "$RATIO" \
  --arg poas "$POAS" --arg fd "$FID" --arg idx "$IDX" \
  '{
    timestamp: $ts,
    hardware: {
      poas: ($poas_hw | tonumber),
      cac: ($cac | tonumber),
      ratio: ($ratio | tonumber)
    },
    business: {
      poas: ($poas | tonumber),
      fidelidad: ($fd | tonumber),
      campana_ganadora: ($idx | tonumber),
      status: "NIRVANA_CODE"
    }
  }')

echo "$JSON_DATA" > "$ROOT/frontend/public/data/shor_stats.json"

echo "📊 Telemetría: POAS HW ${POAS_HW}x | CAC ${CAC} | Ratio ${RATIO} | POAS Biz ${POAS}x | FID ${FID}% | Campaña #${IDX}"
