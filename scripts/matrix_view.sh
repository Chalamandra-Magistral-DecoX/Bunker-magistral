#!/bin/bash
clear
echo -e "\e[1;32m"
echo "  __  __ ___  ___ ___  ___  ___  ___  ___ __  __  ___  ___ "
echo " |  \/  |_ _|/ __| _ \/ _ \/ __|/ _ \/ __|  \/  |/ _ \/ __|"
echo " | |\/| || || (__|   / (_) \__ \ (_) \__ \ |\/| | (_) \__ \\"
echo " |_|  |_|___|\___|_|_\\___/|___/\___/|___/_|  |_|\___/|___/"
echo -e "\e[0m"
echo "------------------------------------------------------------"
echo -e "\e[1;34mESTADO DEL ORÁCULO CUÁNTICO\e[0m"
tail -n 1 ~/microcosmos_elite/data/informe_rendimiento.csv | awk -F',' '{
    printf "FIDELIDAD: [%s%%] | POAS: %sx | CPU: %s%% | RAM: %sMB\n", $6, $5, $4, $3
}'
echo "------------------------------------------------------------"
echo -e "\e[1;33mPROYECTANDO ESPACIO DE ESTADOS (6 QUBITS)...\e[0m"
# Simulación visual de la amplitud
for i in {1..15}; do
    echo -n "█"
    sleep 0.05
done
echo " [OK]"
echo "------------------------------------------------------------"
