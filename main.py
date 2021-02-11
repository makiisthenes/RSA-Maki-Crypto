# RSA Python Implementation
# Michael Peres
# 11/02/2021


def key_generation() -> list:
    """Generates both public and private key pairs"""
    n = 0
    encrypt_exp = 0
    decrypt_exp = 0
    public_key = (n, encrypt_exp)
    private_key = (n, decrypt_exp)
    return [public_key, private_key]


def encrypt(plaintext, public_key) -> bytes:
    """Function used to encrypt plaintext using public key, x^e mod n gives the ciphertext required."""
    # Fast exponentiation is required to encrypt.
    return b''

def decrypt(ciphertext, private_key) -> bytes:
    """Function used to decrypt ciphertext using private key, y^d mod n gives the plaintext required."""
    # Fast exponentiation is required to encrypt.
    return b''
