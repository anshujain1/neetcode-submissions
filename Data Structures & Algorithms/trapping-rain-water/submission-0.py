class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax =[]
        rightmax = []
        for i in range(len(height)):
            if i == 0:
                leftmax.append(height[i])
            else:
                leftmax.append(max(leftmax[i-1], height[i]))
        
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                rightmax.append(height[len(height)-1])
            else:
                rightmax.append(max(rightmax[-1],height[i]))
        answer = 0
        for i in range(len(height)):
            area = min(leftmax[i], rightmax[len(height)-1-i]) - height[i]
            answer += area
        
        return answer
            
                
            
            