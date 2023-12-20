import java.util.Arrays;
import java.util.HashMap;

public class Leetcode169 {
    public int majorityElement(int[] nums) {
        //sorts the array
        mergeSort(nums);

        if (nums.length == 1 || nums.length == 2) {
            return nums[0];
        }
        //we assume the number that appears the most is in the middle so we return that
        return nums[nums.length / 2];
    }
    
    public static void mergeSort(int[] array) {
        if (array.length > 1) {
            // Find the middle of the array
            int mid = array.length / 2;

            // Split the array into two halves
            int[] left = new int[mid];
            System.arraycopy(array, 0, left, 0, mid);

            int[] right = new int[array.length - mid];
            System.arraycopy(array, mid, right, 0, array.length - mid);

            // Recursively sort both halves
            mergeSort(left);
            mergeSort(right);

            // Merge the sorted halves
            merge(array, left, right);
        }
    }

    private static void merge(int[] array, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        // Merge the two sorted arrays into a single sorted array
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                array[k++] = left[i++];
            } else {
                array[k++] = right[j++];
            }
        }

        // Copy the remaining elements of left[], if any
        while (i < left.length) {
            array[k++] = left[i++];
        }

        // Copy the remaining elements of right[], if any
        while (j < right.length) {
            array[k++] = right[j++];
        }
    }
}
