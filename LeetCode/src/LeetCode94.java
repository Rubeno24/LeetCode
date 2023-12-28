import java.util.ArrayList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class LeetCode94 {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1); // Root node with value 1
        TreeNode node2 = new TreeNode(2); // Nodes with values 2 to 6
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);
        TreeNode node6 = new TreeNode(6);

        // Connecting nodes to form the binary tree structure
        root.left = node2; // Attaching left child to the root
        root.right = node3; // Attaching right child to the root

        node2.left = node4; // Attaching left child to node with value 2
        node2.right = node5; // Attaching right child to node with value 2

        node3.left = node6; // Attaching left child to node with value 3

        /*
         * Constructed binary tree:
         * 1
         * / \
         * 2 3
         * / \ \
         * 4 5 6
         */
        System.out.println(inorderTraversal(root));
        ;
    }

    static ArrayList<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<>();
        helper(root, list);

        return list;

    }

    static void helper(TreeNode root, ArrayList<Integer> list) {
        // in order traversal goes far left ,then root, then far right
        if (root != null) {
            helper(root.left, list);
            list.add(root.val);
            helper(root.right, list);
        }

    }
}
