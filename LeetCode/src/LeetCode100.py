from typing import Optional
from TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
 
        list1 = []
        list2 = []
        return self.DFS(p,list1) == self.DFS(q,list2)
        
    def DFS(self,root,list):
        if root is None:
            list.append(None)
            return
        list.append(root.val)
        self.DFS(root.left,list)
        self.DFS(root.right,list)

data1 = [1,2,3]
data2 = [1,2,5]
p = TreeNode().list_to_tree_node(data1)
q = TreeNode().list_to_tree_node(data2)
x = Solution().isSameTree(p,q)
print(x)