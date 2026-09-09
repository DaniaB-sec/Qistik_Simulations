from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(10, 10)

for q in range(10):
    qc.h(q)

qc.measure(range(10), range(10))


shots = 1000

backend = Aer.get_backend("qasm_simulator")

compiled_circuit = transpile(qc, backend)
run_out = backend.run(
    compiled_circuit,
    shots=shots
).result()

out_counts = run_out.get_counts()

print("Raw quantum results:")
print(out_counts)


valid_counts = {}

for bitstring, count in out_counts.items():
    number = int(bitstring, 2)

    if number <= 1000:
        valid_counts[number] = count


print("\nUniform RNG results (0-1000):")
print(valid_counts)