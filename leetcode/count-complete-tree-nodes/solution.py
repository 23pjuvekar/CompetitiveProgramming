# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q = []
        if not root:
            return 0
        q.append(root)
        res = 1

        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
                res += 1
            if node.right:
                q.append(node.right)
                res += 1
            
        return res
