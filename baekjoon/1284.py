# 집 주소

import sys
arr = []

while True:
    input = sys.stdin.readline().strip()
    if (input.strip() == '0'):
        break
    arr.append(input)

def calcNumber(num):
    sum = 0
    for i in range(len(num)):
        if num[i] == '1':
            sum += 2
        elif num[i] == '0':
            sum += 4
        else:
            sum += 3
    sum += len(num)+1
    return sum

for i in range(len(arr)):
    print(calcNumber(list(arr[i])))

