# 더하기 사이클

N = int(input())
n = -1
count = 0
while n != N:
    if n == -1:
        n = N
    n = (n % 10*10)+((n//10+n % 10) % 10)
    count += 1
print(count)
