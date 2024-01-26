public class LeetCode643 {
    public double findMaxAverage(int[] nums, int k) {
        int left = 0;
        int sum = 0;
        int maxSum = 0;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            if (right - left + 1 >= k) {
                maxSum = Math.max(sum, maxSum);
                sum -= nums[left];
                left++;
            }
        }
        maxSum = Math.max(sum, maxSum);

        return (double) maxSum / k;
    }
}
