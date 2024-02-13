# https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 코딩 기초 트레이닝 > 글자 이어 붙여 문자열 만들기

def solution(my_string, index_list):
    return "".join([my_string[idx] for idx in index_list])
