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
