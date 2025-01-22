from collections import deque
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]

        
                


edges = [[1,2],[5,1],[1,3],[1,4]]
x = Solution().findCenter(edges)
print(x)

