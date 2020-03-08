from number_theory.primes import prime_factors


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
