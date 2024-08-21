from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for x in range(len(flowerbed)):
            if flowerbed[x] == 0:
                prev_empty = (x == 0) or (flowerbed[x-1] == 0)
                next_empty = (x == len(flowerbed) - 1) or (flowerbed[x+1] == 0)
                if prev_empty==True and next_empty==True:
                    flowerbed[x] = 1
                    n -= 1  
                    if n == 0:
                        return True
    
        return n <= 0 

solution = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(solution.canPlaceFlowers(flowerbed,n))