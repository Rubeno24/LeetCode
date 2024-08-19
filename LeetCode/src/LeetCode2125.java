public class LeetCode2125 {
    public int numberOfBeams(String[] bank) {
        // variable named rows = to the lenght of the array since that how many rows it
        // will have
        int rows = bank.length;
        // varibale named columns will be equal to the length of each string since its a
        // matrix and the rows are the same length
        int columns = bank[0].length();
        // variables answer and previous will be used later
        int answer = 0;
        int previous = 0;
        // variable current is not initialized since will be resetting it to 0 in the
        // first for loop
        int current;
        // first for loop ,loops through the length of the array simulating the rows of
        // a matrix
        for (int i = 0; i < rows; i++) {
            // current will be set to 0 after each iteration of the for loop simulating
            // moving to a diffrent row
            current = 0;
            // second for loop, loops throught the length of each string
            for (int j = 0; j < columns; j++) {
                // checks if the current char at the current row is equal to 1
                if (bank[i].charAt(j) == '1') {
                    // if so we increment current by 1
                    current++;
                }
            }
            // checks to see if there any 1s in the current row
            if (current != 0) {
                // if so we multiply current which is the current row * the previous which is
                // the previous row. To find how many lasers there we just muliply the the
                // number of secutiy devices in each of the rows, then we add that result to
                // answer
                answer = answer + (current * previous);
                // set the current row equal to previous to use later and because current is
                // going to move on to the next row
                previous = current;
            }
        }
        // return answers which is the security devices of the rows mulitplied by the
        // security devices of the other rows and added to answer
        return answer;

    }
}
