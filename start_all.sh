#!/bin/bash

echo "🌌 INICIANDO MICROCOSMOS: MODO MONETIZACIÓN TOTAL"
echo "------------------------------------------------"

# 1. Activar el Entorno Virtual y el Loop del Oráculo
source /home/chalamandramagistral/microcosmos_elite/venv/bin/activate
echo "🧬 Oráculo Cuántico: ACTIVADO (Bucle de 60s)"
while true; do 
    /home/chalamandramagistral/microcosmos_elite/hi 
    sleep 60
done &

# 2. Iniciar el Backend API
echo "🚀 API de Monetización: ACTIVADA (Puerto 5000)"
node /home/chalamandramagistral/microcosmos_elite/backend/server.js &

# 3. Iniciar el Frontend Dashboard
echo "🖥️ Dashboard React: ACTIVADO (Puerto 5173)"
cd /home/chalamandramagistral/microcosmos_elite/frontend && npm run dev -- --host &

echo "------------------------------------------------"
echo "✅ Todo el sistema está en línea. Abre http://localhost:5173"
echo "Para detener todo, presiona CTRL+C y luego escribe 'pkill node'"
