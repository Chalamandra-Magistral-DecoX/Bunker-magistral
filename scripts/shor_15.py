#!/usr/bin/env python3
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
import collections

def run_shor():
    # Circuito de 4 qubits
    qc = QuantumCircuit(4, 4)
    for q in range(4): qc.h(q)
    qc.measure(range(4), range(4))
    
    # Nueva forma de invocar el backend en Qiskit 1.x
    backend = Aer.get_backend('qasm_simulator')
    
    # Transpilar y ejecutar
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=1024)
    counts = job.result().get_counts()
    
    sorted_counts = collections.OrderedDict(sorted(counts.items()))
    
    print("\033[1;34m--- DISTRIBUCIÓN DE PROBABILIDAD (QFT) ---\033[0m")
    for state, val in sorted_counts.items():
        bar = "█" * int(val / 30)
        print(f"|{state}| {bar} ({val})")
    
    fidelidad = (counts.get('0000', 0) + counts.get('1111', 0)) / 1024 * 100
    print(f"\n\033[1;32m✨ Nirvana Alcanzado: {fidelidad:.2f}% de fidelidad\033[0m")

if __name__ == "__main__":
    run_shor()
