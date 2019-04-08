def is_prime (x):
    return True

def find_primes (x):
    primes = []
    i = 0
    while i <= x:
        if is_prime(i) :
            primes.append(i)
        i += 1
    return primes
    
