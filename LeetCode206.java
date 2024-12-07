import java.util.List;

public class LeetCode206 {
    public ListNode reverseList(ListNode head) {
        ListNode reverseHead = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = reverseHead;
            reverseHead = head;
            head = temp;
        }
        return reverseHead;
    }
}
