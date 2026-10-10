
class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node before the head
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both pointers until fast reaches last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        # Return the updated linked list
        return dummy.next
