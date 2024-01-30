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

# 다른 풀이 2
def solution(s, skip, index):
    answer = ''
    
    for letter in s:
        count = index
        while count:
            if letter == 'z': # 다른 풀이 1에서 ord('z') == 122보다 크면 변경한 것 대신에 letter 문자를 가지고 풀이
                letter = 'a'
            else:
                letter = chr(ord(letter) + 1)
            if letter not in skip:
                count -= 1
        answer += letter
        
    return answer
