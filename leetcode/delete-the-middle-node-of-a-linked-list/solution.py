# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        f = head
        s = head
        prev = None
        while f and f.next and s:
            prev = s
            s = s.next
            f = f.next.next
        if prev is None:
            return None
        prev.next = s.next
        return head
