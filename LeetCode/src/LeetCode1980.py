from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        og = set(nums)
        # Shift 1 n place to the left
        # 1 is 0001
        # would be 0100 so 4
        for i in range(1 << n):
            binary_str = format(i, '0' + str(n) + 'b')
            if binary_str not in og:
                return binary_str
        return -1
        





nums = ["111","011","001"]
x = Solution().findDifferentBinaryString(nums)
print(x)