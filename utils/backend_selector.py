import pennylane as qml

try:
    from qiskit import Aer
    _aer_available = True
except ImportError:
    _aer_available = False

def get_device(backend_name: str, wires: int) -> qml.device:
    if backend_name == "default":
        return qml.device("default.qubit", wires=wires)
    elif backend_name == "lightning":
        return qml.device("lightning.qubit", wires=wires)
    elif backend_name == "aer":
        if not _aer_available:
            raise ImportError("Qiskit Aer is not installed or not available.")
        # Qiskit's Aer simulator does not have a 'wires' argument, so we return the backend object
        # Instead, return PennyLane's qiskit.aer device if available
        return qml.device("qiskit.aer", wires=wires)
    elif backend_name == "ibmq":
        return qml.device("qiskit.ibmq", wires=wires, backend="ibmq_qasm_simulator")
    else:
        raise ValueError("Unsupported backend")
