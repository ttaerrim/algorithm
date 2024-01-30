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


# 다른 풀이 1
def solution(s, skip, index):
    answer = ''
    
    for letter in s:
        idx = ord(letter)
        count = index
        while count:
            idx += 1
            if idx > ord('z'):
                idx = idx%ord('z') + 96
            if chr(idx) not in skip:
                count -= 1
        answer += chr(idx)
        
    return answer
