class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dic = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, n in enumerate(nums):
            nums_dic[n] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, n in enumerate(nums):
            if target - n in nums_dic and i != nums_dic[target - n]: # 딕셔너리를 조회하고, i가 다른 조건을 걸어야 런타임 더 빨라진다
            # if target - n in nums[i+1:]:
                return [i, nums_dic[target - n]]