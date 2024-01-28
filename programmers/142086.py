# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    for i in range(len(s)):
        if s[:i].rfind(s[i]) == -1:
            answer.append(s[:i].rfind(s[i]))
        else:
            answer.append(i - s[:i].rfind(s[i]))
                           
            
    return answer

# 다른 풀이
def solution2(s):
    answer = []
    letter2idx = {}
    for i, letter in enumerate(s):
        if letter in letter2idx:
            answer.append(i - letter2idx[letter])
        else:
            answer.append(-1)
        letter2idx[letter] = i
        
                           
            
    return answer
