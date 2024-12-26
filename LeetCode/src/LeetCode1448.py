from TreeNode import TreeNode
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if root is None:
            return 0
        self.DFS(root,-10000000)
        return self.count


    def DFS(self,node,maxSeen):
        if node is not None:
            if node.val >= maxSeen:
                self.count += 1
                maxSeen = max(maxSeen,node.val)
            self.DFS(node.left,maxSeen)
            self.DFS(node.right,maxSeen)
                

x = Solution()

root = TreeNode(3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5)))
print(x.goodNodes(root))