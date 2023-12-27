n, x = map(int, input().split())
numbers = list(map(int, input().split()))


answer = []
for i in numbers:
    if (i < x):
        answer.append(i)
print(' '.join(str(e) for e in answer))
