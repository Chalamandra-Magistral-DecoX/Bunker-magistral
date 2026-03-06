#!/bin/bash
# ❄️ ENFRIAMIENTO ADIABÁTICO - REINICIO DEL SISTEMA
echo "⚠️ Colapso detectado. Reiniciando el Cosmos..."

# Matar procesos de Node (Entropía Máxima)
killall -9 node 2>/dev/null

# Limpiar caché del sistema
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

# Reiniciar el archivo de datos a t=0
echo "Qubits,Iteraciones,POAS,Disparos,Fidelidad" > ~/microcosmos_elite/data/informe_cuantico.csv
echo "6,6,0.00,1024,100%" >> ~/microcosmos_elite/data/informe_cuantico.csv

echo "✨ El Cosmos ha vuelto a 0 K. Iniciando nueva expansión..."
