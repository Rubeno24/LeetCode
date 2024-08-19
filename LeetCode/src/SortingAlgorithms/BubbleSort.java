package SortingAlgorithms;

public class BubbleSort {
    public void bubbleSort(int[] arr) {
        // boolean variable that keeps the loop going if is true, we keep it true to
        // enter the while loop
        boolean swappedSomething = true;
        // while loop keeps going when elements are swapped which means the array is not
        // sorted yet
        while (swappedSomething == true) {
            // we set the swappedSomething variable to false and it will be changed to true
            // only if something is swapped meaning that they array is not fully sorted
            swappedSomething = false;
            // we itterate through the array and stop and the second to last elemenet
            // because there is not element to compare after it
            for (int i = 0; i < arr.length - 1; i++) {
                // We check if arr[i] is greater than arr[i+1], if that is the case then we swap
                // the 2 elements
                if (arr[i] > arr[i + 1]) {
                    // we set the swappedSomething variable to true since we are swapping something
                    // and so we can go back into the while loop
                    swappedSomething = true;
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;

                }

            }

        }
    }
}