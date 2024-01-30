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
        int[] arr = new int[] { -5, 1, 5, 0, -7 };
        Leetcode1732 x = new Leetcode1732();
        System.out.println(x.largestAltitude(arr));

    }
}