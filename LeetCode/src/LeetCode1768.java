public class LeetCode1768 {
    public String mergeAlternately(String word1, String word2) {
        /*
         * Using the StringBuilder class since its much more efficient than
         * concatenate 2 string because each time you concat 2 strings together to a new
         * String.
         * A new String is created and the previous Strings are discarded. String
         * Builder using a dynamic array to store the added strings together
         * 
         */
        StringBuilder sb = new StringBuilder();
        // set i=0 to loop through the String since the indexs of strings start at 0
        int i = 0;
        // while loop that will excute as long of these condtions are true. As long as i
        // is less than the lenght of one of the word lengths. Which is what we want
        // since if one string ends we have to add the chars to the end of it
        while (i < word1.length() || i < word2.length()) {
            // if loops check if i is less than the length if the first word
            // if it is we add the current char to the sb variable
            if (i < word1.length()) {
                sb.append(word1.charAt(i));
            }
            // if loops check if i is less than the length if the second word
            // if it is we add the current char to the sb variable
            if (i < word2.length()) {
                sb.append(word2.charAt(i));
            }
            // increment i to keep the loop going
            i++;

        }
        // return sb.toString since the method is of type String
        return sb.toString();
    }

}
