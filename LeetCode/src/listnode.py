class ListNode:
    #init method is just the constructor
    def __init__ (self,data):
        self.data = data  # self is the same as this in java
        self.next = None  # Initialize next pointer to None

    def printList(self):
        current = self
        while current is not None:
            print(current.data)
            current=current.next
