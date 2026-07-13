# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(0, head)
        prev = res
        curr = head
        while curr:
            if curr.val * 2 > 9:
                prev.val += 1
            curr.val = (curr.val * 2) % 10
            prev = curr
            curr = curr.next
        if res.val == 0:
            return res.next
        return res
