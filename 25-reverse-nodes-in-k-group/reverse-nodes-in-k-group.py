# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        # Count total nodes
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        # Process groups of size k
        while count >= k:
            prev = None
            cur = group_prev.next
            tail = cur  # first node of group becomes tail after reversal

            # Reverse k nodes
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Connect reversed group back
            group_prev.next = prev
            tail.next = cur

            # Move to next group
            group_prev = tail
            count -= k

        return dummy.next