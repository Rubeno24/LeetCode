
//Container With the Most Water
public class LeetCode11 {
    public int maxArea(int[] height) {
        int first = 0;
        int last = height.length - 1;
        int maxArea = 0;

        while (first < last) {
            if (height[first] < height[last]) {
                maxArea = Math.max(maxArea, height[first] * (last - first));
                first++;
            } else {
                maxArea = Math.max(maxArea, height[last] * (last - first));
                last--;
            }
        }

        return maxArea;
    }
}
