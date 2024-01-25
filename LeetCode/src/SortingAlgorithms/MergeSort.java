package SortingAlgorithms;

public class MergeSort {
    public void mergeSort(int[] arr) {
        int length = arr.length;
        if (length < 2) {
            return;
        }
        int midIndex = length / 2;
        int[] leftHalf = new int[midIndex];
        int[] rightHalf = new int[length - midIndex];

        for (int i = 0; i < midIndex; i++) {
            leftHalf[i] = arr[i];
        }
        for (int i = midIndex; i < length; i++) {
            rightHalf[i - midIndex] = arr[i];
        }

        mergeSort(leftHalf);
        mergeSort(rightHalf);
        merge(arr, leftHalf, rightHalf);

    }

    public void merge(int[] arr, int[] leftHalf, int[] rightHalf) {
        int leftSize = leftHalf.length;
        int rightSize = rightHalf.length;

        int i = 0, j = 0, k = 0;

        while (i < leftSize && j < rightSize) {
            if (leftHalf[i] <= rightHalf[j]) {
                arr[k] = leftHalf[i];
                i++;
            }

            else {
                arr[k] = rightHalf[j];
                j++;
            }
            k++;
        }
        while (i < leftSize) {
            arr[k] = leftHalf[i];
            i++;
            k++;

        }
        while (j < rightSize) {
            arr[k] = rightHalf[j];
            j++;
            k++;

        }

    }
}
