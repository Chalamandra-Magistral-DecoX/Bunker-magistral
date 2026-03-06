#!/bin/bash
# Reemplaza la URL con la que obtengas de Vercel
HOOK_URL="TU_URL_DE_VERCEL_AQUÍ"

echo "📡 Disparando pulso de despliegue al Microcosmos..."
curl -X POST "$HOOK_URL"
echo -e "\n✅ Petición enviada. Revisa el dashboard de Vercel."
