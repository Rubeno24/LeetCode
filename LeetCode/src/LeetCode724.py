from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0 

        for x in range(len(nums)):
            rightSum = total - nums[x] - leftSum

            if rightSum == leftSum:
                return x
            leftSum += nums[x]
        return -1

    


    


x = Solution()
nums = [1,2,3]
print(x.pivotIndex(nums))
