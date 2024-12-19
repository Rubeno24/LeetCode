class ListNode:
    #init method is just the constructor
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def printList(self):
        current = self
        while current is not None:
            print(f"{current.val} --> ", end="")  # Print the value followed by an arrow
            current=current.next
