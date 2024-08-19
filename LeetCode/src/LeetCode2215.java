import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class LeetCode2215 {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        //list of lists of integers
        List< List<Integer> > list = new ArrayList<>();
        //2 lists to add to the list of lists of integers
        List<Integer> firstList = new ArrayList<>();
        List<Integer> secondList = new ArrayList<>();

        //2 hashsets that will hold the contents of nums1 and nums2
        HashSet<Integer> setNum1 = new HashSet<>();
        HashSet<Integer> setNum2 = new HashSet<>();

        //enchanced for loops to add the contents of nums1 to setNums1
        for(int element : nums1){
            setNum1.add(element);
        }
        //enchanced for loops to add the contents of nums2 to setNums2
        for(int element: nums2){
            setNum2.add(element);

        }
        //enchanced for loop that checks if the second doesnt have set contains an element from the first set
        for(int element : setNum1){
            if(!setNum2.contains(element)){
                //if it doesnt we add it to the list to add to the list of 2 lists
                firstList.add(element);
            }

        }
        //enchanced for loop that checks if the first set doesnt contains an element fromt the second set
        for(int element :setNum2){
            if(!setNum1.contains(element)){
                //if it doesnt we add it to the list to add to the list of 2 lists
                secondList.add(element);

            }
        }
        //here we add the lists to the lists of lists
        list.add(firstList);
        list.add(secondList);
        return list;
    }
}
