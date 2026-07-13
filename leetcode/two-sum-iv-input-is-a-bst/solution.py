# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:


        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        
        l = 0
        r = len(res) - 1

        while l < r:
            total = res[l] + res[r]
            if total == k:
                return True
            elif total > k:
                r -= 1
            elif total < k:
                l += 1
        return False
