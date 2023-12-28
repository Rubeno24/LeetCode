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
        LinkedList x = new LinkedList();
        x.add(0);
        x.add(1);
        x.add(2);
        x.remove();
        x.remove();
        x.remove();
        x.add(2);
        x.print();

        ;

    }
}
