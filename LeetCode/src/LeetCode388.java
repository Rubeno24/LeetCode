public class LeetCode388 {
    public int[] countBits(int n) {
        int[] arr = new int[100000];
        for (int i = 0; i < n; i++) {
            int count = n;
            while (count >= 0) {
                arr[i] = n >> 1;

            }

        }
        return arr;

    }

}
