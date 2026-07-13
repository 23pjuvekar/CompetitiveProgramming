"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        q = deque()
        level = 0
        if root:
            q.append(root)
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            level += 1
        
        return level
