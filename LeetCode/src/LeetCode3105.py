from typing import List


class Solution:
    def longesMonotonicSubarray(self, nums: List[int]) -> int:
        incCount = 1
        decCount = 1

        for x in range(1,len(nums)):
            if nums[x] > nums[x-1]:
                incCount+=1
                decCount = 1
            elif nums[x] < nums[x-1]:
                decCount+=1
                incCount = 1
            else:
                incCount = 1
                decCount = 1
            maxLength = max(decCount,incCount)

            return maxLength
    
nums = [1,4,3,3,2]
x = Solution().longesMonotonicSubarray(nums)
print(x)