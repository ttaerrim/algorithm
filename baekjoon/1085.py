# 직사각형에서 탈출 

import sys
input = list(map(int,sys.stdin.readline().split()))

print(min(abs(input[0]-input[2]), abs(input[1]-input[3]), abs(input[0]-0),abs(input[1]-0)))