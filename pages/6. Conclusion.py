import streamlit as st

st.header("Conclusion")
st.markdown("---")

st.markdown("""
This demonstration proves that the security of RSA is entirely dependent on the computational difficulty of factoring its public modulus `n`.

While the small-factor attack is trivial to execute on our example, it is **completely infeasible** against properly implemented RSA.

Modern RSA keys use a modulus of 2048 or 4096 bits, resulting in numbers so large that they cannot be factored with current technology and algorithms. This is why RSA remains a secure and widely trusted encryption standard.
""")