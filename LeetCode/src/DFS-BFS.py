from collections import deque
from TreeNode import TreeNode
class Solution:
    def BFS(self, root):
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            print(node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    

    def DFS(self, root):
        if root is not None:
            print(root)
            self.DFS(root.left)
            self.DFS(root.right)

# Tree structure:
#         1
#        / \
#       2   3
#      / \
#     5   6


x = Solution()
root = TreeNode(1, TreeNode(2 ,TreeNode(5), TreeNode(6)), TreeNode(3))
print("BFS Think Broad")
x.BFS(root)
print ("--------------------------")
print("DFS Think Deep")
x.DFS(root)