# N번째 큰 수

import heapq
import sys

n = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    for num in lst:
        if len(heap) == n:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        else:
            heapq.heappush(heap, num)

print(heap[0])

