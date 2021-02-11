# RSA Python Implementation
# Michael Peres
# 11/02/2021
from Crypto.Util import number
BIT_LENGTH = 2048
# I used a library for determining the random prime number as this was too much work and not a good use of my time.


def generate_large_prime() -> int:
    """Generates a large number, returns integer."""
    # Each prime should be at least 1024 bits long.
    # 1) Preselect a random number with the desired bit-size
    # 2) Ensure the chosen number is not divisible by the first few hundred primes (these are pre-generated)
    # 3) Apply a certain number of Rabin Miller Primality Test iterations, based on acceptable error rate, to get a number which is probably a prime
    # Picking a random number in range(0, 2**1024-1)
    # To limit small primes being generated we limit it to being on the top echelon of numbers in set.
    # Picking a random number in range(2**1023+1, 2**1024-1)
    # random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)
    prime = number.getStrongPrime(BIT_LENGTH)
    # print(prime)
    return prime

def generate_encrypt_expon():
    pass


def key_generation() -> list:
    """Generates both public and private key pairs"""
    # Choose 2 large primes p and q. [x]
    # Compute n  = p . q [x]
    # Compute Phi(n) = (p-1)(q-1) [x]
    # Select public exponent from 1 to Phi(n)-1
    # Such that the public exponent has a inverse gcd(e, phi) = 1
    # Calculate private key such that d.e = 1 mod phi(n)
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi_n = (p-1) * (q-1)
    print(f"P Prime Number: {p}")
    print(f"Q Prime Number: {q}")
    print(f"Product N : {n}")
    print(f"Phi of N: {phi_n}")
    encrypt_exp = 0
    decrypt_exp = 0
    public_key = (n, encrypt_exp)
    private_key = (n, decrypt_exp)
    return [public_key, private_key]



def fast_exponential(base, power) -> int:
    """Function to allow the exponention of base number by large powers."""
    pass


def encrypt(plaintext, public_key) -> bytes:
    """Function used to encrypt plaintext using public key, x^e mod n gives the ciphertext required."""
    # Fast exponentiation is required to encrypt.

    # int ciphertext
    ciphertext = fast_exponential(0, 0)
    return b''

def decrypt(ciphertext, private_key) -> bytes:
    """Function used to decrypt ciphertext using private key, y^d mod n gives the plaintext required."""
    # Fast exponentiation is required to encrypt.
    # int plaintext
    plaintext = fast_exponential(0, 0)
    return b''


key_generation()