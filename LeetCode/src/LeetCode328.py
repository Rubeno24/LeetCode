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
        evenOldHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenOldHead
        return head

    
# create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

# delete the middle node and print the resulting list
new_head = head.deleteMiddle(head)
print(new_head)