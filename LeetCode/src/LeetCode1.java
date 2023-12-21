import java.util.HashMap;
import java.util.Map;

public class LeetCode1 {
    public int[] twoSum(int[] nums, int target) {
        //n is the lenght of the array nums
        int n = nums.length;
        //HashMap where key value pairs are both ints
        Map<Integer, Integer> map = new HashMap<>();
        //Key= the numbers in the array, Values = the indices in the array
        //array of 2 index since we only have to return 2 values
        int[] result = new int[2];
        //loop through the length of the array
        for (int i = 0; i < n; i++) {
            // if the hashmap has the key that is target - nums[i]
            if (map.containsKey(target - nums[i])) {
                //result[1] will be equal to i which is the index
                result[1] = i;
                //result[0] will be equal to the value that the key target-nums[i] gives
                result[0] = map.get(target - nums[i]);
                break;
            }
            //map doesnt contain the key we add nums[i] to the map which is the value
            //also add the value which is the index in this case
            map.put(nums[i], i);
        }
        return result;
    }

}
/*
    Brute force way
 * public int[] twoSum(int[] nums, int target) {
 * int arr []= new int[2];
 * for(int i=0; i<nums.length;i++){
 * for(int j=i+1;j<nums.length;j++){
 * if(nums[i]+nums[j]==target){
 * arr[0]=i;
 * arr[1]=j;
 * }
 * }
 * }
 * return arr;
 * 
 * }
 */