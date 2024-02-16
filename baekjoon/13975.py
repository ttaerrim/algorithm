# 파일 합치기 3

import heapq
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(files)

    answer = 0

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        answer += a+b
        heapq.heappush(files, a+b)

    print(answer)
