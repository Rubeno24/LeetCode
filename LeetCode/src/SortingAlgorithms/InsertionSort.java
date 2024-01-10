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
            // defining a variable j that is one index behind the array[i]jjj
            int j = i - 1;
            // while will keep going untill j is less than or equal to zero and the array[j]
            // is greater then the current value
            while (j >= 0 && arr[j] > currentValue) {
                // once that is the case we are going to store arr[j] inside of array[j+1]
                // sincekkjjijjkk
                // its greater than the current value. This puts array[j] in the correct order
                arr[j + 1] = arr[j];
                // decrementing j keeps the j pointer going to the end of the array
                j--;
            }
            // we put the currenVal inside arr[j+1] since we decremented j-- so that would
            // be like storing it inside arr[j] to flip the 2 numbers into the correct spot
            arr[j + 1] = currentValue;
        }
    }
}
