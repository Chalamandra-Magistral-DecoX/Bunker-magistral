#!/bin/bash
clear
echo -e "\033[1;32m"
echo "  __  __ ___ ___ ___  ___   ___ ___  ___ __  __  ___  ___ "
echo " |  \/  |_ _/ __| _ \/ _ \ / __/ _ \/ __|  \/  |/ _ \/ __|"
echo " | |\/| || | (__|   / (_) | (_| (_) \__ \ |\/| | (_) \__ \\"
echo " |_|  |_|___\___|_|_\\___/ \___\___/|___/_|  |_|\___/|___/"
echo -e "\033[0m"
echo -e "\033[1;34m [ ESTATUS DEL NODO: XALAPA_01 | FIDELIDAD: 95.21% ] \033[0m"
echo "------------------------------------------------------------"

# 1. Iniciar Receptor de Capital (Background)
source ~/microcosmos_elite/venv/bin/activate
python3 ~/microcosmos_elite/scripts/money_trigger.py > /dev/null 2>&1 &
echo -e " ✅ \033[0;32mMoney Trigger:\033[0m Activo (Puerto 5000)"

# 2. Iniciar Heurística Inversa (Background)
~/microcosmos_elite/bucle_infinito.sh > /dev/null 2>&1 &
echo -e " ✅ \033[0;32mOráculo Shor:\033[0m Calibrando Qubits..."

# 3. Iniciar Túnel de Soberanía
echo -e " 📡 \033[0;33mEstableciendo Puente Cuántico...\033[0m"
echo "------------------------------------------------------------"
cloudflared tunnel --url http://localhost:5000
