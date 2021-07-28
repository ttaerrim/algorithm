class Solution:
    def trap(self, height: list[int]) -> int:
        def all_true(elements, left, right):
            result = True
            for element in elements:
              # not 연산자를 통해 형변환이 이루어짐
              if element>=left or element>=right: # bool(element) == False
                result = False
                break
            return result
        
        left, right = 0, 0
        sum = 0
        
        while(left < len(height)-2 and right < len(height)): # while문 이따 수정
            right = left + 2
            while min(height) >= height[left]:
                left += 1
                right = left + 2
            while (right < len(height)):
                result = all_true(height[left+1:right], height[left], height[right])
                print(result, left, right)
                if result:
                    for i in range(left+1, right):
                        sum += min(height[left], height[right]) - height[i]
                    left = right
                    right = left + 2
                    continue
                else:
                    right += 1
                    if right == len(height):
                        left += 1
                        right = left + 2
        return sum

# 노력했지만...... 테스트 케이스만 풀고 실패