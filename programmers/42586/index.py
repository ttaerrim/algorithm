# 기능개발

def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        count = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        while (len(progresses) != 0 and progresses[0] >= 100):
            print("pop: ", progresses.pop(0))
            speeds.pop(0)
            count += 1
        if count != 0:
            answer.append(count)

    return answer


solution([93, 30, 55], [1, 30, 5])
