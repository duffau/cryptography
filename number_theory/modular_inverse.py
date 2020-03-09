from .gcd import eea

def modular_inverse(n, modulo):
    _gcd, s, t = eea(modulo, n)
    if _gcd != 1:
        return None
    else:
        return t % modulo


