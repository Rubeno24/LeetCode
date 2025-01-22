from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        arr = [0] * (n+1)

        
        for x , y in trust:
            arr[x] -=1
            arr[y] +=1
        
        for x in range(1,n+1):
            if arr[x] ==n-1:
                return x
            
        return -1


n = 2
trust = [[1,2]]
x = Solution().findJudge(n,trust)
print(x)

