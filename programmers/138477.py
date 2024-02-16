# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 연습문제 > 명예의 전당 (1)

import heapq
def solution(k, score):
    answer = []
    for i in range(1, len(score)+1):
        heap = [-s for s in score[:i]]
        heapq.heapify(heap)
        
        wins = []
        for _ in range(min(len(heap), k)):
            s = heapq.heappop(heap)
            wins.append(-s)
        answer.append(min(wins))
        
    return answer
