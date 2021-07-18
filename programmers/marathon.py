def solution(participant, completion):

    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if (completion[i] != participant[i]):
            answer = participant[i]
    return answer


############################################
# 결과 출력                                #
############################################


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
