import java.util.HashSet;
import java.util.Set;

public class LeetCode3 {
    public int lengthOfLongestSubstring(String s) {

        // sliding window appraoch 2 pointers right and left. We loop using r
        // Use a hashset since it cant have dupes
        HashSet<Character> set = new HashSet<>();
        int left = 0, maxLength = 0;
        int stringLength = s.length();
        // start at 0 untill r is not less than the length of the string
        for (int right = 0; right < stringLength; right++) {
            if (!set.contains(s.charAt(right))) { // set doesnt have the current character then its unique add to set
                set.add(s.charAt(right));
                maxLength = Math.max(maxLength, right - left + 1);// we either return the max length or right-left plus
                                                                  // 1 since it starts at 0
            } 
            //this case executes if the char is already in the set 
            else {
                //if the char is in the set move the left pointer to the right so the char is not in the set
                while (set.contains(s.charAt(right))) {
                    set.remove(s.charAt(left));
                    left++;
                }
                //then add the duplicated char to the set, its not duped since the pointer was moved and removed
                set.add(s.charAt(right));

            }
        }
        //return the maxlength or right-left +1 since it starts at 0
        return maxLength;

    }

}
