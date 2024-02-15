# https://leetcode.com/problems/top-k-frequent-elements/description/
# 347. Top K Frequent Elements

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = [(-count, item) for item, count in counter.items()]
        heapq.heapify(heap)

        answer = []
        for _ in range(k):
            _, item = heapq.heappop(heap)
            answer.append(item)

        return answer
