# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

def solution(n):
    n2str = [int(s) for s in str(n)]
    return int("".join(sorted(map(str, n2str), reverse=True)))

# 다른 풀이 2
def solution(n):
    lst = []
    while n:
        _, v = divmod(n, 10)
        lst.append(v)
        n //= 10
    lst.sort(reverse=True)
    answer = 0
    for n in lst:
        answer *= 10
        answer += n
    return answer
