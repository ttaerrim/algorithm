# 77. Combinations
# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(prefix, nums, k):
            if 0 == k:
                yield prefix
                return
            elif not nums:
                return
            yield from helper(prefix + [nums[0]], nums[1:], k-1)
            yield from helper(prefix, nums[1:], k)
        return list(helper([], list(range(1, n+1)),k))


# [], [1, 2, 3, 4], 2

# [1], [2, 3, 4], 1
#   [1, 2], [3, 4], 0
#     return [1, 2]
#   [1], [3, 4], 1
#     [1, 3], [4], 0
#     return [1, 3]
    # [1], [4], 1
    #   [1, 4], [], 0
        #  return [1, 4]
    #   [1], [], 1
    #     return
# [], [2, 3, 4], 2
    # [2], [3, 4], 1
        # [2, 3], [4], 0
            # return [2, 3]
        # [2], [4], 1
            # [2, 4], [], 0
                # return [2, 4]
            # [2], [], 1
                # return
    # [], [3, 4], 2
        # [3], [4], 1
            # [3, 4], [], 0
                # return [3, 4]
            # [3], [], 1
                # return
        # [], [4], 2
            # [4], [], 1
                # return 
            # [], [], 2
                # return []

