import math

n, k = map(int, input().split())
room = 0
boys = [0 for _ in range(7)]
girls = [0 for _ in range(7)]

while True:
    try:
        s, y = map(int, input().split())
        if (s==0):
            girls[y] += 1
        else:
            boys[y] += 1
    except:
        break

for i in boys:
    if (i == 0): continue
    room += math.ceil(i/k)

for i in girls:
    if (i == 0): continue
    room += math.ceil(i/k)

print(room)
