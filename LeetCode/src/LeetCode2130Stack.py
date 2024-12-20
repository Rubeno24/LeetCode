from typing import Optional
from listnode import ListNode

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        maxSum = 0
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while slow:
            maxSum = max(stack.pop()+slow.val, maxSum)
            slow = slow.next
        return maxSum
        
        
        
        
        
head = ListNode(5, ListNode(4, ListNode(2, ListNode(1,None ))))
x = Solution()
print(x.pairSum(head))