# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Fast and slow pointer
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        fast = head.next
        slow = head

        # Find middle with fast and slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second part
        curr = slow.next
        prev = None
        slow.next = None # Ends up being start of second half
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
