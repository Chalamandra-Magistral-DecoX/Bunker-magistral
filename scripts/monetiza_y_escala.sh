#!/bin/bash
echo "🚀 Iniciando loop monetización + escalado - $(date)"

# 1. Generar contenido de venta
~/microcosmos_elite/scripts/content_gen.sh > /tmp/post.txt

# 2. Publicar en X (twurl o xdotool o API)
echo "Publicando post de venta..."
# Ejemplo con twurl (instala si no lo tienes)
# twurl -d "status=$(cat /tmp/post.txt) https://ko-fi.com/chalamandra/shop" /1.1/statuses/update.json

# 3. Ejecutar demos públicas (tráfico gratis)
python3 ~/microcosmos_elite/scripts/shor_15.py --public 2>/dev/null &

# 4. Revisar masa crítica y decidir reinversión
TOTAL=$(awk -F',' '{sum += $1} END {printf "%.2f", sum}' ~/microcosmos_elite/data/money.log 2>/dev/null || echo "0")
echo "💰 Masa actual: $ $TOTAL"

if (( $(echo "$TOTAL > 500" | bc -l) )); then
  echo "✅ Reinversión activada: comprando más Chromebooks o cloud nodes"
  # Aquí puedes poner webhook a tu proveedor de servidores o compra automática
fi

echo "Loop completado."
