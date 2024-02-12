# https://school.programmers.co.kr/learn/courses/30/lessons/181931
# 코딩 기초 트레이닝 > 등차수열의 특정한 항만 더하기

def solution(a, d, included):
    return sum(a + d * idx for idx, include in enumerate(included) if include)

def solution(a, d, included):
    return sum(num for idx, num in enumerate(range(a, a + len(included) * d, d)) if included[idx])

