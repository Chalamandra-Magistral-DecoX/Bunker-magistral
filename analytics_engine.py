#!/usr/bin/env python3
import sqlite3
from datetime import datetime, timedelta
import os
import requests

DB_PATH = os.path.expanduser('~/microcosmos_elite/boveda.db')
TELEGRAM_TOKEN = "8083155376:AAFDHxoXZL8Nxqt63pJNwZaMAz88h1hSnR4"
TELEGRAM_CHAT_ID = "-1003260850014"

def get_ventas(dias=7):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    fecha_limite = (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("SELECT fuente, SUM(monto) FROM pagos WHERE fecha > ? GROUP BY fuente", (fecha_limite,))
    data = cursor.fetchall()
    conn.close()
    return data

def analizar():
    ventas = get_ventas(7)
    total = 0
    reporte = "\n📊 REPORTE DE CONVERSIONES (últimos 7 días)\n" + "="*50 + "\n"
    for fuente, monto in ventas:
        reporte += f"  {fuente:<15} → ${monto:.2f}\n"
        total += monto
    reporte += "-"*50 + f"\n  TOTAL          → ${total:.2f}\n"
    
    if ventas:
        mejor_fuente = max(ventas, key=lambda x: x[1])[0]
        reporte += f"\n💡 Recomendación: Invierte más tiempo en {mejor_fuente}\n"
    else:
        reporte += "\n💡 Aún no hay ventas. Publica más.\n"
    
    return reporte

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})

if __name__ == '__main__':
    reporte = analizar()
    print(reporte)
    enviar_telegram(reporte)
