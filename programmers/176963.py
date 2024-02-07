# 연습문제 > 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    scores = {}
    for idx, person in enumerate(name):
        scores[person] = yearning[idx]
    
    
    for p in photo:
        score = 0
        for person in p:
            if person in scores:
                score += scores[person]
        answer.append(score)
            
    return answer


def solution2(name, yearning, photo):
    answer = []
    
    scores = {}
    for n, y in zip(name, yearning): # 이렇게 딕셔너리로 묶을 수도 있다
        scores[n] = y

    # 또는 scores = dict(zip(name, yearning))
    
    for p in photo:
        score = 0
        for person in p:
            if person in scores:
                score += scores[person]
        answer.append(score)
            
    return answer

# 다른 풀이 3
from collections import defaultdict # defaultdict을 사용하기

def solution3(name, yearning, photo):
    answer = []
    scores = defaultdict(int, zip(name, yearning)) # defaultdict을 사용하면 default 값을 지정해 줄 수 있다.
    
    for p in photo:
        score = sum(scores[person] for person in p) # 여기서 총합의 if를 생략할 수 있다
        answer.append(score) 
            
    return answer
