public class LeetCode70 {
    public int climbStairs(int n) {

        int first = 1;
        int last = 1;
        int answer = 0;
        // covers when n is less then or equal to 1, so in this case 1 or 0
        // it returns n because if n is 1 there is only one way to get to the first
        // stair
        // if n = 0 there are no ways to go up 0 stairs
        if (n <= 1) {
            return n;
        }

        // start i=2 since base cases are handled in the if loop
        // stop when i is less than or equal to n
        for (int i = 2; i <= n; i++) {
            // set answer equal to first + last
            // set answer to last to keep first moving along
            // set last to answer to keep last moving along
            answer = first + last;
            first = last;
            last = answer;

        }
        // return answer which has the number we want
        return answer;

    }
}
