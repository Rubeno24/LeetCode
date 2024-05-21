import java.sql.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import SortingAlgorithms.*;

class Driver {
    static Statement st;
    static Connection con;
    static Scanner scnr = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
    TreeNode head = new TreeNode(3);
    TreeNode lefTreeNode = new TreeNode(9);
    TreeNode rightTreeNode = new TreeNode(20);
    
    head.left=lefTreeNode;
    head.right=rightTreeNode;

    TreeNode rightRighTreeNode = new TreeNode(15);
    TreeNode leftLefTreeNode = new TreeNode(7);

    rightRighTreeNode.left=leftLefTreeNode;
    rightTreeNode.right=rightRighTreeNode;

    //head.printTree(head);
    System.out.println(head.maxDepth(head));
    
    

    }
}