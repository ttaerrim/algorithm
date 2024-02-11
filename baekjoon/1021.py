# https://www.acmicpc.net/problem/1021
# 회전하는 큐

from collections import deque

n, m = map(int, input().split(" "))
nums= list(map(int, input().split()))

idx = 0
count = 0
queue = deque()

for i in range(n):
    queue.append(i+1)

while idx < len(nums):
    target = nums[idx]
    if (queue[0] == target):
        queue.popleft()
        idx += 1
    else:
        target_idx = queue.index(target)
        if (target_idx < len(queue)/2):
            left = queue.popleft()
            queue.append(left)
        else:
            right = queue.pop()
            queue.appendleft(right)
        count += 1

print(count)


