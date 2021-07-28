# 조회 구조 개선

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return nums_map[target - num], i
            nums_map[num] = i # if 문 이후에 넣는 이유는 [3, 2, 4], 6의 경우를 생각해 보면 된다
        
            

s = Solution()
print(s.twoSum([2,7,11,15], 9))