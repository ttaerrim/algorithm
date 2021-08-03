# 배열에 넣어 버리기
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        pair=[]
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum