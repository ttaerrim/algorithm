# 모든 순열
# https://www.acmicpc.net/problem/10974

def helper(prefix, num):
    if num == []:
        yield prefix
        return
    for idx, n in enumerate(num):
        yield from helper(prefix + [n], num[:idx]+num[idx+1:])

n = int(input())
nums = [i+1 for i in range(n)]

for arr in helper([], nums):
    print(" ".join(map(str, arr)))
