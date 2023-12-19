import java.sql.*;
import java.util.InputMismatchException;
import java.util.Scanner;

class Driver {
    static Statement st;
    static Connection con;
    static Scanner scnr = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        LeetCode11 x = new LeetCode11();
        int arr []  = new int[]{1,8,6,2,5,4,8,3,9};
        System.out.println(x.maxArea(arr));
        x.maxArea(arr);
        

        
    }

}