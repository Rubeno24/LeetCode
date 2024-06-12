from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #left pointer is 0 the index
        left=0
        #right pointer is moved in the for loop
        for right in range(len(nums)):
            #we move the right pointer until we find a number that isnt zero and switch with left pointer
            if nums[right]!=0:
                temp=nums[right]
                nums[right]=nums[left]
                nums[left]=temp
                left+=1

        

            





x = Solution()
nums = [1,3,0,0,4 ]
x.moveZeroes(nums)
print(nums)