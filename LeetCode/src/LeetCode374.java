public class LeetCode374 {
    public int guessNumber(int n) {
        int start=1;
        int end =n;

        while(start<=end){
            int middle = (start+n)/2;
            if(guess(middle==0)){
                return middle;
            }
            else if(guess(middle)==1){
                start=middle+1;
            }
            else if(guess(middle)==-1){
                end=middle-1
                
            }


        }

        return 0;
        
    }

   
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

}