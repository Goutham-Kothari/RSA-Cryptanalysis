import streamlit as st

st.set_page_config(
    page_title="Implement RSA Cryptanalysis (small factorization attack)",
    layout="wide"
)
st.title("Implement RSA Cryptanalysis (small factorization attack)")

st.markdown("""
This application demonstrates a fundamental cryptanalytic attack against RSA, known as the **"small factorization attack."**

Its security relies on the practical difficulty of factoring the product of two very large prime numbers. This demo shows what happens when that principle is ignored by using tiny, 2-digit primes.


""")