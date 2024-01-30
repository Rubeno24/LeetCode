public class LeetCode643 {
    // not done yet only passed 120 test cases
    public double findMaxAverage(int[] nums, int k) {
        int left = 0;
        int sum = 0;
        int maxSum = 0;
        if (nums.length == 1)
            return nums[0];
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            if (right >= k - 1) {
                maxSum = Math.max(sum, maxSum);
                sum -= nums[left];
                left++;
            }
        }

        return (double) maxSum / k;
    }
}
