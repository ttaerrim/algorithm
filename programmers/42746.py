# 가장 큰 수
def solution(numbers):
    numbers.sort(key=lambda x: ((str(x)*4)[:4]), reverse=True)
    answer = str(int("".join(map(str, numbers))))
    return answer
