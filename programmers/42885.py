# 탐욕법 > 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque 

def solution(people, limit):
    people_queue = deque(sorted(people))
    boat = 0
    
    while people_queue:
        max = people_queue.pop()
        if len(people_queue) > 0:
            min = people_queue.popleft()
            if min + max > limit:
                people_queue.appendleft(min)
        boat += 1
        
    return boat
