# 연습문제 > 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916

from collections import Counter

def solution(s):
    count = Counter(s.lower())
    return count['p'] == count['y']
