import sqlite3, subprocess, datetime
conn = sqlite3.connect('boveda.db')
total = conn.execute('SELECT SUM(monto) FROM pagos').fetchone()[0] or 0
print(f"🦎 Bóveda: ${total:.2f}")
print(f"📡 Túnel: {subprocess.getoutput('strings tunnel.log | grep trycloudflare | tail -1')}")
