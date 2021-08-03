# 배열 파티션 Ⅰ 나의 풀이 == 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(len(nums)):
            if (i % 2 == 0):
                sum += nums[i]
        return sum