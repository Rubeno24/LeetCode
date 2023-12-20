import java.util.ArrayList;
//Find the Index of the First Occurrence in a String
public class LeetCode28 {
    public int strStr(String haystack, String needle) {
        int index = 0;
        for(int i =0; i<haystack.length();i++){
            if(haystack.charAt(i)==needle.charAt(index)){
                index++;
            }
            else{
                i=i-index;
                index=0;

            }
            if(index==needle.length()){
                return i-needle.length()+1;

            }
        }
        return -1;
    }

}
