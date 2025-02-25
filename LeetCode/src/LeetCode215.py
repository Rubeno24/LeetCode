import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap =[]
        for x in nums:
            negNumber = x *-1
            heapq.heappush(maxHeap,negNumber)

        for x in range(k-1):
            heapq.heappop(maxHeap)
        return maxHeap[0] * -1




nums = [3,2,1,5,6,4]
k = 2
x = Solution().findKthLargest(nums,k)
print(x)