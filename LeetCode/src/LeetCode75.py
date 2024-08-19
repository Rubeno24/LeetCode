from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergerSort(nums)

    def mergerSort(self,nums: List[int]):
        if len(nums)>1:

            leftArray = nums[:len(nums)//2]
            rightArray = nums[len(nums)//2:]

            self.mergerSort(leftArray)
            self.mergerSort(rightArray)


            leftIndex = 0
            rightIndex = 0
            mergeIndex = 0

            while leftIndex < len(leftArray) and rightIndex < len(rightArray):
                if leftArray[leftIndex] < rightArray[rightIndex]:
                    nums[mergeIndex] = leftArray[leftIndex]
                    leftIndex+=1
                    mergeIndex+=1
                else:
                    nums[mergeIndex] = rightArray[rightIndex]
                    rightIndex+=1
                    mergeIndex+=1
            
            while leftIndex < len(leftArray):
                nums[mergeIndex] = leftArray[leftIndex]
                leftIndex+=1
                mergeIndex+=1
            
            while rightIndex < len(rightArray):
                nums[mergeIndex] = rightArray[rightIndex]
                rightIndex+=1
                mergeIndex+=1
        


arr = [134, 23, 45, 23, 24, 4, 54, 23, 5, 4, 5, 4]
x=Solution()
x.sortColors(arr)
print(arr)



                
    