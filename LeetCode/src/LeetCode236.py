from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       return self.DFS(root,q,p)
        

    def DFS(self,root: 'TreeNode' , p: 'TreeNode', q: 'TreeNode' ):
        if root is None or root == p or root == q:
            return root
        left = self.DFS(root.left,p,q)
        right = self.DFS(root.right,p,q)
        
        if left and right:
            return root
        
        if left:
            return left
        if right:
            return right
        







data = [3,5,1,6,2,0,8,None,None,7,4]
root = TreeNode.list_to_tree_node(data)
p = root.left
q = root.right

x = Solution()
print(x.lowestCommonAncestor(root,p,q))