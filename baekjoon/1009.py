import sys
import math
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

def power(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    if (result == 0):
        result = 10

    return result

for i in range(len(data)):
    print(power(data[i][0], data[i][1],10))