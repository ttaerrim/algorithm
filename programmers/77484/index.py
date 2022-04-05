# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    for l in lottos:
        if l != 0 and l in win_nums:
            answer += 1
    count = lottos.count(0)
    return [rank[answer+count], rank[answer]]
