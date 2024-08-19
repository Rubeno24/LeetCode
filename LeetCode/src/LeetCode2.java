public class LeetCode2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // head node that we will return
        // current points to the same place in memory as head
        // carry varibale stores a 1 if the sum of 2 numbers is greater than 10
        ListNode head = new ListNode(0);
        ListNode current = head;
        int carry = 0;

        // while loops keeps going if any of these condtions are true
        // if l1 or l2 not null or if carry is 1 since we cant leave a carry unattended
        // to
        while (l1 != null || l2 != null || carry == 1) {
            // sum will be set to 0 every new itteration of the while loop which is what we
            // want
            // since after we add one number we want to move on to the next
            int sum = 0;
            // if list1 is not null we add its current value to sum and move on to the next
            // node
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;

            }
            // if list2 is not null we add its current value to sum and move on to the next
            // node
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            // add sum to carry even if there is not a carry just in case when there is a
            // carry
            sum += carry;
            // find the carry by dividing sum by 10
            // example 17/10 is 1.7 or just 1 in integer division
            carry = sum / 10;
            // create a new node that will be added to our list that we be returned
            // we modulus sum by 10 to only get the last digit
            // example 12%10 =2
            ListNode temp = new ListNode(sum % 10);
            // link current to the new node we made
            current.next = temp;
            // move current to the next position
            current = current.next;

        }
        return head;
    }
}
