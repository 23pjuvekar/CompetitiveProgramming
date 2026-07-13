# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        h1 = l1
        n1 = 0
        h2 = l2
        n2 = 0

        while h1:
            n1 = 10 * n1 + h1.val
            h1 = h1.next
        
        while h2:
            n2 = 10 * n2 + h2.val
            h2 = h2.next
        
        print(n1)
        print(n2)
        n3 = n1 + n2
        print(n1 + n2)

        n3_string = str(n3)

        head = ListNode(0)
        head_res = head

        for c in n3_string:
            node = ListNode(int(c))
            head.next = node
            head = head.next
        
        return head_res.next
