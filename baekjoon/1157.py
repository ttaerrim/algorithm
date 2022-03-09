# 단어 공부
from collections import Counter


def find_max(word):
    if len(word) == 1 or word[0][1] > word[1][1]:
        return word[0][0]
    else:
        return "?"


word = input().upper()
word_counter = Counter(word).most_common(2)
print(find_max(word_counter))
