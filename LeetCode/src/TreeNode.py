from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if not self:
            return "Empty tree"

        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        return " -> ".join(result)
    

    @classmethod
    def list_to_tree_node(cls,data):
        if not data or data[0] is None:
            return None

    # Create the root of the tree
        root = TreeNode(data[0])
        queue = deque([root])
        i = 1

    # Use a queue to keep track of nodes while building the tree
        while queue and i < len(data):
            current = queue.popleft()

        # Add left child
            if i < len(data) and data[i] is not None:
                current.left = TreeNode(data[i])
                queue.append(current.left)
            i += 1

        # Add right child
            if i < len(data) and data[i] is not None:
                current.right = TreeNode(data[i])
                queue.append(current.right)
            i += 1

        return root
