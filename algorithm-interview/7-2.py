# in을 이용한 탐색
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            remainder = target - n
            
            if remainder in nums[i+1:]:
                return [i, nums[i+1:].index(remainder)+i+1]