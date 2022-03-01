# 알람 시계
import sys
arr = list(map(int, sys.stdin.readline().split()))

if (arr[1]<45):
    if (arr[0]==0):
        arr[0]=24
    print(arr[0]-1, arr[1]+60-45)
else:
    print(arr[0], arr[1]-45)