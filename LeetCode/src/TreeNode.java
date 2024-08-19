import java.util.Stack;

public class TreeNode {
    int data;
    TreeNode left;
    TreeNode right;

    public TreeNode(int data) {
        this.data = data;
    }
    public TreeNode(int data, TreeNode left, TreeNode right){
        this.data=data;
        this.left=left;
        this.right=right;
    }
    public void printTree(TreeNode node) {
        if (node == null) {
            return;
        }
    
        Stack<TreeNode> stack = new Stack<>();
        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
    
            node = stack.pop();
            System.out.println(node.data);
    
            node = node.right;
        }
    }
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int maxLeft = maxDepth(root.left);
        int maxRight = maxDepth(root.right);
        return Math.max(maxLeft, maxRight) + 1;
    }
}
