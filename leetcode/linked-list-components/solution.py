# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        in_component = False
        
        curr = head
        while curr:
            if curr.val in num_set:
                if not in_component:
                    res += 1
                    in_component = True
            else:
                in_component = False
            
            curr = curr.next
            
        return res
