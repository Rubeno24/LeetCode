package SortingAlgorithms;

import java.util.Random;

public class QuickSort {
    public void quickSort(int[] arr, int lowIndex, int highIndex) {
        // base case if lowindex is less then or equal to highIndex, that means the
        // array has 1 or 0 elements which cant be sorted
        if (lowIndex >= highIndex)
            return;
        // if you want to pick random index
        /*
         * int pivotIndex = new Random().nextInt(highIndex - lowIndex) + lowIndex;
         * int pivot = arr[pivotIndex];
         * swap(arr, pivotIndex, highIndex);
         */
        // pick a pivot in this case we are using the element at the end of the array
        int pivot = arr[highIndex];
        // a left pointer which points to the first index in the array
        int left = lowIndex;
        // right pointer which points to the last index of the array
        int right = highIndex;

        // while loop keeps going unitl the left and right pointer intersect each other
        while (left < right) {
            // inner while loop keeps going unitl the left pointer is at a location where it
            // is greater or equal to the pivot
            while (arr[left] <= pivot && left < right) {
                // move left until left pointer unitl it is at a number greater than the pivot
                left++;
            }

            // inner while loop keeps going unitl the right pointer is at a location where
            // is greater or equal to the pivot
            while (arr[right] >= pivot && left < right) {
                // move right until the right pointer is at a number less then the pivot
                right--;
            }
            // swaps the left and right pointer with each other
            swap(arr, left, right);

        }
        // swaps the current pivot with the left pointer
        swap(arr, left, highIndex);
        // then recursively call the quicksort method on the left side of pivot
        // example 1,5,3,4,7,8,9
        // p
        // so recursively call the quicksort method on the left side of the pivot by
        // passing in lowindex as the lowindex since that doesnt change and left -1 as
        // the element to the left of the pivot because left points to the pivot
        quickSort(arr, lowIndex, left - 1);
        // quicksort the right side of the pivot by passing in left+1 as the lowIndex
        // since left points
        // to the same location as the pivot and pass in highIndex as the highIndex
        // since that doesnt change
        quickSort(arr, left + 1, highIndex);

    }

    // helper method that swaps 2 numbers in an array
    private static void swap(int[] arr, int index1, int index2) {
        // temp variable that holds a value in the array
        int temp = arr[index1];
        // override the number in the array we stored in temp with a diffrent value
        arr[index1] = arr[index2];
        // overide the second array with the temp value from the first array
        arr[index2] = temp;

    }

    // overriden method that allows the user to pass in just the array and we pass
    // in the low and high index in this method
    public void quickSort(int[] arr) {

        quickSort(arr, 0, arr.length - 1);
    }

}
