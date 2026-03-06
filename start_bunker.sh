#!/bin/bash
cd ~/microcosmos_elite

echo "🧨 Reiniciando bunker..."

# Mata procesos anteriores
pkill -f app_final.py 2>/dev/null
pkill -f asset_hunter.py 2>/dev/null
pkill -f cloudflared 2>/dev/null
sleep 1

# Obtener IP local no loopback
IP=$(ip addr show | grep -oP 'inet \K[\d.]+' | grep -v '^127\.' | head -1)
[ -z "$IP" ] && IP="127.0.0.1"

# Lanza Flask
nice -n 19 python3 app_final.py > flask.log 2>&1 &
echo "✅ Flask lanzado (PID $!)"
sleep 2

# Lanza hunter
touch oportunidades.txt
nice -n 19 python3 asset_hunter.py >> hunter.log 2>&1 &
echo "✅ Hunter lanzado (PID $!)"
sleep 2

# Lanza túnel apuntando a la IP real
cloudflared tunnel --url http://$IP:5000 > tunnel.log 2>&1 &
echo "✅ Túnel lanzado (PID $!)"

# Espera hasta obtener la URL (máx 10 intentos)
for i in {1..10}; do
    URL=$(strings tunnel.log 2>/dev/null | grep -o 'https://.*\.trycloudflare\.com' | head -1)
    if [ -n "$URL" ]; then
        echo "🌐 URL PÚBLICA: $URL"
        break
    fi
    sleep 2
done

if [ -z "$URL" ]; then
    echo "⚠️  No se pudo obtener la URL. Revisa tunnel.log"
fi

echo "🛡️ Bunker activo."
ps aux | grep -E "python|cloudflared" | grep -v grep
