#!/usr/bin/env python3
import sqlite3, requests, os, datetime

SUPA_URL = "https://zpttfvkabsxauqwdyvgg.supabase.co"
SUPA_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpwdHRmdmthYnN4YXVxd2R5dmdnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzE4MDEsImV4cCI6MjA4ODI0NzgwMX0.tWuy4OZUnBGL-lPiRbOg1bonJ4nVVdjBkZumKuftzJU"

DB_FILE = os.path.expanduser('~/microcosmos_elite/boveda.db')

def obtener_total():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(monto) FROM pagos")
        total = cursor.fetchone()[0] or 0.0
        conn.close()
        return total
    except: return 0.0

def sincronizar():
    total = obtener_total()
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    
    headers = {
        "apikey": SUPA_KEY,
        "Authorization": f"Bearer {SUPA_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    # Aquí enviamos EXACTAMENTE las columnas que existen en tu Supabase
    data = {
        "total": f"${total:,.2f}",
        "ultimo": f"Último ping: {hora}",
        "status": "online"
    }
    
    # Actualizamos la fila con id=1
    url = f"{SUPA_URL}/rest/v1/bunker_stats?id=eq.1"
    res = requests.patch(url, headers=headers, json=data)
    
    if res.status_code == 204:
        print(f"[{hora}] 📡 Enlace Supabase Exitoso. Bóveda actualizada a: {data['total']}")
    else:
        print(f"⚠️ Error {res.status_code}: {res.text}")

if __name__ == '__main__':
    sincronizar()
