class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def first():
            ## 첫 풀이
            # 문제점: nums에 0이 있으면 결과가 전부 0이 나온다, 나눗셈 쓰면 안 된다
            mul = 1
            results=[]
            for num in nums:
                mul *= num
            for i in range(len(nums)):
                if nums[i] == 0:
                    results.append(0)
                else:
                    results.append(int(mul/nums[i]))
            return results
        def second():
            ## 타임 리밋 걸림
            mul = 1
            results=[]
            pointer = 0
            while pointer < len(nums):
                for i in range(len(nums)):
                    if i == pointer:
                        continue
                    mul *= nums[i]
                results.append(mul)
                pointer += 1
                mul = 1
            return results