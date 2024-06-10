from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedArray = sorted(heights)  # Sort the list and assign it to sortedArray
        count = 0
        for x in range(len(heights)):
            if heights[x] != sortedArray[x]:
                count += 1
        return count

mylist = [1, 1, 4, 2, 1, 3]
x = Solution()
print(x.heightChecker(mylist))
