import random
import math

# ============================================================
# PARAMETERS
# ============================================================

NUM_BITS = 10
MAX_VALUE = 1000
BIAS = 0.80
shots = 1000


# ============================================================
# UNIFORM CLASSICAL PRNG
# ============================================================

uniform_counts = {}

for _ in range(shots):

    # Generate 10 unbiased random bits
    bitstring = ''.join(
        random.choice('01')
        for _ in range(NUM_BITS)
    )

    # Convert bitstring to integer
    number = int(bitstring, 2)

    # Same rejection rule as the quantum RNG
    if number <= MAX_VALUE:
        uniform_counts[number] = uniform_counts.get(number, 0) + 1


# ============================================================
# BIASED CLASSICAL PRNG
# ============================================================

biased_counts = {}

for _ in range(shots):

    # Generate 10 biased random bits
    #
    # P(1) = 0.80
    # P(0) = 0.20
    #
    # This corresponds to the BIAS = 0.80
    # used in the quantum circuit.

    bitstring = ''.join(
        '1' if random.random() < BIAS else '0'
        for _ in range(NUM_BITS)
    )

    # Convert bitstring to integer
    number = int(bitstring, 2)

    # Same rejection rule as the quantum RNG
    if number <= MAX_VALUE:
        biased_counts[number] = biased_counts.get(number, 0) + 1


# ============================================================
# ANALYSIS FUNCTION
# ============================================================

def process_results(counts, shots, title):

    print()
    print("==========================================")
    print(f"           {title}")
    print("==========================================")

    valid_shots = sum(counts.values())
    unique_values = len(counts)

    acceptance_rate = (valid_shots / shots) * 100

    print(f"Number of shots: {shots}")
    print(f"Valid shots: {valid_shots}")
    print(f"Unique values: {unique_values}")
    print(f"Acceptance rate: {acceptance_rate:.2f}%")

    if counts:

        total = sum(
            number * count
            for number, count in counts.items()
        )

        average = total / valid_shots

        variance = sum(
            count * (number - average) ** 2
            for number, count in counts.items()
        ) / valid_shots

        standard_deviation = math.sqrt(variance)

        print(f"Average: {average:.2f}")
        print(f"Standard deviation: {standard_deviation:.2f}")
        print(f"Minimum: {min(counts)}")
        print(f"Maximum: {max(counts)}")

    return counts


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
    "CLASSICAL UNIFORM RNG"
)

process_results(
    biased_counts,
    shots,
    "CLASSICAL BIASED RNG"
)