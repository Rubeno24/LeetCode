from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = {}
        for edge in edges:
            for node in edge:
                hashmap[edge] = node

        return hashmap
                


edges = [[1,2],[2,3],[4,2]]
x = Solution().findCenter(edges)
print(x)