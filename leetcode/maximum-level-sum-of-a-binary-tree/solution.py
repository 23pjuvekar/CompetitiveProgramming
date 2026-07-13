# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append(root)
        res = 0
        max_v = float("-inf")
        level = 1

        while q:
            value = 0
            for i in range(len(q)):
                node = q.popleft()
                value += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if value > max_v:
                max_v = value
                res = level
            level += 1

        return res
