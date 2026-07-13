# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0

        height = 1
        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return height

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                
            height += 1
        
        return height
