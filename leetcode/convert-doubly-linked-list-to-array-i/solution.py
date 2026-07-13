"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:


        curr_node = root
        res = []
        while curr_node:
            res.append(curr_node.val)
            curr_node = curr_node.next
        return res
