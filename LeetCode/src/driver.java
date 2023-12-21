import java.sql.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import oracle.security.o3logon.a;

class Driver {
    static Statement st;
    static Connection con;
    static Scanner scnr = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        LeetCode1 x = new LeetCode1();
        int arr [] = new int[]{2,7,11,15};
        
        System.out.println(Arrays.toString(x.twoSum(arr, 9)));

        


    }
}
