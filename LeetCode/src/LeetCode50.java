public class LeetCode50 {
    public double myPow(double x, int n) {
        // varible will be retuned and be x^n
        double answer = 1;
        // check if n less than 0
        // if so make n postive and set x = to is reciprical so x=1/x
        if (n < 0) {
            n = -n;
            x = 1 / x;
        }

        // keep looping unitl n=0
        while (n != 0) {
            // if the last significant bit of n =1 go into if loop
            if ((n & 1) != 0) {
                answer *= x;
            }
            // reguardless of least significant bit multply x=x*x
            x *= x;
            // shifts n over to the right by one
            // Example n = 011
            // Shifted n= 01
            n >>= 1;
            // loop ends when n has been shifted over enought that it is 0
        }
        // return answer which is x^n
        return answer;
    }

}
