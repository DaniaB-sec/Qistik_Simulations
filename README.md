# Qiskit Simulations

Quantum Random Number Generator (QRNG) experiments implemented with Qiskit.

This repository contains:
- A classical PRNG baseline for comparison
- A uniform quantum RNG simulation
- A biased quantum RNG simulation
- A ready-to-run program for executing both quantum circuits on IBM Quantum hardware

## Project Overview

The project implements two quantum random number generators that produce 10-bit random bitstrings and convert them into integers in the range **0–1000**.

Values above 1000 are discarded using rejection sampling.

### 1. Uniform Quantum RNG

The uniform circuit uses **Hadamard (H) gates** on all qubits.

The Hadamard gate creates an equal probability of measuring:

- `|0⟩` → 50%
- `|1⟩` → 50%

This produces an ideal uniform quantum distribution when simulated.

### 2. Biased Quantum RNG

The biased circuit is designed to favor larger integer values.

It applies **S, T, and Rz phase/rotation gates between Hadamard gates** on each qubit. The resulting circuit is configured with a target probability of approximately:

- `P(0) = 0.20` → 20%
- `P(1) = 0.80` → 80%

Because the bitstrings contain more `1`s on average, the resulting integer values tend to be higher.

## Repository Contents

| File | Description |
|------|-------------|
| `RNG_Uniforme.py` | Uniform quantum RNG simulation using Hadamard gates |
| `RNG_Bias.py` | Biased quantum RNG simulation using S, T, and Rz gates |
| `Classical_RNG.py` | Classical PRNG baseline for comparison |
| `IBM_Quantum.py` | Runs both quantum circuits on IBM Quantum hardware |

Each simulation uses **1,000 shots**.

## Running the Local Simulations

It is recommended to use a Python virtual environment.

### Create a virtual environment

```bash
python3 -m venv .venv
