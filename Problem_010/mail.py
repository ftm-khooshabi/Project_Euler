from primePy import primes


sum_primes = 0
for n in range (2,2000000) :
    
    if primes.check(n) == True:
        
        sum_primes +=n

print(sum_primes)