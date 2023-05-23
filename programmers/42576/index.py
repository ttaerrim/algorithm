# 완주하지 못한 선수
from collections import Counter


def sortSolution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


def hashSolution(participant, completion):
    hashDict = {}
    sumHash = 0
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    return hashDict[sumHash]


def collectionSolution(participant, completion):
    answer = Counter(participant)-Counter(completion)
    return list(answer.keys())[0]
