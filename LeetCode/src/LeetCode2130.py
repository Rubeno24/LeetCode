from typing import Optional
from listnode import ListNode

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
 
        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp 

        maxSum = 0
        first, second = head, prev
        while second:
            maxSum = max(maxSum, first.val+second.val)
            first = first.next
            second = second.next
        return maxSum

head = ListNode(5, ListNode(4, ListNode(2, ListNode(1,None ))))
x = Solution()
print(x.pairSum(head))