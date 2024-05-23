import java.util.ArrayList;
import java.util.Arrays;

class main{
    public static void main(String[] args) throws Exception {
        LeetCode2215 x = new LeetCode2215();
        int[] list1 = new int[]{1,2,3,3};
        int[] list2 = new int[]{1,1,2,2 };


        ArrayList done =(ArrayList) x.findDifference(list1, list2);
        System.out.println(done.toString());
    
        }
}