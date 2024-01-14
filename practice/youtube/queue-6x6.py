# (249) Queue로 풀 수 있는 코테 문제 유형? [기업 코딩테스트 단골]
# https://www.youtube.com/watch?v=YlIPiNnj0Js&t=404s

def solution(p):
    def update_block(start, p):
        queue = [start] # [[[0][1]], [[1][2]]]
        while (queue != []):
            i, j = queue.pop(0)
            if(i-1 > 0 and p[i-1][j]==0): queue.append([i-1, j])
            if(i+1 < len(p) and p[i+1][j]==0): queue.append([i+1, j])
            if(j-1 > 0 and p[i][j-1]==0): queue.append([i, j-1])
            if(j+1 < len(p[i]) and p[i][j+1]==0): queue.append([i, j+1])
            p[i][j] = 2
    
    answer = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            if(p[i][j]==0):
                answer += 1
                update_block([i, j], p)
            
    print(answer)
            

# panel=[
#     [0, 0, 0, 1, 0, 0],
#     [0, 1, 1, 1, 0, 0],
#     [1, 1, 0, 1, 1, 1],
#     [0, 1, 0, 0, 1, 1],
#     [0, 1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0, 1],
# ]

panel = [
    [0,0,1,1,0,0],
    [1,1,0,1,1,0],
    [1,1,0,1,1,1],
    [0,0,1,0,0,1],
    [1,1,1,1,1,0],
    [0,0,1,1,0,0],
]

solution(panel)
