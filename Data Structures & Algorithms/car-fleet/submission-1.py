class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        for i,j in cars:
            time = (target - i) / j

            if not stack or stack[-1]< time:
                stack.append(time)

        
        return len(stack)
        