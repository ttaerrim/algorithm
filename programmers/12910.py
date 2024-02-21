# https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = [el for el in arr if not el % divisor]
    if answer == []:
        return [-1]
    return sorted([el for el in arr if not el % divisor])
