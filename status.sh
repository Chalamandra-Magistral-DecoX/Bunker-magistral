#!/bin/bash
echo "======================================"
echo "🦎 BÚNKER CHALAMANDRA - ESTADO"
echo "======================================"

echo -e "\n🔹 PROCESOS ACTIVOS:"
ps aux | grep -E "python|cloudflared|watchdog" | grep -v grep

echo -e "\n🔹 BÓVEDA TOTAL:"
sqlite3 ~/microcosmos_elite/boveda.db "SELECT SUM(monto) FROM pagos;" | awk '{print "$" $0}'

echo -e "\n🔹 ÚLTIMOS HALLAZGOS ÉLITE:"
tail -5 ~/microcosmos_elite/hunter.log | grep "ELITE FIND" || echo "Ninguno aún"

echo -e "\n🔹 URL DEL TÚNEL:"
strings ~/microcosmos_elite/tunnel.log | grep -o 'https://.*\.trycloudflare\.com' | tail -1

echo -e "\n🔹 REPORTE MAESTRO:"
python3 ~/microcosmos_elite/reporte_maestro.py 2>/dev/null | head -10
