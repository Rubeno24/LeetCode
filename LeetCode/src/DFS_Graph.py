class Solution:
    def DFS_Runner_List(self, graph):
        self.graph = graph
        self.visted = set()
        self.DFS_List(0)
    
    def DFS_List(self,node):
        self.visted.add(node)
        print(node)
        for x in self.graph[node]:
            if x not in self.visted:
                self.visted.add(x)
                self.DFS_List(x)

    def DFS_Runner_Matrix(self,matrix):
        self.visted = set()
        self.matrix = matrix
        self.DFS_Matrix(0)

    def DFS_Matrix(self, node):
        print(node)
        self.visted.add(node)
        for x in range(len(matrix[node])):
            if matrix[node][x] == 1 and x not in self.visted:
                self.DFS_Matrix(x)




    
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}

matrix = [
    [0, 1, 0, 0, 1, 0],  # Node 0 connections
    [1, 0, 0, 1, 0, 0],  # Node 1 connections
    [0, 0, 0, 1, 0, 1],  # Node 2 connections
    [0, 1, 1, 0, 0, 0],  # Node 3 connections
    [1, 0, 0, 0, 0, 1],  # Node 4 connections
    [0, 0, 1, 0, 1, 0]   # Node 5 connections
]

print("DFS Traversal List")
x = Solution().DFS_Runner_List(graph)
print(x)
print("DFS Traversal Matrix")
y = Solution().DFS_Runner_Matrix(matrix)
print(y)