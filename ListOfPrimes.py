#%%
def is_prime (x):
    if x==0 :
        return True
    if x==1 :
        return True
    i=2
    while i < x:
       if x%i==0 :
           return False
       else: 
           i += 1
    return True

def find_primes (x):
    primes = []
    i = 0
    while i <= x:
        if is_prime(i) :
            primes.append(i)
        i += 1
    return primes

print(find_primes (40))
 #%%   
