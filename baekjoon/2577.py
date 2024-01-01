multiple = 1
for _ in range(3):
    multiple *= int(input())

numbers = [0 for _ in range(10)]

for i in range(len(str(multiple))):
    idx = int(str(multiple)[i])
    numbers[idx] += 1

for i in range(len(numbers)):
    print(numbers[i])
