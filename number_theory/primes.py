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
