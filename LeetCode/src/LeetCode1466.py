from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        self.count = 0
        #makes a adjaency list
        for u , v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))
        self.graph = graph
        self.seen = set()
        self.DFS(0)
        return self.count

    def DFS(self,node):
        self.seen.add(node)
        for neighbor, direction in self.graph[node]:
            if neighbor not in self.seen:
                self.seen.add(node)
                self.count+=direction
                self.DFS(neighbor)




data = [[0,1],[1,3],[2,3],[4,0],[4,5]]

n = 6
x = Solution().minReorder(n,data)
print(x)


