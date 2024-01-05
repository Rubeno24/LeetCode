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

        LeetCode1768 x = new LeetCode1768();
        String word1 = "abc";
        String word2 = "pqr";
        System.out.println(x.mergeAlternately(word1, word2));

    }
}
