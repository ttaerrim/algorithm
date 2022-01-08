# 모의고사
def solution(answers):
    answer = []
    score = [0,0,0]
    patterns = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5], 
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for idx, num in enumerate(answers):
        if num == patterns[0][idx % len(patterns[0])]:
            score[0] += 1
        if num == patterns[1][idx % len(patterns[1])]:
            score[1] += 1
        if num == patterns[2][idx % len(patterns[2])]:
            score[2] += 1
    
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
            
    
    return answer