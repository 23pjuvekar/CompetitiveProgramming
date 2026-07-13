# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        n = 1
        curr = head
        n1 = None
        while curr:
            if n == k:
                n1 = curr
            curr = curr.next
            n += 1
        m = n - k
        i = 1
        n2 = None
        curr = head
        while curr:
            if i == m:
                n2 = curr
            curr = curr.next
            i += 1
        n1.val, n2.val = n2.val, n1.val
        return head
