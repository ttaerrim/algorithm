n = int(input())
lists = list(map(int, input().split()))
x = int(input())

nums = [0 for _ in range(1000000)]

answer = 0
for i in range(n):
    nums[lists[i]-1] = 1
    if(x - lists[i] > 1 and x - lists[i] - 1 < 1000000 and nums[x - lists[i] - 1]): answer+=1

print(answer)
