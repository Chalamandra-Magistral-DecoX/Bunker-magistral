#!/usr/bin/env python3
import sqlite3
import os
import subprocess
from datetime import datetime

DB_FILE = os.path.expanduser('~/microcosmos_elite/boveda.db')

def get_honeygain():
    try:
        with open('honeygain.log', 'r') as f:
            lines = f.readlines()
        for line in reversed(lines):
            if 'Credits' in line:
                parts = line.split()
                for p in parts:
                    if '$' in p:
                        return float(p.replace('$', ''))
        return 0.0
    except:
        return 0.0

def get_packetstream():
    return 0.15  # estimado diario, podés ajustar

def get_trading():
    conn = sqlite3.connect(DB_FILE)
    total = conn.execute('SELECT SUM(precio_venta - precio_compra) FROM trades WHERE estado="vendido"').fetchone()[0] or 0
    conn.close()
    return total

def sync():
    honey = get_honeygain()
    packet = get_packetstream()
    trading = get_trading()
    total = honey + packet + trading

    if total > 0:
        conn = sqlite3.connect(DB_FILE)
        conn.execute('INSERT INTO pagos (monto, cliente) VALUES (?, ?)',
                     (total, f'sync_{datetime.now().strftime("%Y%m%d")}'))
        conn.commit()
        conn.close()
        print(f"[{datetime.now()}] Sincronizados ${total:.2f}")
    else:
        print(f"[{datetime.now()}] No hay ingresos nuevos")

if __name__ == '__main__':
    sync()
