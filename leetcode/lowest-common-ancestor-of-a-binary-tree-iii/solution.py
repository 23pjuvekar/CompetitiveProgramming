"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_curr = p
        p_depth = 0
        while p_curr != None:
            p_depth += 1
            p_curr = p_curr.parent

        q_curr = q
        q_depth = 0
        while q_curr != None:
            q_depth += 1
            q_curr = q_curr.parent

        p_curr = p
        q_curr = q
        while p_depth > q_depth:
            p_depth -= 1
            p_curr = p_curr.parent

        while p_depth < q_depth:
            q_depth -= 1
            q_curr = q_curr.parent
        
        while q_curr != p_curr:
            q_curr = q_curr.parent
            p_curr = p_curr.parent
        
        return q_curr
