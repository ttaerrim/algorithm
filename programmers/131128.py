# 연습문제 > 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter
def solution(X, Y):
    answer = ''
    x_cnt = Counter(X)
    y_cnt = Counter(Y)
    counter = {}
    
    for i in range(0, 10):
        count = min(x_cnt[str(i)], y_cnt[str(i)])
        if count > 0:
            counter[i] = count
            
    if counter == {}:
        return '-1'
    elif len(counter) == 1 and 0 in counter.keys():
        return '0'
    
    for k in reversed(counter):
        v = counter[k]
        for _ in range(0, v):
            answer += str(k)
    return answer
