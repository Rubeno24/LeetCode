from collections import deque
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafArray1 = []
        leafArray2 = []
        self.dfs(root1,leafArray1)
        self.dfs(root2,leafArray2)
        return leafArray1 == leafArray2

            
    def dfs(self,root,leafArray):
        if root is not None:
            if root.left is None and root.right is None:
                leafArray.append(root.val)   
            self.dfs(root.left,leafArray)
            self.dfs(root.right,leafArray)


    def BFS(self, head):
        if not head:
            return []
        result = []
        queue = deque([head])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    

    

simpleRoot = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))

root1 = TreeNode(3, left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))), right=TreeNode(1, left=TreeNode(9), right=TreeNode(8)))
root2 = TreeNode(3, left=TreeNode(5, left=TreeNode(6), right=TreeNode(7)), right=TreeNode(1, left=TreeNode(4), right=TreeNode(2, left=TreeNode(9), right=TreeNode(8))))

x = Solution()
print(x.leafSimilar(root1,root2))