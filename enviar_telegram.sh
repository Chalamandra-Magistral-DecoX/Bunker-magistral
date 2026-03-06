#!/bin/bash
TOKEN="8083155376:AAFDHxoXZL8Nxqt63pJNwZaMAz88h1hSnR4"
CHAT_ID="-1003260850014"   # <--- REEMPLAZA ESTO

if [ -z "$CHAT_ID" ]; then
    echo "❌ Error: No hay CHAT_ID. Configuralo manualmente en el script."
    exit 1
fi

MENSAJE=$(python3 ~/microcosmos_elite/reporte_maestro.py)

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d "chat_id=$CHAT_ID" \
     -d "text=$MENSAJE" \
     -d "parse_mode=Markdown"
