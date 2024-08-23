from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left, mid = float('inf'), float('inf')

        for x in range(len(nums)):
            if nums[x] > mid:
                return True
            if nums[x] < left:
                left = nums[x]
            elif nums[x] > left and nums[x] < mid:
                mid = nums[x]
        return False


solution = Solution()
nums = [20, 100, 10, 12, 5, 13]

print(solution.increasingTriplet(nums))
