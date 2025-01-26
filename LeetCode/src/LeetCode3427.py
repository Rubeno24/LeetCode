from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sumReturn = 0 
        for i in range(len(nums)):
            start = max(0,i-nums[i])
            
            subArr = nums[start:i+1]
            sumReturn = sumReturn + sum(subArr)
        return sumReturn


nums = [3,1,1,2]
x = Solution().subarraySum(nums)
print(x)