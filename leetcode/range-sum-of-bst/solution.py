# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if root is None:
            return 0

        q = deque()
        q.append(root)
        res = 0

        while q:
            node = q.pop()
            if node.val >= low and node.val <= high:
                res += node.val
            if node.left and node.val > low:
                q.append(node.left)
            if node.right and node.val < high:
                q.append(node.right)
        
        return res
