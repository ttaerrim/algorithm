# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

def solution(n):
    n2str = [int(s) for s in str(n)]
    return int("".join(sorted(map(str, n2str), reverse=True)))
