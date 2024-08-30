from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zero = 0
        max_width = 0
        left = 0
        for x in range(len(nums)):
            if nums[x] == 0:
                num_zero+=1
        
            #moves the window in when left == 0 then we are going pass a 0 then we can say numzero -1
            while num_zero > k:
                if nums[left] == 0:
                    num_zero-=1
                left+=1
            #how to find the size of a window
            width = x - left + 1
            max_width = max(max_width,width)
        return max_width




x = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(x.longestOnes(nums,k))