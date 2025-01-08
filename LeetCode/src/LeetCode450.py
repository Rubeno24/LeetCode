from typing import Optional

from TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        if root.val == key: #key found
            #root is a leaf return none cut the branch
            if root.right is None and root.left is None:
                return None
            
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has two children
            successor = self.findMin(root.right)
            root.val = successor.val
            # Delete the successor
            root.right = self.deleteNode(root.right, successor.val)
    
        return root

    def findMin(self,node):
        while node.left:
            node = node.left
        return node

    


data = [5,3,6,2,4,None,7]
root = TreeNode().list_to_tree_node(data)
x = Solution().deleteNode(root,3)
print(x)