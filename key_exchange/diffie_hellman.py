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
    return pow(base, private_key, modulo)

