multiple = 1
for _ in range(3):
    multiple *= int(input())

numbers = [0 for _ in range(10)]

for i in range(len(str(multiple))):
    idx = int(str(multiple)[i])
    numbers[idx] += 1

for i in range(len(numbers)):
    print(numbers[i])


################### 다른 풀이
t = 1
for _ in range(3):
    t *= int(input())

numbers = [0 for _ in range(10)]


while (t > 0):
    numbers[t%10] += 1
    t=t//10

print("\n".join(str(x) for x in numbers))
