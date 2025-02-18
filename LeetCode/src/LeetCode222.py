from typing import Optional

from TreeNode import TreeNode



class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0 
        self.DFS(root)
        return self.count

    def DFS(self,root):
        if root is not None:
            self.count +=1
            self.DFS(root.left)
            self.DFS(root.right)


data = [1,2,3,4,5,6] 
root = TreeNode().list_to_tree_node(data)



x = Solution().countNodes(root)
print(x)