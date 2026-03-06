import requests
from bs4 import BeautifulSoup
import time

def check_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # Aquí buscaríamos el ID del precio (ejemplo genérico)
    price = soup.find(id="priceblock_ourprice")
    return price.text if price else "No detectado"

# Objetivo: Monitorizar un producto de alta rotación
target_url = "https://www.amazon.com.mx/dp/B082G2X9YF" 
print("🕵️ Scraper activo en modo 'Vigía'...")

while True:
    price = check_price(target_url)
    print(f"📊 Precio actual: {price}")
    # Si baja de X, el búnker registra la 'Oportunidad de Arbitraje'
    time.sleep(3600) # Una vez por hora para evitar baneo de IP
