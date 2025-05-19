"""
Number Theory: Theory and Implementation
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

'''
Use Cases:
- Cryptography
- Prime number generation
- Modular arithmetic
- Mathematical problem solving
'''
