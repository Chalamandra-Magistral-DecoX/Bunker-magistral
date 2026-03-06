#!/bin/bash
cd /home/chalamandramagistral/microcosmos_elite
# Añadir solo los cambios en los datos de resultados
git add data/*.csv frontend/public/data/*.json
git commit -m "🤖 Sincronización Automática: Nirvana del Código actualizando resultados"
git push origin main
