class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            ast_survival = True

            while stack and stack[-1] > 0 and asteroid < 0:

                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    ast_survival = False
                    break

                elif abs(stack[-1]) > abs(asteroid):
                    ast_survival = False
                    break

                else:
                    stack.pop()

            if ast_survival:
                stack.append(asteroid)

        return stack