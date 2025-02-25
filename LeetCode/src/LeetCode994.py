from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cols , rows = len(grid[0]), len(grid)
        freshO = 0
        q = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    q.append((x,y,0))
                elif grid[x][y] == 1:
                    freshO +=1


        directions = [(-1,0),(1,0),(0,1),(0,-1)] # up , down , right , left
        # up since -1 decrease the row thus taking us up
        min = 0

        while q:
            x , y , min = q.popleft()

            for dirx ,diry in directions:
                newX , newY = x +dirx, y + diry

                if 0<= newX <rows and 0<= newY < cols and grid[newX][newY] ==1 :
                    grid[newX][newY] =2
                    freshO-=1
                    q.append((newX,newY,min+1))
        if freshO == 0:
                return min
        else:
                return -1


grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
#0 = emty
#1 = fresh
#2 = rotten

x = Solution().orangesRotting(grid)
print(x)