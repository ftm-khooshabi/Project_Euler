Final_list = []

for i in range(1000):

    if i%3 == 0:

        Final_list.append(i)
    
    elif i%5 == 0:

        Final_list.append(i)

print(sum(Final_list))