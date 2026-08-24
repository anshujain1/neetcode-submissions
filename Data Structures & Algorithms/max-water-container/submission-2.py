class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(heights)-1
        while left <= right:
            width = right - left
            area = min(heights[left] , heights[right]) * width
            if area > maxarea:
                maxarea = area
            if heights[left] <= heights[right]:
                left += 1
                
            else:
                right -= 1
                
            
        return maxarea
