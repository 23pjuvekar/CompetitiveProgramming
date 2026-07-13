# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = []

        while curr:
            temp.append(curr.val)
            curr = curr.next

        temp.sort()
        
        curr = head
        i = 0
        while curr:
            curr.val = temp[i]
            curr = curr.next
            i += 1
        
        return head
