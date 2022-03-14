# 다리 놓기
import math
import sys


def bridge(N, M):
    return int(math.factorial(M)//math.factorial(M-N)//math.factorial(N))


n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split(" ")))
        for i in range(n)]

for item in data:
    print(bridge(item[0], item[1]))
