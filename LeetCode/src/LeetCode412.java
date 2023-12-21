import java.util.ArrayList;
import java.util.List;

public class LeetCode412 {
    //fizz buzz
    public List<String> fizzBuzz(int n) {
        //create an arrayList of type String named arr
        ArrayList<String> arr = new ArrayList<>();
        //for loop that starts at 1 and keep going untill its greater than or equal to n
        for (int i = 1; i <= n; i++) {
            //if i is divisible by 3 and 5 evenly add FizzBuzz to the array list
            if (i % 3 == 0 && i % 5 == 0) {
                arr.add("FizzBuzz");
                //if i divisible by 3 evenly add Fizz to the array list 
            } else if (i % 3 == 0) {
                arr.add("Fizz");
                //if i divisible by 5 evenly add Fizz to the array list 
            } else if (i % 5 == 0) {
                arr.add("Buzz");
                //no conditions are true we add the current number i is at to the array list
            } else {
                arr.add(i + "");
            }

        }
        //return the arraylist
        return arr;

    }
}
