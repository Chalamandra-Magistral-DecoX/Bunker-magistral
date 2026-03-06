import sqlite3, hashlib, os, sys
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
# Ruta absoluta automática
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'vault', 'nodos_soberanos.db')
SECRET = "chalamandra_2026_elite"

def init_db():
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS ledger (id INTEGER PRIMARY KEY, ts TEXT, amount REAL, ref TEXT, hash TEXT)')
    conn.commit()
    conn.close()
    print(f"✅ Bóveda lista en: {DB_PATH}")

@app.route('/')
def home():
    return "Nodo Xalapa-01 Activo", 200

@app.route('/kofi', methods=['POST'])
def kofi_bridge():
    try:
        data = request.json or {}
        amount = data.get('amount', 0)
        ref = data.get('from_name', 'Unknown')
        ts = datetime.now().isoformat()
        v_hash = hashlib.md5(f"{ts}{amount}{ref}{SECRET}".encode()).hexdigest()
        
        conn = sqlite3.connect(DB_PATH)
        conn.execute("INSERT INTO ledger (ts, amount, ref, hash) VALUES (?, ?, ?, ?)", (ts, amount, ref, v_hash))
        conn.commit()
        conn.close()
        return jsonify({"status": "secured", "hash": v_hash}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()
    # Forzar host 0.0.0.0 para que el túnel lo vea siempre
    app.run(host='0.0.0.0', port=5000)
