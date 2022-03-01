# 지능형 기차
import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

sum, max_people = 0, 0
for i in range(len(arr)):
    sum = sum - arr[i][0] + arr[i][1]
    if (max_people < sum):
        max_people = sum

print(max_people)

