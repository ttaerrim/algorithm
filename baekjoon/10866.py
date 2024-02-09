import sys
from collections import deque
n = int(input())
queue = deque()
for _ in range(n):
    m = sys.stdin.readline().split()
    if m[0] == 'push_front':
        queue.appendleft(m[1])
    elif m[0] == 'push_back':
        queue.append(m[1])
    elif m[0] == 'pop_front':
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue.popleft())
    elif m[0] == 'pop_back':
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue.pop())
    elif m[0] == 'size':
        print(len(queue))
    elif m[0] == 'empty':
        if (len(queue) == 0):
            print(1)
        else:
            print(0)
    elif m[0] == 'front':
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
    elif m[0] == 'back':
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])
