from number_theory import gcd, eea

def product(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p


def test_gcd_small_numbers():
    assert gcd(1, 0) == 1
    assert gcd(1, 1) == 1
    assert gcd(0, 0) == 0
    assert gcd(2*3, 2*3*5) == 6
    assert gcd(2*3*5, 2*3) == 6


def test_gcd_big_numbers():
    assert gcd(2*3*5*7, 2*3*5*7) == 2*3*5*7
    assert gcd(2*3*5*7*9*11, 2*3*5*7*9*11*13) == 2*3*5*7*9*11



def test_gcd_coprime():
    assert gcd(9, 28) == 1

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]
    for i_max in range(0, len(primes), 2):
        n1 = product([primes[j] for j in range(0, i_max, 2)])
        n2 = product([primes[j] for j in range(1, i_max-1, 2)])
        assert gcd(n1, n2) == 1


def test_eea_small_numbers():
    assert eea(67, 12) == (1, -5, 28)
    assert eea(973, 301) == (7, 13, -42)
