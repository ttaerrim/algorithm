w1 = input()
w2 = input()

a = [0 for _ in range(26)]
for s in w1:
    a[ord(s)-97] += 1
for s in w2:
    a[ord(s)-97] -= 1

answer = 0

for i in a:
    answer += abs(i)
print(answer)
