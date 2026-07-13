# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(node, left, right):

            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            leftCon = valid(node.left, left, node.val)
            rightCon = valid(node.right, node.val, right)

            return leftCon and rightCon
        
        return valid(root, float("-inf"), float("inf"))
