# 코딩 기초 트레이닝 > 문자 개수 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/181902

from collections import defaultdict

def solution(my_string):
    alphabets = defaultdict(int)
    for x in range(65, 91):
        alphabets[chr(x)] = 0
    for x in range(97, 123):
        alphabets[chr(x)] = 0
    
    for s in my_string:
        alphabets[s] += 1
    
    return [alphabets[k] for k in alphabets]


# 다른 풀이 2

def solution(my_string):
    letters = defaultdict(int) # 처음에 굳이 A~Za~z 딕셔너리를 만들지 않아도 됨 
    for s in my_string: 
        letters[s] += 1 
    
    answer = []
    for x in range(ord('A'), ord('Z')+1):
        answer.append(letters[chr(x)])
    for x in range(97, 123):
        answer.append(letters[chr(x)])
    
    return answer
