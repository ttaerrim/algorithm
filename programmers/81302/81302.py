# 2021 카카오 채용 연계형 인턴십
# 거리두기 확인하기

def find(place):
    SIZE = 5
    for i, row in enumerate(place):
        for j, dot in enumerate(row):
            p_array = []
            if dot == "O" or dot == "P":
                if (i > 0):
                    p_array.append(place[i-1][j])
                if (i < SIZE - 1):
                    p_array.append(place[i+1][j])
                if (j > 0):
                    p_array.append(place[i][j-1])
                if (j < SIZE - 1):
                    p_array.append(place[i][j+1])
                p_count = p_array.count("P")
                if (dot == "O" and p_count >= 2) or (dot == "P" and p_count >= 1):
                    return False
    return True


def solution(places):
    answer = []
    for i, place in enumerate(places):
        print(find(place))
        answer.append(1 if find(place) else 0)

    return answer
