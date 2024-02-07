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
