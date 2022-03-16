# 가장 큰 수
def solution(numbers):
    numbers.sort(key=lambda x: ((str(x)*4)[:4]), reverse=True)
    answer = "".join(map(str, numbers))
    answer = answer if int(answer) != 0 else "0"
    return answer
