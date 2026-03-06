import os
import psutil
import time

def get_entropy():
    # Métrica de entropía basada en uso de CPU/RAM
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    # Loop Inverso: A mayor carga, menor fidelidad (Ruido térmico)
    fidelidad_base = 95.21
    ruido = (cpu + ram) / 20
    return max(0, fidelidad_base - ruido)

def pulse():
    fid = get_entropy()
    with open('/home/chalamandramagistral/microcosmos_elite/data/pulsar.log', 'w') as f:
        f.write(f"{fid:.22f}") # El latido con precisión cuántica

if __name__ == "__main__":
    pulse()
