#!/bin/bash
# Selector de Carga Cuántica

case $1 in
  shor)
    echo "⚛️ Ejecutando Factorización de Shor (Aislamiento Docker)..."
    docker run --rm -v ~/microcosmos_elite/scripts:/src qiskit-lab /src/shor_15.py
    ;;
  grover)
    echo "🔍 Ejecutando Búsqueda de Grover (Optimización de Leads)..."
    docker run --rm -v ~/microcosmos_elite/scripts:/src qiskit-lab /src/grover_selector.py
    ;;
  deploy)
    echo "🚀 Sincronizando Flota Vite con Vercel..."
    ~/microcosmos_elite/scripts/deploy_all.sh
    ;;
  *)
    echo "Uso: nirvana {shor|grover|deploy}"
    ;;
esac
