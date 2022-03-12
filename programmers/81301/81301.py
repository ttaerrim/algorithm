# 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어

def solution(s):

    eng_num = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
    for i in range(len(eng_num)):
        s = s.replace(eng_num[i], str(i))

    return int(s)
