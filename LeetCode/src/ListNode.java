public class ListNode {

    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
    ListNode(int val, ListNode next) {
         this.val = val; 
         this.next = next; 
        
        }

    public void print(ListNode x){
        ListNode curr=x;
        while(curr!=null){
            System.out.print(curr.val+" ");
            curr=curr.next;
        }
    }
}
