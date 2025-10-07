import streamlit as st
# Fixed import - use absolute import instead of relative import
try:
    from utils import generate_vulnerable_keys, factor_attack, mod_inverse
except ImportError:
    # If utils is in a parent directory or different location
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent))
    from utils import generate_vulnerable_keys, factor_attack, mod_inverse

st.header("Interactive Simulation")
st.markdown("---")

# Initialize session state if not already done
if 'rsa_keys' not in st.session_state:
    st.session_state.rsa_keys = None
if 'attack_result' not in st.session_state:
    st.session_state.attack_result = None

col1, col2 = st.columns(2)

with col1:
    st.write("Press the first button to generate a weak RSA key pair. Then, press the second button to launch the attack.")

    if st.button("1. Generate Vulnerable RSA Keys"):
        st.session_state.rsa_keys = generate_vulnerable_keys()
        st.session_state.attack_result = None  # Reset attack result

    if st.button("2. Launch Factorization Attack", disabled=(st.session_state.rsa_keys is None)):
        if st.session_state.rsa_keys:
            n = st.session_state.rsa_keys['n']
            e = st.session_state.rsa_keys['e']
            p, q, duration = factor_attack(n)
            if p and q:
                recovered_phi = (p - 1) * (q - 1)
                recovered_d = mod_inverse(e, recovered_phi)
                st.session_state.attack_result = {
                    'p': p, 'q': q, 'd': recovered_d, 'duration': duration
                }

with col2:
    st.markdown("**Results**")
    if st.session_state.rsa_keys is None:
        st.info("Waiting for simulation to start...")
    else:
        keys = st.session_state.rsa_keys
        st.success("✅ Vulnerable keys generated!")
        st.write(f"**Public Key:**")
        st.code(f"e = {keys['e']}\nn = {keys['n']}", language="text")
        with st.expander("Show Original Private Components (for verification)"):
            st.code(f"p = {keys['p']}\nq = {keys['q']}\nd = {keys['d']}", language="text")

    if st.session_state.attack_result:
        st.error("ATTACK LAUNCHED!")
        res = st.session_state.attack_result
        st.write(f"Factorization successful in **{res['duration']:.2f} ms**.")
        st.write(f"**Found Factors:**")
        st.code(f"p = {res['p']}\nq = {res['q']}", language="text")
        st.write(f"**Recovered Private Exponent:**")
        st.code(f"d = {res['d']}", language="text")

        original_d = st.session_state.rsa_keys['d']
        if res['d'] == original_d:
            st.success("✅ SUCCESS: The recovered private key matches the original!")
        else:
            st.error("❌ FAILURE: Recovered key does not match.")