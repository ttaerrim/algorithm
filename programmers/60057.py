# 문자열 압축

def iter_str(s_arr):
    start = ''
    count = 1
    iter_str = ''
    for i in range(len(s_arr)):
        if i == 0:
            start = s_arr[i]
        elif i != 0 and start != s_arr[i]:
            iter_str += start if count == 1 else str(count) + start
            start = s_arr[i]
            count = 1
        else:
            count += 1

        if i == len(s_arr) - 1:
            iter_str += start if count == 1 else str(count) + start

    return len(iter_str)


def solution(s):
    smallest = len(s)

    for i in range(1, len(s)//2+1):
        s_arr = []
        for j in range(0, len(s), i):
            s_arr.append(s[j:j+i])

        len_s_arr = iter_str(s_arr)
        if smallest > len_s_arr:
            smallest = len_s_arr

    return smallest


solution("aabbaccc")
