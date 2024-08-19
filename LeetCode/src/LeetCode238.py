from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lMulti = 1
        rMulti = 1
        lArr = [0] * len(nums)
        rArr = [0] * len(nums)
        lenght = len(nums)
        for i in range(lenght):
            j=-i-1
            lArr[i] = lMulti
            rArr[j] = rMulti
            lMulti *= nums[i]
            rMulti *= nums[j]
        newArr = [0] * lenght
        for i in range(lenght):
            newArr[i]=lArr[i] * rArr[i]
        return newArr




x = Solution()
nums = [1,2,3,4]
print(x.productExceptSelf(nums))