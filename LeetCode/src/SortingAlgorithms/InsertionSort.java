package SortingAlgorithms;

public class InsertionSort {
    public void insertionSort(int[] arr) {
        // variable that will hold the current value of the array
        int currentValue = 0;
        // loop that will iterate through the array but starts at one because we can say
        // that the first element is sorted with itself
        for (int i = 1; i < arr.length; i++) {
            // assigns the current value of the array at i the the current val variable
            currentValue = arr[i];
            // defining a variable j that is one index behind the array[i]
            int j = i - 1;
            // while will keep going untill j is less than or equal to zero and the array[j]
            // is greater then the current value
            while (j >= 0 && arr[j] > currentValue) {
                // once that is the case we are going to store arr[j] inside of array[j+1] since
                // its greater than the current value. This puts array[j] in the correct order
                arr[j + 1] = arr[j];
                // decrementing j keeps the j pointer going to the end of the array
                j--;
            }
            // we put the current which is the smallest number at j+1 since j=i-1 so that
            // would be -1 so we add 1 to j to make it 0 the start of the array.
            arr[j + 1] = currentValue;
        }
    }
}
