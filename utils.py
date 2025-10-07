import math
import random
import time

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """
    Calculate the modular multiplicative inverse of e modulo phi.
    This is used to find the private exponent 'd'.
    """
    m0, x0, x1 = phi, 0, 1
    if phi == 1:
        return 0
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_vulnerable_keys():
    """Generates a weak RSA key pair using small, 2-digit primes."""
    # Using only 2-digit primes to make the modulus very small
    primes_pool = [11, 13, 17, 19, 23, 29]
    p = random.choice(primes_pool)
    q = p
    while p == q:
        q = random.choice(primes_pool)

    n = p * q
    phi = (p - 1) * (q - 1)
    
    # With small phi, 65537 might not be coprime. Let's find one that is.
    # Start with a common small prime exponent
    e = 17
    while gcd(e, phi) != 1:
        e += 2 # Check next odd numbers
    
    d = mod_inverse(e, phi)
    return {'p': p, 'q': q, 'n': n, 'e': e, 'd': d, 'phi': phi}

def factor_attack(n):
    """
    Performs the factorization attack on the modulus 'n'.
    Returns the found factors p and q, and the duration.
    """
    start_time = time.time()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            q = n // i
            duration = (time.time() - start_time) * 1000  # in milliseconds
            return p, q, duration
    return None, None, 0