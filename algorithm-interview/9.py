class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        
        answer=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in answer:
                            answer.append(sorted([nums[i], nums[j], nums[k]]))
        
        return answer

# 브루트 포스 -> 타임 아웃