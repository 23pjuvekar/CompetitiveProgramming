# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        total = m + n
        curr_length = 0
        curr = head
        dummy = ListNode()
        curr_dummy = dummy
        while curr:
            if curr_length < m:
                curr_dummy.next = curr
                curr_dummy = curr_dummy.next
            curr = curr.next
            curr_length += 1
            curr_length = curr_length % total
        curr_dummy.next = None
        return dummy.next
