public class LeetCode206 {
    // Reverse Linked Lists
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

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