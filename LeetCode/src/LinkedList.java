import java.util.List;

public class LinkedList {
    private ListNode head;
    private int index;

    public LinkedList() {
        head = null;
    }

    public void add(int num){
        ListNode newNode = new ListNode(num);
        if (head == null) {
            // If the list is empty, set the new node as the head
            head = newNode;
        } else {
            // Traverse to the end of the list and add the new node
            ListNode current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        
    }

    public void add(int num, int index){
        ListNode nodeToAdd = new ListNode(num);
        if(index<0){
            System.out.println("Index cannot be less than 0");
            return;
        }
        if(index==0){
            nodeToAdd.next =head;
            head=nodeToAdd;
            return;
        }


        ListNode current = head;
        for (int i = 0; i < index - 1 && current != null; i++) {
            current = current.next;
        }
    
        if (current == null) {
            // Handle invalid index (index greater than or equal to the list size)
            System.out.println("Invalid index");
            return;
        }
    }

    public void print(){
       ListNode curr=head;
        while(curr!=null){
            System.out.print(curr.val+" ");
            curr=curr.next;
        }
    }
    
}
