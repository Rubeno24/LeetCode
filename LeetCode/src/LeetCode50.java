public class LeetCode50 {
    public double myPow(double x, int n) {
        double answer =1;
        if(n < 0){
            n = -n;
            x = 1 / x;
        }

        
        
        while(n != 0){
            if((n & 1) != 0){
                answer *= x;
            } 
                
            x *= x;
            n >>= 1;
            
        }
        
        return answer;
    }
        

    
}
