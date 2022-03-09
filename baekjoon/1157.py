# 단어 공부
from collections import Counter

word = input().upper()
word_counter = Counter(word).most_common(2)
print(word_counter[0][0] if len(word_counter) ==
      1 or word_counter[0][1] > word_counter[1][1] else '?')
