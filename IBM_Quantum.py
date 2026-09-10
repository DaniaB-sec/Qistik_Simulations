from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.transpiler import generate_preset_pass_manager
import math


# ============================================================
# IBM QUANTUM CONNECTION
# ============================================================

service = QiskitRuntimeService()

backend = service.least_busy(
    operational=True,
    simulator=False,
    min_num_qubits=10
)

print("IBM backend:", backend.name)
print("Number of qubits:", backend.num_qubits)


# ============================================================
# UNIFORM RNG CIRCUIT
# ============================================================

qc = QuantumCircuit(10)

for q in range(10):
    qc.h(q)

qc.measure_all()


# ============================================================
# BIASED RNG CIRCUIT
# ============================================================

BIAS = 0.80

theta = 2 * math.asin(math.sqrt(BIAS))

qc1 = QuantumCircuit(10)

for q1 in range(10):

    qc1.h(q1)
    qc1.s(q1)
    qc1.t(q1)
    qc1.rz(theta - 3 * math.pi / 4, q1)
    qc1.h(q1)

qc1.measure_all()


# ============================================================
# TRANSPILATION
# ============================================================

print()
print("Transpiling circuits for", backend.name, "...")
print()

pass_manager = generate_preset_pass_manager(
    backend=backend,
    optimization_level=1
)

qc_isa = pass_manager.run(qc)
qc1_isa = pass_manager.run(qc1)

print("Uniform circuit transpiled.")
print("Biased circuit transpiled.")


# ============================================================
# RUN BOTH CIRCUITS ON IBM
# ============================================================

shots = 1000

sampler = SamplerV2(mode=backend)

print()
print("Submitting circuits to IBM Quantum...")
print()

job = sampler.run(
    [qc_isa, qc1_isa],
    shots=shots
)

print("Job ID:")
print(job.job_id())

print()
print("Waiting for IBM Quantum results...")
print()

result = job.result()


# ============================================================
# EXTRACT RESULTS
# ============================================================

uniform_data = result[0].data.meas
biased_data = result[1].data.meas

uniform_counts = uniform_data.get_counts()
biased_counts = biased_data.get_counts()


# ============================================================
# ANALYSIS FUNCTION
# ============================================================

def process_results(counts, shots, title):

    valid_counts = {}

    for bitstring, count in counts.items():

        number = int(bitstring, 2)

        if number <= 1000:
            valid_counts[number] = count

    print()
    print("==========================================")
    print(f"           {title}")
    print("==========================================")

    print(f"Number of shots: {shots}")

    valid_shots = sum(valid_counts.values())
    unique_values = len(valid_counts)

    acceptance_rate = (valid_shots / shots) * 100

    print(f"Valid shots: {valid_shots}")
    print(f"Unique values: {unique_values}")
    print(f"Acceptance rate: {acceptance_rate:.2f}%")

    if valid_counts:

        total = sum(
            number * count
            for number, count in valid_counts.items()
        )

        average = total / valid_shots

        variance = sum(
            count * (number - average) ** 2
            for number, count in valid_counts.items()
        ) / valid_shots

        standard_deviation = math.sqrt(variance)

        print(f"Average: {average:.2f}")
        print(f"Standard deviation: {standard_deviation:.2f}")
        print(f"Minimum: {min(valid_counts)}")
        print(f"Maximum: {max(valid_counts)}")

    return valid_counts


# ============================================================
# DISPLAY RAW RESULTS
# ============================================================

print()
print("RAW UNIFORM RESULTS:")
print(uniform_counts)

print()
print("RAW BIASED RESULTS:")
print(biased_counts)


# ============================================================
# ANALYZE RESULTS
# ============================================================

process_results(
    uniform_counts,
    shots,
    "UNIFORM RNG"
)

process_results(
    biased_counts,
    shots,
    "BIASED RNG"
)