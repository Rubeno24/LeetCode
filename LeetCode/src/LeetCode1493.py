from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_zero = 0
        max_count = 0
        left = 0

        for x in range(len(nums)):      
            if nums[x] == 0:
                num_zero+=1

            while num_zero > 1:
                if nums[left] == 0:
                    num_zero-=1
                left+=1
        
            width = x - left + 1
            max_count = max(max_count,x-left)
        return max_count







x = Solution()
nums = [1,1,0,1]
print(x.longestSubarray(nums))