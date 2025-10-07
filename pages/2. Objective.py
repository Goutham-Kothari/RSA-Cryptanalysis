import streamlit as st

st.header("Objective")
st.markdown("---")

st.markdown("""
The objective of this demonstration is to illustrate how an attacker, given only a public RSA key (`e`, `n`), can recover the corresponding private key (`d`, `n`) if the modulus `n` is small enough to be factored.

This serves as an educational tool to highlight the foundational security principle of RSA: **the intractability of integer factorization for large numbers.**
""")