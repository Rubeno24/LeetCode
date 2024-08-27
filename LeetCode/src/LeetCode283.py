from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sec = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[x], nums[sec] = nums[sec], nums[x]
                sec+=1



            





x = Solution()
nums = [1,3,0,0,4 ]
x.moveZeroes(nums)
print(nums)