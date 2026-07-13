# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == targetSum:
            return True
        q = deque()
        q.append([root.val, root])

        while q:
            for i in range(len(q)):
                path_sum, node = q.popleft()
                if node.left:
                    if node.left.left is None and node.left.right is None and path_sum + node.left.val == targetSum:
                        return True
                    q.append([path_sum + node.left.val, node.left])
                if node.right:
                    if node.right.left is None and node.right.right is None and path_sum + node.right.val == targetSum:
                        return True
                    q.append([path_sum + node.right.val, node.right])
                

        return False
