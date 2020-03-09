from number_theory.primes import prime_factors, primes_less_than, is_prime


def product(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p


def test_prime_factors():
    n_max = 3000
    for n in range(2, n_max):
        pfs = prime_factors(n)
        assert n == product(pfs), "{n} == product({pfs})".format(n=n, pfs=pfs)


def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]
    
    non_primes = [n for n in range(1, max(primes)+1) if n not in set(primes)]

    for prime_candidate in primes:
        assert is_prime(prime_candidate)

    for prime_candidate in non_primes:
        assert not is_prime(prime_candidate)

def test_primes_less_than():
    upper_bound = 10**5
    for prime_candidate in primes_less_than(upper_bound):
        assert is_prime(prime_candidate)