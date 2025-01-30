from collections import defaultdict
class Solution:
    def Driver(self,source,graph):
        self.graph = graph
        self.seen = set([source])
        self.DFS(source)
        
    
    def DFS(self,source):
        print(source)

        for neighbor in self.graph[source]:
            if neighbor not in self.seen:
                self.seen.add(neighbor)
                self.DFS(neighbor)

edge_list = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4)
]
graph = defaultdict(list)
for x ,y in edge_list:
    graph[x].append(y)

x = Solution().Driver(1,graph)


