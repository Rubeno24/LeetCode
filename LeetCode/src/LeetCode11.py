from typing import List

#2 pointer appraoch for containter with the most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW = 1
        x = 0
        y = len(height)-1
        while x<y:
            if height[x] <= height[y]:
                maxW = max(maxW, height[x]*(y-x))
                x+=1
            elif height[y] <= height[x]:
                maxW = max(maxW, height[y]*(y-x))
                y-=1
        return maxW

x=Solution()
height = [1,1]

print(x.maxArea(height))