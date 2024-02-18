# https://www.acmicpc.net/problem/1655
# 가운데를 말해요
# 우선순위 큐

import heapq
import sys

n = int(sys.stdin.readline())
left = []
right = []
heapq.heapify(left)
heapq.heapify(right)

for i in range(n):
    num = int(sys.stdin.readline())
    
    if len(left) > len(right):
        heapq.heappush(right, num)
    else:
        heapq.heappush(left, num * -1)

    if ((len(right) > 0) and right[0] < left[0] * -1):
        heapq.heappush(left, right[0]*-1)
        heapq.heappop(right)
        heapq.heappush(right, left[0]*-1)
        heapq.heappop(left)

    
    print(left[0]*-1)
