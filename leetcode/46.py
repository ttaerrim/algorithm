# 46. Permutations
# https://leetcode.com/problems/permutations/

import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)

# 다른 풀이 2
# 제너레이터(generator), yield, 순열 직접 만들기
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(prefix, num):
            if not num:
                yield prefix
                return
            for idx, n in enumerate(num):
                yield from helper(prefix + [n], num[:idx]+num[idx+1:])
        return list(helper([], nums))
