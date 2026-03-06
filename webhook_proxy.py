#!/usr/bin/env python3
from flask import Flask, request, jsonify
import sqlite3
import json
import os
import requests
from datetime import datetime

app = Flask(__name__)
DB_FILE = os.path.expanduser('~/microcosmos_elite/webhooks.db')

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute('''CREATE TABLE IF NOT EXISTS webhooks
                 (id INTEGER PRIMARY KEY, cliente TEXT, url_destino TEXT, payload TEXT, recibido TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/webhook/<cliente>', methods=['POST'])
def recibir_webhook(cliente):
    data = request.get_json()
    url_destino = request.args.get('url', '')
    conn = sqlite3.connect(DB_FILE)
    conn.execute('INSERT INTO webhooks (cliente, url_destino, payload, recibido) VALUES (?, ?, ?, ?)',
                 (cliente, url_destino, json.dumps(data), datetime.now()))
    conn.commit()
    conn.close()
    if url_destino:
        try:
            requests.post(url_destino, json=data)
        except:
            pass
    return jsonify({'status': 'recibido', 'cliente': cliente}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=False)
