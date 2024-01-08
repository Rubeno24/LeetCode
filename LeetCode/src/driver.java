import java.sql.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

class Driver {
    static Statement st;
    static Connection con;
    static Scanner scnr = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int[] arr = new int[100];

        Random rand = new Random();
        for (int i = 0; i < 100; i++) {
            arr[i] = rand.nextInt(100) + 1;

        }

    }
}
