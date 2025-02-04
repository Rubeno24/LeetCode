from typing import List


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)  
        nums[:] = nums[-k:] + nums[:-k]  
        print(nums)




nums = [1,2,3,4,5]
k = 7
x = Solution().rotate(nums,k)
