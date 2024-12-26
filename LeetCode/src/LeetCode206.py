from typing import Optional
from listnode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
            



x = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, None)))))
newHead = x.reverseList(head)
newHead.printList()