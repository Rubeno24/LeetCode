from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        for x in spells:
            l = 0
            r =len(potions)-1
            while l <= r:
                m = (l+r) //2
                if x * potions[m] >= success:
                    r = m-1
                else:
                    l=m+1
            result.append(len(potions) - l)
        return result



spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
# 1 2 3 4 5
#       l r 
x = Solution().successfulPairs(spells,potions,success)
#answer [4,0,3]

print(x)

print("meem")