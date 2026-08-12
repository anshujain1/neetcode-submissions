class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                a = stack.pop()

                h = heights[a]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                maxarea = max(maxarea , h*width)

            stack.append(i)

        return maxarea