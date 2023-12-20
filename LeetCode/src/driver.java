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
        LeetCode237 x = new LeetCode237();
    
        ListNode first = new ListNode(4);
         ListNode second = new ListNode(5);
          ListNode third = new ListNode(1);
           ListNode last = new ListNode(9);

       
        first.next=second;
        first.next.next=third;
        first.next.next.next=last;
        
  
        x.deleteNode(third);
        first.print(first);
        

      
    }
}

