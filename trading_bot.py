#!/usr/bin/env python3
import requests, time, sqlite3, os

DB_FILE = os.path.expanduser('~/microcosmos_elite/boveda.db')

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute('CREATE TABLE IF NOT EXISTS trades (id INTEGER PRIMARY KEY AUTOINCREMENT, simbolo TEXT, precio_compra REAL, cantidad REAL, estado TEXT, fecha DATETIME DEFAULT CURRENT_TIMESTAMP)')
    conn.close()

def run_trade_logic():
    print("📈 MONITOR DE TRADING ACTIVO...")
    while True:
        # Aquí iría tu lógica de Binance API
        time.sleep(60)

if __name__ == '__main__':
    init_db()
    run_trade_logic()
