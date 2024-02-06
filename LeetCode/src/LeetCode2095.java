public class LeetCode2095 {
    public ListNode deleteMiddle(ListNode head) {
        // Check if the list is null or has fewer than two nodes
        if (head == null || head.next == null) {
            return null;
        }

        ListNode current = head;
        int count = 0;

        // Count the number of nodes in the list
        while (current != null) {
            count++;
            current = current.next;
        }

        // Calculate the index of the middle node
        int middleIndex = count / 2;

        // Reset current to head and move to the node before the middle node
        current = head;
        for (int i = 0; i < middleIndex - 1; i++) {
            current = current.next;
        }

        // Remove the middle node
        current.next = current.next.next;

        return head;
    }
}
// do the slow and fast pointer method later