public class LeetCode237 {
    public void deleteNode(ListNode node) {
        //example linked list given
        //4->5->1->9
        //want to remove the node with the value 5
        node.val=node.next.val;
        //set the node with the value 5 to the next node which is 1
        //4->1->1->9
        //now we are looking at the next node which is the 3rd node in the linked list
        //we want to third node = to the foruth node
        //we call node.next which is the next node after our given node and that points to node.next.next 
        //which skips the middle node between our node and the next.next node
        node.next= node.next.next;

        
    }
}
