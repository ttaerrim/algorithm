# https://www.acmicpc.net/problem/1205
# 등수 구하기

n, score, p = map(int, input().split())
scores = []
if n > 0:
    scores = list(map(int, input().split()))


answer = 1

for idx, s in enumerate(scores):
    if s > score:
        answer += 1
    elif s == score:
        break
    else:
        break

if (len(scores) > 0 and score <= scores[-1]) and p == len(scores):
    answer = -1

print(answer)



