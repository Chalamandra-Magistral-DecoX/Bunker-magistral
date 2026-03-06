#!/bin/bash
clear
echo "✨ VERIFICANDO ESTADO DEL NIRVANA... ✨"
sleep 1
FID=$(tail -n 1 ~/microcosmos_elite/data/informe_rendimiento.csv | cut -d',' -f6)
CPU=$(tail -n 1 ~/microcosmos_elite/data/informe_rendimiento.csv | cut -d',' -f4)

echo "----------------------------------------"
echo "🚀 Fidelidad: $FID%"
echo "💻 Carga CPU: $CPU%"
echo "📂 Disco: $(df -h . | tail -1 | awk '{print $4}') disponible."
echo "----------------------------------------"

if (( $(echo "$FID == 100.00" | bc -l) )); then
    echo "💎 ¡TODO CHALE, TODO AL 100%! 💎"
    echo "Soberana, tu Microcosmos es ley."
else
    echo "📡 Sincronizando... El éxito es inminente."
fi
