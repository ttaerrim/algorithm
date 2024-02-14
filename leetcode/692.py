# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [(-counter[k], k) for k in counter]
        heapq.heapify(heap)

        answer = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            answer.append(word)
        
        return answer
