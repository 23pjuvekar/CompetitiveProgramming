# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse from left to right
        curr = prev.next
        prev_sublist = None
        tail = curr
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev_sublist
            prev_sublist = curr
            curr = temp

        # Step 3: reconnect
        prev.next = prev_sublist
        tail.next = curr

        return dummy.next
