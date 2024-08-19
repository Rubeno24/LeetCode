from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hashmap (dictionary)
        hashMap = {}

        # Iterate over each number and its index in the nums list
        for i, number in enumerate(nums):
            # Calculate the difference needed to reach the target sum
            difference = target - number
    
            # Check if the difference exists in the hashmap
            if difference in hashMap:
                # If found, return the indices that sum up to the target
                return [hashMap[difference], i]
    
            # Store the current number and its index in the hashmap
            hashMap[number] = i



x = Solution()
nums = [2,7,11,15]
print(x.twoSum(nums,9))#0 1
