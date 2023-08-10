from primePy import primes

def Nth_prime(n):

    Nth_prime = primes.first(n)
    print(Nth_prime[-1])


Nth_prime(10001)