# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        res = [float("inf")]
        l = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if len(l) > 0:
                res[0] = min(res[0], abs(l[-1] - node.val))
            l.append(node.val)
            dfs(node.right)
            
        dfs(root)
        print(l)
        return res[0]
