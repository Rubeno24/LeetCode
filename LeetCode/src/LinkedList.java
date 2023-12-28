import java.util.List;

public class LinkedList {
    private ListNode head;
    private int size;

    public LinkedList() {
        head = null;
    }

    public void add(int num) {
        ListNode newNode = new ListNode(num);
        if (head == null) {
            // If the list is empty, set the new node as the head
            head = newNode;
            size++;
        } else {
            // Traverse to the end of the list and add the new node
            ListNode current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
            size++;
        }

    }

    public void add(int num, int index) {
        ListNode newNode = new ListNode(num);
        if (index < 0) {
            System.out.println("Index cannot be less than 0");
            return;
        }
        if (index == 0) {
            newNode.next = head;
            head = newNode;
            size++;
            return;
        }

        ListNode current = head;
        for (int i = 0; i < index - 1 && current != null; i++) {
            current = current.next;
        }

        if (current == null) {
            // Handle invalid index (index greater than or equal to the list size)
            System.out.println("Invalid index");
            return;
        }
        newNode.next = current.next;
        current.next = newNode;
        size++;
    }

    public int peek() {

        if (head != null)
            return head.val;

        return -1; // Safe return!

    }

    public void remove() {
        if (head == null || head.next == null) {
            // List is empty or contains only one node (head node)
            head = null;
            return;
        }
        ListNode curr = head;
        ListNode prev = null;
        while (curr.next != null) {
            prev = curr;
            curr = curr.next;
        }
        prev.next = null;

    }

    public void remove(int index) {
        if (index >= size || index < 0) {
            System.out.println("Invalid Index");
            return;
        }
        if (index == 0) {
            head = head.next;
        } else {
            ListNode curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr.next;
            }
            curr.next = curr.next.next;
        }
        size--;
    }

    public int size() {
        return size;
    }

    public int get(int index) {
        ListNode curr = head;
        if (index > size || index < 0) {
            System.out.println("Invalid Index");
            return -1;

        }
        for (int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr.val;

    }

    public boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }

    public boolean contains(int val) {
        for (int i = 0; i < size; i++) {
            if (get(i) == val) {
                return true;
            }

        }
        return false;
    }

    public void print() {
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
    }

}
