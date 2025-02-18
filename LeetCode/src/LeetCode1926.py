from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row , col = len(maze) , len(maze[0])
        x , y = entrance[0] , entrance[1]
        visted = set((x,y))
        q = deque([(x,y,0)])

        directions = [(-1,0),(1,0),(0,1),(0,-1)] # up , down , right , left
        # up since -1 decrease the row thus taking us up

        while q:
            x, y ,steps = q.popleft()
            #check border
            if (x == 0 or x == row-1 or y==0 or y==col-1) and [x,y] != entrance:
                return steps


            for dirX , dirY in directions:
                new_X , newY = dirX + x , dirY + y
                if 0 <= new_X < row and 0 <= newY < col and  maze[new_X][newY] != '+' and (new_X,newY) not in visted:
                    visted.add((new_X,newY))
                    q.append([new_X,newY,steps+1])
        return -1



maze = [["+","+",".","+"]
       ,[".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,2]
x = Solution().nearestExit(maze,entrance)
print(x)