# AC
# https://www.acmicpc.net/problem/5430

from collections import deque
n = int(input())
for _ in range(n):
    command = input()
    count = int(input())
    arr = input()
    queue = deque()
    
    if count > 0:
        arr = list(map(int, arr.replace('[','').replace(']','').split(',')))
    else:
        arr = []
    queue = deque(arr)


    flag = False
    reverse_flag = False
    for c in command:
        if c=='R':
           reverse_flag = not reverse_flag
        elif c == 'D':
            if len(queue) > 0:
                if reverse_flag:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                flag = True
                break
                

    if flag:
        print('error')
    else:
        answer = []
        if reverse_flag:
            answer = list(reversed(queue))
        else:
            answer = list(queue)
        print("["+",".join(map(str,answer))+"]")
