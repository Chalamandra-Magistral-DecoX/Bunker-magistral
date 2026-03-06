#!/usr/bin/env python3
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

def run_grover():
    # Buscamos el estado |11| (el lead de mayor valor entre 4 opciones)
    qc = QuantumCircuit(2)
    qc.h([0, 1]) # Superposición
    # Oráculo para el estado 11
    qc.cz(0, 1)
    # Difusor
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.measure_all()

    backend = Aer.get_backend('qasm_simulator')
    tqc = transpile(qc, backend)
    counts = backend.run(tqc, shots=1).result().get_counts()
    
    lead_id = list(counts.keys())[0]
    leads = {"00": "Lead A (Frío)", "01": "Lead B (Tibio)", "10": "Lead C (Interés)", "11": "💎 LEAD VIP (ALTO LTV)"}
    print(f"🔍 GROVER TARGET: {leads.get(lead_id)}")

if __name__ == "__main__":
    run_grover()
