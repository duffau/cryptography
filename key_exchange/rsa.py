from number_theory import random_prime, gcd, modular_inverse


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)


def generate_keys(max_bits):
    secret_prime_1 = random_prime(max_bits//2, max_bits)
    secret_prime_2 = random_prime(max_bits//2, max_bits)
    n = secret_prime_1 * secret_prime_2
    phi_n = (secret_prime_1-1)*(secret_prime_2-1)
    e = choose_public_exponent(phi_n)
    d = modular_inverse(e, phi_n)
    return (e, n), (d, n)


def choose_public_exponent(phi_n):
    for e in range(3, phi_n):
        if gcd(e, phi_n) == 1:
            return e
