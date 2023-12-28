import java.sql.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

class Driver {
    static Statement st;
    static Connection con;
    static Scanner scnr = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        BinaryTree BinaryTree = new BinaryTree();
        BinaryTree.insert(1);
        BinaryTree.insert(2);
        BinaryTree.insert(3);

        BinaryTree.print();

    }
}
