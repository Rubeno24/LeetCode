from typing import Optional
from TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.Mirror(root.left,root.right)
    


    def Mirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        
        return self.Mirror(left.left,right.right) and self.Mirror(left.right,right.left)

data = [1,2,2,3,4,4,3]
root = TreeNode().list_to_tree_node(data)
x = Solution().isSymmetric(root)
print(x)