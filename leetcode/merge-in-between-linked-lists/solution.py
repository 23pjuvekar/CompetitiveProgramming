# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        p1 = None
        n2 = None
        prev = None
        curr = list1
        i = 0
        while curr:
            if i == a:
                p1 = prev
            if i == b:
                n2 = curr.next
                break
            prev = curr
            curr = curr.next
            i += 1
        
        p1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = n2
        return list1
