# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(prev, node, right):
            if not node:
                return 0
            
            amt = dfs(node, node.right, True) + node.val + dfs(node, node.left, False)
            if amt == 0:
                if prev:
                    if right:
                        prev.right = None
                    else:
                        prev.left = None
                else:
                    return None
            return amt
        if dfs(None, root, False) == None:
            return None
        return root
