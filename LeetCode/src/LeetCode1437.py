from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k  
        
        for i in range(len(nums)):
            if nums[i] == 1:  
                if count < k:  
                    return False
                count = 0  
            else:
                count += 1 
        
        return True





nums = [1,0,0,0,1,0,0,1]
k = 2
x = Solution().kLengthApart(nums, k)