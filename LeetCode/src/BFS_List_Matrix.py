
from collections import deque


def BFS(maxtrix, start):
    visted = set()
    queue = deque([start])
    visted.add(start)

    while queue:
        node = queue.popleft()
        print(node)

        for x in range(len(maxtrix)):
            if maxtrix[node][x] ==1 and x not in visted:
                visted.add(x)
                queue.append(x)
                
                
matrix = [
    [0, 1, 0, 0, 1, 0],  # Node 0 connections
    [1, 0, 0, 1, 0, 0],  # Node 1 connections
    [0, 0, 0, 1, 0, 1],  # Node 2 connections
    [0, 1, 1, 0, 0, 0],  # Node 3 connections
    [1, 0, 0, 0, 0, 1],  # Node 4 connections
    [0, 0, 1, 0, 1, 0]   # Node 5 connections
]

x = BFS(matrix,0)

