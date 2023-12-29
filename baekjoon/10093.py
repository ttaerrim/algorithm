a, b = map(int, input().split())

swap = -1
if (a > b):
    swap = a
    a = b
    b = swap
    
answers = []
for i in range(a+1, b):
    answers.append(i)

print(len(answers))
print(' '.join(map(str, answers)))
