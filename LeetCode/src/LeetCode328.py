from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"Node(val: {self.val}, ---> {self.next})"


    def deleteMiddle(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        #keep track of the start of even node
        evenOldHead = even
        #Keeps going untill the even node is null or even.next in null
        while even and even.next:
            #moves odd to right of even
            odd.next = even.next
            #moves odd to the next node that odd is pointing to
            odd = odd.next

            even.next = odd.next
            even = even.next
        #links odd nodes to the head of even nodes
        odd.next = evenOldHead
        #head is pointing to the beggining of odd so return this to get the list in order
        return head

    
# create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

# delete the middle node and print the resulting list
new_head = head.deleteMiddle(head)
print(new_head)