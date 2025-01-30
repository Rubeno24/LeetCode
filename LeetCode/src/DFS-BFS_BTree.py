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

    

    def dfs(self, root, current_sum=0):
        if root is None:
            return []

        current_sum += root.val

    # if it's a leaf node, return the current path sum
        if root.left is None and root.right is None:
            return [current_sum]

    # recursively calculate the sum for left and right subtrees
        left_sums = self.dfs(root.left, current_sum)
        right_sums = self.dfs(root.right, current_sum)

        return left_sums + right_sums


# Tree structure:
#         1
#        / \
#       2   3
#      / \
#     5   6


x = Solution()
root = [1,0,1,0,1,0,1]
root = TreeNode(1, TreeNode(2 ,TreeNode(5), TreeNode(6)), TreeNode(3))
print("BFS Think Broad")
x.BFS(root)
print ("--------------------------")
print("DFS Think Deep")
print(x.dfs(root))