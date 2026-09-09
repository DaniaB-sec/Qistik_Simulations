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

print()
print("==========================================")
print("           UNIFORM RNG")
print("==========================================")

print(f"Number of shots: {shots}")
print(f"Valid results: {len(valid_counts)}")

if valid_counts:
    average = sum(valid_counts) / len(valid_counts)

    print(f"Average: {average:.2f}")
    print(f"Minimum: {min(valid_counts)}")
    print(f"Maximum: {max(valid_counts)}")
else:
    print("No valid results were obtained.")


show_results = input(
    "\nClick Y to see all the results after: "
).strip().upper()


if show_results == "Y":

    print("\n==========================================")
    print("           ALL RESULTS")
    print("==========================================")

    for number in sorted(valid_counts):
        print(number)

else:
    print("\nResults not displayed. Please try again.")
