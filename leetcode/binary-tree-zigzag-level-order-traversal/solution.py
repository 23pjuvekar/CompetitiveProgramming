# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        
        # This will track the level number (0-indexed)
        # Even levels (0, 2, 4...) will be left-to-right
        # Odd levels (1, 3, 5...) will be right-to-left
        level_num = 0 
        res = []

        while q:
            current_level_size = len(q)
            current_level_nodes = [] # To store nodes for the current level's processing
            
            # This loop processes all nodes at the current level
            # and prepares for the next level by adding children to the queue
            for _ in range(current_level_size):
                node = q.popleft()
                current_level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_num % 2 == 1:
                current_level_nodes.reverse()
            
            res.append(current_level_nodes)
            level_num += 1
            
        return res
