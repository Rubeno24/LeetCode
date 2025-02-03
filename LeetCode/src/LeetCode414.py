from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # remove duplicates
        nums.sort(reverse=True)  # sort in descending order
    
        if len(nums) >= 3:
            return nums[2]  # third max
        return nums[0]  # return max if < 3 distinct numbers

nums = [2,2,3,1]
x = Solution().thirdMax(nums)
print(x)