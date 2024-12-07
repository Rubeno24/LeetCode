from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for current in asteroids:
            
            while stack and stack[-1] > 0 and current < 0:
                peek = stack[-1]
                if abs(peek) < abs(current):
                    stack.pop()
                elif abs(peek) > abs(current):
                    break
                elif abs(peek) == abs(current):
                    stack.pop()
                    break
            else:
                stack.append(current)

        return stack



            
    
x = Solution()
asteroids = [10,2,-5]
print(x.asteroidCollision(asteroids))