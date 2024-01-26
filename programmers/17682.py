# 2018 KAKAO BLIND RECRUITMENT > [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    scores = []
    idx = 0
    bonus = {'S':1, 'D':2, 'T':3}
    while idx < len(dartResult):
        score = 0
        while dartResult[idx].isdigit():
            score *= 10
            score += int(dartResult[idx])
            idx += 1
        if (dartResult[idx] == 'S' or dartResult[idx] == 'D' or dartResult[idx] == 'T'):
            score = score ** bonus[dartResult[idx]]
            scores.append(score)
        if (dartResult[idx] == '*'):
            scores[-1] = scores[-1] * 2
            if(len(scores)>1):
                scores[-2] = scores[-2] * 2
        if (dartResult[idx] == '#'):
            scores[-1] = scores[-1] * -1
        idx += 1
        
    print(scores)
    return sum(scores)

# 문자열을 숫자로 변환하는 함수

# def str2num(s):
#     idx = 0
#     num = 0
#     while idx < len(s):
#         num *= 10
#         num += int(s[idx])
#         idx +=1
#     return num
