# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        cp = []

        curr = head
        prev = head.val
        i = 0
        while curr:
            if curr.next and ((prev < curr.val > curr.next.val) or (prev > curr.val < curr.next.val)):  
                cp.append(i)
            prev = curr.val
            curr = curr.next
            i += 1
        if len(cp) == 0 or len(cp) == 1:
            return [-1, -1]
        res = float("inf")
        for i in range(len(cp) - 1):
            res = min(res, cp[i+1] - cp[i])
        return [res, cp[-1] - cp[0]]
