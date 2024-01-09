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
        int[] arr = new int[1000];
        int[] arr1 = new int[] { 3, 1, 8, 6, 2 };

        Random rand = new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rand.nextInt(100) + 1;

        }
        System.out.println("Before :");
        System.err.println(Arrays.toString(arr1));

        InsertionSort insertionSort = new InsertionSort();
        insertionSort.insertionSort(arr1);

        System.out.println("After :");
        System.err.println(Arrays.toString(arr1));
    }
}