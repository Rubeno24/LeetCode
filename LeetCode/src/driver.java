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
        int[] arr = new int[] { 0, 1, 0, 3, 12 };

        LeetCode283 x = new LeetCode283();
        x.moveZeroes(arr);
        System.out.println(Arrays.toString(arr));

    }
}
