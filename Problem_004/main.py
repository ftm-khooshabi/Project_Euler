palindrome = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        multiple = i*j
        if str(multiple)[::-1] == str(multiple):
            
            palindrome.append(multiple)

palindrome.sort(reverse=True)

print(palindrome[0])