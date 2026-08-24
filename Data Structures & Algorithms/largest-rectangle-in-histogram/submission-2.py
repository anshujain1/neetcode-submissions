class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []
        for i in range(len(heights)+ 1):
            if i== len(heights):
                curr = 0
            else:
                curr = heights[i]
            while stack and heights[stack[-1]] > curr:
                a = stack.pop()

                h = heights[a]
                w = i if not stack else i-stack[-1]-1

                best = max(best , h*w)
            stack.append(i)
        return best
                
