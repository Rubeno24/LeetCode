public class LeetCode643 {
    public double findMaxAverage(int[] nums, int k) {
        // create left pointer
        int left = 0;
        // set max variable to 0 since we dont have a max yet
        int max = 0;
        // set sum to zero since we dont have a sum yet
        int sum = 0;
        // iterate over nums array with right pointer
        // both left and right pointer start at 0 , the for loop increments the right
        // pointer by 1 everytime
        for (int right = 0; right < nums.length; right++) {
            // add value to sum on each iteration
            sum += nums[right];
            // if right is greater or equal to k then that is our window
            if (right >= k - 1) {
                // compare sum vs the max and assign that to new max
                max = Math.max(sum, max);
                // subtract left most value from sum since we are moving our window over to the
                // left
                sum -= nums[left];
                // move the left pointer over by 1 to the right
                left++;
            }
        }
        // convert max value to double before divise it by k
        return (double) max / k;
    }
}
