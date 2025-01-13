from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for x in range(len(flowerbed)):
            if flowerbed[x] == 0:
                if x > 0:
                    prev = flowerbed[x-1]
                else:
                    prev = 0

                if x < len(flowerbed) - 1:
                    next = flowerbed[x+1]
                else:
                    next = 0

                if prev == 0 and next == 0:
                    flowerbed[x] = 1
                    n-=1

                if n == 0:
                    return True
                
        return n <= 0

flowerbed = [1,0,0,0,1]
n = 1
x = Solution().canPlaceFlowers(flowerbed,n)
print(x)