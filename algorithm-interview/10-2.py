# 파이썬다운 방식으로 한 줄로 출력
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])