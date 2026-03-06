from flask import Flask, request, jsonify
import datetime, os

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def handle_payment():
    try:
        data = request.json
        email = data.get('email', 'anon@microcosmos.ai')
        amount = data.get('amount', '0.00')
        
        # Registro en Money Log
        with open('/home/chalamandramagistral/microcosmos_elite/data/money.log', 'a') as f:
            f.write(f"{amount},{email},CONFIRMADO,{datetime.datetime.now()}\n")
        
        # Sincronización IA
        os.system("python3 /home/chalamandramagistral/microcosmos_elite/scripts/cloud_sync.py &")
        
        return jsonify({"status": "SUCCESS", "received": amount}), 200
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == "__main__":
    # Escuchar en 0.0.0.0 para visibilidad total del túnel
    app.run(host='0.0.0.0', port=5000)
