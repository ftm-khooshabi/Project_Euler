def Square_of_Sum(n):
    numbers = [i**2 for i in range(1,n+1)]
    return sum(numbers)

def Sum_of_Square(n):

    numbers = sum([i for i in range(1,n+1)])
    return numbers**2

print(Sum_of_Square(100)-Square_of_Sum(100))