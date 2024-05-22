public class LeetCode338 {
    public int[] countBits(int n) {
        //array of n+1 size since thats all we need to hold all the numbers
        int arr[] = new int[n+1];
        //loop through n which is the number the user entered
        for(int i=0; i<=n;i++){
            //store the number of 1s in the current itteration of n we are at
            int count=0;
            //temp variable to keep shifting to the right untill its less than 0
            int temp=i;
            //while loop keeps going untill temp is less than 0
            while(temp>0){
                //checks if the right most digit is set or is a 1 and then it checks if it equals 1 if so we increment count by 1
                if((temp&1)==1){
                    count++;
                }
                //we then shift temp by 1 which divides it by 2
                temp>>=1;
            }
            //once temp is less than 0 we insert count to i
            arr[i]=count;
            
        }
        //we return the array
        return arr;
    }
    


    //dynamic programming example
    /* 
    public int[] countBits(int n) {
        int arr [] = new int[n+1];
        for(int i =0;i<=n;i++){
            //use prior iterations of the for loop to find the answer then adds i modulos 2 to the answer if its even
            arr[i]=arr[i>>1]+ (i%2);
        }
        return arr;
        }
        */
}
