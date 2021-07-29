class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]: # 스택이 비어 있지 않고 현재 기둥이 스택의 마지막 순서 기둥보다 높으면
                top = stack.pop() # 스택에서 꺼내 top에 저장
                
                if not len(stack): # 스택이 비어 있으면 while문을 빠져나온다
                    break
                
                distance = i -stack[-1] - 1 # 기둥 사이 차이 계산
                waters = min(height[i], height[stack[-1]]) - height[top] 
                
                volume += distance * waters
            stack.append(i)
        return volume