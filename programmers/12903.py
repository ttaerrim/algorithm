# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 가운데 글자 가져오기

def solution(s):
    # is_odd = len(s) % 2
    # half = len(s) // 2
    half, is_odd = divmod(len(s), 2)
    return s[half] if is_odd else s[half-1:half+1]
