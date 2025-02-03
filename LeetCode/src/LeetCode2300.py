from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        results = []
        for x in spells:
            l = 0
            r = len(potions) - 1
            inx = len(potions)

            while l <= r:
                middle = (l+r)//2

                if x * potions[middle] >= success:
                    r = middle - 1
                    inx = middle
                else:
                    l = middle + 1
            results.append(len(potions) - inx)
        return results

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7



x = Solution().successfulPairs(spells,potions,success)
print(x)