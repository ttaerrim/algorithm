# 나머지 한 점
# https://school.programmers.co.kr/learn/courses/18/lessons/1878

def solution(v):

    xx = []
    yy = []
    for coord in v:
        x, y = coord
        if x not in xx:
            xx.append(x)
        else:
            xx.remove(x)
        
        if y not in yy:
            yy.append(y)
        else:
            yy.remove(y)

    return [xx[0], yy[0]]

# 다른 풀이 2
# XOR 연산자 (^)를 사용하여 중복으로 가지고 있는 값이 아닌 다른 값을 선택할 수 있도록 한다

# 같은 수를 XOR 연산하면 항상 0이 된다
# XOR 연산은 두 비트가 다를 때만 1을 반환하므로, 같은 수의 각 비트는 항상 동일하기 때문에 결과는 항상 0이 된다

# 어떤 수 n과 0을 XOR 연산하면 결과는 항상 n이 된다
# XOR 연산은 두 비트가 다를 때만 1을 반환하므로, 0과의 XOR 연산에서는 원래 숫자의 모든 비트가 그대로 유지된다

def solution2(v):
    x = v[0][0] ^ v[1][0] ^ v[2][0]
    y = v[0][1] ^ v[1][1] ^ v[2][1]

    return [x, y]
