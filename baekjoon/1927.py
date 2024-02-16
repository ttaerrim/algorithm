# 최소 힙

import sys
import heapq
n = int(sys.stdin.readline())
heap=[]
heapq.heapify(heap)
for _ in range(n):
    c = int(sys.stdin.readline())
    if c == 0:
        if len(heap) > 0:
            min = heapq.heappop(heap)
            print(min)
        else:
            print(0)
    else:
        heapq.heappush(heap, c)


