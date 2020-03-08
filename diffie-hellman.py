from random import getrandbits

MODULUS = 13       # Large prime
BASE = 7       # is primitive root modulo MODULUS
KEY_BITS = 3   # The greatest possible integer should be less than MODULUS 
BIT_FORMAT = '{:0%db}' % KEY_BITS


def to_bits(integer):
    return BIT_FORMAT.format(integer)

def generate_secret(n_bits):
    return getrandbits(n_bits)

def calc_key(base, private_key, modulo):
    return base**private_key % modulo

alice_private_key = generate_secret(KEY_BITS)
bob_private_key = generate_secret(KEY_BITS)

print('Alice private key: {}'.format(to_bits(alice_private_key)))
print("Bob's private key: {}".format(to_bits(bob_private_key)))

alice_public_key = calc_key(BASE, alice_private_key, MODULUS)
bob_public_key = calc_key(BASE, bob_private_key, MODULUS)

print('Alice public key: {}'.format(to_bits(alice_public_key)))
print("Bob's public key: {}".format(to_bits(bob_public_key)))

alice_shared_secret_key = calc_key(bob_public_key, alice_private_key, MODULUS)
bob_shared_secret_key = calc_key(alice_public_key, bob_private_key, MODULUS)

print('Alice shared secret key: {}'.format(to_bits(alice_shared_secret_key)))
print("Bob's shared secret key: {}".format(to_bits(bob_shared_secret_key)))
assert alice_shared_secret_key == bob_shared_secret_key
