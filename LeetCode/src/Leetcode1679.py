from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        x = 0
        y = len(nums)-1
        operations =0
        nums.sort()
        
        while x < y:
            if nums[x] + nums[y] == k:
                operations+=1
                x+=1
                y-=1
            elif nums[x] + nums[y] < k:
                x+=1
            else:
                y-=1
        return operations



                

solution = Solution()
nums = [1,2,3,4]

k = 5
print(solution.maxOperations(nums,k))