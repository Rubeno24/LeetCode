import java.util.Stack;

public class LeetCode2390 {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '*') {
                stack.push(s.charAt(i));

            } else {
                stack.pop();
            }
        }
        StringBuilder x = new StringBuilder();
        for (int i = 0; i < stack.size(); i++) {
            x.append(stack.get(i));

        }

        return x.toString();
    }
}
