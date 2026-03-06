#!/bin/bash
# Ejecutar el script de Shor dentro del laboratorio aislado
docker run --rm -v ~/microcosmos_elite/scripts:/src qiskit-lab /src/shor_15.py | grep -E "DISTRIBUCIÓN|✨|\|"
