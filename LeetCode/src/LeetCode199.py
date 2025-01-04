from collections import deque
from  queue import Queue
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        right = []

        while q:
            length = len(q)
            for x in range(length):
                node = q.popleft()

                if x == length-1:
                   right.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return right


data = [1,2,3,None,5,None,4]
root = TreeNode.list_to_tree_node(data)
x = Solution().rightSideView(root)
print(x)