from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.seen = set()
        self.connections = connections
        self.DFS()

    def DFS(self):
        stack = [0]
        while stack:
            node = stack.pop()
            print(node)
            if node not in self.seen:
                self.seen.add(node)
                for x in range(len(self.connections[node])-1,-1,-1):
                    stack.append(x)



data = [[0,1],[1,3],[2,3],[4,0],[4,5]]
n = 6
x = Solution().minReorder(n,data)
