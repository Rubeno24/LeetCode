from typing import Optional
from listnode import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        seen = set()
        while current and current.next:
            seen.add(current.val)
            if current.next.val in seen:
                current.next = current.next.next
            current = current.next
        return head

head = ListNode(1, ListNode(1, ListNode(2, None)))
newhead = x = Solution().deleteDuplicates(head)
newhead.printList()