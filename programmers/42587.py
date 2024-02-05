from collections import deque

def solution(priorities, location):
    data = deque()
    answer = []
    for idx, p in enumerate(priorities):
        data.append(idx)
    
    
    popflag = True
    
    while data:
        popflag = True
        curr = data.popleft()
        for idx, p in enumerate(priorities):
            if idx in answer:
                continue
            if idx == curr:
                continue
            if priorities[curr] < p:
                data.append(curr)
                popflag = False
                break
        if popflag:
            answer.append(curr)

        
    return answer.index(location) + 1
