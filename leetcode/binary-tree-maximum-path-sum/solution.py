# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            lm = max(l, 0)
            rm = max(r, 0)
            res[0] = max(res[0], lm + rm + root.val)
            return root.val + max(lm, rm)
        dfs(root)
        return res[0]
