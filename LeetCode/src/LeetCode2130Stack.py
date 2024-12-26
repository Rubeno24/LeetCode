from typing import Optional
from listnode import ListNode

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        stack = []
        maxSum = 0

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while slow is not None:
            maxSum = max(maxSum,stack.pop()+slow.val)
            slow = slow.next
        return maxSum


        
head = ListNode(5, ListNode(4, ListNode(2, ListNode(1,None ))))
x = Solution()
print(x.pairSum(head))