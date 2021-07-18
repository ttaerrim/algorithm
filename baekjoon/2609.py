x, y = map(int, input().split(" "))


def gdc(x, y):
    while y:
        x, y = y, x % y
    return x

    # if (x % y == 0):
    #     return y
    # else:
    #     return gdc(x, x % y)


def lcm(x, y):
    return x*y//gdc(x, y)


g = gdc(x, y)
l = lcm(x, y)
print(g)
print(l)
