# 투 포인터 최대로 이동하기
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: # 빈 배열의 out of range 방지
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left] # 좌 기둥 최대 높이에서 현재 기둥 차이만큼 빼서 volume에 추가
                left += 1
            else:
                volume += right_max - height[right] # 우 기둥 최대 높이에서 현재 기둥 차이만큼 빼서 volume에 추가
                right -= 1
            # 최대 지점에서 좌우 포인터가 만나게 됨
        return volume