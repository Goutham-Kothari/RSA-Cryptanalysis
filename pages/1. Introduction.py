import streamlit as st

st.header("Introduction")
st.markdown("---")

st.markdown("""
The RSA (Rivest-Shamir-Adleman) algorithm is a cornerstone of modern public-key cryptography. Its security relies on the practical difficulty of factoring the product of two very large prime numbers.

This application demonstrates a fundamental cryptanalytic attack against RSA, known as the **"small factorization attack."**

This attack is only feasible when the RSA modulus (`n`) is created from trivially small prime numbers, such as the **2-digit primes** used in our simulation. By understanding this vulnerability, we can appreciate why key size is so critical for robust security.
""")