def solution(s):
    length = len(s)//2
    if (len(s) % 2 == 0):
        answer = s[length-1:length+1]
    else:
        answer = s[length]

    return answer

############################################
# 결과 출력                                #
############################################


s = 'qwer'
print(solution(s))

s = 'abcde'
print(solution(s))
