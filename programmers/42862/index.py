# 체육복
def solution(n, lost, reserve):

    lost, reserve = list(set(lost) - set(reserve)
                         ), list(set(reserve) - set(lost))

    answer = n - len(lost)

    for l in lost:
        if l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            answer += 1
            reserve.remove(l+1)

    return answer
