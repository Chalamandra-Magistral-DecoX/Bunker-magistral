#!/bin/bash
while true; do
  clear
  echo "--- ESTADO DEL MICROCROMOS ---"
  echo "Fecha: $(date)"
  tail -n 1 ~/microcosmos_elite/data/informe_cuantico.csv | awk -F',' '{print "POAS: "$2"x | FIDELIDAD: "$3"% | GANADOR: #"$4}'
  echo "------------------------------"
  # Simular el histograma en ASCII
  echo -n "Probabilidad: ["
  FID=$(tail -n 1 ~/microcosmos_elite/data/informe_cuantico.csv | cut -d',' -f3 | cut -d'.' -f1)
  for i in {1..20}; do
    if [ $i -le $(($FID/5)) ]; then echo -n "#"; else echo -n "."; fi
  done
  echo "]"
  sleep 5
done
