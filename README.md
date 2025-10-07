# RSA-algorithm
## 📄 README.md for the RSA Cryptanalysis Demonstration

This is a demonstration application that implements a fundamental cryptanalytic attack against the **RSA (Rivest-Shamir-Adleman) public-key cryptosystem**, known as the **"small factorization attack."**

The application is built using **Streamlit** to provide an interactive, educational simulation of how a weak RSA key can be broken by factoring its public modulus.

-----

### 💡 Objective

The primary goal is to illustrate the foundational security principle of RSA: **the practical difficulty of integer factorization for large numbers.**

This demonstration shows what happens when that principle is ignored by generating keys with a trivially small modulus ($\mathbf{n}$) derived from small, 2-digit prime numbers. An attacker, given only the public key $(e, n)$, can easily factor $n$ back into its primes $p$ and $q$, and subsequently derive the private key $d$.

### ⚙️ How the Attack Works

The RSA algorithm relies on the following key generation steps:

1.  Choose two large primes: $\mathbf{p}$ and $\mathbf{q}$.
2.  Calculate the modulus: $\mathbf{n = p \cdot q}$.
3.  Calculate Euler's totient function: $\mathbf{\phi(n) = (p-1) \cdot (q-1)}$.
4.  Choose a public exponent $\mathbf{e}$ (coprime to $\phi(n)$).
5.  Calculate the private exponent $\mathbf{d}$ such that $\mathbf{d \cdot e \equiv 1 \pmod{\phi(n)}}$.

The **public key** is $(\mathbf{e}, \mathbf{n})$ and the **private key** is $(\mathbf{d}, \mathbf{n})$.

The "small factorization attack" reverses this:

1.  **Factorization:** The attacker factors the public modulus $n$ to find $p$ and $q$.
2.  **Derivation:** They use the recovered $p$ and $q$ to compute $\phi(n)$.
3.  **Recovery:** They use the extended Euclidean algorithm (via `mod_inverse`) with $e$ and $\phi(n)$ to find the private exponent $d$.

**Note:** This attack is **completely infeasible** against properly implemented RSA, which uses a modulus of 2048 or 4096 bits.

-----

### 🚀 Running the Application

This application is built with Streamlit and requires Python.

#### Prerequisites

Ensure you have all the provided files in a structured project directory (e.g., `rsa_app/` with a `pages/` subdirectory for the numerical files).

#### Installation

Install the necessary Python library:

```bash
pip install streamlit
```

#### Execution

Run the application from your terminal in the directory containing the main script (`Home.py` or equivalent):

```bash
python -m streamlit run Home.py
```

### 📋 Simulation Procedure

1.  **Navigate** to the **Interactive Simulation** page in the sidebar.
2.  Click the **"1. Generate Vulnerable RSA Keys"** button. The application will create a public key $(\mathbf{e}, \mathbf{n})$ using two small, random 2-digit primes (from a pool like 11, 13, 17, etc.).
3.  Click the **"2. Launch Factorization Attack"** button.
      * The application performs a **trial division loop** to factor $\mathbf{n}$ into $\mathbf{p}$ and $\mathbf{q}$.
      * It then calculates the corresponding private key $\mathbf{d}$.
4.  **Verification:** The recovered private key $\mathbf{d}$ will be displayed, and a success message will confirm that it matches the original private key generated in Step 2.

-----

### 📂 File Structure

The application is structured using Streamlit's multi-page layout:

| File Name | Description |
| :--- | :--- |
| `Home.py` | The main entry point and title page of the Streamlit application. |
| `1. Introduction.py` | Explains RSA and introduces the small factorization attack. |
| `2. Objective.py` | States the educational goal of the demonstration. |
| `3. Theory.py` | Outlines the RSA key generation steps and the mathematical theory of the attack. |
| `4. Simulation.py` | The core interactive Streamlit page with buttons to generate keys and launch the attack. |
| `5. Procedure.py` | A step-by-step guide on how to run and verify the simulation, including a consolidated Python code example of the attack logic. |
| `6. Conclusion.py` | Summarizes the findings, emphasizing that real-world RSA (2048/4096 bits) is secure. |
| `utils.py` | Contains helper functions for RSA key generation, modular arithmetic (`gcd`, `mod_inverse`), and the implementation of the `factor_attack` logic. |
