# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        total = 0
        MOD = 10**9 + 7

        def dfs_total(node):
            if not node:
                return 0
            return node.val + dfs_total(node.right) + dfs_total(node.left)
        total = dfs_total(root) % MOD

        def dfs(node):
            if not node:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            self.res = max(self.res, (total - right) * right, (total - left) * left)
            return right + left + node.val % MOD
        dfs(root)
        return self.res % MOD
