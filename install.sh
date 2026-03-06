#!/bin/bash
# ============================================
#       INICIANDO INSTALACIÓN BÚNKER V5
# ============================================

echo -e "\033[1;35m[+] Preparando el Nodo de Poder...\033[0m"

# 1. Actualizar sistema y dependencias base
sudo apt-get update && sudo apt-get install -y python3-pip python3-venv zip curl

# 2. Crear entorno virtual limpio para el cliente
echo -e "\033[1;34m[+] Configurando el entorno de ejecución...\033[0m"
python3 -m venv venv
source venv/bin/activate

# 3. Instalar librerías necesarias (El motor)
pip install --upgrade pip
pip install flask requests tweepy python-dotenv cloudflared

# 4. Configurar el Túnel de Cloudflare
echo -e "\033[1;32m[+] El software está listo.\033[0m"
read -p "Introduce tu Token de Cloudflare (o presiona Enter para configurar luego): " CF_TOKEN
if [ ! -z "$CF_TOKEN" ]; then
    sudo cloudflared service install $CF_TOKEN
fi

echo -e "\n\033[1;35m============================================\033[0m"
echo -e "   INSTALACIÓN COMPLETADA: BÚNKER ACTIVO    "
echo -e "============================================\033[0m"
