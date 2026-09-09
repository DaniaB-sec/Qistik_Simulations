# Qistik_Simulations
Qiskit Simulations for Qubits in Quantum Computing. RNG_Uniforme is a qiskit simulation of 1000 shots without bias. RNG_Bias has a bias toward bigger numbers.


The biased simulator uses Quantum Phases (T, S, and Rz) between the Hadamard gates to introduce that bias (0.80 to 0.20 -- 80% to 20%). The uniform simulation simply uses the Hadamard (H) gate, delivering a true 50%-50% (random) simulation.
