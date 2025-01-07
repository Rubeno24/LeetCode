from typing import Optional
from TreeNode import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.DFS(root,val)
        

    def DFS(self,root, val):
        if root is None:
            return None
        if root is not None and root.val == val:
            return root
        if root.val > val:
            left = self.DFS(root.left,val)
            if left:
                return left
        else:
            right = self.DFS(root.right,val)
            if right:
                return right

data  = [4,2,7,1,3]
root = TreeNode.list_to_tree_node(data)
x = Solution().searchBST(root,2)
print(x)