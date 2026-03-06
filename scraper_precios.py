#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

# Lista de URLs a monitorear (ejemplo: tiendas de tecnología en Xalapa)
URLS = [
    'https://www.cyberpuerta.mx',
    'https://www.digimex.com',
    # Agregá las que quieras
]

def extraer_precios(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Ejemplo: buscar precios en etiquetas específicas (ajustar según cada sitio)
        precios = soup.find_all(class_='precio')
        return [p.text.strip() for p in precios if p.text]
    except:
        return []

def generar_reporte():
    with open('reporte_diario.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['fecha', 'url', 'precios'])
        for url in URLS:
            precios = extraer_precios(url)
            writer.writerow([datetime.now().isoformat(), url, ' | '.join(precios[:5])])
    print(f"📊 Reporte generado: {len(URLS)} sitios analizados.")

if __name__ == '__main__':
    generar_reporte()
