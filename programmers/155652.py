# 155652
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    alphabet = []
    
    for n in range(ord('a'), ord('z')+1):
        if chr(n) not in skip:
            alphabet.append(chr(n))
    
    for letter in s:
        idx = (alphabet.index(letter) + index) % len(alphabet)
        answer += alphabet[idx]
    return answer
