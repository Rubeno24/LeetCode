from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]  
        curr_sum = nums[0] 
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i] 
        
        return max(max_sum, curr_sum)


nums = [10,20,30,5,10,50]

x = Solution().maxAscendingSum(nums)
print(x)