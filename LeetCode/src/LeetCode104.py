from typing import Optional
from TreeNode import TreeNode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    

    def walk(self, root: Optional[TreeNode]) -> None:
        if root is not None:
            print(root)  # Assuming TreeNode has a 'val' attribute
            self.walk(root.left)
            self.walk(root.right)





head = TreeNode(3,left = TreeNode(9),right = TreeNode(20,left = TreeNode(15),right = TreeNode(7)))
x = Solution()
print(x.maxDepth(head))
print("-------------------------------------------------------------------")
print(x.walk(head))

