# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:

        curr = head
        res = 0
        while curr:
            odd = curr.next.val
            even = curr.val
            if even > odd:
                res += 1
            elif even < odd:
                res -= 1
            curr = curr.next.next
        
        if res == 0:
            return "Tie"
        elif res > 0:
            return "Even"
        else:
            return "Odd"
