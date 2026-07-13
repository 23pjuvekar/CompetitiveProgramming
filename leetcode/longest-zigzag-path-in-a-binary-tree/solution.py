# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append([root, 0, 0]) # [root, length, dir] --> -1: left, 1:right
        res = 0

        while q:
            node, length, direction = q.popleft()
            res = max(res, length)
            if node.left:
                if direction == 1:
                    q.append([node.left, length + 1, -1])
                else:
                    q.append([node.left, 1, -1])
            if node.right:
                if direction == -1:
                    q.append([node.right, length + 1, 1])
                else:
                    q.append([node.right, 1, 1])
        
        return res
