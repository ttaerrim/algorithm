# 스택/큐 > 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587


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


# 다른 풀이
# [[파이썬 기초 코테 꿀팁] deque 알아보기](https://www.youtube.com/watch?v=Ckua6-QH5tU&list=PLDFJ6OuoOt_whs1SJ3MS5HXK_52r57qIB&index=6)

def solution2(priorities, location):
    waiting = deque(enumerate(priorities))
    sorting = sorted(priorities)
    
    order = 1
    while waiting:
        idx, process = waiting.popleft()
        if process < sorting[-1]:
            waiting.append((idx, process))
        else:
            if idx == location:
                return order # pop 한 것을 배열에 저장하지 않고도 order를 사용해서 정답을 리턴할 수 있다
            sorting.pop()
            order += 1
        