def is_divisible_by(n, q):
    return n % q == 0


def prime_factors(n): 
    factors = []
    # Print the number of two's that divide n 
    while is_divisible_by(n, 2): 
        factors.append(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3, int(n**0.5) + 1, 2): 
          
        # while i divides n , print i ad divide n 
        while is_divisible_by(n, i): 
            factors.append(i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(n)
    return factors


def primes_less_than(upper_bound):
    '''Generating primes using Sieves of Eratosthenes method'''
    prime_indicator = [True for _ in range(upper_bound + 1)]

    p = 2
    while p*p <= upper_bound:
        if prime_indicator[p]:
            for i in range(p * 2, upper_bound + 1, p):
                prime_indicator[i] = False
        p += 1
    return [i for i in range(2, upper_bound) if prime_indicator[i]]


def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n %(i + 2) == 0:
            return False
        i += 6
    return True


