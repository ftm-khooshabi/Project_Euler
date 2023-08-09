final_number = 4000000
Fibo_series = [1,2]
while Fibo_series[-1] < final_number:  # # Building the Fibonacci series up to a certain number

    Fibo_series.append(Fibo_series[-1]+Fibo_series[-2])


Even_number = []

for i in Fibo_series :  # # choose even numbers from that sereis

    if i%2 == 0:
        Even_number.append(i)

print(sum(Even_number))

