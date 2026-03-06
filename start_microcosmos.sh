#!/bin/bash
echo "🌌 INICIANDO MICROCOSMOS COMPLETO"

# 1. Backend API
cd ~/microcosmos_elite/backend
nohup node server.js > backend.log 2>&1 &

# 2. Frontend Dashboard
cd ~/microcosmos_elite/frontend
nohup npm run dev -- --host > frontend.log 2>&1 &

# 3. Latido + Oráculo
cd ~/microcosmos_elite
nohup bash scripts/latido.sh > data/latido.log 2>&1 &

echo "Todo en línea:"
echo "- Backend: http://localhost:5000"
echo "- Frontend: http://localhost:5173"
echo "- Logs: tail -f data/latido.log backend.log frontend.log"
