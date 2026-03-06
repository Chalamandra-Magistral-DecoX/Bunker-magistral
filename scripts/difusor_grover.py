from qiskit import QuantumCircuit

def aplicar_difusor_maestro(qc, n):
    """
    Difusor Grover clásico: Inversión sobre la media.
    Prepara |0...0> como estado marcado (H+X inicial).
    Usa mcx (Qiskit >=1.0) para multi-control.
    """
    # 1. Cambio de base: Hadamard + X → |0...0> → |1...1>
    for i in range(n):
        qc.h(i)
        qc.x(i)

    # 2. Multi-controlled Z (H + mcx + H)
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)  # mcx = multi-controlled NOT (equiv Z con H)
    qc.h(n - 1)

    # 3. Restauración de base
    for i in range(n):
        qc.x(i)
        qc.h(i)

    return qc


# Prueba simple
if __name__ == "__main__":
    n_qubits = 3
    qc = QuantumCircuit(n_qubits)
    qc = aplicar_difusor_maestro(qc, n_qubits)
    print(qc.draw(output='text'))
