import os
import shutil
import json
import subprocess
import sqlite3
from datetime import datetime

# --- CONFIGURACIÓN DE RUTAS ---
BASE_PATH = "/home/chalamandramagistral"
DB_FILE = os.path.join(BASE_PATH, "microcosmos_elite/boveda.db")
TARGET_FOLDERS = [
    "microcosmos_elite",
    "backup_microcosmos",
    ".git",
    ".config"
]

def get_dir_size(path):
    """Calcula el tamaño de una carpeta en MB."""
    total_size = 0
    try:
        if not os.path.exists(path):
            return 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return round(total_size / (1024 * 1024), 2)
    except Exception:
        return 0

def check_process(name):
    """Verifica si un proceso está corriendo."""
    try:
        output = subprocess.check_output(["ps", "aux"]).decode()
        return name in output
    except:
        return False

def get_vault_stats():
    """Extrae el total de la boveda.db de app_final.py"""
    try:
        if not os.path.exists(DB_FILE):
            return {"total": 0, "ultimo": "No DB"}
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        total = cursor.execute('SELECT SUM(monto) FROM pagos').fetchone()[0] or 0
        ultimo = cursor.execute('SELECT cliente, monto FROM pagos ORDER BY id DESC LIMIT 1').fetchone()
        conn.close()
        return {
            "total": total,
            "ultimo": f"{ultimo[0]}: ${ultimo[1]}" if ultimo else "Sin transacciones"
        }
    except Exception as e:
        return {"total": 0, "error": str(e)}

def get_bunker_report():
    """Genera el reporte de estado para el monitor."""
    total, used, free = shutil.disk_usage(BASE_PATH)
    vault = get_vault_stats()
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "node_id": "CHALAMANDRA_CELERON_01",
        "finances": vault,
        "disk": {
            "free_gb": round(free / (1024**3), 2),
            "used_percent": round((used / total) * 100, 2)
        },
        "services": {
            "flask_app": check_process("app_final.py"),
            "asset_hunter": check_process("asset_hunter.py"),
            "cloudflare_tunnel": check_process("cloudflared")
        },
        "folders": {}
    }

    for folder in TARGET_FOLDERS:
        full_path = os.path.join(BASE_PATH, folder)
        report["folders"][folder] = f"{get_dir_size(full_path)} MB"

    return report

if __name__ == "__main__":
    data = get_bunker_report()
    # Guardar para el monitor web
    with open(f"{BASE_PATH}/health_log.json", "w") as f:
        json.dump(data, f, indent=4)
    # Salida inmediata para terminal
    print(json.dumps(data, indent=4))
