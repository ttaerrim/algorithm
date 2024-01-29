# 연습 문제 > 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = []
    
    head = 0
    idx = 0
    firstLetter = s[0]
    letters = [0, 0]
    
    while idx < len(s):
        if s[idx] == firstLetter:
            letters[0] += 1
        else:
            letters[1] +=1
        
        if letters[0] == letters[1]:
            answer.append(s[head:(idx+1)])
            if idx + 1 < len(s):
                firstLetter = s[idx+1]
            letters = [0, 0]
            head = idx + 1
    
        idx += 1
        
    if head < idx:
        answer.append(s[head:idx])
            
    return len(answer)

# 다른 풀이
def solution2(s):
    answer = 0
    
    firstLetter = s[0]
    countFirst = countRest = 0
    
    for i, letter in enumerate(s):
        if letter == firstLetter:
            countFirst += 1
        else:
            countRest += 1
            
        if countFirst == countRest:
            answer += 1
            if i != len(s) - 1:
                firstLetter = s[i+1]
            countFirst = countRest = 0
    if countFirst != countRest:
        answer += 1
        
    return answer
