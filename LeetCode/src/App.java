import java.sql.Array;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class App {
    public static void main(String[] args) throws Exception {

        int[] intArray = new int[] {4,3,2,1};
        
       // System.out.println(Arrays.toString((sort(intArray))));

        LeetCode58 x = new LeetCode58();
       
        System.out.println( x.lengthOfLastWord("   fly me   to   the moon  "));
        
    }


   
}
