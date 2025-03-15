import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        minNumber = 10000000000
        sum = 0
        for x in range(len(nums2)):
            heapq.heappush(heap,(nums2[x]*-1,x))

        for x in range(k):
            num , index = heapq.heappop(heap)
            notNeg = num *-1
            minNumber = min(notNeg,minNumber)
            sum += nums1[index]
        return sum * minNumber


nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
x = Solution().maxScore(nums1,nums2,k)
print(x)