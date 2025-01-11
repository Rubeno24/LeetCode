class Solution:
    def DFS(self, graph , start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                print(node)

                #Add unvisited nodes to stack
                for x in reversed(graph[node]):
                    if x not in visited:
                        stack.append(x)



    
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}

print("DFS Traversal (Iterative):")
x = Solution().DFS(graph,1)