# 컵라면
# https://www.acmicpc.net/problem/1781
# 우선순위 큐

import heapq
import sys

N = int(sys.stdin.readline())
dl = [[]for _ in range(N+1)]

for _ in range(N):
    priority, cup = list(map(int, sys.stdin.readline().split()))
    dl[priority].append(cup)

answer = 0
queue = []
for i in range(N, 0, -1):
    for cup in dl[i]:
        heapq.heappush(queue, -cup)

    if not queue:
        continue

    answer -= heapq.heappop(queue)


    
