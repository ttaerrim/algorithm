a, b, c = map(int, input().split())

def findDuplicate(array):
    x = []
    new_a = []
    for i in array:
        if (i not in x):
            x.append(i)
        else:
            if i not in new_a: 
                new_a.append(i)
    return new_a[0]


def calcReward(a, b, c):
    if (a == b and b == c and a == c):
        return 10000 + 1000 * a
    if (a != b and b != c and a != c):
        return 100 * max([a, b, c])
    return findDuplicate([a, b, c]) * 100 + 1000

print(calcReward(a, b, c))


################### 다듬기

a, b, c = map(int, input().split())

def calcReward(a, b, c):
    if (a == b and b == c):
        return 10000 + 1000 * a
    if (a == b or a == c):
        return 1000 + a * 100
    if (b == c):
        return 1000 + b * 100
    return max(a, b, c) * 100

print(calcReward(a, b, c))
