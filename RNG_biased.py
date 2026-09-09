from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import math


BIAS = 0.80

theta = 2 * math.asin(math.sqrt(BIAS))

qc = QuantumCircuit(10, 10)


for q in range(10):

   
    qc.h(q)

  
    qc.s(q)
    qc.t(q)

  
    qc.rz(theta - 3 * math.pi / 4, q)

    
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
print("            BIASED RNG")
print("==========================================")

print(f"Number of shots: {shots}")


valid_shots = sum(valid_counts.values())
unique_values = len(valid_counts)

print(f"Valid shots: {valid_shots}")
print(f"Unique values: {unique_values}")


if valid_counts:

    total = sum(number * count for number, count in valid_counts.items())

    average = total / valid_shots

    print(f"Average: {average:.2f}")
    print(f"Minimum: {min(valid_counts)}")
    print(f"Maximum: {max(valid_counts)}")

else:

    print("No valid results were obtained.")


show_results = input(
    "\nClick Y to see all the results after: "
).strip().upper()


if show_results == "Y":

    print()
    print("==========================================")
    print("             ALL RESULTS")
    print("==========================================")

    for number, count in sorted(valid_counts.items()):

        for _ in range(count):
            print(number)

else:

    print()
    print("Results not displayed. Please try again.")
