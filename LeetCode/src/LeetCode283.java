
public class LeetCode283 {

    public void moveZeroes(int[] nums) {

        // 2 pointer approach left pointer starts at the first index and right pointer
        // starts at the second index
        int left = 0;
        int right = 1;
        int temp = 0;
        // base case when the length of the array = 1 or less we return
        if (nums.length == 0 || nums.length == 1) {
            return;

        }
        // Left pointer looks for 0 numbers
        // Right pointer looks for non 0 numbers

        // keeps looping while the right pointer is less than the lenght of the array
        while (right < nums.length) {
            // if left pointer is not zero then move the left and right pointer over 1, but
            // if it is 0 then go to else if loop to find when right is non zero
            if (nums[left] != 0) {
                // moves left and right if left not equal to zero
                left++;
                right++;
                // if right pointer == 0 then move over the right pointer until its a non zero
                // number than the else statement will be executed
            } else if (nums[right] == 0) {

                right++;
                // else statement is executed when left =0 and right is non 0
            } else {
                // switches the numbers at the left and right pointers
                temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }

        }
        /*
         * // base case when length is 1 or 0
         * if (nums.length <= 1) {
         * return;
         * }
         * 
         * // variable named nonZeroIndex since the nonzero elements will be stored at
         * // the front of the array
         * int nonZeroIndex = 0;
         * 
         * 
         * // loops through the array
         * for (int i = 0; i < nums.length; i++) {
         * // checks if the number at i is not 0, if its not swap it with the
         * // nonZeroIndex that starts at the beggining since we want to move non zeros
         * to
         * // the front
         * if (nums[i] != 0) {
         * // Just does the swapping
         * int temp = nums[i];
         * nums[i] = nums[nonZeroIndex];
         * nums[nonZeroIndex] = temp;
         * //increment nonZeroIndex to the next nonZeroIndex
         * nonZeroIndex++;
         * }
         * }
         * }
         * 
         */

    }
}