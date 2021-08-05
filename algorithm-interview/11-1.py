# 풀이 힌트 보고 푼 풀이
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, right = 1, 1
        results_l, results_r, results=[], [], []
        for i in range(len(nums)):
            results_l.append(left)
            results_r.append(right)
            
            left *= nums[i]
            right *= nums[len(nums)-1-i]
        results_r.reverse()
        for i in range(len(results_l)):
            results.append(results_l[i] * results_r[i])
        return results
    ## 메모리 줄이기    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mul = 1
        results=[]
        for i in range(len(nums)):
            results.append(mul)
            mul *= nums[i]
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            results[i] *= mul
            mul *= nums[i]
        return results
