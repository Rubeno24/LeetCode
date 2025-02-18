from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < length:
            if arr[i] == 0:
                arr.insert(i,0)
                i+=2
                arr.pop(-1)
            else:
                i+=1
        print(arr)





arr = [1,2,3]
x = Solution().duplicateZeros(arr)
print(x)

