def gcd(n1, n2):
    '''Greates common divisor'''
    while n2 != 0:
        n2, n1 = n1 % n2, n2
    return n1


def eea(n1, n2):
    '''
    Extended Euclidean Algorithm (EEA) for GCD 
    and factors producing the GCD from the inpus numbers. 
    '''
    s0, t0 = 1, 0 
    s1, t1 = 0, 1
    while n2 != 0:
        tmp = n2
        n2 = n1 % n2
        q = (n1 - n2)//tmp
        n1 = tmp
        s0, s1 = s1, s0 - q * s1 
        t0, t1 = t1, t0 - q * t1 

    return n1, s0, t0