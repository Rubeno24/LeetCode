from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        newArr = []
        maxCandies = max(candies)
        for x in range(len(candies)):
            if candies[x]+extraCandies>=maxCandies:
                newArr.append(True)
            else:
                newArr.append(False)
        return newArr
               
            


solution = Solution()
candies = [4,2,1,1,2]
extraCandies = 1
print(solution.kidsWithCandies(candies,extraCandies))