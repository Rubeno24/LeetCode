class Solution:
    def Driver(self,matrix,x,y):
        self.matrix = matrix
        self.row = len(matrix)
        self.colm = len(matrix[0])
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]

        if not (0 <= x < self.row and 0 <= y < self.colm) or matrix[x][y] == 0:
            print(f"starting point ({x}, {y}) is invalid.")
            return

        self.seen = set([(x,y)])
        self.DFS(x,y)


    def DFS(self,x,y):
        print(f"visting: {x}: {y}")
        for dirx , diry in self.directions:
            nx = dirx + x
            ny = diry + y

            if 0<= nx < self.row and 0<= ny <self.colm and (nx,ny) not in self.seen and self.matrix[nx][ny] == 1:           
                self.seen.add((nx, ny))  # Mark the node as visited
                self.DFS(nx, ny)  # Recursive DFS call

edge_list = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
]


n = 4
matrix= []
for x in range(n):
    matrix.append([0] * n)

for x , y in edge_list:
    matrix[x][y] = 1
print(matrix)

x = Solution().Driver(matrix,0,1)