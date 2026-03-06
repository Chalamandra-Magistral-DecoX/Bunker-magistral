#!/bin/bash
TOKEN="8623611704:AAEqL1y_WAdtJU-MsCGTQLymM1p4f9Zb0nI"
CHAT_ID="6369018440"

# Verificar procesos críticos
HUNTER=$(pgrep -f asset_hunter.py)
TUNNEL=$(pgrep -f cloudflared)

if [ -z "$HUNTER" ]; then
    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
         -d "chat_id=$CHAT_ID" -d "text=⚠️ *ALERTA:* Hunter caído. Reiniciando..." -d "parse_mode=Markdown"
    nice -n 19 python3 /home/chalamandramagistral/microcosmos_elite/asset_hunter.py >> /home/chalamandramagistral/microcosmos_elite/hunter.log 2>&1 &
fi

if [ -z "$TUNNEL" ]; then
    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
         -d "chat_id=$CHAT_ID" -d "text=🌐 *ALERTA:* Túnel fuera de línea. Revisando servicio..." -d "parse_mode=Markdown"
    sudo systemctl restart microcosmos.service
fi
