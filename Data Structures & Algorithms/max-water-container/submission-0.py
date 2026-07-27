class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxarea= 0
        
        while l<r:
            width= r-l
            area = min(heights[l], heights[r]) * width 
            if area > maxarea:
                maxarea = area 
            if heights[l] < heights[r]:
                l+=1    
                continue
            elif heights[l] > heights[r]:
                r -= 1
                continue
            else:
                l +=1
                continue
            
        
        return maxarea