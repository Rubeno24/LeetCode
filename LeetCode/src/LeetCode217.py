from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #set to store numbers since it doesnt hold dupes
        hashSet = set()
        #loop through numbers in nums
        for x in nums:
            # the current number is in the set return true since that means its a dupe
            if x in hashSet:
                return True
                
            else:
                # not in the set add it to the set for the next itteration
                hashSet.add(x)
        # return false if true is never returned
        return False




    

x = Solution()

nums = [1,1,2,3,1,4]
print(x.containsDuplicate(nums))

