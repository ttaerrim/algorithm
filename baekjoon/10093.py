a, b = map(int, input().split())

if (a > b):
    a, b = b, a
    
answers = []
for i in range(a+1, b):
    answers.append(i)

print(len(answers))
print(' '.join(map(str, answers)))
