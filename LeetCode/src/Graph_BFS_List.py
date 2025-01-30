from collections import defaultdict, deque


class Solution:
    def driver(self,source,graph):
        self.seen = set([source])
        self.q = deque([source])
        self.graph = graph
        self.BFS(source)


    def BFS(self,source):
        while self.q:
            node = self.q.popleft()
            print(node)
            for neighbor in self.graph[node]:
                if neighbor not in self.seen:
                    self.seen.add(neighbor)
                    self.q.append(neighbor)


edge_list = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4)
]

graph = defaultdict(list)
for x , y in edge_list:
    graph[x].append(y)

x = Solution().driver(1,graph)