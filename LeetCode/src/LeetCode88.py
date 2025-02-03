from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        num3 = nums1[:m]
        i = 0
        j = 0 
        k = 0
        while i < m and j < n:
            if num3[i] < nums2[j]:
                nums1[k] = num3[i]
                k+=1
                i+=1
            elif nums2[j] < num3[i]:
                nums1[k] = nums2[j]
                k+=1
                j+=1
            else:
                nums1[k] = num3[i]
                k+=1
                i+=1
        if i == m:
            nums1[k:] = nums2[j:]
        else:
            nums1[k:] = num3[i:]
        print(nums1)







nums1 = [1]
m = 1
nums2 = []
n = 0
x = Solution().merge(nums1,m, nums2,n)