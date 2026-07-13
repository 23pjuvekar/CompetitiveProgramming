# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0, None)

        curr = head
        curr_1 = l1
        curr_2 = l2
        carry = 0
        while curr_1 or curr_2:
            value = carry
            if curr_1:
                value += curr_1.val
                curr_1 = curr_1.next
            if curr_2:
                value += curr_2.val
                curr_2 = curr_2.next
            if value > 9:
                carry = value // 10
                value = value % 10
            else:
                carry = 0
            curr.next = ListNode(value, None)
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(carry, None)
        
        return head.next
