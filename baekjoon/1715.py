# 카드 정렬하기

import heapq
import sys

n = int(sys.stdin.readline())
answer = 0
heap = []
heapq.heapify(heap)
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

while len(heap) > 1:
    min1 = heapq.heappop(heap)
    min2 = heapq.heappop(heap)
    answer += min1+min2
    heapq.heappush(heap, min1+min2)

print(answer)

