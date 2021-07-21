class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 포인터 사용해서 교환하는 방법
        left, right = 0, len(s)-1
        while left <= right: # <= 라고 썼는데 < 로 쓰는 것이 더 효율적이다
            swap = s[left]
            s[left] = s[right]
            s[right] = swap
            # s[left], s[right] = s[right], s[left]
            # 로 쓰면 swap 없이 한 줄로도 바꿀 수 있다
            left += 1
            right -= 1

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))