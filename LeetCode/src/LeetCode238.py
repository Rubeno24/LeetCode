from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [1] * len(nums)
        rarr = [1] * len(nums)
        lMul = 1
        rMul=1

        for x in range(len(nums)):
            j=-x-1
            larr[x]=lMul
            rarr[j]=rMul
            lMul=lMul*nums[x]
            rMul=rMul*nums[j]


        return [a * b for a, b in zip(larr, rarr)]



        






x = Solution()
nums = [1,2,3,4]
print(x.productExceptSelf(nums))