class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1] # 리트코드 상에서는 얘는 안 먹히고
        s[:] = s[::-1] # 얘는 먹힌다
            