import requests
import os

# Credenciales de Chalamandra (Ya configuradas previamente)
TOKEN = "TU_BOT_TOKEN_AQUI"
CHAT_ID = "TU_CHAT_ID_AQUI"

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🦎 [BÚNKER CHALAMANDRA]:\n{mensaje}"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error enviando Telegram: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        enviar_alerta(sys.argv[1])
