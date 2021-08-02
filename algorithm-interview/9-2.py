class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                elif sum == 0:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left]==nums[left+1]: # 현재 left와 다음 left 값이 같으면 다를 때까지 넘김
                                                                     # 인덱스 오류 나지 않게 left < right 필수로 지정해 준다
                        left += 1
                    while left < right and nums[right]==nums[right-1]: # 현재 right와 다음 right 값이 같으면 다를 때까지 넘김
                        right -= 1
                    left += 1
                    right -= 1
        
        return results