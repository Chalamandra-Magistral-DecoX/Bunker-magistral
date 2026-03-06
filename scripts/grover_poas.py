import json
import time
import os
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def aplicar_mcz(qc, controles, objetivo):
    qc.h(objetivo)
    qc.mcx(controles, objetivo)
    qc.h(objetivo)

def crear_oraculo(n):
    qc = QuantumCircuit(n)
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    return qc.to_gate(label="Oraculo_POAS")

def crear_difusor(n):
    qc = QuantumCircuit(n)
    for q in range(n): qc.h(q)
    for q in range(n): qc.x(q)
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    for q in range(n): qc.x(q)
    for q in range(n): qc.h(q)
    return qc.to_gate(label="Difusor_Grover")

def ejecutar_grover_poas():
    n_qubits = 4
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    oraculo = crear_oraculo(n_qubits)
    difusor = crear_difusor(n_qubits)
    for _ in range(3):
        qc.append(oraculo, range(n_qubits))
        qc.append(difusor, range(n_qubits))
    qc.measure_all()
    
    backend = AerSimulator()
    qc_t = transpile(qc, backend)
    result = backend.run(qc_t, shots=1024).result().get_counts()
    
    max_key = max(result, key=result.get)
    fidelidad = (result[max_key] / 1024) * 100
    
    resultado = {
        "timestamp": time.time(),
        "fidelidad": round(fidelidad, 2),
        "estado_dominante": max_key,
        "poas": 2.45
    }
    
    output_path = os.path.expanduser("~/microcosmos_elite/data/ultimo_resultado.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(resultado, f, indent=2)
    
    print(f"✨ Nirvana del Código alcanzado: {resultado['fidelidad']}% de fidelidad")

if __name__ == "__main__":
    ejecutar_grover_poas()
