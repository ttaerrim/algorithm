# 연습 문제 > 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930?itm_content=course14743

def solution(s):
    answer = ''
    strs = s.split(' ')
    for i in range(len(strs)):
        temp = ''
        for j in range(len(strs[i])):
            if j % 2 == 0:
                temp += strs[i][j].upper()
            else:
                temp += strs[i][j].lower()
        strs[i] = temp
    
    return " ".join(strs)

# 다른 풀이
def solution2(s):
    answer = ''
    even = True
    
    for letter in s:
        if letter == ' ':
            answer += letter
            even = True
            continue
        elif even:
            answer += letter.upper()
        else:
            answer += letter.lower()
        even = not even
    return answer
