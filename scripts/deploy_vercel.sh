#!/bin/bash
# Sincronización masiva con Vercel
echo -e "\033[1;35m🚀 SUBIENDO FRONTEND A LA NUBE (VERCEL)...\033[0m"

# Entrar a la carpeta de tu proyecto Vite
cd ~/proyectos/tu-app-vite

# Despliegue en producción saltando confirmaciones
vercel --prod --token $VERCEL_TOKEN --confirm

echo -e "\033[1;32m✅ SINGULARIDAD WEB ACTIVA EN VERCEL\033[0m"
