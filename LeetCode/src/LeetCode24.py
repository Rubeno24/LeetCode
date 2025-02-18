from typing import Optional

from listnode import ListNode


class Solution:
    def swapPairs(self , head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next 
        while head and head.next:
            next_pair = head.next.next  
            second = head.next

            second.next = head
            head.next = next_pair

            if prev is not None:
                prev.next = second

            prev = head
            head = next_pair

        return new_head







head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))


x = Solution().swapPairs(head)
printNode = x
printNode.printList()