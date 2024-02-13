# https://school.programmers.co.kr/learn/courses/30/lessons/181928
# 코딩 기초 트레이닝 > 이어 붙인 수

def solution(num_list):
    odd = int("".join(map(str, [num for num in num_list if num % 2 == 1])))
    even = int("".join(map(str, [num for num in num_list if num % 2 == 0])))
    return odd + even
    