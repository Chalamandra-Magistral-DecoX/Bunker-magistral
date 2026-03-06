from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app) # Permitir que tu React de Vercel lea estos datos

# Almacenamiento volátil en la nube (se actualiza con el latido del Celeron)
current_data = {
    "counts": {"0000": 0, "0100": 0, "1000": 0, "1100": 0},
    "time": 0,
    "success": False,
    "metrics": {"ram_mb": 0, "cpu_percent": 0}
}

@app.route('/api/shor', methods=['GET'])
def get_shor():
    return jsonify(current_data)

@app.route('/api/update', methods=['POST'])
def update_shor():
    global current_data
    data = request.json
    current_data = data
    return jsonify({"status": "updated", "timestamp": time.time()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
