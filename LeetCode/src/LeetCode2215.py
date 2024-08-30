from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        # Elements in nums1 but not in nums2
        diff1 = list(set1 - set2)
        # Elements in nums2 but not in nums1
        diff2 = list(set2 - set1)
        return diff1,diff2




x = Solution()
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(x.findDifference(nums1,nums2))