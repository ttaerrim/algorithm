import math

n = input()
numbers = [0 for _ in range(9)]

for i in range(len(n)):
    idx = 6 if int(n[i]) == 9 else int(n[i])
    numbers[idx] += 1

numbers[6] = math.ceil(numbers[6]/2) 
print(max(numbers))
    