public class LeetCode50 {
    public double myPow(double x, int n) {
        double answer = 1;
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }
        if (n > 1) {
            for (int i = 0; i < n; i++) {
                answer *= x;
            }
        } else if (n < 0) {
            for (int i = 0; i > n; i--) {
                answer /= x;
            }

        }
        return answer;
        // not right answer

    }
}
