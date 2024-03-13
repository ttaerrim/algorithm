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