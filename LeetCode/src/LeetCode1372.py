from typing import Optional
from TreeNode import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        self.DFS(root,'left',0)
        return self.maxLength
        

    def DFS(self,root,direction: str,length):
        if root is not None:
            self.maxLength = max(self.maxLength,length)

            if direction == 'right':
                self.DFS(root.left,'left',length + 1)
                self.DFS(root.right, 'right', 1)  # Start a new zigzag path

            elif direction == 'left':
               self.DFS(root.right,'right',length + 1) 
               self.DFS(root.left, 'left', 1)  # Start a new zigzag path

            
    
            

data = [4,2,7,1,3]

root = TreeNode.list_to_tree_node(data)
print(root)


    