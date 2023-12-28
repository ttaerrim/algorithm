nums = []
odds = []
for i in range(7):
    nums.append(int(input()))
for i in nums:
    if (i % 2 != 0):
        odds.append(i)
if (len(odds) == 0):
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
