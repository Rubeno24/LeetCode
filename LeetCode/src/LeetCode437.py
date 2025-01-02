
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.DFS(root,targetSum)
        return self.count

    def DFS (self,root,targetSum):
        if root is not None:
            self.helperDFS(root,targetSum,0)
            self.DFS(root.left,targetSum)
            self.DFS(root.right,targetSum)
    
    def helperDFS(self,root,targetSum,currSum):
        if root is not None:
            currSum += root.val
        
            if currSum == targetSum:
                self.count+=1
            self.helperDFS(root.left,targetSum,currSum)
            self.helperDFS(root.right,targetSum,currSum)




x = Solution()
root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
print(x.pathSum(root,8))