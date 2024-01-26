# https://school.programmers.co.kr/learn/courses/30/lessons/120825?language=python3
# 코딩테스트 입문 > 문자 반복 출력하기

def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s*n
    return answer
