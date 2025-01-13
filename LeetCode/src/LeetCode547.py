from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.seen = set()
        self.isConnected = isConnected
        provinces = 0 
        for x in range(len(isConnected)):
            if x not in self.seen:
                provinces += 1
                self.DFS(x)
        return provinces
        
                

    def DFS(self,start):
        stack = [start]

        while stack:
            node = stack.pop()


            if node not in self.seen:
                self.seen.add(node)
                for neighbor in range(len(self.isConnected[node])-1,-1,-1):
                    if self.isConnected [node] [neighbor] == 1 and neighbor not in self.seen:
                        stack.append(neighbor)

    




isConnected = [
    [1,1,0], #node 0
    [1,1,0], #node 1
    [0,0,1]] #node 2
x = Solution().findCircleNum(isConnected)
print(x)
