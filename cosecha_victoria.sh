#!/bin/bash
echo "♻️ [FASE 1] Limpieza de Entropía (Docker & RAM)"
# Matar contenedores zombis que causan el error 'not running'
docker rm -f $(docker ps -aq) 2>/dev/null
# Liberar caché de memoria para el Celeron
sync && sudo sysctl -w vm.drop_caches=3

echo "📊 [FASE 2] Sincronización de Masa Crítica"
# Extraer total de ventas de money.log y actualizar JSON para Vercel
TOTAL_VENTAS=$(awk -F',' '{sum += $1} END {print sum}' ~/Microcosmos_Elite/data/money.log)
echo "{\"masa_critica\": $TOTAL_VENTAS, \"ultima_fidelidad\": \"97%\"}" > ~/Microcosmos_Elite/data/metrics.json

echo "🚀 [FASE 3] Despliegue de Soberanía (Vercel)"
vercel --prod --yes
echo "✅ Cosecha completada. Masa Crítica en: $TOTAL_VENTAS USD"
