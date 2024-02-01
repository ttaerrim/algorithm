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
