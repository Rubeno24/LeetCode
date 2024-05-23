public class LeetCode206 {
    // Reverse Linked Lists
    public ListNode reverseList(ListNode head) {
        ListNode prev = null; // Initialize previous node to null

        while (head != null) {
            ListNode temp = head.next; // Temporarily store the next node
            head.next = prev;          // Reverse the current node's pointer
            prev = head;               // Move previous to the current node
            head = temp;               // Move to the next node in the list
        }

        // Return the new head of the reversed list
        return prev;
    }
}
/*
 * Example run through
 * 1->2->3
 * temp=head.next (temp=2)
 * 
 * head.next=prev
 * null<-1 2->3
 * prev=head (prev=1)
 * 
 * head=temp (head=2)
 * ----------------------------------------
 * 1 2->3
 * temp=head.next (temp=3)
 * 
 * head.next=prev
 * 1<-2 3
 * prev=head (prev=2)
 * 
 * head=temp (head=3)
 * ---------------------------------------
 * 1<-2 3
 * temp=head.next (temp=null)
 * 
 * head.next=prev
 * 1<-2<-3
 * prev=head (prev=3)
 * 
 * head=temp (head null)
 * STOP HEAD == NULL
 */