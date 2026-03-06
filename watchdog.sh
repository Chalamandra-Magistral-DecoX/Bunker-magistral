#!/bin/bash
cd ~/microcosmos_elite

IP=$(ip addr show | grep -oP 'inet \K[\d.]+' | grep -v '^127\.' | head -1)
[ -z "$IP" ] && IP="127.0.0.1"

while true; do
    if ! pgrep -f app_final.py > /dev/null; then
        nice -n 19 python3 app_final.py >> flask.log 2>&1 &
        echo "[$(date)] Flask reiniciado" >> watchdog.log
    fi
    if ! pgrep -f asset_hunter.py > /dev/null; then
        nice -n 19 python3 asset_hunter.py >> hunter.log 2>&1 &
        echo "[$(date)] Hunter reiniciado" >> watchdog.log
    fi
    if ! pgrep -f cloudflared > /dev/null; then
        cloudflared tunnel --url http://$IP:5000 >> tunnel.log 2>&1 &
        echo "[$(date)] Túnel reiniciado" >> watchdog.log
    fi
    # PacketStream (Docker)
    if ! sudo docker ps | grep -q packetstream; then
        sudo docker run -d --name packetstream --restart always -e CID=TU_NUEVO_CID packetstream/psclient
        echo "[$(date)] PacketStream reiniciado" >> watchdog.log
    fi
    sleep 30
done
python3 passive_income.py &

# Auto-limpieza si el disco está lleno
DISK_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
if [ "$DISK_USAGE" -gt 90 ]; then
    echo "Disco al $DISK_USAGE%. Iniciando purga de emergencia..."
    python3 ~/microcosmos_elite/notificador.py "⚠️ ALERTA: Disco al $DISK_USAGE%. Iniciando limpieza automática."
    sudo apt-get clean
    journalctl --vacuum-size=10M
    truncate -s 0 ~/microcosmos_elite/data/*.log
fi
