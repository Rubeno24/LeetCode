import java.util.HashMap;

public class Leetcode169 {
    //Majority Element
    public int majorityElement(int[] nums) {
        /*
         * simpler solution
         * 
         * Arrays.sort(nums);
         * 
         * if (nums.length==1 || nums.length==2){
         * return nums[0];
         * }
         * return nums[nums.length/2];
         * }
         */

        int maxCount = 0;
        int majorityElement = 0;
        // hashmap with key value pair as 2 ints
        HashMap<Integer, Integer> map = new HashMap<>();
        // for loop to store every element in the array into our hashmap
        for (int key : nums) {
            // adds the key to the hashmpa and uses the getOrDefault method to get the value
            // associated
            // with the key, if no value is there then the default value is 0.
            // if the value is there then we increment it by 1
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        // using a for loop to itterate through the hashmap
        for (int key : map.keySet()) {
            // if statement to check if value is greater then maxCount
            if (map.get(key) > maxCount) {
                // it is we assign max count with that value
                maxCount = map.get(key);
                // majorityElement will be set equal to the key which is the number and the
                // value is
                // how many times is occurs
                majorityElement = key;

            }

        }
        // we return the key which is the number that occurs the most
        return majorityElement;

    }

}
