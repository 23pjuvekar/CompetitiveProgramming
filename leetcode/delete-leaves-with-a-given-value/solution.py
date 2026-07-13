# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            node.left = l
            r = dfs(node.right)
            node.right = r
            if not l and not r and node.val == target:
                return None
            return node 
        return dfs(root)
