# 최소 직사각형
def solution(sizes):
    answer = 0
    max_width, max_height = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            swap = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = swap

        if max_width < sizes[i][0]:
            max_width = sizes[i][0]

        if max_height < sizes[i][1]:
            max_height = sizes[i][1]

    answer = max_width * max_height

    return answer
