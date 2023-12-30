import math

n = int(input())
list = list(map(int, input().split()))

sumY = 0
sumM = 0
for i in range(n):
    sumY += (list[i]//30 + 1) * 10
    sumM += (list[i]//60 + 1) * 15

if (sumY > sumM):
    print('M', sumM)
elif (sumM > sumY):
    print('Y', sumY)
else:
    print('Y M', sumM)
