# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        small = 0
        large = 0
        if p.val < q.val:
            small = p.val
            large = q.val
        else:
            small = q.val
            large = p.val

        while root:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root
