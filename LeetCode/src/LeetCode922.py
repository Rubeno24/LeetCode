from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd =1
        n = len(nums)

        while even < n and odd < n:
            if nums[even] %2 ==0:
                even +=2
            elif nums[odd] %2 !=0:
                odd+=2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums



nums = [4,2,5,7]
x = Solution().sortArrayByParityII(nums)
print(x)
