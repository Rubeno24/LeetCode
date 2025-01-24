
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        
        for x in range(len(nums)):
            targetNumber = target - nums[x]
            if targetNumber not in hashmap:
                hashmap[nums[x]] = x
            else: 
                return [hashmap[targetNumber] ,x ]
            


nums = [2,7,11,15]
x = Solution().twoSum(nums,9)
print(x)