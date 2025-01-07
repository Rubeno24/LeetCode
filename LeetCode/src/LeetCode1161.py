from collections import deque
from typing import Optional

from TreeNode import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        return self.BFS(root)
    
    def BFS(self,root):

        q = deque([root])
        level = 1
        maxSum = float('-inf')
        maxLevel = 0
        while q:
            sum = 0
            currentLvl = len(q)
            for x in range(currentLvl):
                node = q.popleft()
                sum += node.val

                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            if sum > maxSum:
                maxSum = sum
                maxLevel = level
            level +=1  
        return maxLevel


    


data = [1,7,0,7,-8,None,None]
root = TreeNode.list_to_tree_node(data)
hashmap2 = x = Solution().maxLevelSum(root)
print(hashmap2)



