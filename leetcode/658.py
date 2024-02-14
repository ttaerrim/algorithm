# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/description/

import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(num-x), num) for num in arr]
        heapq.heapify(heap)
        print(heap)
        
        answer = []
        for _ in range(k):
            _, el = heapq.heappop(heap)
            answer.append(el)

        return sorted(answer)
        