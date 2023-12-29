a, b = map(int, input().split())

swap = -1
if (a > b):
    a, b = b, a
    
if (a == b or b - a == 1):
    print(0)

else:
    print(b-a-1)
    for i in range(a+1, b):
        print(i, end=" ")
