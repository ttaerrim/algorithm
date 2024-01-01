n = int(input())
lists = list(map(int, input().split()))
v = int(input())
nums = [0 for _ in range(201)]

for i in range(n):
    idx = lists[i] if lists[i] >= 0 else lists[i] * -1 + 100
    nums[idx] += 1

nIdx = v if v >= 0 else v * -1 + 100
print(nums[nIdx])

################# 100을 더해 음수를 더 쉽게 다루자
n = int(input())
lists = list(map(int, input().split()))
v = int(input())
nums = [0 for _ in range(201)]

for i in range(n):
    nums[lists[i]+100] += 1

print(nums[v+100])
