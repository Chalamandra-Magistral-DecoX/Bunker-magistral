#!/usr/bin/env python3
import os
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_FILE = "/home/chalamandramagistral/microcosmos_elite/boveda.db"

def init_db():
    """Asegura que la bóveda exista antes de arrancar."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            monto REAL,
            cliente TEXT,
            fuente TEXT,
            fecha TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "activo", "nodo": "Chalamandra Bunker"}), 200

@app.route('/webhook', methods=['POST'])
def kofi_webhook():
    """Recibe los impactos de ventas desde Ko-fi."""
    try:
        data = request.json or request.form.to_dict()
        monto = float(data.get('amount', 0.0) or data.get('data', {}).get('amount', 0.0))
        cliente = data.get('from_name', 'Desconocido')
        fuente = 'Ko-fi'
        
        conn = sqlite3.connect(DB_FILE)
        conn.execute(
            'INSERT INTO pagos (monto, cliente, fuente, fecha) VALUES (?, ?, ?, ?)',
            (monto, cliente, fuente, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Activo asegurado en bóveda"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    init_db()
    # 0.0.0.0 es crítico para que Cloudflare y el contenedor puedan acceder al puerto 5000
    app.run(host='0.0.0.0', port=5000)
