# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:

        hash_map = {}
        curr = head
        while curr:
            hash_map[curr.val] = 1 + hash_map.get(curr.val, 0)
            curr = curr.next
        
        
        sort_keys = dict(sorted(hash_map.items()))

        head = ListNode()
        curr = head
        for keys, value in sort_keys.items():
            curr.next = ListNode(value)
            curr = curr.next

        return head.next
