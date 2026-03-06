#!/bin/bash
# Rotación Shor / Grover - Ejecuta uno por ciclo

ALGO=$((RANDOM % 2))

if [ $ALGO -eq 0 ]; then
  echo -e "\033[1;32m⚛️  SHOR ACTIVADO\033[0m"
  docker run --rm -v ~/microcosmos_elite/scripts:/src qiskit-lab /src/shor_15.py | grep -E "DISTRIBUCIÓN|Nirvana|✨" || echo " (Shor en espera)"
else
  echo -e "\033[1;33m🔍 GROVER ACTIVADO\033[0m"
  docker run --rm -v ~/microcosmos_elite/scripts:/src qiskit-lab /src/grover_selector.py || echo " (Grover calibrando)"
fi
