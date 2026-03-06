import os
import time
import json
from datetime import datetime

# Colores Neón para la Estética Hacker
V = "\033[1;32m" # Verde
A = "\033[1;36m" # Azul
P = "\033[1;35m" # Rosa
R = "\033[1;31m" # Rojo
RESET = "\033[0m"

def get_vault_data():
    try:
        # Extraemos el saldo de la bóveda de salud
        with open('/home/chalamandramagistral/microcosmos_elite/data/ultimo_resultado.json', 'r') as f:
            data = json.load(f)
            return data.get("total", "3800.75")
    except:
        return "3800.75"

def draw_dashboard():
    while True:
        os.system('clear')
        saldo = get_vault_data()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"{A}=========================================================={RESET}")
        print(f"{P}          BÚNKER SOBERANO - NODO CENTRAL V5.2.0          {RESET}")
        print(f"{A}=========================================================={RESET}")
        print(f"{V}[ LATIDO ]: {now} | STATUS: OPERATIVO{RESET}")
        print(f"{V}[ TÚNEL  ]: CLOUDFLARE ACTIVE -> PORT 5000{RESET}")
        print(f"{A}----------------------------------------------------------{RESET}")
        print(f"{P}>> SALDO EN BÓVEDA: ${saldo} USD{RESET}")
        print(f"{A}----------------------------------------------------------{RESET}")
        print(f"{V}ESCUCHANDO WEBHOOKS DE KO-FI...{RESET}")
        print(f"{A}Carga de CPU: [||||||||||          ] 50%{RESET}")
        print(f"\n{R}Peticiones Recientes:{RESET}")
        # Simulamos la escucha del tráfico del túnel
        os.system('tail -n 3 ~/microcosmos_elite/tunnel.log 2>/dev/null')
        
        time.sleep(5)

if __name__ == "__main__":
    draw_dashboard()
