package SortingAlgorithms;

public class BinarySearch {
    public int Binary_Search(int[] array, int target){
        int start = 0;
        int end = array.length-1;

        while(start<=end){
        int middle = (start+end)/2;
        if(array[middle]==target)
        return middle;

        if(array[middle]<target){
            start=middle+1;
        }

        if(array[middle]>target){
            end=middle-1;
        }

        }
        return 0;

    }
    
    
}
