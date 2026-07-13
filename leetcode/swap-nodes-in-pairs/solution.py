# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        new_head = head.next

        prev = None
        curr = head
        while curr and curr.next:
            first_node = curr
            second_node = curr.next
            next_pair_start = second_node.next
            second_node.next = first_node
            first_node.next = next_pair_start
            if prev:
                prev.next = second_node
            prev = first_node
            curr = next_pair_start
        return new_head
