# 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# all

def solution(s):
    return len(s) in [4, 6] and all(letter.isdigit() for letter in s)
