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

        LeetCode2125 x = new LeetCode2125();

        String[] arr = new String[] { "011001", "000000", "010100", "001000" };
        System.out.println(x.numberOfBeams(arr));

    }
}
