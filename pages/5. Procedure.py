import streamlit as st

st.header("Procedure")
st.markdown("---")

st.markdown("""### Step-by-Step Guide to Run the RSA Factorization Attack""")

st.markdown("""#### 🔧 Prerequisites""")
st.markdown("""
1.  Ensure you have created all the project files (`rsa_attack_app.py`, `utils.py`, and all files in the `pages/` directory).
2.  Install the required library from your terminal:
""")
st.code('pip install streamlit', language="bash")

st.markdown("""#### 📋 Step 1: Setup and Key Generation""")
st.markdown("""
1.  Run the application from your terminal: `python -m streamlit run rsa_attack_app.py`
2.  Navigate to the **Simulation** page using the sidebar.
3.  Click the **"1. Generate Vulnerable RSA Keys"** button.
4.  The application will automatically create a weak RSA key pair using two small, 2-digit prime numbers.
5.  The public key (`e` and `n`) will be displayed. You can expand the section below it to see the original private components for later verification.
""")

st.markdown("""#### 💥 Step 2: The Attack Process""")
st.markdown("""
1.  With the keys generated, click the **"2. Launch Factorization Attack"** button.
2.  The application will:
    -   Take the public modulus `n`.
    -   Perform a trial division loop to find its prime factors, `p` and `q`.
    -   Use `p` and `q` to calculate the original totient, `φ(n)`.
    -   Use `φ(n)` and `e` to calculate the private exponent `d`.
3.  The results of the attack, including the recovered factors and the private key, will be displayed.
""")

st.markdown("""#### ✅ Step 3: Verification""")
st.markdown("""
1.  Compare the **"Recovered Private Exponent"** from the attack results with the **"Original Private Components"** you viewed in Step 1.
2.  If they match, the application will display a "SUCCESS" message and launch some celebratory balloons.
3.  This confirms that by factoring the small modulus `n`, we were successfully able to reverse-engineer the private key.
""")

st.markdown("---")

st.markdown("""### 💻 Code Implementation Example""")
st.markdown("This consolidated example shows the entire attack logic in a single script.")
st.code('''
import math
import random

# --- Core RSA Functions ---

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    m0, x0, x1 = phi, 0, 1
    if phi == 1: return 0
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += m0
    return x1

# --- Full Attack Simulation ---

# 1. SETUP: Generate a weak key pair
primes_pool = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
p_orig = random.choice(primes_pool)
q_orig = random.choice(list(set(primes_pool) - {p_orig}))

n = p_orig * q_orig
phi_orig = (p_orig - 1) * (q_orig - 1)
e = 17 # A common small exponent
if gcd(e, phi_orig) != 1: e = 19 # Fallback
d_orig = mod_inverse(e, phi_orig)

print(f"Original Primes: p={p_orig}, q={q_orig}")
print(f"Public Key: (e={e}, n={n})")
print(f"Original Private Key: d={d_orig}\\n")

# 2. ATTACK: We only have the public key (e, n)
print("--- Attack Begins ---")
p_found, q_found = None, None
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        p_found = i
        q_found = n // i
        break

if p_found:
    print(f"Factors Found: p={p_found}, q={q_found}")
    
    # 3. RECOVER: Re-calculate phi and d
    phi_recovered = (p_found - 1) * (q_found - 1)
    d_recovered = mod_inverse(e, phi_recovered)
    print(f"Recovered Private Key: d={d_recovered}")

    # 4. VERIFY
    if d_recovered == d_orig:
        print("\\nSUCCESS: Recovered key matches the original!")
    else:
        print("\\nFAILURE: Key mismatch.")
else:
    print("Factorization failed.")

''', language='python')

st.markdown('''---''')