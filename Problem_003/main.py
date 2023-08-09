from primePy import primes

number = 600851475143



factor = primes.factors(number)

print (factor[-1])


# # Another version

# factor = []

# for n in range(1,number):
    
#     if number%n == 0:
#         print (n)
#         number = number/n
#         factor.append(n)
        
        
#     else:
#         continue

# for i in factor :
#     if primes.check(i)==True:
#         largest_number = i
#     else:
#         continue

# print(largest_number)